import asyncio
from playwright.async_api import async_playwright

# example to print simple title 
# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("https://kaushalbundel.com")
#         print(await page.title())
#         await browser.close()


# asyncio.run(main()) # not able to run this. Need to explore something different

# Notes
'''
Installing playwrite using pip or uv is not fine. One needs to install its dependencies as well. It can be done via package based installs in ubuntu or arch. All such information is readily available if an issue during installation is reported.
'''
'''
Things to learn:
    - async and await 
'''

# example to get the screenshot of the page

async def main():
    async with async_playwright() as p:
        browser = await p.webkit.launch()
        page = await browser.new_page()
        await page.goto("https://kaushalbundel.com")
        await page.screenshot(path="web_image_timed.png") # absolute path is needed here.
        await browser.close()
        print("Screenshot taken successfully")

asyncio.run(main()) #The image is printed fine. 

# The problem now lies with the dimensions of the image, how do I control the dimensions dynamically and ensure the screenshot is of high quality
# I would also like to maintain the execution speed ie. the speed at which the image is printed (the timing here is ~ 1.2 secs to take a picture from starting a browser to taking a picture.)
