import asyncio
import aiohttp

# throttler function
async def gather_with_concurrency(n: int, delay: int, *tasks) -> list:
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            # next coroutine(s) will stuck here until the previous is done
            await asyncio.sleep(delay)

            return await task

    return await asyncio.gather(*(sem_task(task) for task in tasks))


# load data from every request
async def get_async(url: str, session, func):
    async with session.get(url, ssl=False) as response:
        raw_data = await response.read()
        processed_data = func(raw_data, url)
        return processed_data


async def controller(urls: list, parallel_request: int, delay: int, handler) -> list:
    """
    parallel_request: throttling the connection to server, higher value the better but if the value is set too high it will degrade performance

    delay: introduce delay between request, value equal 0 means no delay
    """

    conn = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300)
    timeout = aiohttp.ClientTimeout(total=3600, connect=300)

    session = aiohttp.ClientSession(connector=conn,timeout=timeout)

    results = await gather_with_concurrency(
        parallel_request,
        delay,
        *[get_async(i, session, handler) for i in urls]
    )
    await session.close()

    return results
