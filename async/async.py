import time
import asyncio

async def func_1():
    print("Start func 1")
    print("Sleep func 1")
    await asyncio.sleep(3)
    print("Stop func 1")

async def func_2():
    print("Start func 2")
    print("Sleep func 2")
    await asyncio.sleep(2)
    print("Stop func 2")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(asyncio.gather(func_1(), func_2()))
    end_time = time.time()
    print("Run time :", end_time-start_time)