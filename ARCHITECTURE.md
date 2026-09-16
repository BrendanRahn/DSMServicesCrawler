---
description: Architecture plan for this project (see README.md)
---

### Stack
Planning on using:
- C# ASP.NET for backened
- Angular Typescript for frontend
    - Maybe use Blazor for front end, to keep stack to one language? 
    - Should use a SPA, the information should be mostly static (?), load info asynchronously but do it all at once

### AI Agent Bridge pattern
To avoid vendor lock, AI agent calls should be made to an interface. The implementation of that interface can be swapped out if neccessary, reducing the dependency on one AI agent provider.

Not sure if the Strategy or Bridge pattern should be used to accomplish this. Tool cals and skill belong to the implementation (ai provider). The only thing we are abstracting here is the call to the provider.
Ex:
```csharp
# Interface 
var agentExecutor = new IAgentExecutor(); # use a factory to give the implementation to the executor
var res = agentExecutor.Prompt("find a DSM service that helps people book medical appointments");

# No Interface
var firecrawl = new FirecrawlSession(); # This code would have to be changed
var res = firecrawl.Prompt("find a DSM service that helps people book medical appointments");
```

Business knowledge should be above the abstraction level (md documents, etc.)
Agent tool calls and skills should belong to the implementation level (firecrawl, claude)


**Bridge**
 This decouples the abstraction (prompts/tool calls(?)/skills) from the implementation (llm modle provider)

