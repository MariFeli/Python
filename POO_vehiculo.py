class Vehiculo:
    def __init__(self, marca, modelo,tipo,Fuel_max,FuelNivel_Act,Ruedas, Color,Esta_Averiado):
        self.marca= marca
        self.modelo=modelo
        self.tipo=tipo
        self.Fuel_max=Fuel_max
        self.FuelNivel_Act=FuelNivel_Act
        self.Esta_Averiado=Esta_Averiado
        self.Ruedas=Ruedas
        self.Color=Color
        
        
    def conducir(self):
        if not self.Esta_Averiado and self.FuelNivel_Act>8:
            print(f"El vehículo  {self.marca} está conduciendo")
        else:
            print(f"El vehículo esta averiado o necesita llenar depósito")

    def actualizar_deposito(self):
       if self.Fuel_max>=self.FuelNivel_Act:
           print(f"El depósito de su {self.marca} está lleno")
       else:
           print("Lo siento, no te queda gasolina")
       
    def chocar(self,camion,moto):
        return self.chocar
    
    def accidente(self):
        print(f"Accidente con un vehículo {self.marca} ")

class camion(Vehiculo):
    def __init__(self, marca, modelo, tipo, Fuel_max, FuelNivel_Act, Ruedas, Color, Esta_Averiado,cabina):
        super().__init__(marca, modelo, tipo, Fuel_max, FuelNivel_Act, Ruedas, Color, Esta_Averiado)
        self.cabina=cabina

    def Dormir(self):
        print(f"El vehículo {self.marca} está dormido en estos momentos")

    def Transportar_Prod(self):
        print(f"El camión {self.marca} transporta productos")
 
    def accidente(self):
        print(f"Accidente con un camión {self.marca} ")

class moto(Vehiculo):
    def __init__(self, marca, modelo, tipo, Fuel_max, FuelNivel_Act, Ruedas, Color, Esta_Averiado,cadena,manillar):
        super().__init__(marca, modelo, tipo, Fuel_max, FuelNivel_Act, Ruedas, Color, Esta_Averiado)
        self.cadena=cadena
        self.manillar=manillar

    def Hacer_caballito(self):
        print(f"La moto {self.marca} con {self.Ruedas} y {self.manillar} esta haciendo caballito")

    def accidente(self):
        print(f"Accidente con una moto {self.marca} ")

def accidente(vehiculos):
      for vehiculo in vehiculos:
        vehiculo.accidente()




coche1= Vehiculo("Toyota","rav4","diesel",6,7,4,"Rojo", False)
coche1.conducir()
coche1.actualizar_deposito()
camion1= camion("VOLVO","C40","diesel",10,8,4,"Gris",True,1)
camion1.conducir()
camion1.actualizar_deposito()
moto1=moto("Honda","rav2","gasolina",9,9,2,"Negra",False,"Did","Gris")
moto1.conducir()
moto1.actualizar_deposito()
reporte=accidente([coche1,moto1,camion1])
print(reporte)
