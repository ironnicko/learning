import asyncio
##async def main():
##    print("Nikhil")
##    task = asyncio.create_task(foo("Something"))
##    await asyncio.sleep(0.5)
##    print("done")
##
##
##async def foo(text):
##    print(text)
##    await asyncio.sleep(5) # within this sleep amount we get the other job done
##
##
##asyncio.run(main())


##async def fetch():
##    print("start fetching")
##    await asyncio.sleep(1)# this is the cue for printem to start printing #
##    print("done fetching")
##    return {"data": 1}
##
##async def printem():
##    for i in range(1,11):
##        print(i)
##        await asyncio.sleep(0)# this is the cue for the other task to finish so if does end it stops when this function is in sleep
##
##async def main():
##    task1 = asyncio.create_task(fetch())
##    task2 = asyncio.create_task(printem())
##
##    value = await task1
##    print(value)
####    await task2
##
##asyncio.run(main())


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    except Exception as e:
        pass
    finally:
        loop.close()
