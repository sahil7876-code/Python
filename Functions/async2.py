import asyncio

async def greet(name):
    print("hello", name)
    await asyncio.sleep(2)
    print("Welcome", name)

async def obj():
    await asyncio.gather(
        greet("Sahil"),
        greet("Sujal"),
        greet("Shivam")
    )

asyncio.run(obj())