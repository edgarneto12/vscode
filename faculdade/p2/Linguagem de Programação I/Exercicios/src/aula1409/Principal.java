package aula1409;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Pessoa p = new Pessoa();

        System.out.println("Digite sua idade");
        p.setIdade(sc.nextInt());
        sc.close();
        System.out.println("Idade:"+ p.getIdade());
    }
}