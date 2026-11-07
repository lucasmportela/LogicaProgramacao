package biblioteca;

public interface Controle extends Regras {

// Todos os atributos definidos em uma interface

// são implicitamente static e final

int POTENCIAMAXIMA = 350; // static e final

int POTENCIAMINIMA = 120; // static e final

// Somente os métodos Getters

// como os atributos em uma interface são final

//não poderão ser alterados, ou seja, não teremos

// os métodos Setters

public int getPotenciaMaxima( );

public int getPotenciaMinima( );

// Todos os métodos definidos em uma interface

// são implicitamente public e abstract

void assar(int potencia); // public e abstract

void aquecer(int potencia); // public e abstract

void desligar(); // public e abstract

}