import webbrowser
from devtools import pprint


from convore_api_client import CreateAuthorizationFlowRequest
from modules import convore

connector_id = "cnntr_01hrajq1pcfcqa1hb0v6bhmt4t"
redirect = "https://httpbin.org/anything"

auth_flow = convore.authorization_flows.create_authorization_flow(
    create_authorization_flow_request=CreateAuthorizationFlowRequest(
        connector_id=connector_id,
        success_redirect_uri=redirect,
        error_redirect_uri=redirect
    )
)

print(pprint(auth_flow))
webbrowser.open(auth_flow.grant_url, new=2)
