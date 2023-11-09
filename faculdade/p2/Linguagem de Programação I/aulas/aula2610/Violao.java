public class Violao extends Instrumentos{
    public Violao(String nome, int codigo) {
        super(nome,codigo);
    }

    @Override
        public void tocar() {
            System.out.println("tlim");
    }

    @Override
        public void afinar() {
            System.out.println("Torou a corda");
    }
}