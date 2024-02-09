from devtools import pprint
from convore_api_client import SendMessageRequest, MessageParticipant

from modules import convore

message_id = 'msg_01hrakwwcveccsnm6xpn1wvmd4'

replyMessage = convore.messages.send_message(
    send_message_request=SendMessageRequest(
        body="This is a reply to a test message sent using the Convore API",
        reply_to_message_id=message_id
    )
)

print(pprint(replyMessage))
