class Animal:
  def __init__(self, nome):
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentando(self):
    print(f"O {self.nome}, está amamentando.")
    return

class Ave(Animal):
  
  def voar(self):
    print(f"O {self.nome}, está voando.")
    return
  
class Morcego(Mamifero, Ave): # Herança múltipla
  def emitir_som(self):
    print(f"O {self.nome}, esta emitindo sons ultrassônicos.")
    return 
  
morcego = Morcego("Morcego")
morcego.amamentando()
morcego.voar()
morcego.emitir_som()