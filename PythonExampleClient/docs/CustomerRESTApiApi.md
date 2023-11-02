# swagger_client.CustomerRESTApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_customer_rest_api_estimated_co2_post**](CustomerRESTApiApi.md#api_customer_rest_api_estimated_co2_post) | **POST** /api/CustomerRESTApi/estimated_CO2 | 
[**api_customer_rest_api_estimated_cost_post**](CustomerRESTApiApi.md#api_customer_rest_api_estimated_cost_post) | **POST** /api/CustomerRESTApi/estimated_cost | 
[**api_customer_rest_api_get_available_meters_post**](CustomerRESTApiApi.md#api_customer_rest_api_get_available_meters_post) | **POST** /api/CustomerRESTApi/get_available_meters | 
[**api_customer_rest_api_hourly_kwh_usage_post**](CustomerRESTApiApi.md#api_customer_rest_api_hourly_kwh_usage_post) | **POST** /api/CustomerRESTApi/hourly_kwh_usage | 
[**api_customer_rest_api_login_and_get_jwt_token_post**](CustomerRESTApiApi.md#api_customer_rest_api_login_and_get_jwt_token_post) | **POST** /api/CustomerRESTApi/login_and_get_jwt_token | 
[**api_customer_rest_api_refresh_jwt_key_token_post**](CustomerRESTApiApi.md#api_customer_rest_api_refresh_jwt_key_token_post) | **POST** /api/CustomerRESTApi/refresh_jwt_key_token | 

# **api_customer_rest_api_estimated_co2_post**
> list[CustKwhMeteresReading] api_customer_rest_api_estimated_co2_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.FilterCustKwhMeteresReading() # FilterCustKwhMeteresReading |  (optional)

try:
    api_response = api_instance.api_customer_rest_api_estimated_co2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_estimated_co2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md)|  | [optional] 

### Return type

[**list[CustKwhMeteresReading]**](CustKwhMeteresReading.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customer_rest_api_estimated_cost_post**
> list[EsitmatedCostPerMeter] api_customer_rest_api_estimated_cost_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.FilterCustKwhMeteresReading() # FilterCustKwhMeteresReading |  (optional)

try:
    api_response = api_instance.api_customer_rest_api_estimated_cost_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_estimated_cost_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md)|  | [optional] 

### Return type

[**list[EsitmatedCostPerMeter]**](EsitmatedCostPerMeter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customer_rest_api_get_available_meters_post**
> list[CustomerWithInstallations] api_customer_rest_api_get_available_meters_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.api_customer_rest_api_get_available_meters_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_get_available_meters_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomerWithInstallations]**](CustomerWithInstallations.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customer_rest_api_hourly_kwh_usage_post**
> list[CustKwhMeteresReading] api_customer_rest_api_hourly_kwh_usage_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.FilterCustKwhMeteresReading() # FilterCustKwhMeteresReading |  (optional)

try:
    api_response = api_instance.api_customer_rest_api_hourly_kwh_usage_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_hourly_kwh_usage_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilterCustKwhMeteresReading**](FilterCustKwhMeteresReading.md)|  | [optional] 

### Return type

[**list[CustKwhMeteresReading]**](CustKwhMeteresReading.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customer_rest_api_login_and_get_jwt_token_post**
> api_customer_rest_api_login_and_get_jwt_token_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))
body = swagger_client.LoginInput() # LoginInput |  (optional)

try:
    api_instance.api_customer_rest_api_login_and_get_jwt_token_post(body=body)
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_login_and_get_jwt_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginInput**](LoginInput.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_customer_rest_api_refresh_jwt_key_token_post**
> api_customer_rest_api_refresh_jwt_key_token_post()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomerRESTApiApi(swagger_client.ApiClient(configuration))

try:
    api_instance.api_customer_rest_api_refresh_jwt_key_token_post()
except ApiException as e:
    print("Exception when calling CustomerRESTApiApi->api_customer_rest_api_refresh_jwt_key_token_post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

