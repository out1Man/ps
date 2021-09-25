filename=input("输入文件位置")
f=open(filename,"rb")
png=f.read()
png_list=list(png)
nu_byte=8
a_list=[]
while nu_byte<len(png_list):
    length=(2 ** 24) * png_list[nu_byte] + \
                 (2 ** 16) * png_list[nu_byte + 1] + \
                 (2 ** 8) * png_list[nu_byte + 2] + \
                 (2 ** 0) * png_list[nu_byte + 3]
    b_data={"length":length,
            "type":png[nu_byte+4:nu_byte+8],
            "crc":png_list[nu_byte+8+length:nu_byte+12+length]}
    nu_byte+=12+length
    a_list.append(b_data)
print("length   type    crc")
for i in a_list:
    print("%5s   %5s   %5s" %(i["length"], i["type"].decode(), i["crc"]))