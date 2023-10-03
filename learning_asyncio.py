import requests
import time
import asyncio
import aiohttp
import time

def fetch_url(url):
    response = requests.get(url)
    return response.text

def main_sync():
    urls = [
        'https://www.google.com' for i in range(100)

    ]

    start_time = time.time()
    for url in urls:
        result = fetch_url(url)
        print(f"URL: {url}, 길이: {len(result)}")

    end_time = time.time()
    print(f"총 실행 시간: {end_time - start_time} 초")


async def fetch_url_async(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    return response.text

async def main_async():
    urls = [
        'https://www.google.com' for i in range(100)
    ]
    start_time = time.time()


    tasks = [fetch_url_async(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, result in zip(urls, results):
        print(f"URL: {url}, 길이: {len(result)}")
    end_time = time.time()
    print(f"총 실행 시간: {end_time - start_time} 초")


if __name__ == "__main__":
    # main_sync()
    asyncio.run(main_async())