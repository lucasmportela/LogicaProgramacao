#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome[50];
    float nota;
    int i = 0, num;

    FILE *fptr;
    fptr = fopen("alunos.txt","a");

        if(fptr == NULL)
        {
            printf("Erro ao abrir arquivo!");
            exit(1);
        }

        printf("Para o aluno %d \nEntre com o nome: ", i+1);
        scanf("%s", &nome);

        printf("Entre com a nota: ");
        scanf("%f", &nota);

        fprintf(fptr,"\nNome: %s \nNota=%.2f \n", nome, nota);

    fclose(fptr);
    return 0;
}