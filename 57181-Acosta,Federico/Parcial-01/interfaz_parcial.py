from hexadecimal import conversor

def interfaz(x):
    try:
        integral = int(x)
        resultado = conversor(integral)
        return resultado
    except ValueError:
        return "Debe ingresar solo numeros!"

    except TypeError:
        return "Type Error"
    
