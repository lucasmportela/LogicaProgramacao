
public class App {
    public static void main(String[] args) {
        //Sabendo que todo livro possui autor, editora e preço, crie uma classe pública
        //comconstrutor padrão e métodos modificadores e de acesso. Depois, crie dois livros com
        //dados obtidos via console.


        Livro livro1 = new Livro(" ", 0 , " ");
        livro1.entrada();
        livro1.imprimir();

        Livro livro2 = new Livro(" ", 0 , " ");
        livro2.entrada();
        livro2.imprimir();
 
    }
}
