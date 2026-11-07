//3. Escreva um programa em C que leia um valor inicial A e imprima a sequência de valores do cálculo de fatorial de A (A!) 
//e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120.
#include<stdio.h>

int fat = 1, A, n;

int main()

{
  printf("Digite um número a ser fatorado:\n"); 
  scanf("%d", &A) ;

  for(n = A; n > 1; n--)

  {

      printf("%d x ", n);

      fat = fat * n;

  }

  printf("%d ", n);

  printf(" = %d", fat);

}