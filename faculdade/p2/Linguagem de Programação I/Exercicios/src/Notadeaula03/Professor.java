package Notadeaula03;

class Professor extends Pessoa {
    private String espec;

    public Professor(String nome, int idade, String espec) {
        super(nome, idade);
        this.espec = espec;
    }

    public void exibirDados() {
        super.exibirDados();
        System.out.println("Especialização: " + espec);
    }
}
