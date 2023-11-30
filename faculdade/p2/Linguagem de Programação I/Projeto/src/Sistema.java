import java.util.ArrayList;

public class Sistema {
    private ArrayList<Livro> livros;

    public Sistema() {
        livros = new ArrayList<Livro>();
    }

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public Livro consultarLivro(String titulo) {
        for (Livro livro : livros) {
            if (livro.getTitulo().equals(titulo)) {
                return livro;
            }
        }
        return null;
    }

    public ArrayList<Livro> listarLivrosPorTipo(String tipo) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro.getTipo().equals(tipo)) {
                lista.add(livro);
            }
        }
        return lista;
    }

    public ArrayList<Livro> listarLivrosPorAutor(String autor) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro.getAutor().equals(autor)) {
                lista.add(livro);
            }
        }
        return lista;
    }

    public ArrayList<Livro> listarLivrosPorAno(int ano) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro.getAno() == ano) {
                lista.add(livro);
            }
        }
        return lista;
    }

    public ArrayList<Livro> listarLivrosPorPreco(double preco) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro.getPreco() == preco) {
                lista.add(livro);
            }
        }
        return lista;
    }

    public ArrayList<Livro> listarLivrosPorGenero(String genero) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro instanceof Ficcao) {
                Ficcao ficcao = (Ficcao) livro;
                if (ficcao.getGenero().equals(genero)) {
                    lista.add(livro);
                }
            }
        }
        return lista;
    }

    public ArrayList<Livro> listarLivrosPorTema(String tema) {
        ArrayList<Livro> lista = new ArrayList<Livro>();
        for (Livro livro : livros) {
            if (livro instanceof NaoFiccao) {
                NaoFiccao naoFiccao = (NaoFiccao) livro;
                if (naoFiccao.getTema().equals(tema)) {
                    lista.add(livro);
                }
            }
        }
        return lista;
    }

    public void imprimirLivros() {
    }
}



