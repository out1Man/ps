#include <stdio.h>

int main()
{
	FILE* a = fopen("C:\\Users\\out Man\\Desktop\\ps���\\task2\\test3.png", "rb");
	fseek(a, 16, 0);//�����ļ���ͷ
	unsigned char b[100] = { 0 };
	unsigned char c[100] = { 0 };
	int b1 = fread(b, 1, 4, a);
	int c1 = fread(c, 1, 4, a);
	printf("widthΪ�� %d\n", (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3]);
	printf("heightΪ�� %d\n", (c[0] << 24) + (c[1] << 16) + (c[2] << 8) + c[3]);
	printf("bit_depthΪ�� %d\n", fgetc(a));
	printf("color_typeΪ�� %d\n", fgetc(a));
	printf("compressionΪ�� %d\n", fgetc(a));
	printf("FilterhΪ�� %d\n", fgetc(a));
	printf("InterlaceΪ�� %d\n", fgetc(a));
	fclose(a);
	return 0;
}