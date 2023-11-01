# Org.OpenAPITools.Api.CustomerRESTApiApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ApiCustomerRESTApiEstimatedCO2Post**](CustomerRESTApiApi.md#apicustomerrestapiestimatedco2post) | **POST** /api/CustomerRESTApi/estimated_CO2 |  |
| [**ApiCustomerRESTApiEstimatedCostPost**](CustomerRESTApiApi.md#apicustomerrestapiestimatedcostpost) | **POST** /api/CustomerRESTApi/estimated_cost |  |
| [**ApiCustomerRESTApiGetAvailableMetersPost**](CustomerRESTApiApi.md#apicustomerrestapigetavailablemeterspost) | **POST** /api/CustomerRESTApi/get_available_meters |  |
| [**ApiCustomerRESTApiHourlyKwhUsagePost**](CustomerRESTApiApi.md#apicustomerrestapihourlykwhusagepost) | **POST** /api/CustomerRESTApi/hourly_kwh_usage |  |
| [**ApiCustomerRESTApiLoginAndGetJwtTokenPost**](CustomerRESTApiApi.md#apicustomerrestapiloginandgetjwttokenpost) | **POST** /api/CustomerRESTApi/login_and_get_jwt_token |  |
| [**ApiCustomerRESTApiRefreshJwtKeyTokenPost**](CustomerRESTApiApi.md#apicustomerrestapirefreshjwtkeytokenpost) | **POST** /api/CustomerRESTApi/refresh_jwt_key_token |  |

<a id="apicustomerrestapiestimatedco2post"></a>
# **ApiCustomerRESTApiEstimatedCO2Post**
> List&lt;CustKwhMeteresReading&gt; ApiCustomerRESTApiEstimatedCO2Post (FilterCustKwhMeteresReading filterCustKwhMeteresReading = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiEstimatedCO2PostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);
            var filterCustKwhMeteresReading = new FilterCustKwhMeteresReading(); // FilterCustKwhMeteresReading |  (optional) 

            try
            {
                List<CustKwhMeteresReading> result = apiInstance.ApiCustomerRESTApiEstimatedCO2Post(filterCustKwhMeteresReading);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiEstimatedCO2Post: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiEstimatedCO2PostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<CustKwhMeteresReading>> response = apiInstance.ApiCustomerRESTApiEstimatedCO2PostWithHttpInfo(filterCustKwhMeteresReading);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiEstimatedCO2PostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **filterCustKwhMeteresReading** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md) |  | [optional]  |

### Return type

[**List&lt;CustKwhMeteresReading&gt;**](CustKwhMeteresReading.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="apicustomerrestapiestimatedcostpost"></a>
# **ApiCustomerRESTApiEstimatedCostPost**
> List&lt;EsitmatedCostPerMeter&gt; ApiCustomerRESTApiEstimatedCostPost (FilterCustKwhMeteresReading filterCustKwhMeteresReading = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiEstimatedCostPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);
            var filterCustKwhMeteresReading = new FilterCustKwhMeteresReading(); // FilterCustKwhMeteresReading |  (optional) 

            try
            {
                List<EsitmatedCostPerMeter> result = apiInstance.ApiCustomerRESTApiEstimatedCostPost(filterCustKwhMeteresReading);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiEstimatedCostPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiEstimatedCostPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<EsitmatedCostPerMeter>> response = apiInstance.ApiCustomerRESTApiEstimatedCostPostWithHttpInfo(filterCustKwhMeteresReading);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiEstimatedCostPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **filterCustKwhMeteresReading** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md) |  | [optional]  |

### Return type

[**List&lt;EsitmatedCostPerMeter&gt;**](EsitmatedCostPerMeter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="apicustomerrestapigetavailablemeterspost"></a>
# **ApiCustomerRESTApiGetAvailableMetersPost**
> List&lt;CustomerWithInstallations&gt; ApiCustomerRESTApiGetAvailableMetersPost ()



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiGetAvailableMetersPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);

            try
            {
                List<CustomerWithInstallations> result = apiInstance.ApiCustomerRESTApiGetAvailableMetersPost();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiGetAvailableMetersPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiGetAvailableMetersPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<CustomerWithInstallations>> response = apiInstance.ApiCustomerRESTApiGetAvailableMetersPostWithHttpInfo();
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiGetAvailableMetersPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;CustomerWithInstallations&gt;**](CustomerWithInstallations.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="apicustomerrestapihourlykwhusagepost"></a>
# **ApiCustomerRESTApiHourlyKwhUsagePost**
> List&lt;CustKwhMeteresReading&gt; ApiCustomerRESTApiHourlyKwhUsagePost (FilterCustKwhMeteresReading filterCustKwhMeteresReading = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiHourlyKwhUsagePostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);
            var filterCustKwhMeteresReading = new FilterCustKwhMeteresReading(); // FilterCustKwhMeteresReading |  (optional) 

            try
            {
                List<CustKwhMeteresReading> result = apiInstance.ApiCustomerRESTApiHourlyKwhUsagePost(filterCustKwhMeteresReading);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiHourlyKwhUsagePost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiHourlyKwhUsagePostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<CustKwhMeteresReading>> response = apiInstance.ApiCustomerRESTApiHourlyKwhUsagePostWithHttpInfo(filterCustKwhMeteresReading);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiHourlyKwhUsagePostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **filterCustKwhMeteresReading** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md) |  | [optional]  |

### Return type

[**List&lt;CustKwhMeteresReading&gt;**](CustKwhMeteresReading.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="apicustomerrestapiloginandgetjwttokenpost"></a>
# **ApiCustomerRESTApiLoginAndGetJwtTokenPost**
> void ApiCustomerRESTApiLoginAndGetJwtTokenPost (LoginInput loginInput = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiLoginAndGetJwtTokenPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);
            var loginInput = new LoginInput(); // LoginInput |  (optional) 

            try
            {
                apiInstance.ApiCustomerRESTApiLoginAndGetJwtTokenPost(loginInput);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiLoginAndGetJwtTokenPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiLoginAndGetJwtTokenPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    apiInstance.ApiCustomerRESTApiLoginAndGetJwtTokenPostWithHttpInfo(loginInput);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiLoginAndGetJwtTokenPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **loginInput** | [**LoginInput**](LoginInput.md) |  | [optional]  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="apicustomerrestapirefreshjwtkeytokenpost"></a>
# **ApiCustomerRESTApiRefreshJwtKeyTokenPost**
> void ApiCustomerRESTApiRefreshJwtKeyTokenPost ()



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Example
{
    public class ApiCustomerRESTApiRefreshJwtKeyTokenPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure API key authorization: Bearer
            config.AddApiKey("Authorization", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // config.AddApiKeyPrefix("Authorization", "Bearer");

            var apiInstance = new CustomerRESTApiApi(config);

            try
            {
                apiInstance.ApiCustomerRESTApiRefreshJwtKeyTokenPost();
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiRefreshJwtKeyTokenPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApiCustomerRESTApiRefreshJwtKeyTokenPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    apiInstance.ApiCustomerRESTApiRefreshJwtKeyTokenPostWithHttpInfo();
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CustomerRESTApiApi.ApiCustomerRESTApiRefreshJwtKeyTokenPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters
This endpoint does not need any parameter.
### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

