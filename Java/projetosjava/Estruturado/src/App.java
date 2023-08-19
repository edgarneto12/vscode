public class App {
    public static void main(String[] args) throws Exception {
        String filme = "Vingadores"; // %s 
        int anoLancamento = 2015; // %d 
        int duracao = 240; 
        double notaCritica = 8.7; // %f
        char letraInicial = 'V'; // %c
        boolean foiSucesso = true; // %d
        
        System.out.println(filme);
        System.out.println(anoLancamento);
        System.out.println(duracao);
        System.out.println(notaCritica);
        System.out.println(letraInicial);
        System.out.println(foiSucesso);

        System.out.println("O filme " + filme);
        System.out.println("Ano de lançamento: " + anoLancamento);
        System.out.println("Nota média: " + notaCritica );
        System.out.println("Letra inicial: " + letraInicial);
        System.out.println("Foi um sucesso? " + foiSucesso);
        // O filme <filme> lançado em  <ano> tem uma duração de <duracao> minutos.
        System.out.println("O filme " + filme + " lançado em " + anoLancamento + " tem uma duração de " + duracao + " minutos" );
        System.out.format("O filme %s lançado em  %d tem uma duração de %d minutos.", filme, anoLancamento, duracao);
    }   
}           