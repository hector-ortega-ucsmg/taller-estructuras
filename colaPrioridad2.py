# ==========================================
# CLASES BASE: NODO Y NODO DOBLE
# ==========================================

class Nodo:
    """Nodo para lista simple y circular."""
    def __init__(self, dato):
        self.dato = dato         # Guarda el valor numérico del nodo
        self.siguiente = None    # Apunta al siguiente nodo


class NodoDoble(Nodo):
    """Nodo para lista doble (hereda de Nodo)."""
    def __init__(self, dato):
        super().__init__(dato)   # Hereda dato y siguiente
        self.anterior = None     # Apunta al nodo anterior


# ==========================================
# 1. LISTA ENLAZADA SIMPLE
# ==========================================

class ListaSimple:
    """Lista donde cada nodo apunta solo al siguiente."""
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano += 1

    def eliminar(self, dato):
        if self.esta_vacia():
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
            self.tamano -= 1

    def __str__(self):
        resultado = ""
        actual = self.cabeza
        while actual:
            resultado += str(actual.dato) + " -> "
            actual = actual.siguiente
        return resultado + "None"


# ==========================================
# 2. LISTA ENLAZADA DOBLE
# ==========================================

class ListaDoble:
    """Lista donde los nodos tienen doble enlace."""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cabeza is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamano += 1

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamano += 1

    def __str__(self):
        resultado = "None <-> "
        actual = self.cabeza
        while actual:
            resultado += str(actual.dato) + " <-> "
            actual = actual.siguiente
        return resultado + "None"


# ==========================================
# 3. LISTA ENLAZADA CIRCULAR
# ==========================================

class ListaCircular:
    """Lista donde el último nodo se conecta con el primero."""
    def __init__(self):
        self.cola = None
        self.tamano = 0

    def esta_vacia(self):
        return self.cola is None

    def __len__(self):
        return self.tamano

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cola = nuevo
            nuevo.siguiente = nuevo
        else:
            nuevo.siguiente = self.cola.siguiente
            self.cola.siguiente = nuevo
        self.tamano += 1

    def insertar_final(self, dato):
        self.insertar_inicio(dato)
        self.cola = self.cola.siguiente

    def __str__(self):
        if self.esta_vacia():
            return "Lista circular vacía"
        resultado = "Inicio -> "
        actual = self.cola.siguiente
        for _ in range(self.tamano):
            resultado += str(actual.dato) + " -> "
            actual = actual.siguiente
        return resultado + "(Vuelve al inicio)"


# ==========================================
# MENÚS INTERACTIVOS CON ESTILO
# ==========================================

def gestionar_lista(lista, nombre_tipo):
    """Menú interactivo para cualquier tipo de lista seleccionado."""
    while True:
        print(f"\n ======= 📄 MENÚ LISTA {nombre_tipo} ======= ")
        print(f"Estado: {lista}")
        print("1. ➕ Ingresar al inicio")
        print("2. ➕ Ingresar al final")
        print("3. 🗑️ Eliminar dato")
        print("4. 🔙 Volver al menú principal")
        
        op = input("Digite una opción: ")
        
        if op == "1":
            dato = int(input("Ingrese el número a insertar: "))
            lista.insertar_inicio(dato)
            print(f"✅ ¡Dato {dato} insertado al inicio!")
        elif op == "2":
            dato = int(input("Ingrese el número a insertar: "))
            lista.insertar_final(dato)
            print(f"✅ ¡Dato {dato} insertado al final!")
        elif op == "3":
            dato = int(input("Ingrese el número a eliminar: "))
            lista.eliminar(dato)
            print(f"🗑️ Operación de eliminación procesada.")
        elif op == "4":
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    # Instanciamos los tres tipos de listas requeridos
    ls = ListaSimple()
    ld = ListaDoble()
    lc = ListaCircular()

    while True:
        print("\n ======= 🔗 MENÚ PRINCIPAL - TALLER ======= ")
        print("1.  Gestionar Lista Simple")
        print("2.  Gestionar Lista Doble")
        print("3.  Gestionar Lista Circular")
        print("4.  Salir")
        
        opcion = input("Digite una opción: ")
        
        if opcion == "1":
            gestionar_lista(ls, "SIMPLE")
        elif opcion == "2":
            gestionar_lista(ld, "DOBLE")
        elif opcion == "3":
            gestionar_lista(lc, "CIRCULAR")
        elif opcion == "4":
            print("FInalizando programa")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.")