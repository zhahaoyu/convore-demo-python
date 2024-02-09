from convore_api_client import SendMessageRequest, MessageParticipant
from devtools import pprint

from modules import convore

recipients = [ "haoyu@tryforest.com" ]
channel_id = 'chnnl_01hrak3jpaefnvk899sya9crzd'

message = convore.messages.send_message(
    send_message_request=SendMessageRequest(
        channel_id=channel_id,
        subject="Test using Convore",
        body="This is a test message sent using the Convore API",
        to=recipients
    )
)

print(pprint(message))
