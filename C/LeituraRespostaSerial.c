#include <Windows.h>

#include <stdio.h>

int main(void)

{

HANDLE hComm;

char ComPortName[] = "COM2"; //Nome da porta a ser aberta

BOOL Status; //Estado de operações

DWORD dwEventMask; //Máscara de evento para capturar

char TempChar; //Caractere temporário

char SerialBuffer[2560]; //Buffer contendo dados recebidos

DWORD NoBytesRead; //Bytes lidos pela função ReadFile()

int i = 0;

char c;

printf("\n\n +====================================+");

printf("\n | Recepcao por porta serial |");

printf("\n +===================================+\n");

/*--------- Abrindo a porta serial -------------*/

hComm = CreateFile( ComPortName, //Nome da porta

GENERIC_READ | GENERIC_WRITE, //Modo leitura/escrita

0, //Sem compartilhamento

NULL, //Sem segurança

OPEN_EXISTING, //Abre somente a porta existente

0, //Sem sobreposição de E/S

NULL); //Null para porta serial

if (hComm == INVALID_HANDLE_VALUE)

printf("\n Erro! - Porta %s nao pode ser aberta\n", ComPortName);

else

printf("\n Porta %s aberta\n ", ComPortName);

/*--- Ajustando os parâmetros para a porta serial -----*/

DCB dcbSerialParams = { 0 }; //Inicializando a estrutura DCB

dcbSerialParams.DCBlength = sizeof(dcbSerialParams);

Status = GetCommState(hComm, &dcbSerialParams); //Recebendo o estado corrente

if (Status == FALSE)

printf("\n Erro em GetCommState()");

dcbSerialParams.BaudRate = CBR_115200; //Ajustando Baud Rate = 115200

dcbSerialParams.ByteSize = 8; //Tamanho do byte = 8 dadosdcbSerialParams.StopBits = ONESTOPBIT; //Ajustando stop bits = 1

dcbSerialParams.Parity = NOPARITY; //Ajustando sem paridade

Status = SetCommState(hComm, &dcbSerialParams); //Configurando a porta de acordo com os ajustes em DCB

if (Status == FALSE)

{

printf("\n Erro em ajustar estrutura DCB");

}

else //Se houve sucesso, mostra os valores ajustados

{

//printf(“\n\n Setting DCB Structure Successfull\n”);

printf("\n Baudrate = %d", dcbSerialParams.BaudRate);

printf("\n ByteSize = %d", dcbSerialParams.ByteSize);

printf("\n StopBits = %d", dcbSerialParams.StopBits);

printf("\n Parity = %d", dcbSerialParams.Parity);

}

/*------ Ajustando timeouts --------------*/

COMMTIMEOUTS timeouts = { 0 };

timeouts.ReadIntervalTimeout = 50;

timeouts.ReadTotalTimeoutConstant = 50;

timeouts.ReadTotalTimeoutMultiplier = 10;

timeouts.WriteTotalTimeoutConstant = 50;

timeouts.WriteTotalTimeoutMultiplier = 10;

if (SetCommTimeouts(hComm, &timeouts) == FALSE)

printf("\n\n Erro em ajustar TimeOuts");

/*--------- Ajustando a máscara para receber -----------------*/

Status = SetCommMask(hComm, EV_RXCHAR); //Configura Windows para monitorar a porta serial

if (Status == FALSE)

printf("\n\n Erro! em ajustar CommMask");

else

printf("\n\n Aguardando recepcao de dados\n\n... ");

while (1){

/*------------ Ajustando evento WaitComm() -------*/

Status = WaitCommEvent(hComm, &dwEventMask, NULL); //Aguarda por caractere

/*-------- Programa aguarda aqui até o caractere ser recebido ------------*/

if (Status == FALSE)

{

printf("\n Erro ao ajustar WaitCommEvent()");

}

else //SE WaitCommEvent()==True LÍ a string com ReadFile();

{

i=0;

do

{

Status = ReadFile(hComm, &TempChar, sizeof(TempChar), &NoBytesRead, NULL);

SerialBuffer[i] = TempChar;

i++;

}

while (NoBytesRead > 0);

/*------------ Imprime a string lida ----------------------*/

printf("\n ");

int j =0;

for (j = 0; j < i; j++) //j < i-1 para remover o último caractere duplicado

printf("%c", SerialBuffer[j]);

}

////////////////////////////////////////

char lpBuffer[100];

char pergunta1[] = "Qual a sua idade?";

char pergunta2[] = "Onde voce nasceu?";

char pergunta3[] = "Onde voce vive?";

char pergunta4[] = "Tudo bem?";

int r1 = strncmp(pergunta1, SerialBuffer, 17);

if (r1 == 0)

strcpy (lpBuffer," 30 anos!\n\n" );

int r2 = strncmp(pergunta2, SerialBuffer, 17);

if (r2 == 0)

strcpy (lpBuffer, "Em Sao Paulo\n\n" );

int r3= strncmp(pergunta3, SerialBuffer, 15);

if (r3 == 0)

strcpy (lpBuffer, "Em Vitoria - ES\n\n" );

int r4= strncmp(pergunta4, SerialBuffer, 9);

if (r4 == 0)

strcpy (lpBuffer, "Tudo bem. E você?\n\n" );

if (r1 != 0 && r2 != 0 && r3 != 0 && r4 != 0)

strcpy (lpBuffer, "Nao entendi a pergunta.\n\n");

/*-------- Escrevendo caracteres para a porta serial -------------------*/

DWORD dNoOFBytestoWrite; //Número de bytes para escrever na porta

DWORD dNoOfBytesWritten = 0; //Número de bytes escritos na porta

dNoOFBytestoWrite = strlen(lpBuffer); //Calculando o número de bytes (caracteres) a escrever

Status = WriteFile(hComm,

lpBuffer, //Dados a serem escritos

dNoOFBytestoWrite,

&dNoOfBytesWritten,

NULL);

if (Status == TRUE)

;

else

printf("\n\n Erro %d ao escrever na porta serial",GetLastError());

/////////////////////////////////////

}

CloseHandle(hComm); //Fecha a porta serial

printf("\n +=====================================+\n");

}