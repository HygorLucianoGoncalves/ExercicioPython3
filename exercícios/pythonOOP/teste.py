#call 
#sytaxe
class computador:
  def __init__(self,marca,ram,placa_de_video):
    self.marca = marca
    self.menoria_ram = ram
    self.placa_de_video = placa_de_video
  def Ligar(self):
    print("Estou ligando")

  def Desligar(self):
    print("Estou desligando")

  def ExibirInformaçõesDesteComputado(self):
    print(self.marca, self.menoria_ram, self.placa_de_video)
computador1 = computador("asus","8g","nvideo")
computador2 = computador("dell","10g","GeForce")
computador3 = computador("acer","4g","atm")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformaçõesDesteComputado()

      