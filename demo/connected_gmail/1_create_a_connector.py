import os
from convore_api_client import CreateConnectorRequest, CreateGmailConnectorParams, ProviderType
from devtools import pprint

from modules import convore

client_id = os.environ.get("GOOGLE_CLIENT_ID")
client_secret = os.environ.get("GOOGLE_CLIENT_SECRET")

connector = convore.connectors.create_connector(
    create_connector_request=CreateConnectorRequest(
        name="Gmail Connector",
        provider=ProviderType.GMAIL,
        gmail=CreateGmailConnectorParams(
            client_id=client_id,
            client_secret=client_secret
        )
    )
)

print(pprint(connector))
