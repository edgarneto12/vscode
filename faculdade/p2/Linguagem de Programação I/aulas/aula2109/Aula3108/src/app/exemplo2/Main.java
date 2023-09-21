package app.exemplo2;

public class Main {
    public static void main(String[] args) {
        Aluno a = new Aluno("João", 12345);

        System.out.println("Nome: "+ a.getNome());
        System.out.println("Matrícula: " + a.getIdade());
    }
}