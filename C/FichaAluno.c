#include <stdio.h>
#include <conio.h>

int main (void){

struct ficha_aluno{

char nome[50];
char disciplina[30];
float nota_1;
float nota_2;

};

struct ficha_aluno aluno;

  printf("\n------------cadastro do aluno------------\n");
  printf("Nome do aluno:");
  fflush(stdin);
  fgets(aluno.nome, 40, stdin);

  printf("Disciplina:");
  fgets(aluno.disciplina, 40,stdin);

  printf("Informe a primeira nota:");
  scanf("%f", &aluno.nota_1);

  printf("Informe a segunda nota:");
  scanf("%f", &aluno.nota_2);

  printf("\n------------lendo dados------------\n");
  printf("Nome: %s", aluno.nome);
  printf("Disciplina: %s", aluno.disciplina);
  printf("Nota da prova 1: %.2f\n", aluno.nota_1);
  printf("Nota da prova 2: %.2f\n", aluno.nota_2);

  getch();
  return(0);

};
