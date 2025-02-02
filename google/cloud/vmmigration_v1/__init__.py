# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .services.vm_migration import VmMigrationClient
from .services.vm_migration import VmMigrationAsyncClient

from .types.vmmigration import AddGroupMigrationRequest
from .types.vmmigration import AddGroupMigrationResponse
from .types.vmmigration import AppliedLicense
from .types.vmmigration import CancelCloneJobRequest
from .types.vmmigration import CancelCloneJobResponse
from .types.vmmigration import CancelCutoverJobRequest
from .types.vmmigration import CancelCutoverJobResponse
from .types.vmmigration import CloneJob
from .types.vmmigration import ComputeEngineTargetDefaults
from .types.vmmigration import ComputeEngineTargetDetails
from .types.vmmigration import ComputeScheduling
from .types.vmmigration import CreateCloneJobRequest
from .types.vmmigration import CreateCutoverJobRequest
from .types.vmmigration import CreateDatacenterConnectorRequest
from .types.vmmigration import CreateGroupRequest
from .types.vmmigration import CreateMigratingVmRequest
from .types.vmmigration import CreateSourceRequest
from .types.vmmigration import CreateTargetProjectRequest
from .types.vmmigration import CreateUtilizationReportRequest
from .types.vmmigration import CutoverJob
from .types.vmmigration import DatacenterConnector
from .types.vmmigration import DeleteDatacenterConnectorRequest
from .types.vmmigration import DeleteGroupRequest
from .types.vmmigration import DeleteMigratingVmRequest
from .types.vmmigration import DeleteSourceRequest
from .types.vmmigration import DeleteTargetProjectRequest
from .types.vmmigration import DeleteUtilizationReportRequest
from .types.vmmigration import FetchInventoryRequest
from .types.vmmigration import FetchInventoryResponse
from .types.vmmigration import FinalizeMigrationRequest
from .types.vmmigration import FinalizeMigrationResponse
from .types.vmmigration import GetCloneJobRequest
from .types.vmmigration import GetCutoverJobRequest
from .types.vmmigration import GetDatacenterConnectorRequest
from .types.vmmigration import GetGroupRequest
from .types.vmmigration import GetMigratingVmRequest
from .types.vmmigration import GetSourceRequest
from .types.vmmigration import GetTargetProjectRequest
from .types.vmmigration import GetUtilizationReportRequest
from .types.vmmigration import Group
from .types.vmmigration import ListCloneJobsRequest
from .types.vmmigration import ListCloneJobsResponse
from .types.vmmigration import ListCutoverJobsRequest
from .types.vmmigration import ListCutoverJobsResponse
from .types.vmmigration import ListDatacenterConnectorsRequest
from .types.vmmigration import ListDatacenterConnectorsResponse
from .types.vmmigration import ListGroupsRequest
from .types.vmmigration import ListGroupsResponse
from .types.vmmigration import ListMigratingVmsRequest
from .types.vmmigration import ListMigratingVmsResponse
from .types.vmmigration import ListSourcesRequest
from .types.vmmigration import ListSourcesResponse
from .types.vmmigration import ListTargetProjectsRequest
from .types.vmmigration import ListTargetProjectsResponse
from .types.vmmigration import ListUtilizationReportsRequest
from .types.vmmigration import ListUtilizationReportsResponse
from .types.vmmigration import MigratingVm
from .types.vmmigration import MigrationError
from .types.vmmigration import NetworkInterface
from .types.vmmigration import OperationMetadata
from .types.vmmigration import PauseMigrationRequest
from .types.vmmigration import PauseMigrationResponse
from .types.vmmigration import RemoveGroupMigrationRequest
from .types.vmmigration import RemoveGroupMigrationResponse
from .types.vmmigration import ReplicationCycle
from .types.vmmigration import ReplicationSync
from .types.vmmigration import ResumeMigrationRequest
from .types.vmmigration import ResumeMigrationResponse
from .types.vmmigration import SchedulePolicy
from .types.vmmigration import SchedulingNodeAffinity
from .types.vmmigration import Source
from .types.vmmigration import StartMigrationRequest
from .types.vmmigration import StartMigrationResponse
from .types.vmmigration import TargetProject
from .types.vmmigration import UpdateGroupRequest
from .types.vmmigration import UpdateMigratingVmRequest
from .types.vmmigration import UpdateSourceRequest
from .types.vmmigration import UpdateTargetProjectRequest
from .types.vmmigration import UtilizationReport
from .types.vmmigration import VmUtilizationInfo
from .types.vmmigration import VmUtilizationMetrics
from .types.vmmigration import VmwareSourceDetails
from .types.vmmigration import VmwareVmDetails
from .types.vmmigration import VmwareVmsDetails
from .types.vmmigration import ComputeEngineBootOption
from .types.vmmigration import ComputeEngineDiskType
from .types.vmmigration import ComputeEngineLicenseType
from .types.vmmigration import UtilizationReportView

__all__ = (
    "VmMigrationAsyncClient",
    "AddGroupMigrationRequest",
    "AddGroupMigrationResponse",
    "AppliedLicense",
    "CancelCloneJobRequest",
    "CancelCloneJobResponse",
    "CancelCutoverJobRequest",
    "CancelCutoverJobResponse",
    "CloneJob",
    "ComputeEngineBootOption",
    "ComputeEngineDiskType",
    "ComputeEngineLicenseType",
    "ComputeEngineTargetDefaults",
    "ComputeEngineTargetDetails",
    "ComputeScheduling",
    "CreateCloneJobRequest",
    "CreateCutoverJobRequest",
    "CreateDatacenterConnectorRequest",
    "CreateGroupRequest",
    "CreateMigratingVmRequest",
    "CreateSourceRequest",
    "CreateTargetProjectRequest",
    "CreateUtilizationReportRequest",
    "CutoverJob",
    "DatacenterConnector",
    "DeleteDatacenterConnectorRequest",
    "DeleteGroupRequest",
    "DeleteMigratingVmRequest",
    "DeleteSourceRequest",
    "DeleteTargetProjectRequest",
    "DeleteUtilizationReportRequest",
    "FetchInventoryRequest",
    "FetchInventoryResponse",
    "FinalizeMigrationRequest",
    "FinalizeMigrationResponse",
    "GetCloneJobRequest",
    "GetCutoverJobRequest",
    "GetDatacenterConnectorRequest",
    "GetGroupRequest",
    "GetMigratingVmRequest",
    "GetSourceRequest",
    "GetTargetProjectRequest",
    "GetUtilizationReportRequest",
    "Group",
    "ListCloneJobsRequest",
    "ListCloneJobsResponse",
    "ListCutoverJobsRequest",
    "ListCutoverJobsResponse",
    "ListDatacenterConnectorsRequest",
    "ListDatacenterConnectorsResponse",
    "ListGroupsRequest",
    "ListGroupsResponse",
    "ListMigratingVmsRequest",
    "ListMigratingVmsResponse",
    "ListSourcesRequest",
    "ListSourcesResponse",
    "ListTargetProjectsRequest",
    "ListTargetProjectsResponse",
    "ListUtilizationReportsRequest",
    "ListUtilizationReportsResponse",
    "MigratingVm",
    "MigrationError",
    "NetworkInterface",
    "OperationMetadata",
    "PauseMigrationRequest",
    "PauseMigrationResponse",
    "RemoveGroupMigrationRequest",
    "RemoveGroupMigrationResponse",
    "ReplicationCycle",
    "ReplicationSync",
    "ResumeMigrationRequest",
    "ResumeMigrationResponse",
    "SchedulePolicy",
    "SchedulingNodeAffinity",
    "Source",
    "StartMigrationRequest",
    "StartMigrationResponse",
    "TargetProject",
    "UpdateGroupRequest",
    "UpdateMigratingVmRequest",
    "UpdateSourceRequest",
    "UpdateTargetProjectRequest",
    "UtilizationReport",
    "UtilizationReportView",
    "VmMigrationClient",
    "VmUtilizationInfo",
    "VmUtilizationMetrics",
    "VmwareSourceDetails",
    "VmwareVmDetails",
    "VmwareVmsDetails",
)
