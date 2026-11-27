import asyncio 

async def greet(): #defines an asynchronous function.

    print("hello") 
    await asyncio.sleep(2)  #asyncio.sleep(2) creates a 2-second asynchronous delay.
    print("Welcome")

asyncio.run(greet()) #runs the async program.

#await pauses the current coroutine while the awaited operation is pending.