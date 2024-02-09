from devtools import pprint
from modules import convore

channels = convore.channels.list_channels().data
print(pprint(channels))
