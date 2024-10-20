- **Instrucciones de Instalación y Ejecución:**
    - Primero para clonar el repositorio en una maquina local, debes abrir una terminal, ingresa hasta el directorio donde desees tener el repositorio y luego debes clonar el repositorio con el siguiente codigo "git clone <https://github.com/hacUPB/prog-2420-eval-u3-AnaSofiaH12.git>
    - Para esto debes tener Python instalado. 


- **Uso del Programa:**
    - Este es un programa de gestion de datos, que te permite ver, agregar, actualizar y eliminar productos de una tienda por medio de un inventario, aqui te mostrare como utilizar el programa:
    Cuando tu ejecutes el programa, al instante veras en la terminal el menú de lo que puedes hacer, podras elegir cualquiera de las siguientes opciones: 
    1. Consultar Inventario: Esta funcion permite mostrar los productos que se encuentran en el invenatrio con su respectivo precio, cantidad total, tallas y la cantidad por cada talla. 
    2. Agregar producto: En este caso, si llego nueva mercancia el administrador del negocio por medio de esta funcion puede agregar un nuevo producto al inventario con su cantidad total, precio, cantidad de tallas y unidades por cada talla. Se te solicitara que ingreses todos los datos respectivos a ese producto y será añadido al inventario.
    3. Actualizar Producto: Luego de haber vendido cualquier producto o si algun cliente hace algun cambio y tu debes de resgistrar ese cambio en el sistema, puedes actualizar el dato de culalquier producto del inventario que exista. 
    4. Eliminar Producto: Como su nombre lo dice puedes eliminar algun producto del inventario, el sistema te preguntara el nombre del producto y automaticamente se elimina y asi cualquier dato relacionado con este. 
    5. Salir: Selecciona esta opcion para salir del programa. 


- **Ejemplos:**
1. Por ejemplo para consultar el inventario, el programa te mostrará algo asi: 
        producto: Vestidos 
        cantidad: 50
        precio: 100000
        Las tallas que estan disponibles y sus cantidades son:
            Talla S: 25
            Talla M: 20
            Talla L: 5
        
        producto: Pantalon 
        cantidad: 100
        precio: 180000
        Las tallas que estan disponibles y sus cantidades son:
            Talla S: 40
            Talla M: 40
            Talla L: 20

        producto: Chaquetas:
        cantidad: 40
        precio: 260
        Las tallas que estan disponibles y sus cantidades son: 
            Talla S: 15
            Talla M: 15
            Talla L: 10

2. Para agregar algun producto al inventario: 
        Ingrese el nombre del producto: Zapatos
        Agregue el precio del producto: 120000
        Ingrese la cantidad total: 60
        ¿Cuántas tallas tiene este producto?: 3
            Qué talla desea ingresar (Por ejemplo: S, M, L): S
                ¿Cantidad de unidades que desea agregar para la talla S?: 20
            Qué talla desea ingresar (Por ejemplo: S, M, L): M
                ¿Cantidad de unidades que desea agregar para la talla M?: 25
            Qué talla desea ingresar (Por ejemplo: S, M, L): L
                ¿Cantidad de unidades que desea agregar para la talla L?: 15


3. Para actualizar algun producto:
        Nombre del producto que desea actualizar(Asegurese de que la primera letra sea mayuscula): Vestidos
        Ingrese el nuevo precio para el producto: 105000
        Ingrese la nueva cantidad para este producto: 45
            La cantidad actual para la talla S es 25. Por favor, ingrese la nueva cantidad para la talla: 20
            La cantidad actual para la talla M es 20. Por favor, ingrese la nueva cantidad para la talla: 15
            La cantidad actual para la talla L es 5. Por favor, ingrese la nueva cantidad para la talla: 10

4. Para eliminar algun producto: 
        Nombre del producto que desea eliminar(Asegurese de que la primera letra sea mayuscula): Pantalon
        Producto: Pantalon, fue eliminado con éxito.

Estos fueron algunos ejemplos del funcionamiento del programa. 
