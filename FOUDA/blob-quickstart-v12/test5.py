import os
from haikunator import Haikunator
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import (
    StorageAccountCreateParameters,
    StorageAccountUpdateParameters,
    Sku,
    SkuName,
    Kind
)
WEST_US = 'westus'
GROUP_NAME = 'azure-sample-group'
STORAGE_ACCOUNT_NAME = Haikunator().haikunate(delimiter='')
def get_credentials():
    subscription_id = os.environ.get(
        'AZURE_SUBSCRIPTION_ID',
        '1134015b-74cb-4c87-9766-ce234a087cc7')  # your Azure Subscription Id
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['e97e04b4-1367-4c10-9c30-415c956cc39e'],
        secret=os.environ['267f637f-c067-4484-b2af-730f2756ddb5'],
       tenant=os.environ['1b3dde29-70fd-4cc6-8b7b-535c5ec4a644']
    )
    return credentials, subscription_id
credentials, subscription_id = get_credentials()
def run_example():
    """Storage management example."""
    #
    # Create the Resource Manager Client with an Application (service principal) token provider
    #
    credentials, subscription_id = get_credentials()

    resource_client = ResourceManagementClient(credentials, subscription_id)
    storage_client = StorageManagementClient(credentials, subscription_id)
    # You MIGHT need to add Storage as a valid provider for these credentials
    # If so, this operation has to be done only once for each credentials
    resource_client.providers.register('Microsoft.Storage')
    # Create a storage account
    print('Create a storage account')
    storage_async_operation = storage_client.storage_accounts.create(
        GROUP_NAME,
        STORAGE_ACCOUNT_NAME,
        StorageAccountCreateParameters(
            sku=Sku(name=SkuName.standard_ragrs),
            kind=Kind.storage,
            location='westus',
            enable_https_traffic_only=True
        )
    )
    print(storage_async_operation)
run_example()    