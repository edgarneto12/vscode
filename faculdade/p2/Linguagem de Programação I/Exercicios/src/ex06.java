import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        soma p = new soma();
        p.n1 = entrada.nextInt();
        System.out.print("Digite outro número inteiro: ");
        p.n2 = entrada.nextInt();
        p.soman1n2();
        System.out.println(p.total);
    }

}