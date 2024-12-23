# POO
# Os pilares encapsulamento, herança, polimorfismo e abstração. 


# Classe exemplo 
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá, meu nome é: {self.nome} e eu tenho {self.idade} anos"

# Objetos
pessoa1 = Pessoa("Gabriel", 24)
saudacao = pessoa1.saudacao()
print(saudacao)

pessoa2 = Pessoa("Laís", 47)
saudacao = pessoa2.saudacao()
print(saudacao)

"""
Pontos positivos: Reutilização melhor do código, proteção das propriedades, herança, abstração...
Pontos negativos: Complexidade
"""