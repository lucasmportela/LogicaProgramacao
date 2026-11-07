/* Biblioteca.c */

#include "biblioteca.h"

int main (int n){

                int i, resultado;

                resultado = 1;

                for(i=1; i <= n; i++)

                               resultado *= i;

                return resultado;            

}

int retornaCubo (int n){

return (n * n * n);

}
