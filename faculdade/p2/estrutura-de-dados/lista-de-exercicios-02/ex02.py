class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"


livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
livro2 = Livro("Orgulho e Preconceito", "Jane Austen")

print(livro1.detalhes())  
print(livro2.detalhes())  
