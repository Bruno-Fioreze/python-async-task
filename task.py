import asyncio, time, functools

def show_message(*args):
    print("========================")
    print("success finish message")
    print("========================")

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    task = asyncio.create_task(say_after(2, 'hello'))
    cb_function = functools.partial(show_message, "Future:")
    task.add_done_callback(cb_function)

    await asyncio.gather(task)

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
