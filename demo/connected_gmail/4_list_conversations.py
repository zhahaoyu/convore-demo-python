from modules import convore
from devtools import pprint

chanenl_id = 'chnnl_01hrak3jpaefnvk899sya9crzd'
relavant_contacts = ["EMAIL:haoyu@convore.dev"]

conversations = convore.conversations.list_conversations(
    channel_id=chanenl_id,
    contact_handle_tokens=relavant_contacts,
).data

print(pprint(conversations))
