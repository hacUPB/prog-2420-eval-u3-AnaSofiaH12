
def main():
    # Creo el diccionario para el inventario
    inventario = {}
    
    # Menu de opciones que se le solicita al usuario 
    def menu():
        print("/nOpciones posibles: ")
        print("1. Consultar Inventario ")
        print("2. Agregar producto ")
        print("3. Actualizar Producto ")
        print("4. Eliminar Producto ")
        print("5. Salir")
        opcion = int(input("Elige una de las opciones (1-5): "))
        
        if opcion == "1":
            consultar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            salir()
            
            
            
    # Funcion para 1. Consultar inventario 
        def consultar_inventario():
            if inventario:
                for nombre_productos in inventario.items():
                    print("/n")
                    print(f"producto: {nombre_productos}")
                    print(f"precio: {}")
                    print(f"cantidad: {}")
            
    
    
    
    
    # Funcion para 2. Agregar Producto al inventario
        def agregar_producto():
            nombre = str(input("Ingrese el nombre del producto: "))
            precio = float(input("Agregue el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad total: "))
            tallas = {}             #Diccionario aparte para la cantidad de tallas que pueden haber 
            cant_tallas = 
            for i in range(cant_tallas)
            
            
    
    
    
    
    
    
    
    # Funcion para 3. Actualizar algun producto del inventario 
        def actualizar_producto():
    
    
    
    
    
    
      
    # Funcion para 4. Eliminar producto del inventario 
        def eliminar_producto():
    
    
    
    
    
    
    # Funcion para 5. Salir
        def salir():
                     
            
    



















if __name__ == "__main__":
    main()
