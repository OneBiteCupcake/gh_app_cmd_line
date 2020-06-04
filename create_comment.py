import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "Bret", oauth_token=os.getenv("GH_AUTH"))

        response = await gh.post('/repos/bretbailey1120/gh_app_cmd_line/issues/1/comments',
                                 data={
                                     'body': 'will add in the next sprint'
                                 })

        print(f"Comment created at {response['html_url']}")

asyncio.run(main())
