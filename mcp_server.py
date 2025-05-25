# demo.py
import json
import os

import httpx
import xmltodict
from fastmcp import FastMCP

mcp = FastMCP("kakao search API", dependencies=["httpx", "xmltodict"])

kakao_app_key = ''

cafe_api = 'https://dapi.kakao.com/v2/search/cafe'
# cafe_api = "https://apigw.9rum.cc/cafe-dev/apibook",

@mcp.tool(
    name="search_cafe",
    description="Search cafe on daum cafe",
)
async def search_cafe(
    query: str,
    display: int = 50,
    page: int = 1,
    sort: str = "timely",
):
    """
    Search cafe post on daum cate

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

        response.raise_for_status()  # Raise an error for bad responses

        return response.text

if __name__ == "__main__":
    mcp.run()