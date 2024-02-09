import os
from dotenv import load_dotenv
from convore_sdk.client import Convore

load_dotenv()

api_key = os.environ.get("CONVORE_API_KEY")

convore = Convore(
    base_url="https://api.convore.dev",
    api_key=api_key,
)
