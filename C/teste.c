//4. Desenvolva um programa em C que leia a altura de pessoas, cujo nÃºmero de pessoas Ã© dado pelo usuÃ¡rio. Este programa deverÃ¡ verificar e mostrar:

//a. A menor altura do grupo;

//b. A maior altura do grupo.

#include <stdio.h>
float altura, maior, menor= 99999;
int pessoas;

int main(){

    printf("Quantas pessoa sao?\n");
    scanf("%d", &pessoas);
for(int i = 0; i <pessoas; i++)
{
    printf("Digite a sua altura:\n");
    scanf("%f", &altura);


    if (altura > maior){
        maior = altura;
    }
    if (altura < menor){
        menor = altura;
    }
 }

    printf("A maior pessoa e: %.2f\n", maior);
    printf("A menor pessoa e: %.2f\n", menor);
}