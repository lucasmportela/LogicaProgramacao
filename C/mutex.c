#include <stdio.h>

#include <pthread.h>



#define MAXTHREADS 10

void *funcaoC (void *);

pthread_mutex_t meuMutex = PTHREAD_MUTEX_INITIALIZER;

int contador = 0;



void main ()

{

pthread_t identificacaoDaThread [ MAXTHREADS ];

int i, j;



for (i = 0; i<MAXTHREADS; i ++)

{

pthread_create (&identificacaoDaThread[ i ], NULL, funcaoC, NULL);

}



for (j = 0; j<MAXTHREADS; j ++)

{

pthread_join (identificacaoDaThread [j], NULL);

}

//* Agora que todas as threads estão completas, posso imprimir o resultado final. Sem o uso da junção, o printf abaixo poderia ser chamado antes de todas as threads sejam concluídas e imprimir o valor final incorreto. * //



printf ("Valor final do contador: %d \n", contador);

}



void *funcaoC(void *meuPTR)

{

printf ( "Número desta thread: %ld \n", pthread_self() );

pthread_mutex_lock( &meuMutex );

contador++;

pthread_mutex_unlock( &meuMutex );

}