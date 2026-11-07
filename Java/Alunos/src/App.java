import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //Exercício : Faça um programa em Java que crie uma lista de alunos, sabendo que
        //qualquer aluno possui nome, matrícula e média. Depois de criada a lista , faça o que se pede:
        //b) imprima os nomes do alunos com média abaixo de 6.0.
        //a) imprima todos os dados de todos os alunos.
        Scanner ent = new Scanner(System.in);

            String nome [] = new String [3];
            double media [] = new double [3];
            int matricula [] = new int [3];
            double soma = 0;
            double MediaGeral = 0;
            int cont = 0;

            for (int i = 1; i<=2; i++){
                System.out.println("\nInformações do aluno "+ i +" :");

                System.out.println("Nome:");
                nome [i] = ent.next();

                System.out.println("Matricula:");
                matricula [i] = ent.nextInt();

                System.out.println("Media:");
                media [i] = Double.parseDouble(ent.next());

                soma = soma + media[i];
            }
            
            ent.close();
            MediaGeral = soma / 2;

            System.out.println("\nMedia da turma:" + MediaGeral);

            for(int i = 1; i <=2; i++){
                if (media[i] < 6.0){
                    cont = cont + 1;
                    System.out.println("\nAbaixo da média: "+ nome[i]);    
                }
            }

            for (int i = 1; i <=2; i++){
                System.out.println("\nAluno: "+ i);
                System.out.println("Nome:" + nome[i]);
                System.out.println("Matricula: "+ matricula[i]);
                System.out.println("Media: " + media[i]);

            }


    }
}
