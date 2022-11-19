
# Example Python program that adds a completion 
# call back to an asyncio.Task object
import asyncio
from datetime import datetime

# Callback - context object is the actual
# task object 
def task_cb(context):
    print("Task completion received...")
    print("Name of the task:%s"%context.get_name())
    print("Wrapped coroutine object:%s"%context.get_coro())
    print("Task is done:%s"%context.done())
    print("Task has been cancelled:%s"%context.cancelled())
    print("Task result:%s"%context.result())
    print(type(context))
    print(context)

# A simple Python coroutine
async def simple_coroutine():
    await asyncio.sleep(1)
    return 1

# Create an asyncio.Task object
async def main():
    t1 = asyncio.create_task(simple_coroutine())
    t1.add_done_callback(task_cb)
    await t1
    print("Coroutine main() exiting")

# Execute the task
el = asyncio.new_event_loop()
asyncio.set_event_loop(el)
asyncio.run(main())