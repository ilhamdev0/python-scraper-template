from scrap_logic import posts as scrapPosts
from url import posts as urlPosts
from output import dataframe, save_csv, save_csv_incremental
import numpy as np


def normal():
    """
    Normal strategy is doing scrapping in one go. Suitable for small set of url or if the server is not strict
    """

    posts_urls = urlPosts()
    posts_data = scrapPosts(posts_urls)

    # saving results
    posts_data = dataframe(posts_data)
    save_csv(posts_data)


def incremental(chunk: int, divider: int):
    """
    Scrap with small amount of url then increment until done, use this strategy when normal strategy is failed.

    Step by step to use this strategy, First. set 'chunk' value to 1 (chunk = 1) then run the strategy until finished, if no error occured then increment 'chunk' by one (chunk = 2) rerun the strategy again. Repeat until the value of 'chunk' is equal to 'divider'.

    This strategy will produce multiple file sequentially based on value of chunk. Last step is merge all file into one file.
    """

    if chunk <= 0:
        print("chunk value must be positive")
        return

    if divider <= 0:
        print("divider value must be positive")
        return

    if chunk > divider:
        print("value of chunk is too large")
        return

    posts_urls = urlPosts()

    # break list of url into smaller chunk by divider
    chunk_urls = np.array_split(posts_urls, divider)

    posts_data = scrapPosts(chunk_urls[chunk-1])

    # saving current results
    posts_data = dataframe(posts_data)
    save_csv_incremental(chunk, posts_data)
