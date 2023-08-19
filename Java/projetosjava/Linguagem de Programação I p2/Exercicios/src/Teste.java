import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {
        while(true) {
            try{
                //cria um scanner que vai ler oque entra no sistema
                Scanner entrada = new Scanner(System.in);
                // inicia a variável salario
                //int salario;
                // imprime na tela a frase "Digite seu salário: R$"
                System.out.print("Digite seu salário: R$ ");
                // define a entrada do usuário na variável salario
                double salario = entrada.nextDouble();
                // condição caso o salario inserido seja menor que 900 reais
                if (salario <= 900) {
                    System.out.println("Seu salário é isento de imposto logo será de R$" + salario);
                } 
                // condição caso o salario inserido esteja entre 901 e 1500 reais
                else if (salario > 900 && salario <= 1500) {
                    System.out.println("Seu salário antes do desconto de IR: R$" + salario);
                    System.out.println("Seu salário após desconto de IR (5%): R$" + (salario - salario * 5/100));
                }
                // condição caso o salario inserido esteja entre 1501 e 2500 reais 
                else if (salario > 1500 && salario <= 2500) {
                    System.out.println("Seu salário antes do desconto de IR: R$" + salario);
                    System.out.println("Seu salário após desconto de IR (10%): R$" + (salario - salario * 10/100));
                }
                // condição caso o salario inserido esteja acima de 2500 reais
                else if (salario > 2500) {
                    System.out.println("Seu salário antes do desconto de IR: R$" + salario);
                    System.out.println("Seu salário após desconto de IR (20%): R$" + (salario - salario * 20/100));
                }
                break;
            } catch (Exception e) {
                System.out.println("Escreva um número válido!!");
            }

        }
    }
}
