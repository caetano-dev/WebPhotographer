import sys
import asyncio
from time import sleep
from pyppeteer import launch

async def screenshot():
    browser = await launch()
    page = await browser.newPage()
    print("Going to website")
    #await page.goto('https://r1.ufrrj.br/sisu/3-lista-de-espera/manifestacao-de-interesse/')
    await page.goto("http://www.time-time.net/timer/digital-clock.php")
    print("Taking screenshot...")
    sleep(2)
    await page.screenshot({"path":'webScreenshot.png'})
    sleep(2)
    print("Screenshot taken")
    await browser.close()

asyncio.get_event_loop().run_until_complete(screenshot())
sys.modules[__name__] = screenshot