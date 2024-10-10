from fastapi import FastAPI
from crawl4ai import AsyncWebCrawler
import asyncio

app = FastAPI()

@app.get("/")
async def read_root():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://www.example.com")
        return {"content": result.markdown}
