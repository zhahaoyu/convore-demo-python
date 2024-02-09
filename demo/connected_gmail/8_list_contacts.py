from modules import convore
from devtools import pprint

contacts = convore.contacts.list_contacts().data

print(pprint(contacts))
