#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

typedef struct NO{
    int dado;
    struct NO *prox;
}NO;

typedef struct FILA{
    NO *ini;
    NO *fim;
}FILA;

void inicializaFila(FILA *f){
    f->ini = NULL;
    f->fim = NULL;
}

void enfileira(int dado, FILA *f){
    NO *ptr = (NO*) malloc(sizeof(NO));
    if(ptr == NULL){
        printf("Erro alocacao de no\n");
        return;
    } else{
        ptr->dado = dado;
        ptr->prox = NULL;
        if(f->ini == NULL){
            f->ini = ptr;
        } else {
            f->fim->prox = ptr;
        }
        f->fim = ptr;
        return;
    }
}

int desenfileira(FILA *f){
    NO *ptr = f->ini;
    int dado;
    if(ptr != NULL){
        f->ini = ptr->prox;
        ptr->prox = NULL;
        dado = ptr->dado;
        free(ptr);
        if(f->ini == NULL){
            f->fim = NULL;
        }
        return dado;
    } else{
        printf("Fila vazia.\n");
        return 0;
    }
}

void imprimeFila(FILA *f){
    NO *ptr = f->ini;
    if(ptr != NULL){
        while (ptr !=NULL){
            printf("%d ", ptr->dado);
            ptr = ptr->prox;
        }
        printf("\n");
    } else{
            printf("Fila vazia.\n");
            return;
    }
}

int main(){
    FILA *f1 = (FILA*) malloc(sizeof(FILA));
    if(f1 == NULL){
        printf("Erro de alocacao da fila.\n");
        exit(-1);  
    } else{

        inicializaFila(f1);

        enfileira(2, f1);
        enfileira(3, f1);
        enfileira(1, f1);

        imprimeFila(f1);

        printf("Tentando desenfileirar - resultado: %d\n", desenfileira(f1));
        imprimeFila(f1);
        printf("Tentando desenfileirar - resultado: %d\n", desenfileira(f1));
        imprimeFila(f1);
        printf("Tentando desenfileirar - resultado: %d\n", desenfileira(f1));
        imprimeFila(f1);

    }
}