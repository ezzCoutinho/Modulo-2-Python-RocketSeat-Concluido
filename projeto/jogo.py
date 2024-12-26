# Personagem: classe mae 
# Herói: controlado pelo usuário
# Inimigo: adversário do usuário

class Personagem:
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  def exibir_detalhes(self):
    return f" Nome: {self.get_nome()} \n Vida: {self.get_vida()} \n Nivel: {self.get_nivel()}"
  

class Heroi(Personagem):

  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()} \n Habilidade: {self.__habilidade}\n"
  
class Inimigo(Personagem):
  
  def __init__(self, nome, vida, nivel,tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()} \n Tipo: {self.__tipo} \n"
  
class Jogo:
  """" classe orquestradora do jogo."""
  def __init__(self):
    self.heroi = Heroi("Herói", 100, 5, "Super Força")
    self.inimigo = Inimigo("Morcego", 50, 3, "Voador")
  
  def iniciando_batalha(self):
    """" Fazer a gestão da batalha em turnos """

    while self.heroi.get_vida() > 0 and self.inimigo.get_vida():
      print("\n Detalhes dos Personagens: ")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())
      input("Tecle Enter para iniciar a batalha...")
      escolha = int(input("Escolha (1 - Ataque Normal, 2 Ataque Especial): "))

jogo = Jogo()
jogo.iniciando_batalha()