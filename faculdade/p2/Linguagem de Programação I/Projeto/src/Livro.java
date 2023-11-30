

public abstract class Livro {
    private String titulo;
    private String autor;
    private int ano;
    private double preco;

    public Livro(String titulo, String autor, int ano, double preco) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.preco = preco;
    }
    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }
    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public abstract String getTipo();

    public String toString() {
        return "Título: " + titulo + "\nAutor: " + autor + "\nAno: " + ano + "\nPreço: R$ " + preco + "\nTipo: " + getTipo();
    }
}



