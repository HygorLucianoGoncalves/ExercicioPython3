class carro:
  def __init__(self,marca,portas,tipo):
    self.marca = marca
    self.portas = portas
    self.tipo = tipo  
  def ligar(self):
    print("carro esta ligando")
  def desligar(self):
    print("carro foi desligado")
  def inforCarro(self):
    print(f"A marca do carro e {self.marca} o carro tem {self.portas} portas e o tipo do carro e {self.tipo}")
    
carro1 = carro(input("marca do carro: "),input("quantas portas: "),input("tipo de carro: "))
carro1.ligar()
carro1.inforCarro()
