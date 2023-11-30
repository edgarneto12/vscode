public class Ficcao extends Livro {
    private String genero;

    public Ficcao(String titulo, String autor, int ano, double preco, String genero) {
        super(titulo, autor, ano, preco);
        this.genero = genero;
    }
    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    // Método que retorna o tipo do livro
    public String getTipo() {
        return "Ficção";
    }
    // Método que retorna uma representação textual do livro
    public String toString() {
        // Chamando o método da classe pai
        return super.toString() + "\nGênero: " + genero;
    }
}


