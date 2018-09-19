import asyncio
import random
import json


async def remote_sort():
    reader, writer = await asyncio.open_connection("127.0.0.1", 2015)
    print("Generating random list...")
    numbers = [random.randrange(10000) for r in range(10000)]
    data = json.dumps(numbers).encode()
    print("List Generated, Sending data")
    writer.write(len(data).to_bytes(8, "big"))
    writer.write(data)

    print("Waiting for data...")
    data = await reader.readexactly(len(data))
    print("Received data")
    sorted_values = json.loads(data.decode())
    print(sorted_values)
    print("\n")
    writer.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(remote_sort())
loop.close()
