import java.util.Scanner;

public class aula02 {
    public static void main(String[] args) {
        // Inicia o leitor da entrada do sistema
        Scanner entrada = new Scanner(System.in);
        // Inicia a variável escolha_do_usuario
        int escolha_do_usuario;
        // Imprime mensagem de boas vindas e menu
        System.out.println("------------------------ \nBem Vindo ao Menu da Jampa pets!!! \n[1] Comprar nossos produtos \n[2] Solicitar o valor do produto ou serviço \n[3] Falar com um atendente");
        // Imprime escolha de menu
        System.out.print("Digite o número de acordo com a sua escolha: ");
        // Define a entrada do usuário na variável escolha_do_usuario
        escolha_do_usuario = entrada.nextInt();
        // Fecha o leitor
        entrada.close();
        // Inicia condição de acordo com a entrada
        switch (escolha_do_usuario){
            // Caso o usuário escolha a opção 1 
            case 1:
                System.out.println("Opção 1 escolhida.");
                break;
            // Caso o usuário escolha a opção 2
            case 2:
                System.out.println("Opção 2 escolhida.");
                break;
            // Caso o usuário escolha a opção 3
            case 3:
                System.out.println("Opção 3 escolhida.");
                break;
            // Caso o usuário escolha nenhuma opção ou inexistente
            default:
                System.out.println("Opção invalida! ");
        }
    }
}
