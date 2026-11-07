#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    float num;
    FILE *fptr;

    if ((fptr = fopen("program.txt","r")) == NULL){
        printf("Erro ao abrir o arquivo.");
        //Se o arquivo não existe, retorna NULL
        exit(1);
    }

        fscanf(fptr,"%f", &num);
        printf("Valor lido do arquivo e = %.1f", num);
    fclose(fptr);

    return 0;
}