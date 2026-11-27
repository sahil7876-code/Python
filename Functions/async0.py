import asyncio

async def printer():
    print('hello')
    await asyncio.sleep(4)
    print ("Friend")
    await asyncio.sleep(2)
    print("Sahil")

asyncio.run(printer())