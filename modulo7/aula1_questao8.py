def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verif1 = 0
    else:
        digito_verif1 = 11 - resto
    
    if digito_verif1 != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verif2 = 0
    else:
        digito_verif2 = 11 - resto
    
    if digito_verif2 != int(cpf[10]):
        return False
    
    return True

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

if validar_cpf(cpf):
    print("CPF Válido")
else:
    print("CPF Inválido")
