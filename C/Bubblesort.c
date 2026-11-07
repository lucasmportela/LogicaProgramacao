#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#define TAM 5

int main (){
    setlocale(LC_ALL, "");

    int numeros[TAM];
    int i, aux, contador;

    printf("Digite 5 numeros:\n");
    for (i = 0; i <TAM; i++){
        scanf("%d", &numeros[i]);
    }

    printf("Ordem dos numeros:\n");

    for (i = 0; i < TAM; i++){
        printf("%4d", numeros[i]);
    }

    for (contador = 1; contador < TAM; contador++){
        for (i = 0; i < TAM - 1; i++){
            if(numeros[i] > numeros[i + 1]){
                aux = numeros [i];
                numeros[i] = numeros [i + 1];
                numeros[i + 1] = aux;
            }
        }
    }

    printf("\n Numeros em ordem crescente: \n");

    for (i = 0; i < TAM; i ++){
        printf("%4d", numeros[i]);
    }

     for (contador = 1; contador < TAM; contador++){
        for (i = 0; i < TAM - 1; i++){
            if(numeros[i] < numeros[i + 1]){
                aux = numeros [i];
                numeros[i] = numeros [i + 1];
                numeros[i + 1] = aux;
            }
        }
    }

    printf("\n Numeros em ordem decrescente: \n");

    for (i = 0; i < TAM; i ++){
        printf("%4d", numeros[i]);
    }

    return 0;
}