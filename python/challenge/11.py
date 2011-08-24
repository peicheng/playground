#!/usr/bin/env python
import Image

if __name__ == "__main__":
    im = Image.open('/home/jxq/downloads/cave.jpg')
    odd = even = Image.new('RGB', (320, 240))
    for x in range(0, 640):
        for y in range(0, 480):
            if x % 2 == 0 and y % 2 == 0:
                even.putpixel((x / 2, y / 2), im.getpixel((x, y)))
            elif x % 2 == 0 and y % 2 == 1:
                odd.putpixel((x / 2, (y - 1) / 2), im.getpixel((x, y)))
            elif x % 2 == 1 and y % 2 == 0:
                even.putpixel(((x - 1) / 2, y / 2), im.getpixel((x, y)))
            else:
                odd.putpixel(((x - 1) / 2, (y - 1) / 2), im.getpixel((x, y)))

    odd.save('/home/jxq/downloads/odd.jpg', 'JPEG')
    even.save('/home/jxq/downloads/even.jpg', 'JPEG')
