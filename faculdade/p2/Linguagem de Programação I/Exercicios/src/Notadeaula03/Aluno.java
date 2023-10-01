package Notadeaula03;

class Aluno extends Pessoa{
    private double nota1;
    private double nota2;

    public Aluno(String nome, int idade, double nota1, double nota2) {
        super(nome, idade);
        this.nota1 = nota1;
        this.nota2 = nota2;
    }
    
}
