public class Main{
    public static void main(String[] args) {
        Animal c = new Cachorro("Thor", 3);
        //Cachorro p = new Cachorro("thor", 3);
        c.emitirSom();
        //c.correr();

        Teste t = new Teste();

        t.fazerCorrer(new Cachorro("Thor", 3));
        
    }
}