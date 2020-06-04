import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "Bret", oauth_token=os.getenv("GH_AUTH"))

        response = await gh.post('/repos/bretbailey1120/racquetballReferee/issues',
                      data={
                          'title': 'we got a problem',
                          'body': 'user more emoji!'
                      })

        print(f"Issue created at {response['html_url']}")

asyncio.run(main())
