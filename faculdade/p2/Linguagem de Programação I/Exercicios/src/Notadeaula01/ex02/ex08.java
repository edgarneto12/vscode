package Notadeaula01.ex02;
import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        calculoex08 p = new calculoex08();
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite o nome do aluno: ");
        p.nome = entrada.nextLine();
        System.out.print("Digite a primeira nota: ");
        p.n1 = entrada.nextFloat();
        System.out.print("Digite a segunda nota: ");
        p.n2 = entrada.nextFloat();
        System.out.print("Digite a terceira nota: ");
        p.n3 = entrada.nextFloat();
        entrada.close();
        p.media();
    }

}