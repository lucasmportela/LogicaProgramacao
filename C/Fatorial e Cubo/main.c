/* main.c */

#include <stdio.h>

#include "biblioteca.h"

int main() {

                int num;

                printf ("Digite um numero:");

                scanf("%d", &num);

                printf("\nO fatorial de %d eh igual a %d e o seu cubo eh %d", num, fatorial(num),retornaCubo(num));
                
			}
            #include "biblioteca.h"

int fatorial (int n){

                int i, resultado;

                resultado = 1;

                for(i=1; i <= n; i++)

                               resultado *= i;

                return resultado;            

}

int retornaCubo (int n){

return (n * n * n);

}
