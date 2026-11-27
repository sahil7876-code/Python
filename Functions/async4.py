import asyncio

async def greet(n):
    await asyncio.sleep(2)
    return n*n

async def obj():
    res = await asyncio.gather(
        greet(2),
        greet(3),
        greet(4)
    )
    print(res)

asyncio.run(obj())