# @classmethod
# @staticmethod 

class MinhaClasse:
  valor = 10 # Atributo da Class

  def __init__(self, nome):
    self.nome = nome # Atributo da instância.

  # requer uma instância para ser executado.
  def metodo_instancia(self):
    print(f"Método de instância chamado para {self.nome}.")

  @classmethod # Não precisa de instância para ser executado.
  def metodo_classe(cls):
    print(f"Método de classe chamada para valor {cls.valor}.")
    return
  
  @staticmethod
  def metodo_static():
    print("Método estático.")


obj = MinhaClasse("Classe exemplo")
obj.metodo_instancia()
MinhaClasse.metodo_classe() 
MinhaClasse.metodo_static()

class Carro:
  
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
  
  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",") ## criando uma lista.
    return cls(marca, modelo, int(ano))
  
configuracao1 = "Toyota, Corolla, 2022"
carro1  = Carro.criar_carro(configuracao1)
print(f" Marca: {carro1.marca}, Modelo: {carro1.modelo}, Ano: {carro1.ano}")


class Matematica:

  @staticmethod  
  def somar(a, b):
    return a + b
  
print(Matematica.somar(15, 10))