#include <Windows.h>

#include <stdio.h>

#include <string.h>

int main(void)

{

HANDLE hComm;

char ComPortName[] = "COM1"; //Nome da porta a ser aberta.

BOOL Status;

printf("\n\n +==========================================+");

printf("\n | Transmissao Serial |");

printf("\n +==========================================+\n");

/*--------- Abrindo a porta serial -------------*/

hComm = CreateFile( ComPortName, //Nome da porta

GENERIC_READ | GENERIC_WRITE, //Modo leitura/escrita

0, //Sem compartilhamento

NULL, //Sem segurança

OPEN_EXISTING, //Abre somente a porta existente

0, //Sem sobreposição de E/S

NULL); //Null para porta serial

if (hComm == INVALID_HANDLE_VALUE)

printf("\n Erro! - Port %s nao pode ser aberta\n", ComPortName);

else

printf("\n Porta %s aberta\n ", ComPortName);

/*--- Ajustando os parâmetros para a porta serial -----*/

DCB dcbSerialParams = { 0 }; //Inicializando a estrutura DCB

dcbSerialParams.DCBlength = sizeof(dcbSerialParams);

Status = GetCommState(hComm, &dcbSerialParams); //Recebendo o estado corrente

if (Status == FALSE)

printf("\n Erro! em ajustar GetCommState()");

dcbSerialParams.BaudRate = CBR_115200; //Ajustando Baud Rate = 115200

dcbSerialParams.ByteSize = 8; //Tamanho do byte de dados dcbSerialParams.StopBits = ONESTOPBIT; //Ajustando stop bits = 1

dcbSerialParams.Parity = NOPARITY; //Ajustando sem paridade

Status = SetCommState(hComm, &dcbSerialParams);

//Configurando a porta de acordo com os ajustes em DCB

if (Status == FALSE)

{

printf("\n Erro! ao ajustar estrutura DCB");

}

else //Se houve sucesso, mostra os valores ajustados

{

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

printf("\n Erro em ajustar TimeOuts");

else

printf("\n\n Escreva dados para a porta e tecle Enter\n\n... ");

///////////////////////////////////////////////////////////

/*--------- Ajustando a máscara para receber ---------------*/

Status = SetCommMask(hComm, EV_RXCHAR); //Configura Windows para monitorar a porta serial

if (Status == FALSE)

printf("\n\n Erro! em ajustar CommMask");

else

;

///////////////////////////////////////////////////////////

while(1) {

char lpBuffer[100];

fgets(lpBuffer, 100, stdin); //Recebe string do usuário

/*---------- Escrevendo caracteres para a porta serial -----------------------*/

DWORD dNoOFBytestoWrite; //Número de bytes para escrever na porta

DWORD dNoOfBytesWritten = 0; //Número de bytes escritos na porta

dNoOFBytestoWrite = strlen(lpBuffer); //Calculando o número de bytes (caracteres) a escrever

Status = WriteFile(hComm,

lpBuffer, //Dados a serem escritos

dNoOFBytestoWrite,

&dNoOfBytesWritten,

NULL);

if (Status == TRUE)

;//printf(“\n %s \n”, lpBuffer); //Imprime dados escritos na porta

else

printf("\n\n Erro %d ao escrever na porta serial",GetLastError());

DWORD dwEventMask; //Máscara de evento para capturar

DWORD NoBytesRead; //Bytes lidos pela função ReadFile()

int i = 0;

Status = WaitCommEvent(hComm, &dwEventMask, NULL); //Aguarda por caractere

/////////////////////////////////////////////////////////////////

/*-------- Programa aguarda aqui até o caractere ser recebido ------------*/

char TempChar; //Caractere temporário

char SerialBuffer[2560]; //Buffer contendo dados recebidos

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

for (j = 0; j < i-1; j++) //j < i-1 para remover o último caractere duplicado

printf("%c", SerialBuffer[j]);

}

////////////////////////////////////////////////////////

}

CloseHandle(hComm);

printf("\n ===================================\n");

}