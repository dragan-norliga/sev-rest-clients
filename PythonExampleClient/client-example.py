from __future__ import print_function
from pprint import pprint
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration
from swagger_client.models.login_input import LoginInput
from swagger_client.models.filter_cust_kwh_meteres_reading import FilterCustKwhMeteresReading

# create an instance of the API class
configuration = Configuration()
# configuration.verify_ssl = False # if the custom docker certificate is used, only for test environment!
# configuration.host = "https://localhost:44346" # only for development
configuration.host = "https://api.sev.fo"

api_client = swagger_client.ApiClient(configuration = configuration)
api_instance = swagger_client.CustomerRESTApiApi(api_client)

header_params = {}
token = ""
meter_ids = []
try:
    body = LoginInput()
    body.user_name = "Put your REST API User ID!"
    body.password = "You REST API Key!"
    (data, status, header) = api_instance.api_customer_rest_api_login_and_get_jwt_token_post_with_http_info(body = body)      
    token = data.decode('ansi')
    configuration.api_key_prefix = { 'Authorization': 'Bearer' }
    configuration.api_key =  { 'Authorization': token }
                            
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_login_and_get_jwt_token_post_with_http_info: %s\n" % e)

try:  
    (data, status, header) = api_instance.api_customer_rest_api_get_available_meters_post_with_http_info()
    meter_ids = [meter.meter_id for customer in data for installation in customer.installations for meter in installation.meters]
    print("Result from api_customer_rest_api_get_available_meters_post_with_http_info")
    print("**************************************************************************")
    pprint(data)
except ApiException as e:
    print("Exception when calling DataFlexApi->api_data_flex_fetch_wind_production_forecast_post_with_http_info: %s\n" % e)

try:
    
    body = FilterCustKwhMeteresReading()
    body.from_date ="2023-04-12T16:00:00Z"
    body.to_date = "2023-04-12T17:00:00Z"    
    body.meters = meter_ids    
    (data, status, header) = api_instance.api_customer_rest_api_hourly_kwh_usage_post_with_http_info(body=body) 
    print("Result from api_customer_rest_api_hourly_kwh_usage_post_with_http_info")
    print("**************************************************************************")
    pprint(data)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_hourly_kwh_usage_post_with_http_info: %s\n" % e)

try:    
    body = FilterCustKwhMeteresReading()
    body.from_date ="2023-04-12T16:00:00Z"
    body.to_date = "2023-04-12T17:00:00Z"    
    body.meters = meter_ids    
    (data, status, header) = api_instance.api_customer_rest_api_estimated_cost_post_with_http_info(body=body)
    print("Result from api_customer_rest_api_estimated_cost_post_with_http_info")
    print("**************************************************************************")
    pprint(data)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_estimated_cost_post_with_http_info: %s\n" % e)

try:    
    body = FilterCustKwhMeteresReading()
    body.from_date ="2023-04-12T16:00:00Z"
    body.to_date = "2023-04-12T17:00:00Z"    
    body.meters = meter_ids    
    (data, status, header) = api_instance.api_customer_rest_api_estimated_co2_post_with_http_info(body=body)
    print("Result from api_customer_rest_api_estimated_co2_post_with_http_info")
    print("**************************************************************************")
    pprint(data)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_estimated_co2_post_with_http_info: %s\n" % e)



