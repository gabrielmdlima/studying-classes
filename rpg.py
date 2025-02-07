from utils import clear_screen

class Personagens:
  def __init__(self, name, vida, ataque, defesa):
    self.name = name
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa


  def realizar_ataque(self, ataque, defesa):
    pass


  def cura(self):
    pass


def print_personagens(personagem):
  if not personagem[0].defesa == 0:
    print(f'{"Heróis":^37}')
    print(' '+'-'*37)
    print(f'|{"CLASSE":^12}|{"VIDA":^6}|{"ATAQUE":^8}|{"DEFESA":^8}|')
    print('|'+'-'*37+'|')
    for i, d in enumerate(personagem):
      vida = f'{d.vida:02}'
      ataque = f'{d.ataque:02}'
      defesa = f'{d.defesa:02}'
      print(f'|{i+1}.{d.name:10}|{vida:^6}|{ataque:^8}|{defesa:^8}|')
  else:
    print(f'{"Monstros":^37}')
    print(' '+'-'*37)
    print(f'|{"CLASSE":^12}|{"VIDA":^11}|{"ATAQUE":^12}|')
    print('|'+'-'*37+'|')
    for i, d in enumerate(personagem):
      vida = f'{d.vida:02}'
      ataque = f'{d.ataque:02}'
      print(f'|{i+1}.{d.name:10}|{vida:^11}|{ataque:^12}|')
  print(' '+'-'*37)


def run(heroi, monstro):
  clear_screen()
  print_personagens(monstro)
  print_personagens(heroi)
  player = input('Escolha seu personagem: ')


if __name__ == '__main__':
  heroi = [
    Personagens('Cavaleiro', 10, 10, 5),
    Personagens('Mago', 15, 8, 8),
    Personagens('Tanque', 20, 5, 15),
    Personagens('Arqueiro', 5, 15, 5)
  ]

  monstro = [
    Personagens('Goblin', 5, 4, 0),
    Personagens('Lobo', 10, 7, 0),
    Personagens('Orc', 15, 10, 0)
  ]

  run(heroi, monstro)
