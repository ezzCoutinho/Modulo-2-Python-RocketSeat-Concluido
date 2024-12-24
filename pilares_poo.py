# Exemplo de herança
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

# Exemplo de polimorfismo.

print("\nExemplo de polimorfismo:")
animais = [cachorro, gato]

for animal in animais:
  print(f"O {animal.nome}, faz: {animal.emitir_som()}")

# Exemplo de encapsulamento.

class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo # Atributo privado.
  
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor 

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def get_saldo(self):
    return self.__saldo
  
conta = ContaBancaria(1000)
print(f"\nSeu saldo é de: {conta.get_saldo()}")
conta.depositar(500)
print(f"\nSeu saldo é de: {conta.get_saldo()}")
conta.sacar(-500)
print(f"\nSeu saldo é de: {conta.get_saldo()}")
conta.sacar(2000)
print(f"\nSeu saldo é de: {conta.get_saldo()}")


  