import asyncio
from pathlib import Path
from re import sub

import aiofiles
from wikipediaapi import AsyncWikipedia, AsyncWikipediaPage

wikipedia = AsyncWikipedia (
    language = "en",
    user_agent = "wiki-scraper (279409447+python-neo@users.noreply.github.com)",
)

SAVE_DIR = Path (__file__).parents [2] / "pages"
SAVE_DIR.mkdir (exist_ok = True, parents = True)


semaphore = asyncio.Semaphore (16)
async def save_page (page : AsyncWikipediaPage) -> None :
    filename = sub (r'[<>:"/\\|?*]', "_", page.title) + ".txt"
    async with semaphore :
        text = await page.text
        async with aiofiles.open (SAVE_DIR / filename, "w", encoding = "utf-8") as f :
            print (page.title)
            await f.write (page.title + "\n")
            await f.write (text)


async def _main () -> None :
    python = wikipedia.page (
        title = "Python_(programming_language)"
    )
    links = await python.links
        
    await asyncio.gather (
        *[save_page (page) for page in links.values ()]
    )


def main () -> None :
    asyncio.run (_main ())