#include <stdlib.h>

#include <pthread.h>

#include <stdio.h>



int main (int argc, char ** argv)
{

    int IdentificacaoDoProcesso; /*PID – Identificação do processo junto ao S.O.*/

    IdentificacaoDoProcesso = fork ();



    if( IdentificacaoDoProcesso == 0 ) /*Este é o processo Filho*/

    {

    printf ("Eu sou o processo filho: PID = %d \n", getpid() );

    }

    else if ( IdentificacaoDoProcesso > 0 ) /* Este é o processo pai*/

    {

    printf ("Eu sou o processo pai com PID = %d, o PID do filho é = %d \n", getpid(), IdentificacaoDoProcesso);

    }

    else

    {

    printf( "Erro ao tentar criar processo filho\n" );

    perror ( "fork" );

    exit( 1 );

    }

    exit( 0 );

}