import java.util.Scanner;

public class ex08 {
    public static void main(String[] args) {
        calculoex08 p = new calculoex08();
        Scanner entrada = new Scanner(System.in);
        Scanner entrada2 = new Scanner(System.in);
        System.out.println("Digite o nome do aluno: ");
        p.nome = entrada.nextLine();
        System.out.println("Digite a primeira nota: ");
        p.n1 = entrada2.nextFloat();
        System.out.println("Digite a segunda nota: ");
        p.n2 = entrada2.nextFloat();
        System.out.println("Digite a terceira nota: ");
        p.n3 = entrada2.nextFloat();
        p.media();
    }

}