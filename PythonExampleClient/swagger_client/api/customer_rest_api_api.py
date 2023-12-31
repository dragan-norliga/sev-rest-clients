# coding: utf-8

"""
    Sev Data flex API v1.0

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomerRESTApiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_customer_rest_api_estimated_co2_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_estimated_co2_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_estimated_co2_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[CustKwhMeteresReading]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_estimated_co2_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_estimated_co2_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_estimated_co2_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_estimated_co2_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_estimated_co2_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[CustKwhMeteresReading]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_estimated_co2_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/estimated_CO2', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustKwhMeteresReading]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_customer_rest_api_estimated_cost_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_estimated_cost_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_estimated_cost_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[EsitmatedCostPerMeter]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_estimated_cost_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_estimated_cost_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_estimated_cost_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_estimated_cost_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_estimated_cost_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[EsitmatedCostPerMeter]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_estimated_cost_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/estimated_cost', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EsitmatedCostPerMeter]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_customer_rest_api_get_available_meters_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_get_available_meters_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_get_available_meters_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CustomerWithInstallations]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_get_available_meters_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_get_available_meters_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_get_available_meters_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_get_available_meters_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_get_available_meters_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[CustomerWithInstallations]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_get_available_meters_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/get_available_meters', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustomerWithInstallations]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_customer_rest_api_hourly_kwh_usage_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_hourly_kwh_usage_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_hourly_kwh_usage_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[CustKwhMeteresReading]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_hourly_kwh_usage_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_hourly_kwh_usage_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_hourly_kwh_usage_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_hourly_kwh_usage_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_hourly_kwh_usage_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FilterCustKwhMeteresReading body:
        :return: list[CustKwhMeteresReading]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_hourly_kwh_usage_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/hourly_kwh_usage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CustKwhMeteresReading]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_customer_rest_api_login_and_get_jwt_token_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_login_and_get_jwt_token_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_login_and_get_jwt_token_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginInput body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_login_and_get_jwt_token_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_login_and_get_jwt_token_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_login_and_get_jwt_token_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_login_and_get_jwt_token_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_login_and_get_jwt_token_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LoginInput body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_login_and_get_jwt_token_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/login_and_get_jwt_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=bytes,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_customer_rest_api_refresh_jwt_key_token_post(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_refresh_jwt_key_token_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_refresh_jwt_key_token_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_customer_rest_api_refresh_jwt_key_token_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_customer_rest_api_refresh_jwt_key_token_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_customer_rest_api_refresh_jwt_key_token_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_customer_rest_api_refresh_jwt_key_token_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_customer_rest_api_refresh_jwt_key_token_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_customer_rest_api_refresh_jwt_key_token_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/CustomerRESTApi/refresh_jwt_key_token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=bytes,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
