import csv
import os

# Função para verificar se um arquivo existe; se não, cria o arquivo com cabeçalho
def verificar_arquivo(file_name, header):
    if not os.path.isfile(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

# Verifica e cria os arquivos CSV se não existirem
verificar_arquivo('usuarios.csv', ['username', 'password', 'type'])
verificar_arquivo('produtos.csv', ['name', 'price', 'quantity'])

# Função para carregar dados de usuários de um arquivo CSV para um dicionário
def carregar_usuarios(file_name):
    usuarios = {}
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[row['username']] = {
                'password': row['password'],
                'type': row['type']
            }
    return usuarios

# Função para salvar dados de usuários de um dicionário para um arquivo CSV
def salvar_usuarios(usuarios, file_name):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['username', 'password', 'type']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for username, data in usuarios.items():
            writer.writerow({'username': username, 'password': data['password'], 'type': data['type']})

# Função para carregar dados de produtos de um arquivo CSV para uma lista de dicionários
def carregar_produtos(file_name):
    produtos = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append({
                'name': row['name'],
                'price': float(row['price']),
                'quantity': int(row['quantity'])
            })
    return produtos

# Função para salvar dados de produtos de uma lista de dicionários para um arquivo CSV
def salvar_produtos(produtos, file_name):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['name', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)

# Função para adicionar novo usuário ao sistema
def adicionar_usuario(username, password, type, usuarios, file_name):
    if username not in usuarios:
        usuarios[username] = {'password': password, 'type': type}
        salvar_usuarios(usuarios, file_name)
        print(f"Usuário '{username}' adicionado com sucesso.")
    else:
        print(f"Usuário '{username}' já existe.")

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    print("Lista de Usuários:")
    for username, data in usuarios.items():
        print(f"Usuário: {username}, Tipo: {data['type']}")

# Função para remover usuário do sistema
def remover_usuario(username, usuarios, file_name):
    if username in usuarios:
        del usuarios[username]
        salvar_usuarios(usuarios, file_name)
        print(f"Usuário '{username}' removido com sucesso.")
    else:
        print(f"Usuário '{username}' não encontrado.")

# Função para atualizar tipo de usuário
def atualizar_usuario(username, new_type, usuarios, file_name):
    if username in usuarios:
        usuarios[username]['type'] = new_type
        salvar_usuarios(usuarios, file_name)
        print(f"Tipo de usuário para '{username}' atualizado para '{new_type}'.")
    else:
        print(f"Usuário '{username}' não encontrado.")

# Função para adicionar novo produto ao sistema
def adicionar_produto(name, price, quantity, produtos, file_name):
    produtos.append({'name': name, 'price': price, 'quantity': quantity})
    salvar_produtos(produtos, file_name)
    print(f"Produto '{name}' adicionado com sucesso.")

# Função para listar todos os produtos
def listar_produtos(produtos):
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Produto: {produto['name']}, Preço: R${produto['price']}, Quantidade: {produto['quantity']}")

# Função para remover produto do sistema
def remover_produto(name, produtos, file_name):
    for produto in produtos:
        if produto['name'] == name:
            produtos.remove(produto)
            salvar_produtos(produtos, file_name)
            print(f"Produto '{name}' removido com sucesso.")
            return
    print(f"Produto '{name}' não encontrado.")

# Função para buscar produto por nome
def buscar_produto_por_nome(name, produtos):
    for produto in produtos:
        if produto['name'] == name:
            print(f"Produto encontrado: {produto['name']}, Preço: R${produto['price']}, Quantidade: {produto['quantity']}")
            return
    print(f"Produto '{name}' não encontrado.")

# Função para listar produtos ordenados por nome
def listar_produtos_ordem_nome(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['name'])
    print("Produtos ordenados por nome:")
    for produto in produtos_ordenados:
        print(f"Produto: {produto['name']}, Preço: R${produto['price']}, Quantidade: {produto['quantity']}")

# Função para listar produtos ordenados por preço
def listar_produtos_ordem_preco(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['price'])
    print("Produtos ordenados por preço:")
    for produto in produtos_ordenados:
        print(f"Produto: {produto['name']}, Preço: R${produto['price']}, Quantidade: {produto['quantity']}")

# Função principal para demonstrar funcionalidades
def main():
    # Carregar dados iniciais de usuários e produtos
    usuarios = carregar_usuarios('usuarios.csv')
    produtos = carregar_produtos('produtos.csv')
    
    # Exemplo de uso das funcionalidades
    adicionar_usuario('admin', 'admin123', 'gerente', usuarios, 'usuarios.csv')
    adicionar_usuario('user1', 'password1', 'funcionario', usuarios, 'usuarios.csv')
    adicionar_produto('Camiseta Azul', 39.99, 100, produtos, 'produtos.csv')
    adicionar_produto('Calça Jeans', 89.99, 50, produtos, 'produtos.csv')

    listar_usuarios(usuarios)
    listar_produtos(produtos)

    buscar_produto_por_nome('Calça Jeans', produtos)
    buscar_produto_por_nome('Blusa Branca', produtos)

    listar_produtos_ordem_nome(produtos)
    listar_produtos_ordem_preco(produtos)

    remover_usuario('user1', usuarios, 'usuarios.csv')
    remover_produto('Camiseta Azul', produtos, 'produtos.csv')

    atualizar_usuario('admin', 'administrador', usuarios, 'usuarios.csv')

    listar_usuarios(usuarios)
    listar_produtos(produtos)

if __name__ == "__main__":
    main()
