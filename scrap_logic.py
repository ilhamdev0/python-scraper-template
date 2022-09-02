from scrap_processor import controller
import asyncio
import itertools


"""
High level API, only import and use function below
"""


def posts(urls: list) -> list:
    # control how many request to server in parallel
    request = 10
    # introduce delay between request (in second)
    delay = 0

    # custom logic to processing loaded data
    def handler(obj, currenturl):
        return obj

    data = asyncio.run(controller(urls, request, delay, handler))

    # flatten list
    data = list(itertools.chain(*data))
    return data
