using Firecrawl;

var firecrawlKey = Environment.GetEnvironmentVariable("FIRECRAWL_API_KEY");


var client = new FirecrawlClient(firecrawlKey);
var res = await client.Crawling.CrawlUrlsAsync(
    scrapeOptions: new ScrapeOptions
    {
        
    }

)