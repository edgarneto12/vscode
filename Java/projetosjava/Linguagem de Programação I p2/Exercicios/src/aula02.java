import java.util.Scanner;

public class aula02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int escolha_do_ususario;
        System.out.println("------------------------ \nBem Vindo ao Menu da Jampa pets!!! \n[1] Comprar nossos produtos \n[2] Solicitar o valor do produto ou serviço \n[3] Falar com um atendente");
        System.out.print("Digite o número de acordo com a sua escolha: ");
        escolha_do_ususario = entrada.nextInt();
        entrada.close();
        switch (escolha_do_ususario){
            case 1:
                System.out.println("Opção 1 escolhida.");
                break;
            case 2:
                System.out.println("Opção 2 escolhida.");
                break;
            case 3:
                System.out.println("Opção 3 escolhida.");
                break;
        }

    }
}
