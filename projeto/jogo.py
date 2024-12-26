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

  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida <= 0:
      self.__vida = 0 
  
  def atacar(self, alvo):
    dano = self.__nivel * 2
    alvo.receber_ataque(dano)
    print(f"\nO {self.get_nome()} está atacando {alvo.get_nome()} e causou: {dano} de dano! \n")
    
  

class Heroi(Personagem):

  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()} \n Habilidade: {self.__habilidade}\n"

  def ataque_especial(self, alvo):
    dano = self.get_nivel() * 5 
    alvo.receber_ataque(dano)
    print(f"\nO {self.get_nome()} usou {self.get_habilidade()} no {alvo.get_nome()} e causou: {dano} de dano! \n")
  
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
      str(input("Tecle Enter para iniciar a batalha..."))
      escolha = input("Escolha (1 - Ataque Normal, 2 Ataque Especial): ")

      
      if escolha == "1":
        self.heroi.atacar(self.inimigo)
      elif escolha == "2":
        self.heroi.ataque_especial(self.inimigo)
      elif escolha == "0":
        break
      else:
        print("Escolha inválida")

      if self.inimigo.get_vida() > 0:
        self.inimigo.atacar(self.heroi)

    if self.heroi.get_vida() > 0:
      print(f"Parabéns, você venceu...")
    else:
      print(f"O Heroi está morto...")



jogo = Jogo()
jogo.iniciando_batalha()