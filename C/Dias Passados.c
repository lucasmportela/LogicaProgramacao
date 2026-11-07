
#include <stdio.h>

#include <time.h> //necessário para usar localtime() e struct tm

int main(void)

{

 //ponteiro para struct que armazena data e hora

 struct tm *data_hora_atual;

//variável do tipo time_t para armazenar o tempo atual

 time_t curtime;

 //obtém hora corrente do sistema

 curtime = time(NULL);

 //converte para a hora local

 data_hora_atual = localtime(&curtime);

//extrai o dia do ano de 1 a 365 da struct tm

 printf("\nDia do ano...: %d\n", data_hora_atual->tm_yday);

 return 0;
}