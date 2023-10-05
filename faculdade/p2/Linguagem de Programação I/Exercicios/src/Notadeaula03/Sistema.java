package Notadeaula03;
import java.util.Scanner;

public class Sistema {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("-=-=Cadastro de professor=-=- ");
        System.out.print("Nome: ");
        String nomeProfessor = scanner.nextLine();
        System.out.print("Idade: ");
        int idadeProfessor = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Especialização: ");
        String especializacao = scanner.nextLine();

        Professor professor = new Professor(nomeProfessor, idadeProfessor, especializacao);

        System.out.println("\n-=-=Cadastro de Aluno=-=-");
        System.out.print("Nome: ");
        String nomeAluno = scanner.nextLine();
        System.out.print("Idade: ");
        int idadeAluno = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Nota 1: ");
        double nota1 = scanner.nextDouble();
        System.out.print("Nota 2: ");
        double nota2 = scanner.nextDouble();
        scanner.nextLine();

        Aluno aluno = new Aluno(nomeAluno, idadeAluno, nota1, nota2);

        System.out.println("\n-=-=Cadastro de Coordenador=-=- ");
        System.out.print("Nome: ");
        String nomeCoordenador = scanner.next();
        System.out.print("Idade: ");
        int idadeCoordenador = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Titulação: ");
        String titulacao = scanner.nextLine();

        Coordenador coordenador = new Coordenador(nomeCoordenador, idadeCoordenador, titulacao);

        System.out.println("\nDados cadastrados:\n");
        System.out.println("Professor: ");
        professor.exibirDados();
        System.out.println("\nAluno: ");
        aluno.exibirDados();
        System.out.println("\nCoordenador: ");
        coordenador.exibirDados();
    }
}
