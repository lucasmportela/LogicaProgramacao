package App;
import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        ArrayList letras = new ArrayList();
        ArrayList contador = new ArrayList();
        String str;

        // Le a string
        System.out.println("Digite uma string:");
        str = t.nextLine();
        t.close();

        // Retira os espacos do fim e do inicio
        str = str.trim();

        // Converte tudo para maiuscula
        str = str.toUpperCase();

        // Percorre a string caracter por caracter

            for (int i = 0; i < str.length(); i++) {
                // Pega o caracter da i-esima posicao
                char c = str.charAt(i);

                // Verifica se caracter esta no intervalo de A a Z
                if (c >= 'A' && c <= 'Z') {
                // Verificar se a letra ja existe na lista de letras

                    if (letras.contains(c)) {
                        // Incrementa o contador da letra
                        // Recuperar a posicao da letra na lista
                        int p = letras.indexOf(c);

                        // Incrementar o contador na posicao P
                        int cont = (int) contador.get(p);
                        cont++;
                        contador.set(p, cont);
                    }
                    else {
                            // Inserir a letra na lista de letras com contador = 1
                            letras.add(c);

                            // Inserir o 1 no contador
                            contador.add(1);
                    }
                }
            }

        System.out.println("Estatistica:");

        for (int i = 0; i < letras.size(); i++)
        System.out.printf("%c %d\n", letras.get(i), contador.get(i));

    }
}
