import asyncio
from os import path
from playwright.async_api import async_playwright, Playwright

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
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://kaushalbundel.com")
        # await page.screenshot(path="web_image_timed.png", full_page=True) # absolute path is needed here.
        await page.screenshot(path="web_image_timed.jpg", full_page=True, quality=100) # absolute path is needed here.
        await browser.close()
        print("Screenshot taken successfully")

# asyncio.run(main()) #The image is printed fine. 

# example to get screenshot of a mobile device
async def mobile_device():
    async with async_playwright() as p:
        iphone_15 = p.devices["iPad (gen 11)"] #iPhone_15
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(**iphone_15) # I have just passed the context but other things such as screensize, geolocation etc can be entered
        page = await context.new_page()
        await page.goto("https://news.ycombinator.com")
        await page.screenshot(path="mobile_screen_shot.png")
        await browser.close()
        print("Screenshot printed succesfully!")

asyncio.run(mobile_device())


# The problem now lies with the dimensions of the image, how do I control the dimensions dynamically and ensure the screenshot is of high quality
# I would also like to maintain the execution speed ie. the speed at which the image is printed (the timing here is ~ 1.2 secs to take a picture from starting a browser to taking a picture.)

#Additional features
# 1. Take a screenshot of selected region: Can be done with clip tag
# 2. Take the screenshot of a mobile view: Can be done (The screenshot can also be taken in landscape or portrait by selecting appropriate phone)
# 3. Take a screenshot of a full page: This can be accomplished by a simple flag (full_page)as screenshot is taken
# 4. quality of the screenshot can be determined by the "quality" flog. This flag could be provided in the user context.
# 5. style or masking can be done to hide/show certain elements on the screnshot taken

# 6. Should have the time and location of the user so that these smaller thing sync between the screenshot and the access point
