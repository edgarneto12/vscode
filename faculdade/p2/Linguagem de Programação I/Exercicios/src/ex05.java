import java.util.Scanner;
public class ex05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Pessoa p = new Pessoa();
        System.out.print("Digite a sua idade: ");
        p.idade = entrada.nextInt();
        System.out.println("antiga "+ p.idade);
        p.niver();
        System.out.println("atual: "+ p.idade);

    }
}