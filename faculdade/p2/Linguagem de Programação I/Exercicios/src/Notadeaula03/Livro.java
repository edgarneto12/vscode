package Notadeaula03;

public class Livro {
    //Declarar atributos
    private String titulo;
    private String autor;
    private int ano_lacamento;

    //Construtor da classe
    public Livro(String titulo, String autor, int ano_lacamento) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano_lacamento = ano_lacamento; 
    }

    public void exibirInformacoes() {
        // Implementar a exibição dos atributos
        System.out.println("Livro: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano que foi lançado: " + ano_lacamento);

        
    }
  
    public static void main(String[] args) {
        Livro meuLivro = new Livro("Aventuras de Sherlock Holmes", "Arthur Doyle", 1892);

        // Imprime as Informaçoes do livro
        meuLivro.exibirInformacoes();
}
    }
