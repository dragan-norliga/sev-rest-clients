using System;
using System.Collections.Generic;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;
using System.Text.Json;
using System.Globalization;


namespace DotNetExampleClient
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Log the client....");
            var instance = new CustomerRESTApiApi(
                "https://localhost:44346"
                //"https://api.sev.fo/"
            );
            var httpRes = instance.ApiCustomerRESTApiLoginAndGetJwtTokenPostWithHttpInfoAsync(new LoginInput
            {
                UserName = "Put your REST API User ID!",
                Password = "You REST API Key!"
            });
            var Token = httpRes.GetAwaiter().GetResult().Data;
            Console.WriteLine($"Getting the Bearer token {Token}");

            // put the token in the configuration so that it is automatically attached
            instance.Configuration = new Configuration
            {
                ApiKeyPrefix = { { "Authorization", $"Bearer {Token}" } },
            };

            Console.WriteLine($"Getting available meters...");
            Console.WriteLine(new String('*', 30));
            var meters = await instance.ApiCustomerRESTApiGetAvailableMetersPostAsync();            
            Console.WriteLine(JsonSerializer.Serialize(meters));

            List<int> meterIds = meters
                       .SelectMany(customer => customer.Installations)
                       .SelectMany(installation => installation.Meters)
                       .Select(meter => meter.MeterId)
                       .ToList();

            // get a data for the first meter in the list
            Console.WriteLine($"Getting kwh hours for the consumption...");
            Console.WriteLine(new String('*', 30));
            var kwhConsumption = await instance.ApiCustomerRESTApiHourlyKwhUsagePostAsync(
                         new FilterCustKwhMeteresReading
                         {
                             FromDate = DateTime.ParseExact("2023-08-25 00:00:00", "yyyy-MM-dd HH:mm:ss",
                             CultureInfo.InvariantCulture),
                             ToDate = DateTime.ParseExact("2023-08-26 00:00:00", "yyyy-MM-dd HH:mm:ss",
                             CultureInfo.InvariantCulture),
                             Meters = meterIds // Put your meters here
                         }
                     );
            Console.WriteLine(JsonSerializer.Serialize(kwhConsumption));

            Console.WriteLine($"Getting esitmated cost in DKR...");
            Console.WriteLine(new String('*', 30));
            var cost = await instance.ApiCustomerRESTApiEstimatedCostPostAsync(
                    new FilterCustKwhMeteresReading
                    {
                        FromDate = DateTime.ParseExact("2023-08-25 00:00:00", "yyyy-MM-dd HH:mm:ss",
                        CultureInfo.InvariantCulture),
                        ToDate = DateTime.ParseExact("2023-08-26 00:00:00", "yyyy-MM-dd HH:mm:ss",
                        CultureInfo.InvariantCulture),
                        Meters = meterIds // Put your meters here
                    }
                );
            Console.WriteLine(JsonSerializer.Serialize(cost));

            Console.WriteLine($"Getting esitmated CO2...");
            Console.WriteLine(new String('*', 30));

            var co2Emission = await instance.ApiCustomerRESTApiEstimatedCO2PostAsync(
                           new FilterCustKwhMeteresReading
                           {
                               FromDate = DateTime.ParseExact("2023-08-25 00:00:00", "yyyy-MM-dd HH:mm:ss",
                               CultureInfo.InvariantCulture),
                               ToDate = DateTime.ParseExact("2023-08-26 00:00:00", "yyyy-MM-dd HH:mm:ss",
                               CultureInfo.InvariantCulture),
                               Meters = meterIds // Put your meters here
                           }
                       );
            Console.WriteLine(JsonSerializer.Serialize(co2Emission));
        }
    }
}