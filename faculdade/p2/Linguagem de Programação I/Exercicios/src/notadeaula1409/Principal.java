package notadeaula1409;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            Pessoa p = new Pessoa();

            System.out.print("Digite seu peso: ");
            p.setPeso(sc.nextDouble());
            System.out.print("Digite sua altura: ");
            p.setAltura(sc.nextDouble());
            sc.close();
            System.out.printf("Seu Imc é: %.2f", p.getImc());


        }  
}
