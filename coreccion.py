import random
import pyqrcode
import os 
os.system("cls")

detalleCompra = [[],[],[],[],[],[]]
iva = 0.15
paq1 = 500 
paq2 = 2000
paq3 = 1500
paq4 = 3000

def menu():
    print(f"Qué acción desea realizar?") 
    print(f"* 1) Registro pedidos") 
    print(f"* 2) Mostrar pedidos") 
    print(f"* 3) Mostrar detalle de un pedido") 
    print(f"* 4) Eliminar un pedido")
    print(f"* 5) Salir del sistema")
    return int(input("Ingrese una opcion: "))
    
def ingresar():
    print("\n----- Nuevo pedido -----\n")
    print("    Ingresar los datos del cliente      \n")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = int(input("Telefono: "))
    direccion = input("Direccion: ")
    precio = 0.0
    detalleCompra[0].append(nombre)
    detalleCompra[1].append(apellido)
    detalleCompra[2].append(telefono)
    detalleCompra[3].append(direccion)
    detalleCompra[4].append(random.randint(1,1000))
    print("\n    Seleccione el paquete ofimatico a contratar      \n")
    print("1) Opción 1: PC + Monitor = $500")
    print("2) Opción 2: PC + Monitor 4K = $2000")
    print("3) Opción 3: Laptop UltraProIA = $1500")
    print("4) OPción 4: Worstation Servidor = $3000")
    paquete = int(input("Seleccine una opcion: "))
    while (paquete < 1 or paquete > 4):
        paquete = int(input("ERROR: Ingrese una opcion valida: "))
    if (paquete == 1):
        precio = paq1 + (paq1 * iva)
    elif (paquete == 2):
        precio = paq2 + (paq2 * iva)
    elif (paquete == 3):
        precio = paq3 + (paq3 * iva)
    elif (paquete == 4):
        precio = paq4 + (paq4 * iva)
    detalleCompra[5].append(precio)
    print("\nPedido registrado con exito\n")

def qrpichincha(i):
    textoPago = (f"Datos del pago\n *Codigo del pedido: {detalleCompra[4][i]}\n *Pago final: ${detalleCompra[5][i]}\n")
    codigoQR = pyqrcode.create(textoPago)
    nombreArchivo = "CodigoQR.png"
    codigoQR.png(nombreArchivo, scale=8)
    print("Codigo QR generado exitosamente\n")

def mostrar(i): #Una forma de hacerlo
    print(f"* Nombre: {detalleCompra[0][i]}")
    print(f"* Apellido: {detalleCompra[1][i]}")
    print(f"* Telefono: {detalleCompra[2][i]}")
    print(f"* Direccion: {detalleCompra[3][i]}")
    print(f"* Codigo: {detalleCompra[4][i]}")
    print(f"* Precio a pagar con IVA: {detalleCompra[5][i]}")
    print("\n")

def mostrarPedidos():
    if (len(detalleCompra[0]) == 0):
        print("ERROR: No hay pedidos registrados\n")
        return
    else:
        print("\n----- Detalle de los pedidos -----\n")
        for c in range(len(detalleCompra[0])):
            mostrar(c)

def mostrardetalle():
    if (len(detalleCompra[0]) == 0):
        print("ERROR: No hay pedidos registrados")
        return
    else:
        codigo = int(input("Ingrese el codigo del pedido: "))
        if (codigo in detalleCompra[4]):
            codigoindex = detalleCompra[4].index(codigo)
            print("\nPedido encontrado")
            print("----------------------------------")
            print("Detalle")
            mostrar(codigoindex)
            qrpichincha(codigoindex)
        else:
            print("ERROR: Coigo ingresado no existe\n")

def eliminar():
    codigo = int(input("Ingrese el codigo del pedido: "))
    if codigo in detalleCompra[4]:
        codigoIndex = detalleCompra[4].index(codigo) #index hace que codigoIndex tome la posicion que ocupa el codigo en detallecompra[4]
        for f in range(len(detalleCompra[0])):
            detalleCompra[f].pop(codigoIndex)
        print("Pedido eliminado con exito\n")
    else:
        print("Error: Pedido no encontrado\n")

def main():
    print("\n =========== TECHWORLD S.A ==========\n")
    print("         *** Bienvenido(a) ***       \n")
    opc = menu()
    while (opc != 5):
        if (opc == 1):
            ingresar()
        elif (opc == 2):
            mostrarPedidos()
        elif (opc == 3):
            mostrardetalle()
            pass
        elif (opc == 4):
            eliminar()
            pass
        opc = menu()

main()