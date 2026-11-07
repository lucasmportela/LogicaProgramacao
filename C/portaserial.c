#include<windows.h>

#include<stdio.h>

int main()

{

HANDLE hComm;

hComm = CreateFile("COM1", //Nome da porta

GENERIC_READ | GENERIC_WRITE, //Leitura/escrita

0, //Sem compartilhamento

NULL, //Sem segurança

OPEN_EXISTING, //Abre somente a porta existente

0, //Sem sobreposição de E/S

NULL); //Null para porta serial
  
if (hComm == INVALID_HANDLE_VALUE)

printf("Erro ao abrir porta serial");

else

printf("Abrindo porta serial com sucesso");

CloseHandle(hComm); //Fechando porta serial

return 0;

}