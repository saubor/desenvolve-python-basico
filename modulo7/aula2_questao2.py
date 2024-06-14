def main():
    frase = input("Digite uma frase: ")
    vogais = 'aeiouAEIOU'
    frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
    
    print(f"Frase modificada: {frase_modificada}")

if __name__ == "__main__":
    main()
