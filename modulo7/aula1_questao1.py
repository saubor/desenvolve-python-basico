def main():
    nome = input("Digite seu nome: ")
    
    
    for i in range(1, len(nome) + 1):
        print(nome[:i])

if __name__ == "__main__":
    main()
