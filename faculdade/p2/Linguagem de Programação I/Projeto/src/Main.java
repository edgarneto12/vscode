import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {

        Sistema sistema = new Sistema();

        Ficcao f1 = new Ficcao("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 99.90, "Fantasia");
        Ficcao f2 = new Ficcao("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 29.90, "Fantasia");
        NaoFiccao n1 = new NaoFiccao("Uma Breve História do Tempo", "Stephen Hawking", 1988, 39.90, "Ciência");
        NaoFiccao n2 = new NaoFiccao("O Diário de Anne Frank", "Anne Frank", 1947, 19.90, "História");

        sistema.cadastrarLivro(f1);
        sistema.cadastrarLivro(f2);
        sistema.cadastrarLivro(n1);
        sistema.cadastrarLivro(n2);

        sistema.imprimirLivros();

        Livro livro = sistema.consultarLivro("Harry Potter e a Pedra Filosofal");

        if (livro != null) {
            System.out.println("Livro encontrado:");
            System.out.println(livro);
        } else {
            System.out.println("Livro não encontrado");
        }

        ArrayList<Livro> ficcoes = sistema.listarLivrosPorTipo("Ficção");

        if (!ficcoes.isEmpty()) {
            System.out.println("\nLivros de ficção:");
            for (Livro ficcao : ficcoes) {
                System.out.println(ficcao);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de ficção");
        }
        ArrayList<Livro>naoFiccoes = sistema.listarLivrosPorTipo("Não-ficção");

        if (!naoFiccoes.isEmpty()) {
            System.out.println("Livros de não-ficção:");
            for (Livro naoFiccao : naoFiccoes) {
                System.out.println(naoFiccao);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de não-ficção");
        }

        ArrayList<Livro> tolkiens = sistema.listarLivrosPorAutor("J.R.R. Tolkien");

        if (!tolkiens.isEmpty()) {
            System.out.println("Livros de J.R.R. Tolkien:");
            for (Livro tolkien : tolkiens) {
                System.out.println(tolkien);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de J.R.R. Tolkien");
        }

        ArrayList<Livro> livros1997 = sistema.listarLivrosPorAno(1997);

        if (!livros1997.isEmpty()) {
            System.out.println("Livros de 1997:");
            for (Livro livro1997 : livros1997) {
                System.out.println(livro1997);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de 1997");
        }

        ArrayList<Livro> fantasias = sistema.listarLivrosPorGenero("Fantasia");

        if (!fantasias.isEmpty()) {
            System.out.println("Livros de fantasia:");
            for (Livro fantasia : fantasias) {
                System.out.println(fantasia);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de fantasia");
        }

        ArrayList<Livro> historias = sistema.listarLivrosPorTema("História");

        if (!historias.isEmpty()) {
            System.out.println("Livros de história:");
            for (Livro historia : historias) {
                System.out.println(historia);
                System.out.println();
            }
        } else {
            System.out.println("Não há livros de história");
        }
    }
}











