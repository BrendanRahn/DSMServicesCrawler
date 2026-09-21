from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# from firecrawl import Firecrawl
from Fcwl.FcwlClient import client
from firecrawl.v2.types import ScrapeOptions
from Fcwl.Models.ResultSchema import ResultSchema

fcwl_client = client # Get the Firecrawl client instance


# mock load websites to find forms for
target_sites = [
    "https://hhsservices.iowa.gov/apspssp/ssp.portal"
]

schema = ResultSchema.model_json_schema()
print("Schema:", schema)

scrape_opts = ScrapeOptions(
    only_main_content=True,
    max_age=172800000,
    # parsers=["pdf"], 
    formats=[
        "markdown",
        {
            "type": "json",
            "schema": ResultSchema.model_json_schema(),
        },
    ],
)
for site in target_sites:


    crawl_result = fcwl_client.crawl(
        site,
        sitemap="include",
        crawl_entire_domain=False,
        limit=10,
        prompt="Selectively crawl the website, find services that are offered, and then find any requirements that must be met. Navigate forms and compile a list of each form field",
        scrape_options=scrape_opts
    )

print(crawl_result)