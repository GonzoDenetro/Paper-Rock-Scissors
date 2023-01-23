import random


def eleccionComputadora(opciones):
    opcion_computadora = random.choice(opciones)
    return opcion_computadora


def ganadorUsuario(usuario, computadora):
    if usuario=="Tijera" and computadora=="Papel" or usuario=="Papel" and computadora=="Piedra" or usuario=="Piedra" and computadora=="Tijera":
        return True
    else:
        return False 
    

def run():
    print("""Bienvenido!
          Este es el juego de Piedra, Papel o Tijera, vas a escoger una de las tres opciones y vas a jugar contra la computadora.
          Tienes 3 vidas""")
    
    vidas = 3
    ganancias = 0
    perdidas = 0
    lista_piedra_papel_tijera = ("Piedra", "Papel", "Tijera")
    
    while vidas > 0:
        usuario = input("\nPiedra, Papel o Tijera =>: ")
        usuario = usuario.capitalize()
        
        if usuario in lista_piedra_papel_tijera:
            opcion_computadora = eleccionComputadora(lista_piedra_papel_tijera)
            
            if opcion_computadora == usuario:
                print("\nEmpate")
            else:
                if ganadorUsuario(usuario, opcion_computadora):
                    ganancias += 1
                    print("\nGANASTE!")
                else:
                    print("\nPerdiste esta partida")
                    perdidas += 1
                    vidas = vidas - 1
            
            print("Opción computadora:", opcion_computadora, "\n")
        else:
            print("Introduce una opción correcta")    
        
        print("##" * 10)
        
    print("\nEl juego termino")
    print("Ganaste:", ganancias, "veces")
    print("Perdiste:", perdidas, "veces")
     


if __name__ == '__main__':
    run()  