public class NaoFiccao extends Livro {
    private String tema;

    public NaoFiccao(String titulo, String autor, int ano, double preco, String tema) {
        super(titulo, autor, ano, preco);
        this.tema = tema;
    }
    public String getTema() {
        return tema;
    }

    public void setTema(String tema) {
        this.tema = tema;
    }

    // Método que retorna o tipo do livro
    public String getTipo() {
        return "Não-ficção";
    }
    // Método que retorna uma representação textual do livro
    public String toString() {
        // Chamando o método da classe pai
        return super.toString() + "\nTema: " + tema;
    }
}

