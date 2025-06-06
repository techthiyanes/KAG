# coding: utf-8

"""
kag

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kag.common.rest.configuration import Configuration


class UpsertEdgeRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "project_id": "int",
        "upsert_adjacent_vertices": "bool",
        "edges": "list[EdgeRecordInstance]",
    }

    attribute_map = {
        "project_id": "projectId",
        "upsert_adjacent_vertices": "upsertAdjacentVertices",
        "edges": "edges",
    }

    def __init__(
        self,
        project_id=None,
        upsert_adjacent_vertices=None,
        edges=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """UpsertEdgeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._upsert_adjacent_vertices = None
        self._edges = None
        self.discriminator = None

        self.project_id = project_id
        self.upsert_adjacent_vertices = upsert_adjacent_vertices
        self.edges = edges

    @property
    def project_id(self):
        """Gets the project_id of this UpsertEdgeRequest.  # noqa: E501


        :return: The project_id of this UpsertEdgeRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpsertEdgeRequest.


        :param project_id: The project_id of this UpsertEdgeRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and project_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project_id`, must not be `None`"
            )  # noqa: E501

        self._project_id = project_id

    @property
    def upsert_adjacent_vertices(self):
        """Gets the upsert_adjacent_vertices of this UpsertEdgeRequest.  # noqa: E501


        :return: The upsert_adjacent_vertices of this UpsertEdgeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._upsert_adjacent_vertices

    @upsert_adjacent_vertices.setter
    def upsert_adjacent_vertices(self, upsert_adjacent_vertices):
        """Sets the upsert_adjacent_vertices of this UpsertEdgeRequest.


        :param upsert_adjacent_vertices: The upsert_adjacent_vertices of this UpsertEdgeRequest.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and upsert_adjacent_vertices is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `upsert_adjacent_vertices`, must not be `None`"
            )  # noqa: E501

        self._upsert_adjacent_vertices = upsert_adjacent_vertices

    @property
    def edges(self):
        """Gets the edges of this UpsertEdgeRequest.  # noqa: E501


        :return: The edges of this UpsertEdgeRequest.  # noqa: E501
        :rtype: list[EdgeRecordInstance]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this UpsertEdgeRequest.


        :param edges: The edges of this UpsertEdgeRequest.  # noqa: E501
        :type: list[EdgeRecordInstance]
        """
        if (
            self.local_vars_configuration.client_side_validation and edges is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `edges`, must not be `None`"
            )  # noqa: E501

        self._edges = edges

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpsertEdgeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertEdgeRequest):
            return True

        return self.to_dict() != other.to_dict()
