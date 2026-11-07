#include <stdio.h>

#include <stdlib.h>

#include <pthread.h>



void * imprime_mensagem (void * ptr);



int main()

{

pthread_t threadUm, threadDois;

char * mensagem1 = "threadUm: Frase 1";

char * mensagem2 = "threadDois Frase 2";

int retorno1, retorno2;



/* Crie threads independentes, cada uma deles executará a função. */



retorno1 = pthread_create (&threadUm, NULL, imprime_mensagem, (void *) mensagem1);

retorno2 = pthread_create (&threadDois, NULL, imprime_mensagem, (void *) mensagem2);



/* Aguarde até que as threads sejam concluídas antes que o main continue. */



pthread_join (threadUm, NULL);

pthread_join (threadDois, NULL);



printf ("A threadUm retornou: %d \n", retorno1);

printf ("A threadDois retornou: %d \n", retorno2);

exit(0);

}



void * imprime_mensagem (void * ptr)

{

char * mensagem;

mensagem = (char *) ptr;

printf (" %s \n", mensagem);

}