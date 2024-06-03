from itertools import islice
from PIL import Image

def batched(iterable, n):
    iterator = iter(iterable)
    while (batch := tuple(islice(iterator, n))):
        yield batch

def iter_bits(bytes):
    for byte in bytes:
        for i in range(8):
            yield byte >> (7 - i) & 1

def least_significant_bit(message):
    message_bytes = message.encode()

    img = Image.open("source.png")
    im_bytes = bytearray(img.tobytes())

    assert len(message_bytes) * 8 <= len(im_bytes), "Message too long for encoding in this image."

    for n, bit in enumerate(iter_bits(message_bytes)):
        im_bytes[n] = (im_bytes[n] & ~1) | bit
    
    new_im = Image.frombytes('RGB', img.size, im_bytes)
    new_im.show()
    new_im.save("encoded.png")

    img.close()

def decode_least_singificant_bit():
    img = Image.open("stlouisEncode.png")
    im_bytes = bytearray(img.tobytes())

    bits = []
    for byte in im_bytes:
        bits.append(byte & 1)

    b = [sum([byte[7 - b] << b for b in range(0,8)])
        for byte in batched(bits[:len(bits) - len(bits) % 8], 8)]
    
    print(bytearray(b)[:1000])

    img.close()
    
if __name__ == '__main__':
    #least_significant_bit("fine i guess you are kind of goated. come here vro <3\0")
    decode_least_singificant_bit()
    # print(decode_least_significant_bit())
