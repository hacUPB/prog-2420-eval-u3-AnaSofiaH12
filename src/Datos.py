
def main():

    # Creo el diccionario para el inventario
    inventario = {
        "Vestidos": { "cantidad": 50, "precio": 100.000, "tallas": { "S": 25, "M": 20, "L": 5 }},
        "Pantalon": { "cantidad": 100, "precio": 180.000, "tallas": { "S": 40, "M": 40, "L": 20 }},
        "Chaqueta": { "cantidad": 40, "precio": 260.000 , "tallas": { "S": 15, "M":15, "L":10 }}
        }

                
    # Funcion para 1. Consultar inventario 
    def consultar_inventario():
        if inventario:
            for nombre_producto, datos in inventario.items():
                print(f"producto: {nombre_producto}")
                print(f"precio: {datos['precio']}")
                print(f"cantidad: {datos['cantidad']}")
                print("Las tallas que estan disponibles y sus cantidades son: ")
                for talla, cantidad in datos["tallas"].items():
                    print(f" Talla {talla}: {cantidad} unidades")
        else:
            print("El inventario esta vacio")
                
        
        
    # Funcion para 2. Agregar Producto al inventario
    def agregar_producto():
        nombre = str(input("Ingrese el nombre del producto: "))
        precio = float(input("Agregue el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad total: "))
        tallas = {}             #Diccionario aparte para la cantidad de tallas que pueden haber 
        cant_tallas =int(input("¿Cuantas tallas tiene este producto?: "))
        for i in range(cant_tallas):
            talla = str(input("Que tallas desea ingresar (Por ejemplo: S, M, L): "))
            cant_por_talla = int(input(f"¿Cantidad de unidades que desea agregar para la talla {talla}?: "))
            tallas[talla] = cant_por_talla
                    
        inventario[nombre] = {"cantidad": cantidad, "precio": precio, "tallas": tallas}
        print(f"Producto: {nombre}, fue agregado de manera exitosa")
                
    # Funcion para 3. Actualizar producto en el inventario 
    def actualizar_producto():
        nombre = str(input("Nombre del producto que desea actualizar(Asegurese de que la primera letra sea mayuscula): "))
        if nombre in inventario:
            precio_n = float(input("Ingrese el nuevo precio para el producto: "))
            cantidad_n = int(input("Ingrese la nueva cantidad para este producto: "))
            tallas = inventario[nombre]["tallas"]
            for talla, cantidad in tallas.items():
                cantidad_n_talla = int(input(f"La cantidad actual para la talla {talla} es {cantidad}. Porfavor ingrese la nueva cantidad para la talla: "))
                tallas[talla] = cantidad_n_talla
                        
            #Ahora, para actualizar los datos, haremos esto:
            inventario[nombre]["precio"] = precio_n
            inventario[nombre]["cantidad"] = cantidad_n
            inventario[nombre]["tallas"] = tallas
            print(f"El producto: {nombre}, ha sido actualizado con exito")
        else:
            print(f"El producto: {nombre}, no fue encontrado en el inventario")

    # Funcion para 4. Para Eliminar producto 
    def eliminar_producto():
        nombre = str(input("Nombre del producto que desea eliminar(Asegurese de que la primera letra sea mayuscula): "))     
        if nombre in inventario:
            #metodo para eliminar:
            del inventario[nombre]
            print(f"Producto: {nombre}, fue eliminado con exito.") 
        else: 
            print(f"Producto: {nombre}, no fue encontrado en el inventario.")     
        
    # Funcion para 5. Salir 
    def salir():
        print("Saliendo del programa...")    
         
        
    # Menu de opciones que se le solicita al usuario     
    while True: 
        print("\nOpciones posibles: ")
        print("1. Consultar Inventario ")
        print("2. Agregar producto ")
        print("3. Actualizar Producto ")
        print("4. Eliminar Producto ")
        print("5. Salir")
        opcion = int(input("Elige una de las opciones (1-5): "))
        
        
        #Llamando a las funciones:                     
        if opcion == 1:
            consultar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            actualizar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            salir()
            break
        else: 
            print("Opción no válida, por favor escoga una opcion del 1 a 5.")    
            
            
if __name__ == "__main__":
    main()
