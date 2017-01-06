# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
import uuid

from .. import models


class ServicesOperations(object):
    """ServicesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def create_or_update(
            self, resource_group_name, search_service_name, service, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a Search service in the given resource group. If the
        Search service already exists, all properties will be updated with the
        given values.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service to
         create or update. Search service names must only contain lowercase
         letters, digits or dashes, cannot use dash as the first two or last
         one characters, cannot contain consecutive dashes, and must be between
         2 and 60 characters in length. Search service names must be globally
         unique since they are part of the service URI
         (https://<name>.search.windows.net). You cannot change the service
         name after the service is created.
        :type search_service_name: str
        :param service: The definition of the Search service to create or
         update.
        :type service: :class:`SearchService
         <azure.mgmt.search.models.SearchService>`
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`SearchService
         <azure.mgmt.search.models.SearchService>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(service, 'SearchService')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SearchService', response)
        if response.status_code == 201:
            deserialized = self._deserialize('SearchService', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get(
            self, resource_group_name, search_service_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets the Search service with the given name in the given resource
        group.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`SearchService
         <azure.mgmt.search.models.SearchService>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SearchService', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, resource_group_name, search_service_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a Search service in the given resource group, along with its
        associated resources.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Search service
         associated with the specified resource group.
        :type search_service_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        # Construct URL
        url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}'
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'searchServiceName': self._serialize.url("search_service_name", search_service_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204, 404]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list_by_resource_group(
            self, resource_group_name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets a list of all Search services in the given resource group.

        :param resource_group_name: The name of the resource group within the
         current subscription. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`SearchServicePaged
         <azure.mgmt.search.models.SearchServicePaged>`
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices'
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.SearchServicePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.SearchServicePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def check_name_availability(
            self, name, search_management_request_options=None, custom_headers=None, raw=False, **operation_config):
        """Checks whether or not the given Search service name is available for
        use. Search service names must be globally unique since they are part
        of the service URI (https://<name>.search.windows.net).

        :param name: The Search service name to validate. Search service names
         must only contain lowercase letters, digits or dashes, cannot use dash
         as the first two or last one characters, cannot contain consecutive
         dashes, and must be between 2 and 60 characters in length.
        :type name: str
        :param search_management_request_options: Additional parameters for
         the operation
        :type search_management_request_options:
         :class:`SearchManagementRequestOptions
         <azure.mgmt.search.models.SearchManagementRequestOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`CheckNameAvailabilityOutput
         <azure.mgmt.search.models.CheckNameAvailabilityOutput>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        client_request_id = None
        if search_management_request_options is not None:
            client_request_id = search_management_request_options.client_request_id
        check_name_availability_input = models.CheckNameAvailabilityInput(name=name)

        # Construct URL
        url = '/subscriptions/{subscriptionId}/providers/Microsoft.Search/checkNameAvailability'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['x-ms-client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized