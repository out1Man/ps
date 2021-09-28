import zlib


filename=input("请输入文件位置")
f=open(filename,"rb")
png=f.read()
png_list=list(bytearray(png))
filetype_list = png_list[:8]
is_png = (filetype_list == [0x89, 0x50, 0x4e, 0x47, 0xd, 0xa, 0x1a, 0xa])
if png_list:
    count = 16
    width = (2 ** 24) * png_list[count] + \
            (2 ** 16) * png_list[count + 1] + \
            (2 ** 8) * png_list[count + 2] + \
            (2 ** 0) * png_list[count + 3]
    height = (2 ** 24) * png_list[count + 4] + \
             (2 ** 16) * png_list[count + 5] + \
             (2 ** 8) * png_list[count + 6] + \
             (2 ** 0) * png_list[count + 7]
    BitDepth = png_list[count + 8]
    ColorType = png_list[count + 9]
    compressionmethod = png_list[count + 10]
    Filtermethod = png_list[count + 11]
    Interlacemethod = png_list[count + 12]
    print("width: ", width)
    print("heigt: ", height)
    print("bit:", BitDepth)
    print("col:", ColorType)
    print("com: ", compressionmethod)
    print("FIL", Filtermethod)
    print("int: ", Interlacemethod)
    length = (2 ** 24) * png_list[16] + \
             (2 ** 16) * png_list[17] + \
             (2 ** 8) * png_list[18] + \
             (2 ** 0) * png_list[19]
    height = (2 ** 24) * png_list[20] + \
             (2 ** 16) * png_list[21] + \
             (2 ** 8) * png_list[22] + \
             (2 ** 0) * png_list[23]
    print("height: ", height)
    print("length: ", length)

    nu_byte = 8

    by_idat = b""

    while nu_byte < len(png_list):
        length2 = (2 ** 24) * png_list[nu_byte] + \
                  (2 ** 16) * png_list[nu_byte + 1] + \
                  (2 ** 8) * png_list[nu_byte + 2] + \
                  (2 ** 0) * png_list[nu_byte + 3]
        b_data = {"length2": length2,
                  "type": png[nu_byte + 4:nu_byte + 8],
                  "crc": png_list[nu_byte + 8 + length2:nu_byte + 12 + length2]}
        if b_data["type"].decode() == 'IDAT':
            idat = png[nu_byte + 8:nu_byte + 8 + length2]
            by_idat += idat
        nu_byte += 12 + length2

    zobj = zlib.decompressobj()
    uncom = zlib.decompress(by_idat)
    # print(uncom[1000000:1000100])
    rlist = []
    glist = []
    blist = []
    rgblist = list(uncom)
    for i in range(height):
        if rgblist[i * (length * 3 + 1)] == 0:
            continue
        elif rgblist[i * (length * 3 + 1)] == 1:
            for j in range(4, 3 * length + 1):
                rgblist[i * (length * 3 + 1) + j] = int(
                    (rgblist[i * (length * 3 + 1) + j] + rgblist[i * (length * 3 + 1) + j - 3]) % 256)
        elif rgblist[i * (length * 3 + 1)] == 2:
            for j in range(1, 3 * length + 1):
                rgblist[i * (length * 3 + 1) + j] = int(
                    (rgblist[(i - 1) * (length * 3 + 1) + j] + rgblist[i * (length * 3 + 1) + j]) % 256)
        elif rgblist[i * (length * 3 + 1)] == 3:
            for j in range(1, 4):
                rgblist[i * (length * 3 + 1) + j] = int(
                    (rgblist[(i - 1) * (3 * length + 1) + j]) / 2 + rgblist[i * (length * 3 + 1) + j]) % 256
            for j in range(4, 3 * length + 1):
                rgblist[i * (length * 3 + 1) + j] = int(
                    (rgblist[(i - 1) * (3 * length + 1) + j] + rgblist[i * (length * 3 + 1) + j - 3]) / 2 + rgblist[
                        i * (length * 3 + 1) + j]) % 256
        elif rgblist[i * (length * 3 + 1)] == 4:
            for j in range(1, 4):
                a = 0
                b = rgblist[j + (i - 1) * (length * 3 + 1)]
                c = 0
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                if pa <= pb and pa <= pc:
                    count = a
                elif pb <= pc:
                    count = b
                else:
                    count = c
                rgblist[j + i * (length * 3 + 1)] = int((rgblist[j + i * (length * 3 + 1)] + count) % 256)
            for j in range(4, 3 * length + 1):
                a = rgblist[j - 3 + i * (length * 3 + 1)]
                b = rgblist[j + (i - 1) * (length * 3 + 1)]
                c = rgblist[j - 3 + (i - 1) * (length * 3 + 1)]
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                if pa <= pb and pa <= pc:
                    count = a
                elif pb <= pc:
                    count = b
                else:
                    count = c
                rgblist[j + i * (length * 3 + 1)] = int((rgblist[j + i * (length * 3 + 1)] + count) % 256)

    for i in range(height):
        for j in range(1, length * 3 + 1):
            if j % 3 == 1:
                rlist.append(rgblist[i * (length * 3 + 1) + j])
            elif j % 3 == 2:
                glist.append(rgblist[i * (length * 3 + 1) + j])
            elif j % 3 == 0:
                blist.append(rgblist[i * (length * 3 + 1) + j])
    while 1:
        x = int(input(("请输入x")))
        y = int(input(("请输入y")))
        print("r:", 257 * rlist[y * length + x])
        print("g:", 257 * glist[y * length + x])
        print("b:", 257 * blist[y * length + x])
else:
    print("not png")
f.close()








