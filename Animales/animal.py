import animales


#Menú
#While
#Decisiones
#Clases con propiedades y métodos

menu = {
    '1': '1. Gato 😸',  
    '2': '2. Perro 🐶', 
    '3': '3. Loro 🦜',
    '4': '4. Serpiente 🐍',
    '5':'5. Zorro 🦊',
    '6': '6. León 🦁',
    '7': '7. Mariposa 🦋',
    '8': '8. Halcón 🦅',
    '9': '9. Alacrán 🦂',
    '0': '0. Salir 👋',
}


class Animal():
    animales_tipos = {
        1:animales.gato,
        2:animales.perro,
        3:animales.loro,
        4:animales.serpiente,
        5:animales.zorro,
        6:animales.leon,
        7:animales.mariposa,
        8:animales.halcon,
        9:animales.alacran,
    }
    def __init__(self, gato, perro, loro, serpiente, zorro, leon, mariposa, halcon, alacran):
        self.gato = gato
        self.perro = perro
        self.loro = loro
        self.serpiente = serpiente
        self.zorro = zorro
        self.leon = leon
        self.mariposa = mariposa
        self.halcon = halcon
        self.alacran = alacran
    
    def mostrar_animal(self, tipo):
        animales_tipos = getattr(animales, self)
        print(self.animales_tipos[tipo])
        
        
    
    

#Ejecución principal
if __name__=='__main__':
    for tipo in menu:
        print(menu.get(tipo))
    while True:
        user_input = input('Elige un animal y mira la magia✨: ')
        if  user_input == '0':
            print('Vuelve pronto 👋')
            #El usuario quiere dejar de jugar
            break
        elif user_input == '1':
            #Imprimir animal
            #animales_tipo = menu.get(tipo)
            print(animales.gato)
            #print(menu_value.split(' '))
            #animal = Animal(user_input)
            #print('mostrar') 
        elif user_input == '2':
            print(animales.perro)
        elif user_input == '3':
            print(animales.loro)
        elif user_input == '4':
            print(animales.serpiente)
        elif user_input == '5':
            print(animales.zorro)
        elif user_input == '6':
            print(animales.leon)
        elif user_input == '7':
            print(animales.mariposa)
        elif user_input == '8':
            print(animales.halcon)
        elif user_input == '9':
            print(animales.alacran)
        else:
            #Opción inválida
            print('Opción inválida')

