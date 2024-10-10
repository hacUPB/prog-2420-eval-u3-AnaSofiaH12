[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PehQeuqy)
# Unidad 3
---
## Documentación del proyecto
### Nombre:  Ana Sofía Henao Agudelo

### ID:  000550158

**1. Título del Proyecto:** Inventario de la tienda de Sofi 

**2. Descripción:**  Este código permite gestionar el inventario de una tienda de ropa para mujer, llamada “La tienda de Sofí”. El programa permite averiguar, agregar, actualizar y eliminar productos de interés que estén disponibles en la tienda. Cualquier persona que haga parte del grupo de trabajo de la tienda puedes acceder a la cantidad de prendas disponibles, el precio, y las tallas disponibles. 
La importancia del programa es que lleva un control de toda la mercancia disponible actualizada para tener la certeza de la cantidad de los productos o evitar el sobreabasteciminto, entre otros. 

**3. Alcance:** En este caso el usuario es un trabajador que quiere buscar en la base de datos alguna caracteristicas de diversas prendas, entonces el usuario puede añadir nuevos productos con su respectiva cantidad, precio y tallas, puede eliminar productos, puede consultar cualquier producto para los clientes y tambien puede actualizar datos tras alguna venta, cambio o llegada de mercancia. 

**4. Estructuras de Datos Utilizadas:** De las estructuras de datos vistas en clase, para este codigo preferí utilizar los diccionarios, ya que su estructura general es "clave:valor" y para alamacenar toda la informacion de los distintos productos es ideal y práctico utilizar la clave como el tipo de producto y el valor será otro dicccionario con informacion de la cantidad, el precio y aprate otro con las tallas disponibles de cada producto. 

**5. Pseudocódigo:** 
///
Inicio 
    Se crea un diccionario vacio llamado "inventario"

    Opciones posibles que puede solicitar el usuario:
    Menu de opciones:
        1. Consultar inventario, 2. Agregar producto, 3. Actualizar producto, 4. Eliminar producto, 5. Salir 

    Leer la opcion escogida por el usuario 

    Si la opción es "Consultar inventario":
        Si en el inventario no hay nada:
            Mensaje diciendo que el inventario de la tienda entá vacío 
        Si no:
            Por cada producto dentro del sistema:
                Mostrar el nombre especifico del producto, mostrar la cantidad disponibles, mostrar el precio y mostrar cada talla y su cantidad
    
    Si la opción es "Agregar producto":
        Preguntarle al usuario el nombre del producto 
        Preguntarle el precio del producto
        Preguntarle la cantidad de unidades que agregara
        Preguntarle al usuario las diferentes tallas que tiene el producto
            En otro diccionario para cada talla:
                Preguntarle al usuario las tallas que desea ingresar
                Preguntarle la cantidad de unidades que hay para cada talla 
                En el diccionario de tallas guardar los datos
        Guardar todo en el diccionario del inventario 
        Imprimir "Este producto fue agregado al inventario con éxito"
    
    Si la opción es "Actualizar producto":
        Solicitarle al usuario que ingrese el producto que desea actualizar 
            Si el producto hace parte del inventario:
                Solicitar el nuevo precio del producto
                Preguntarle la cantidad de unidades nuevas 
                Para las tallas:
                    solicitar la cantidad nueva para esa talla 
                    Guardar la cantidad para las tallas 
                Guardar todo en el inventario
                Imprimir un mensaje donde se confirme que la actualizacion del producto fue exitosa
            si no hace parte del inventario:
                Imprimir "Este producto no existe, si requiere lo puede agregar como un nuevo producto"
        
    Si la opción es "Eliminar Producto":
        Solicitar el nombre del producto 
            Si el producto esta en el inventario:
                Eliminar el producto del diccionario "inventario" 
                Imprimir "El producto fue eliminado exitosamente"
            Si no esta en el inventario:
                Imprimir "Este producto no existe"
    
    Si la opción es "Salir"
        Imprimir "Muchas gracias por hacer parte de Tienda de Sofi, Lo esperamos..."
Fin 
///

