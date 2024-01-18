import asyncio
import sys
import time
import aiohttp

from config import headers, download_dir, urls

root_path = download_dir('asynio')
start_time = time.time()


async def download(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            content = await response.content.read()
            filename = url.split('/')[-1]
            with open(f'{root_path}/{filename}', 'wb') as file:
                file.write(content)


# @working_hours
async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
        await asyncio.gather(*tasks)
    print(f'Время выполнения кода: {time.time() - start_time:.2f} сек.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    asyncio.run(main(urls))
