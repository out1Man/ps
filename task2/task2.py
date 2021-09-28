filename="C:\\Users\\out Man\\Desktop\\ps后端\\task7\\before.png"
f=open(filename,"rb")
png=f.read()
png_list=list(png)
filetype_list = png_list[:8]
is_png = (filetype_list == [0x89, 0x50, 0x4e, 0x47, 0xd, 0xa, 0x1a, 0xa])
if is_png:
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
else:
    print("not png")
f.close()