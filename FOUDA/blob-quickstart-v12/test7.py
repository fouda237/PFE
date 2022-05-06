import os, json, random, traceback, uuid, logging
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from azure.identity import ClientSecretCredential

from msrestazure.azure_exceptions import CloudError

from haikunator import Haikunator
from msrestazure.azure_cloud import get_cloud_from_metadata_endpoint
from msrestazure.azure_active_directory import UserPassCredentials
from azure.profiles import KnownProfiles

haikunator = Haikunator()