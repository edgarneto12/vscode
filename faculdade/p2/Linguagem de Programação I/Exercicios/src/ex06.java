import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        soma p = new soma();
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite um número inteiro: ");
        p.n1 = entrada.nextInt();
        System.out.print("Digite outro número inteiro: ");
        p.n2 = entrada.nextInt();
        entrada.close();
        p.soman1n2();
        System.out.println(p.total);
    }

}