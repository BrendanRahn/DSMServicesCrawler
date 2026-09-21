from firecrawl import Firecrawl
import os

class FcwlClient:
    _client: Firecrawl | None = None

    def __new__(cls):
        if cls._client is None:
            #add load_dotenv() here to load the environment variables from .env file?
            key = os.getenv("FIRECRAWL_API_KEY")
            if not key:
                raise Exception("FIRECRAWL_API_KEY env variable not set")
            cls._client = Firecrawl(api_key=key)
        return cls._client

client = FcwlClient()
        