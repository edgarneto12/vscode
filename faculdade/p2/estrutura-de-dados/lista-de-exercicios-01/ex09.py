lista, lista_a= ["Maçã", "Banana", "Laranja", "Morango", "Abacaxi", "Uva", "Pera", "Kiwi", "Melancia", "Limão", "Manga", "Cereja", "Pêssego", "Ameixa", "Goiaba", "Caju", "Maracujá", "Framboesa", "Tangerina"], []

for i in lista:
    lista_a = [nome for nome in lista if nome.startswith("A")]
print(f"Lista com todos nomes que começam com A: {lista_a}")