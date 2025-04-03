import asyncio
import aiohttp
import time

URLs = [
    "https://archive.org/",
    "https://infnet.online/",
    "https://www.youtube.com/",
    "https://duckduckgo.com/",
    "https://www.gmail.com",
    "https://www.github.com",
    "https://www.google.com/"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def main():
    for num_downloads in [1,2,4,5,7]:
        start_time = time.time()
        await download_all(URLs[:num_downloads])
        duration = time.time() - start_time
        print(f"Baixando {num_downloads} URLs levou {duration} segundos")


asyncio.run(main())

