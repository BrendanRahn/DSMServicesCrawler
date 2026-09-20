// dotnet 8

using Firecrawl;


var firecrawlKey = Environment.GetEnvironmentVariable("FIRECRAWL_API_KEY");

var client = new FirecrawlApp(firecrawlKey);

var options = new Firecrawl.ScrapeOptions()
{
    
}
