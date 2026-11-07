#include <stdio.h>
#include <conio.h>

int main (void){
    int v_num = 10;
    
    int *ptr;

    ptr = &v_num;

    printf("Ponteiros:");
    printf("Conteudo da variavel v_num: %d \n",v_num);
    printf("Endereco da variavel v_num: %x \n", &v_num);
    printf("Conteudo da variavel ponteiro prt: %x", ptr);

    getch();
    return(0);

}
