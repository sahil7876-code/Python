
import asyncio

async def greet():
    print('Hello')
    await asyncio.sleep(2)
    print('Welcome')

async def wish(name):
    print('Good Morning')
    await asyncio.sleep(2)
    print(name)


async def main():
    await asyncio.gather(greet(), wish('Sahil'))
    
asyncio.run(main())

