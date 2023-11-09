public class Cachorro extends Animal implements Corrida{
    public Cachorro(String nome, int idade) {
        super(nome,idade);
    }

    @Override
        public void emitirSom() {
            System.out.println("auau");
    }

    @Override
        public void correr() {
            System.out.println("Estou correndo rápido");
    }
}