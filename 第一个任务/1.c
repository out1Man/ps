#include <stdio.h>
#include <malloc.h>
#define SIZE 111111024*1111111024
#include <math.h>
int main()
{
	FILE* a = fopen("C:\\Users\\out Man\\Desktop\\ps���\\task1\\test2.png", "rb");
	fseek(a, 8, 0);//�����ļ���ͷ
	while (1)
	{
		unsigned char b[200] = { 0 };
		unsigned char c[200] = { 0 };
		int x = fread(b, 1, 4, a);//��ȡ����			   
		int y = fread(c, 1, 4, a);//��ȡ����
		c[x] = '\0';
		c[y] = '\0';
		printf("����Ϊ%s ", c);
		int n = (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3];
		printf("����Ϊ%6d ", n);
		fseek(a, n, 1);//�������ݿ�
		printf("crcΪ ");
		printf("%3d ", fgetc(a));//crc��һ���ֽ�
		printf("%3d ", fgetc(a));//crc�ڶ����ֽ�
		printf("%3d ", fgetc(a));
		printf("%3d ", fgetc(a));
		printf("\n");
		if (n==0)
			break;
	}
	return 0;
}











////qsort���� ���ܵĿ�������
////void qsort(void* base,size_t num,size_t width,int (*cmp)(const void* e1,const void* e2))
//#include <stdio.h>
//#include <stdlib.h>
//struct stu
//{
//	char name[20];
//	int age;
//};
//int cmp_int(const void* e1, const void* e2)
//{
//	return *(int*)e1 - *(int*)e2;
//}
//int cmp_float(const void* e1, const void* e2)
//{
//	return (int)(*(float*)e1 - *(float*)e2);
//}
//int cmp_stu(const void* e1, const void* e2)
//{
//	return (((struct stu*)e1)->age) - (((struct stu*)e2)->age);
//}
//void test1()
//{
//	int arr1[] = { 9,8,7,6,5,4,3,2,1,0 };
//	qsort(arr1, sizeof(arr1) / sizeof(arr1[0]), sizeof(arr1[0]), cmp_int);
//	int j = 0;
//	for (j = 0; j < sizeof(arr1) / sizeof(arr1[0]); j++)
//		printf("%d ", arr1[j]);
//	printf("\n");
//}
//void test2()
//{
//	float arr2[] = { 9.0,8.0,7.0,6.0,4.0,3.0 };
//	qsort(arr2, sizeof(arr2) / sizeof(arr2[0]), sizeof(arr2[0]), cmp_int);
//	int j = 0;
//	for (j = 0; j < sizeof(arr2) / sizeof(arr2[0]); j++)
//		printf("%f ", arr2[j]);
//}
//void test3()
//{
//	struct stu s[3] = { {"zhangsan",20},{"lisi",10},{"wuhan",50} };
//	qsort(s, sizeof(s) / sizeof(s[0]), sizeof(s[0]), cmp_stu);
//	
//}
//int main()
//{
//	test1();
//	test2();
//	test3();
//	
//	
//	return 0;
//}
//




























































 

















