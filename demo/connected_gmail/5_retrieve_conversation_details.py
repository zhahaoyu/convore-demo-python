from convore_api_client import MessageFormat
from devtools import pprint

from modules import convore

conversation_id = 'conv_01hrak3m9qe27v5dbyr1ba968m'

messages = convore.messages.list_messages(
    conversation_id=conversation_id,
    format=MessageFormat.FULL
).data

print(pprint(messages))


