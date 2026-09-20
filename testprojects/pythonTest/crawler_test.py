from firecrawl import Firecrawl
from firecrawl.v2.types import ScrapeOptions

app = Firecrawl(api_key="fc-a26a8373e88d437d875f5ea962c75d30")

scrape_opts = ScrapeOptions(
    only_main_content=True,
    max_age=172800000,
    parsers=["pdf"],
    formats=["markdown"]
)

crawl_result = app.crawl(
    "www.svdpdsm.org/",
    sitemap="include",
    crawl_entire_domain=False,
    limit=10,
    prompt="Crawl the entire website, identify any requirements or forms that are needed to recieve help",
    # scrape_options=scrape_opts
)

print(crawl_result)