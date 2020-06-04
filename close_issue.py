import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "Bret", oauth_token=os.getenv("GH_AUTH"))

        response = await gh.patch('/repos/bretbailey1120/gh_app_cmd_line/issues/1',
                                 data={
                                     'state': 'closed'
                                 })

        print(f"Issue closed: {response['html_url']}")

asyncio.run(main())
