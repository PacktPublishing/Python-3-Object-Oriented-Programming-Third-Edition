import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from PIL import Image
from bitarray import bitarray
from pathlib import Path


def compress_row(row):
    compressed = bytearray()
    chunks = split_bits(row, 127)
    for chunk in chunks:
        compressed.extend(compress_chunk(chunk))
    return compressed


def compress_chunk(chunk):
    compressed = bytearray()
    count = 1
    last = chunk[0]
    for bit in chunk[1:]:
        if bit != last:
            compressed.append(count | (128 * last))
            count = 0
            last = bit
        count += 1
    compressed.append(count | (128 * last))
    return compressed


def split_bits(bits, width):
    for i in range(0, len(bits), width):
        yield bits[i : i + width]


def compress_in_executor(executor, bits, width):
    row_compressors = []
    for row in split_bits(bits, width):
        compressor = executor.submit(compress_row, row)
        row_compressors.append(compressor)

    compressed = bytearray()
    for compressor in row_compressors:
        compressed.extend(compressor.result())
    return compressed


def compress_image(in_filename, out_filename, executor=None):
    executor = executor if executor else ThreadPoolExecutor(4)
    with Image.open(in_filename) as image:
        bits = bitarray(image.convert("1").getdata())
        width, height = image.size

    compressed = compress_in_executor(executor, bits, width)

    with open(out_filename, "wb") as file:
        file.write(width.to_bytes(2, "little"))
        file.write(height.to_bytes(2, "little"))
        file.write(compressed)


def compress_dir(in_dir, out_dir):
    if not out_dir.exists():
        out_dir.mkdir()

    executor = ThreadPoolExecutor(4)
    futures = []
    for file in (f for f in in_dir.iterdir() if f.suffix == ".bmp"):
        out_file = (out_dir / file.name).with_suffix(".rle")
        futures.append(
            executor.submit(compress_image, str(file), str(out_file))
        )
    for future in futures:
        future.result()


def single_image_main():
    in_filename, out_filename = sys.argv[1:3]
    executor = ThreadPoolExecutor(4)
    # executor = ProcessPoolExecutor()
    compress_image(in_filename, out_filename, executor)


def dir_images_main():
    in_dir, out_dir = (Path(p) for p in sys.argv[1:3])
    compress_dir(in_dir, out_dir)


if __name__ == "__main__":
    dir_images_main()
    # single_image_main()
