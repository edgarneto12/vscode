package Notadeaula01.ex01;
import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) {
        //cria um scanner que vai ler oque entra no sistema
        Scanner entrada = new Scanner(System.in);
        // inicia a variável salario
        double salario;
        // imprime na tela a frase "Digite seu salário: R$"
        System.out.print("Digite seu salário: R$ ");
        // define a entrada do usuário na variável salario
        salario = entrada.nextFloat();
        entrada.close();
        double desc5 = (salario - salario * 0.05);
        double desc10 = (salario - salario * 0.1);
        double desc20 = (salario - salario * 0.2);
        // condição caso o salario inserido seja menor que 900 reais
        if (salario <= 900) {
            System.out.printf("Seu salário é isento de imposto logo será de R$ %.2f ", salario);
        } 
        // condição caso o salario inserido esteja entre 901 e 1500 reais
        else if (salario > 900 && salario <= 1500) {
            System.out.println("Seu salário antes do desconto de IR: R$" + salario);
            System.out.printf("Seu salário após desconto de IR (5%): R$ %.2f ", desc5);
        }
        // condição caso o salario inserido esteja entre 1501 e 2500 reais 
        else if (salario > 1500 && salario <= 2500) {
            System.out.println("Seu salário antes do desconto de IR: R$" + salario);
            System.out.printf("Seu salário após desconto de IR (10%): R$ %.2f ", desc10);
        }
        // condição caso o salario inserido esteja acima de 2500 reais
        else if (salario > 2500) {
            System.out.println("Seu salário antes do desconto de IR: R$" + salario);
            System.out.printf("Seu salário após desconto de IR (20%): R$ %.2f ", desc20);
        }
    }
    
}
