#include <stdio.h>

int main()
{
	FILE* a = fopen("C:\\Users\\out Man\\Desktop\\ps后端\\task2\\test3.png", "rb");
	fseek(a, 16, 0);//跳过文件开头
	unsigned char b[100] = { 0 };
	unsigned char c[100] = { 0 };
	int b1 = fread(b, 1, 4, a);
	int c1 = fread(c, 1, 4, a);
	printf("width为： %d\n", (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3]);
	printf("height为： %d\n", (c[0] << 24) + (c[1] << 16) + (c[2] << 8) + c[3]);
	printf("bit_depth为： %d\n", fgetc(a));
	printf("color_type为： %d\n", fgetc(a));
	printf("compression为： %d\n", fgetc(a));
	printf("Filterh为： %d\n", fgetc(a));
	printf("Interlace为： %d\n", fgetc(a));
	fclose(a);
	return 0;
}