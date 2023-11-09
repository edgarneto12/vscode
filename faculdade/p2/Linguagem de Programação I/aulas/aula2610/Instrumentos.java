public abstract class Instrumentos {
    protected String nome;
    protected int codigo;

    public Instrumentos(String nome, int codigo) {
        this.nome = nome;
        this.codigo = codigo;
    }
    //get e set

    public abstract void tocar();
    public abstract void afinar();
}