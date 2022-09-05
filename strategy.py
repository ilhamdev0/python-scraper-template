from scrap_logic import posts as scrapPosts
from url import posts as urlPosts
from output import dataframe, save_parquet, save_parquet_incremental
import numpy as np
from time import sleep


def normal():
    """
    Normal strategy is doing scrapping in one go. Suitable for small set of url or if the server is not strict
    """

    posts_urls = urlPosts()
    posts_data = scrapPosts(posts_urls)

    # saving results
    posts_data = dataframe(posts_data)
    save_parquet(posts_data, "posts")


def incremental(loop: int, divider: int, delay: int):
    """
    Scrap with small amount of url then increment until done, use this strategy when normal strategy is failed.

    Step by step to use this strategy. First set 'loop' value to 1 (loop = 1) then run the strategy until finished, if error occured for example where loop = 20 then stop the strategy process then set 'loop' value to 20 and rerun the strategy again. Repeat until no error and the value of 'loop' is equal to 'divider'.

    You can also set value of 'delay' in second, this will pause the loop iteration by x second

    This strategy will produce multiple file sequentially. you can later merge all into one file.
    """

    if loop <= 0:
        print("loop value must be positive")
        return

    if divider <= 0:
        print("divider value must be positive")
        return

    if loop > divider:
        print("value of loop is too large")
        return

    posts_urls = urlPosts()

    # break list of url into smaller chunk by divider
    chunks_urls = np.array_split(posts_urls, divider)

    for i in range(loop, divider + 1):
        print(f"loop: {i}")

        posts_data = scrapPosts(chunks_urls[i - 1])

        # saving current results
        posts_data = dataframe(posts_data)
        save_parquet_incremental(
            "posts",
            i,
            divider,
            posts_data,
        )

        sleep(delay)
