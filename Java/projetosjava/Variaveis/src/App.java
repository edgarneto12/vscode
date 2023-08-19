public class App {
    public static void main(String[] args) throws Exception {
        // Variáveis do tipo Inteiro  
        // tipo byte -128/127
        byte numeroPequeno = 127;
        // tipo short -32768/ 32767
        short numeroShort = 32767;
        // tipo int -2147483648/2147483647
        int numeroMaior = 2147483647;
        // tipo long -9223372036854775808l/9223372036854775807l
        long numeroEnorme = -9223372036854775808l;
        
        // Variáveis do tipo Ponto Flutuante
        float peso = 78.7f; 
        double pi = 3.1413;

        // Variáveis do tipo caractere aspas simples
        char letra = 'c';
        
        // Variável booliano true/false
        boolean estouComFome = false;

        // Variável do tipo String Mais de um caractere aspas duplas
        String nome = "Edgar de Souza Lima Neto";

        
        System.out.println(numeroPequeno);
        System.out.println(numeroShort);
        System.out.println(numeroMaior);
        System.out.println(numeroEnorme); 
        System.out.println(peso);
        System.out.println(pi);
        System.out.println(letra);
        System.out.println(estouComFome);
        System.out.println(nome);
    }
}
