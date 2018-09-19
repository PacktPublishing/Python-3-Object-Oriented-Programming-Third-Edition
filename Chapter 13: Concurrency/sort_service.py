import asyncio
import json
from concurrent.futures import ProcessPoolExecutor


def sort_in_process(data):
    nums = json.loads(data.decode())
    curr = 1
    while curr < len(nums):
        if nums[curr] >= nums[curr - 1]:
            curr += 1
        else:
            nums[curr], nums[curr - 1] = nums[curr - 1], nums[curr]
            if curr > 1:
                curr -= 1

    return json.dumps(nums).encode()


async def sort_request(reader, writer):
    print("Received connection")
    length = await reader.read(8)
    data = await reader.readexactly(int.from_bytes(length, "big"))
    result = await asyncio.get_event_loop().run_in_executor(
        None, sort_in_process, data
    )
    print("Sorted list")
    writer.write(result)
    writer.close()
    print("Connection closed")


loop = asyncio.get_event_loop()
loop.set_default_executor(ProcessPoolExecutor())
server = loop.run_until_complete(
    asyncio.start_server(sort_request, "127.0.0.1", 2015)
)
print("Sort Service running")

loop.run_forever()
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
