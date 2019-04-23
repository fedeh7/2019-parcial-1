def conversor(num):
    lista = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    resultado = []
    res = ""
    x = int(num)
    z = 0
    resto = ""
    
    while x > 15:
        z = x % 16
        resto = lista[z]
        resultado.insert(0, resto)
        x = x // 16

    if x != 0:
        resto = lista[x]
        resultado.insert(0, resto)
    
    if len(resultado) < 1:
        resto = lista[0]
        resultado.insert(0, resto)
        
    res = "".join(resultado)
    return res
