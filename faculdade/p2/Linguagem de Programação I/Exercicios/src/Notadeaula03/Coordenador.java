package Notadeaula03;

class Coordenador extends Pessoa {
    private String titulacao;

    public Coordenador(String nome, int idade, String titulacao) {
        super(nome,idade);
        this.titulacao = titulacao;
    }

    public void exibirDados() {
        super.exibirDados();
        System.out.println("Titulação: " + titulacao);
    }
}
