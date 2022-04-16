from extras.utils import (singleton, get_conn)
from sqlite3.dbapi2 import Row

# Create table
conn = get_conn()

c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    );
""")

conn.commit()

# Database requests
class UserManager:
    def create_user(self, name, surname, age, email):
        c.execute("""
        INSERT INTO user (name, surname, age, email) VALUES (?,?,?,?)
    """, (name, surname, age, email))
        return conn.commit()

    def update_user(self, id, field, value):
        c.execute(f"Update user set {field} = ? where id = ?", (value, id))
        conn.commit()

    def delete_user(self, id):
        c.execute("DELETE FROM user WHERE id = ?", (id, ))
        conn.commit()

@singleton
class InterfaceManager(UserManager):
    def home(self):
        print("=========== Bienvenido ===========")
        print("")
        print("1) Crear usuario")
        print("2) Actualizar usuario")
        print("3) Borrar usuario")
        print("4) Listar usuarios")
        print("5) Ir al Inicio")
        print("")
        flag = True
        while flag:
            try:
                action = int(input("Que desea hacer?: "))
                flag = False
            except: pass
        return self.redirect(action)

    # CRUD functions
    def create_user_interface(self):
        name = input("ingrese nombre: ")
        surname = input("ingrese apellido: ")
        email = input("ingrese email: ")
        try:
            age = int(input("ingrese edad: "))
        except: age = 0
        print("USUARIO CREADO")
        self.create_user(name, surname, age, email)
        return self.home()

    def update_user_interface(self):
        user = self.select_user_interface()
        field = input("Inserte el campo a actualizar (name, surname, age, email): ")
        if field in ['name', 'surname', 'age', 'email']:
            if field == 'age':
                try:
                    value = int(input("Inserte nuevo valor: "))
                except: value = 0
            else:
                value = input("Inserte nuevo valor: ")
            
            self.update_user(user[0], field, value)
            print("USUARIO ACTUALIZADO")
        return self.home()

    def delete_user_interface(self):
        user = self.select_user_interface()
        self.delete_user(user[0])
        print("USUARIO ELIMNADO")
        return self.home()

    def render_user(self):
        rows = c.execute("SELECT * FROM user").fetchall()
        for row in rows:
            print(row[0], row[1],row[2],row[3], row[4])
        return rows
    
    # Return a user for CRUD
    def select_user_interface(self):
        self.render_user()
        try:
            id = int(input("Inserte id del usuario a seleccionar: 2"))
            user = c.execute("SELECT * FROM user WHERE id = ?", (id, )).fetchone()
            return user
        except: return self.home()

    # Redirect to selected interface
    def redirect(self, action):
        actions = {
            1: self.create_user_interface,
            2: self.update_user_interface,
            3: self.delete_user_interface,
            4: self.render_user,
            5: self.home
        }
        try:
            return actions[action]()
        except: return self.home()