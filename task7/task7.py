import zlib
import struct
import math
filename="C:\\Users\\out Man\\Desktop\\ps后端\\task1\\test1.png"
f=open(filename,"rb")
png=f.read()
#png_list2=list(png)

png_list=list(bytearray(png))
headlist=png_list[0:33]
endlist=png_list[len(png_list)-12:len(png_list)]
#print(endlist)
length=(2 ** 24) * png_list[16] + \
                 (2 ** 16) * png_list[17] + \
                 (2 ** 8) * png_list[18] + \
                 (2 ** 0) * png_list[19]
height=(2 ** 24) * png_list[20] + \
                 (2 ** 16) * png_list[21] + \
                 (2 ** 8) * png_list[22] + \
                 (2 ** 0) * png_list[23]
#print("height: ",height)
#print("length: " ,length)



nu_byte=8

by_idat=b""

while nu_byte<len(png_list):
    length2=(2 ** 24) * png_list[nu_byte] + \
                 (2 ** 16) * png_list[nu_byte + 1] + \
                 (2 ** 8) * png_list[nu_byte + 2] + \
                 (2 ** 0) * png_list[nu_byte + 3]
    b_data={"length2":length2,
            "type":png[nu_byte+4:nu_byte+8],
            "crc":png_list[nu_byte+8+length2:nu_byte+12+length2]}
    if b_data["type"].decode()=='IDAT':
        typelist=b_data["type"]
        crclist=b_data["crc"]
        idat=png[nu_byte+8:nu_byte+8+length2]
        by_idat += idat
    nu_byte+=12+length2
#print(len(by_idat))
#print(by_idat[0:100])
uncom=zlib.decompress(by_idat)

#print(uncom[0:100])
rlist=[]
glist=[]
blist=[]
rgblist=list(uncom)
#print(rgblist[0:100])
for i in range(height):
    if rgblist[i * (length * 3+1 )] == 0:
        continue
    elif rgblist[i * (length * 3 +1)] == 1:
        for j in range(4,3*length+1):
            rgblist[i * (length*3+1) + j] = int((rgblist[i * (length*3+1) + j] + rgblist[i * (length*3+1) + j - 3]) % 256)
    elif rgblist[i * (length * 3 +1)] == 2:
        for j in range(1,3*length+1):
           rgblist[i * (length*3+1) + j] = int((rgblist[(i - 1) * (length*3+1) + j] + rgblist[i * (length*3+1) + j]) % 256)
    elif rgblist[i * (length * 3 +1)] == 3:
        for j in range(1,4):
            rgblist[i * (length*3+1) + j] = int((rgblist[(i - 1) * (3*length+1) + j] ) / 2 + rgblist[i * (length*3+1) + j]) % 256
        for j in range(4,3*length+1):
            rgblist[i * (length*3+1) + j] = int((rgblist[(i - 1) * (3*length+1) + j] + rgblist[i * (length*3+1) + j - 3]) / 2 + rgblist[i * (length*3+1) + j]) % 256
    elif rgblist[i * (length * 3 +1)] == 4:
        for j in range(1,4):
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
        for j in range(4,3*length+1):
            a = rgblist[j - 3 + i * (length*3+1)]
            b = rgblist[j + (i - 1) * (length*3+1)]
            c = rgblist[j - 3 + (i - 1) * (length*3+1)]
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
            rgblist[j + i * (length*3+1)] = int((rgblist[j + i * (length*3+1)] + count) % 256)
#print(rgblist[0:100])
for i in range(height):
    for j in range(1,3*length+1,3):
        a=max(rgblist[j+i*(3*length+1)],rgblist[j+1+i*(3*length+1)],rgblist[j+2+i*(3*length+1)])
        b=min(rgblist[j+i*(3*length+1)],rgblist[j+1+i*(3*length+1)],rgblist[j+2+i*(3*length+1)])
        c=int((a+b)/2)
        rgblist[j +1+ i * (3 * length + 1)]=c
        rgblist[j +2+ i * (3 * length + 1)] = c
        rgblist[j + i * (3 * length + 1)] = c
        '''rgblist[j+i*(3*length+1)]=int((rgblist[j+i*(3*length+1)]*0.299+rgblist[j+1+i*(3*length+1)]*0.587+(rgblist[j+2+i*(3*length+1)]*0.114))%256)
        rgblist[j+1+i*(3*length+1)]=int((rgblist[j+i*(3*length+1)]*0.299+rgblist[j+1+i*(3*length+1)]*0.587+(rgblist[j+2+i*(3*length+1)]*0.114))%256)
        rgblist[j+2+i*(3*length+1)]=int((rgblist[j+i*(3*length+1)]*0.299+rgblist[j+1+i*(3*length+1)]*0.587+(rgblist[j+2+i*(3*length+1)]*0.114))%256)'''
#边缘检测算法
for i in range(height-1):
    for j in range(1,3*length):
        x=int((rgblist[j + i * (length*3+1)]-rgblist[j+1+(i+1)*(3*length+1)])**2)
        y=int((rgblist[j+1+i*(3*length+1)]-rgblist[j+(i+1)*(3*length+1)])**2)
        rgblist[j + i * (3 * length + 1)]=int((math.sqrt(x+y))%256)
'''for i in range(height-1):
    for j in range(1,3*length):
        x=int((rgblist[j + i * (length*3+1)]-rgblist[j+1+(i+1)*(3*length+1)])**2)
        y=int((rgblist[j+1+i*(3*length+1)]-rgblist[j+(i+1)*(3*length+1)])**2)
        rgblist[j + i * (3 * length + 1)]=int((math.sqrt(x+y))%256)'''


for i in range(height - 1, -1, -1):
    if rgblist[i * (length * 3 + 1)] == 0:
        continue
    elif rgblist[i * (length * 3 + 1)] == 1:
        for j in range(3 * length, 0, -1):
            if j < 4:
                rgblist[i * (length * 3 + 1) + j] -= 0
            else:
                rgblist[i * (length * 3 + 1) + j] -= rgblist[i * (length * 3 + 1) + j - 3]
            rgblist[i * (length * 3 + 1) + j] %= 256

    elif rgblist[i * (length * 3 + 1)] == 2:
        for j in range(3 * length, 0, -1):
            rgblist[i * (length * 3 + 1) + j] -= rgblist[(i - 1) * (length * 3 + 1) + j]
            rgblist[i * (length * 3 + 1) + j] %= 256

    elif rgblist[i * (length * 3 + 1)] == 3:
        for j in range(3 * length, 0, -1):
            if j < 4:
                rgblist[i * (length * 3 + 1) + j] -= rgblist[(i - 1) * (length * 3 + 1) + j] // 2
            else:
                rgblist[i * (length * 3 + 1) + j] -= (rgblist[i * (length * 3 + 1) + j - 3] + rgblist[(i - 1) * (length * 3 + 1) + j]) // 2
            rgblist[i * (length * 3 + 1) + j] %= 256

    else:
        for j in range(3 * length, 0, -1):
            if j < 4:
                a, c = 0, 0
            else:
                a = rgblist[i * (length * 3 + 1) + j - 3]
                c = rgblist[(i - 1) * (length * 3 + 1) + j - 3]
            b = rgblist[(i - 1) * (length * 3 + 1) + j]

            p = a + b - c
            min_abs = min(abs(a - p), abs(b - p), abs(c - p))
            if min_abs == abs(a - p):
                rgblist[i * (length * 3 + 1) + j] -= a
            elif min_abs == abs(b - p):
                rgblist[i * (length * 3 + 1) + j] -= b
            else:
                rgblist[i * (length * 3 + 1) + j] -= c
            rgblist[i * (length * 3 + 1) + j] %= 256

#print(rgblist[0:100])
umidat=b""
umidat+=bytearray(rgblist[0:len(rgblist)])
comidat=zlib.compress(umidat)
#print(rgblist[0:100])
#print(len(rgblist))
#print(len(comidat))

comlist=list(bytearray(comidat))
f1=len(comlist)

f2=struct.pack('i',f1)
longlist=list(bytearray(f2))
#print(f1)
#print(f2)
#print(longlist)
tlonglist=list(reversed(longlist))
#print(tlonglist)
png2=bytearray(headlist)
png2+=bytearray(tlonglist)
png2+=bytearray(typelist)
png2+=bytearray(comlist)
png2+=bytearray(crclist)
png2+=bytearray(endlist)
#print(endlist)
testfile = open("C:\\Users\\out Man\\Desktop\\ps后端\\task7\\test6.png", mode = 'wb')
testfile.write(png2)
f.close()
testfile.close()
