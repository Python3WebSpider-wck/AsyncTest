import aiohttp
import asyncio
import time


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html: {html[:100]}...')
        print(f'status: {status}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # Python3.7 及其之后版本，不用显式声明事件循环
    # asyncio.run(main())
    # time.sleep(10)
