#include <stdio.h>
int main()
{
int X;
float Y;
printf("\n\n Entre com um inteiro e um fracionario:\n");
printf("---------------------------------------\n");

scanf("%d %f", &X, &Y);
printf("\n\n Numero inteiro: %d \n Numerofracionario %.2f \n", X, Y);
return 0;
}