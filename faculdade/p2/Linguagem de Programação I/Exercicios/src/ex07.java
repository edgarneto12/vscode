import java.util.Scanner;

public class ex07 {
    public static void main(String[] args) {
        calculoex07 p = new calculoex07();
        Scanner entrada = new Scanner(System.in);
        Scanner entrada2 = new Scanner(System.in);
        System.out.print("Digite sua Matrícula: ");
        p.matricula = entrada.nextInt();
        System.out.print("Digite seu nome completo: ");
        p.nome = entrada2.nextLine();
        System.out.print("Digite seu salario: ");
        p.salariobruto = entrada.nextDouble();
        p.desconto();
    }
}