def validador_senha(senha):
    if len(senha) < 8:
        return False
    
    if not any(c.islower() for c in senha):
        return False
    
    if not any(c.isupper() for c in senha):
        return False
    
    if not any(c.isdigit() for c in senha):
        return False
    
    if not any(c in '@#$%^&+=' for c in senha):
        return False
    
    return True

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  
print(validador_senha(senha2))  
print(validador_senha(senha3))  
