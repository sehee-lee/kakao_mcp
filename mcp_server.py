import json
import os
import requests

import httpx
from fastmcp import FastMCP

mcp = FastMCP("kakao search API", dependencies=["httpx", "xmltodict"])

kakao_app_key = os.environ["KAKAO_APP_KEY"]

cafe_api = 'https://dapi.kakao.com/v2/search/cafe'
web_api = 'https://dapi.kakao.com/v2/search/web'
blog_api = 'https://dapi.kakao.com/v2/search/blog'
book_api = 'https://dapi.kakao.com/v3/search/book'

video_api = 'https://dapi.kakao.com/v2/search/vclip'
image_api = 'https://dapi.kakao.com/v2/search/image'


def search_test(collection: str, query: str):
    api = ''
    sort = ''
    if collection == 'cafe':
        api = cafe_api
        sort = 'timely'

    params = {
        "query": query,
        "size": 50,
        "page": 1,
        "sort": sort,
    }

    headers = {
        "Authorization": f"KakaoAK {kakao_app_key}"
    }

    response = requests.get(api, params=params, headers=headers)

    res = response.json()

    print(res)




@mcp.tool(
    name="search_cafe",
    description="Search cafe post from daum cafe",
)
async def search_cafe(
    query: str,
    display: int = 50,
    page: int = 1,
    sort: str = "timely",
):
    """
    Search cafe post from kakao search api.

    Args:
        query (str): The query to search for.
        display (int, optional): The number of items to display. Defaults to 10.
        page (int, optional): The page for the search. Defaults to 1.
        sort (str, optional): The sorting method. Defaults to "accuracy".
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            cafe_api,
            params={
                "query": query,
                "size": display,
                "page": page,
                "sort": sort,
            },
            headers={
                "Authorization": f"KakaoAK {kakao_app_key}"
            }
        )

        response.raise_for_status()
        result = response.json()
        cafe_docs = result['documents']

        return cafe_docs

@mcp.tool(
    name="search_web",
    description="Search web page from kakao search",
)
async def search_web(
        query: str,
        display: int = 50,
        page: int = 1,
):
    """
    Search web from kakao search api.

    Args:
        query (str): The query to search for.
        display (int, optional): The number of items to display. Defaults to 10.
        page (int, optional): The page for the search. Defaults to 1.
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(
            web_api,
            params={
                "query": query,
                "size": display,
                "page": page,
            },
            headers={
                "Authorization": f"KakaoAK {kakao_app_key}"
            }
        )

        response.raise_for_status()
        result = response.json()
        web_docs = result['documents']

        return web_docs

@mcp.tool(
    name="search_blog",
    description="Search blog post from kakao",
)
async def search_cafe(
        query: str,
        display: int = 50,
        page: int = 1,
):
    """
    Search full text from kakao search api.

    Args:
        query (str): The query to search for.
        display (int, optional): The number of items to display. Defaults to 10.
        page (int, optional): The page for the search. Defaults to 1.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            blog_api,
            params={
                "query": query,
                "size": display,
                "page": page,
            },
            headers={
                "Authorization": f"KakaoAK {kakao_app_key}"
            }
        )

        response.raise_for_status()
        result = response.json()
        blog_docs = result['documents']

        return blog_docs


if __name__ == "__main__":
    # search_test('cafe', '손흥민')

    mcp.run()