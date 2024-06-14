def main():
    data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
    dia, mes, ano = map(int, data_nascimento.split('/'))
    
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril',
        'Maio', 'Junho', 'Julho', 'Agosto',
        'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    
    mes_extenso = meses[mes - 1]
    
    print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")

if __name__ == "__main__":
    main()
