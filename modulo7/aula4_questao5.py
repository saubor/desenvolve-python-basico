import csv

# Lista de listas com os dados dos livros
livros = [
    ["1984", "George Orwell", 1949, 328],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 863],
    ["Moby Dick", "Herman Melville", 1851, 635],
    ["Guerra e Paz", "Liev Tolstói", 1869, 1225],
    ["O Grande Gatsby", "F. Scott Fitzgerald", 1925, 180],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 671],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["A Divina Comédia", "Dante Alighieri", 1320, 798]
]

# Definir o nome do arquivo
nome_arquivo = 'meus_livros.csv'

# Abrir o arquivo para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho
    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escrever os dados dos livros
    for livro in livros:
        escritor.writerow(livro)

print(f"O arquivo '{nome_arquivo}' foi criado com sucesso.")
