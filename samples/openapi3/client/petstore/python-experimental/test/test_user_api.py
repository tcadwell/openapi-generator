# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.api.user_api import UserApi  # noqa: E501
from petstore_api import configuration, schemas, api_client

from . import ApiTestMixin


class TestUserApi(ApiTestMixin, unittest.TestCase):
    """UserApi unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = UserApi(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create user  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import create_user as endpoint_module
        response_status = 0
        response_body = ''
        content_type = 'application/json'



    def test_create_users_with_array_input(self):
        """Test case for create_users_with_array_input

        Creates list of users with given input array  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import create_users_with_array_input as endpoint_module
        response_status = 0
        response_body = ''
        content_type = 'application/json'



    def test_create_users_with_list_input(self):
        """Test case for create_users_with_list_input

        Creates list of users with given input array  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import create_users_with_list_input as endpoint_module
        response_status = 0
        response_body = ''
        content_type = 'application/json'



    def test_delete_user(self):
        """Test case for delete_user

        Delete user  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import delete_user as endpoint_module
        response_status = 400
        response_body = ''
        pass

    def test_get_user_by_name(self):
        """Test case for get_user_by_name

        Get user by user name  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import get_user_by_name as endpoint_module
        response_status = 200
        accept_content_type = 'application/xml'



        accept_content_type = 'application/json'



        pass

    def test_login_user(self):
        """Test case for login_user

        Logs user into the system  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import login_user as endpoint_module
        response_status = 200
        accept_content_type = 'application/xml'



        accept_content_type = 'application/json'



        pass

    def test_logout_user(self):
        """Test case for logout_user

        Logs out current logged in user session  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import logout_user as endpoint_module
        response_status = 0
        response_body = ''
        pass

    def test_update_user(self):
        """Test case for update_user

        Updated user  # noqa: E501
        """
        from petstore_api.api.user_api_endpoints import update_user as endpoint_module
        response_status = 400
        response_body = ''
        content_type = 'application/json'




if __name__ == '__main__':
    unittest.main()
