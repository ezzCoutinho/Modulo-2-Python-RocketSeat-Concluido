# Exemplo e herança
print("\nExemplo de herança: ")
class Animal:
  def __init__(self, nome):
    self.nome = nome
  
  def andar(self):
    print(f"O {self.nome}, esta andando.")
    return

  def emitir_som(self):
      pass
  
class Cachorro(Animal):
  def emitir_som(self):
    return "Au, au"
  
class Gato(Animal):
  def emitir_som(self):
    return "Miau"
  
cachorro = Cachorro("Fluky")
gato = Gato("Preto")

cachorro.andar()
print(cachorro.emitir_som())
gato.andar()
print(gato.emitir_som())