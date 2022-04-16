Practica 1:
Para correr el codigo en loop, se debe instanciar la clase DataManager y luego llamar al metodo loop. de la siguiente manera:
    dm = Datamanager()
    dm.loop()

    Test:
        Entre los test de esta practica se encuentra uno de larga duracion, por lo que al correr el comando "pytest .\test\test_practica1.py" se debe esperar aproximadamente 65 segundos en total. ("pytest -v .\test\test_practica1.py" para ver test por test)

Practica 2:
Para correr la interface visual se debe instanciar la clase InterfaceManager, y luego llamar al metodo home, de la siguiente manera:
    im = InterfaceManager()
    im.home()

Al momento de crear un usuraio, en caso de que la edad ingresada no sea un caracter valido, se le proporcionara 0 (cero) por default. Podras cambiarlo en la opcion "actualizar usuario".
Podras salir de la interface ingresando la opcion 4 (listar usuarios) en el home