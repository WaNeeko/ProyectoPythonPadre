#funciones y verificacion
def putNum(text):
  return int(input(text))

class Verificar:
  @staticmethod
  def fecha(fecha):
    fechaArr = fecha.split("/")
    if int(fechaArr[2]) < 22:
      return Verificar.fecha(input("reingrese la fecha: "))
    if int(fechaArr[1]) > 12 and int(fechaArr[1]) < 1:
      return Verificar.fecha(input("reingrese la fecha: "))
    return fecha

  @staticmethod
  def rangoDePrecios(precio):
    if precio > 10 and precio < 1000:
      return precio
    return Verificar.rangoDePrecios(int(input("reintrodusca el precio")))

  @staticmethod
  def DNIPosible(DNI):
    if DNI > 5000000 and DNI < 99000000:
      return DNI
    return Verificar.DNIPosible(int(input("reingrese el DNI: ")))
  
  @staticmethod
  def correo(correo):
    import re
    if (re.match("[a-zA-Z0-9]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]+", correo)) != None:
      return correo
    return Verificar.correo(input("reingrese su correo: "))
    
#Entrada

#Entrada
    
fecha = Verificar.fecha(input("fechaEntrega: "))

class Producto:
  def __init__(self, precio, cantidad):
    self.precio = precio
    self.cantidad = cantidad


    
#class Carrito:
#  @staticmethod
#  def __init__(self):
#    teNegro = Producto("", "")



class Carrito:
  pass



carrito = {
  "teNegro": Producto(Verificar.rangoDePrecios(int(input("TN precio: "))), putNum("TN cantidad: ")),
  "teVerde": Producto(Verificar.rangoDePrecios(int(input("TV precio: "))), putNum("TV cantidad: ")),
  "mielAlgarrobo1kg": Producto(Verificar.rangoDePrecios(int(input("MA precio: "))), putNum("MA cantidad: ")),
}
datosDelCliente = {
  "nroDNI" : Verificar.DNIPosible(int(input("DNI: "))),
  "correoElectronico": Verificar.correo(input("Correo: "))
}
formulario = {
  "fecha":fecha,
  "carrito": carrito,
  "datosDelCliente":datosDelCliente
}

class Venta:
  def __init__(self, fecha, compras, cliente):
    fecha = ''
    compras = ''
    cliente = ''

Venta()

def realizarVenta():
  return {
    "fecha": "",
    "compras": "",
    "cliente": ""
  }

#Salida
