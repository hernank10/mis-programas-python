import cmd

class Adventure(cmd.Cmd):
    intro = 'Bienvenido a la aventura. Escribe ayuda o ? para listar los comandos.\n'
    prompt = '(aventura) '

    def do_salir(self, arg):
        'Salir del juego: salir'
        print('¡Gracias por jugar!')
        return True

    def do_ir(self, arg):
        'Moverse a otra habitación: ir [dirección]'
        print(f'Vas hacia {arg}.')

    def do_agarrar(self, arg):
        'Agarrar un objeto: agarrar [objeto]'
        print(f'Has agarrado {arg}.')

if __name__ == '__main__':
    Adventure().cmdloop()
