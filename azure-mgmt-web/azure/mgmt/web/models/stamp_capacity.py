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

from msrest.serialization import Model


class StampCapacity(Model):
    """Stamp capacity information.

    :param name: Name of the stamp.
    :type name: str
    :param available_capacity: Available capacity (# of machines, bytes of
     storage etc...).
    :type available_capacity: long
    :param total_capacity: Total capacity (# of machines, bytes of storage
     etc...).
    :type total_capacity: long
    :param unit: Name of the unit.
    :type unit: str
    :param compute_mode: Shared/dedicated workers. Possible values include:
     'Shared', 'Dedicated', 'Dynamic'
    :type compute_mode: str or ~azure.mgmt.web.models.ComputeModeOptions
    :param worker_size: Size of the machines. Possible values include:
     'Default', 'Small', 'Medium', 'Large'
    :type worker_size: str or ~azure.mgmt.web.models.WorkerSizeOptions
    :param worker_size_id: Size ID of machines:
     0 - Small
     1 - Medium
     2 - Large
    :type worker_size_id: int
    :param exclude_from_capacity_allocation: If <code>true</code>, it includes
     basic apps.
     Basic apps are not used for capacity allocation.
    :type exclude_from_capacity_allocation: bool
    :param is_applicable_for_all_compute_modes: <code>true</code> if capacity
     is applicable for all apps; otherwise, <code>false</code>.
    :type is_applicable_for_all_compute_modes: bool
    :param site_mode: Shared or Dedicated.
    :type site_mode: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'available_capacity': {'key': 'availableCapacity', 'type': 'long'},
        'total_capacity': {'key': 'totalCapacity', 'type': 'long'},
        'unit': {'key': 'unit', 'type': 'str'},
        'compute_mode': {'key': 'computeMode', 'type': 'ComputeModeOptions'},
        'worker_size': {'key': 'workerSize', 'type': 'WorkerSizeOptions'},
        'worker_size_id': {'key': 'workerSizeId', 'type': 'int'},
        'exclude_from_capacity_allocation': {'key': 'excludeFromCapacityAllocation', 'type': 'bool'},
        'is_applicable_for_all_compute_modes': {'key': 'isApplicableForAllComputeModes', 'type': 'bool'},
        'site_mode': {'key': 'siteMode', 'type': 'str'},
    }

    def __init__(self, name=None, available_capacity=None, total_capacity=None, unit=None, compute_mode=None, worker_size=None, worker_size_id=None, exclude_from_capacity_allocation=None, is_applicable_for_all_compute_modes=None, site_mode=None):
        self.name = name
        self.available_capacity = available_capacity
        self.total_capacity = total_capacity
        self.unit = unit
        self.compute_mode = compute_mode
        self.worker_size = worker_size
        self.worker_size_id = worker_size_id
        self.exclude_from_capacity_allocation = exclude_from_capacity_allocation
        self.is_applicable_for_all_compute_modes = is_applicable_for_all_compute_modes
        self.site_mode = site_mode
