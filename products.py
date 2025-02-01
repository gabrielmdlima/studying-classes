from utils import clear_screen

class Product:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.original_price = price
    self.stock = stock


  def update_stock(self, action):
    while True:
      try:
        amount = int(input('Quantos produtos: '))
        if amount < 0:
          print('Erro: Digite um valor maior que zero!')
          continue
        if action == 'venda':
          if amount > self.stock:
            print("Erro: Estoque insuficiente!")
            continue
          else:
            self.stock -= amount
            return
        else:
          self.stock += amount
          return
      except ValueError:
        print('Erro: Digite um valor numérico válido!')


  def set_discount(self):
    while True:
      try:
        discount = int(input('Qual o desconto em %: '))
        if discount < 0:
          print('Erro: Desconto não pode ser negativo!')
          continue
        new_price = self.price - self.price * discount / 100
        self.price = new_price
        return
      except ValueError:
        print('Erro: Digite um valor numérico válido!')


  def reset_price(self):
    self.price = self.original_price


def print_system(products):
  clear_screen()

  print('='*40)
  print(f'{"SISTEMA DA LOJA":^40}')
  print('='*40)

  print(f'\n{"PRODUTOS":<15}{"PREÇOS":<15}{"ESTOQUES":<15}')
  for p in products:
    price = f'R$ {p.price:.2f}'
    print(f'{p.name:<15}{price:<15}{p.stock:<15}')
  print('''
[1] Venda
[2] Devolução
[3] Aplicar promoção
[4] Remover promoção
[5] Adicionar produto
[6] Remover produto
[7] SAIR
''')


def add_product(products, name):
  while True:
    try:
      price = float(input('Preço do produto: '))
      stock = int(input('Quantidade em estoque: '))
      if price < 0 or stock < 0:
        print('Erro: Preço ou Estoque não podem ser negativos!')
        continue
      products.append(Product(name, price, stock))
      return
    except ValueError:
      print('Erro: Insira valores válidos!')


def get_name(products, choice):
  while True:
    name = str(input('Nome do produto: '))
    
    if choice == 5:
      return name, None

    for i, p in enumerate(products):
      if p.name.lower() == name.lower():
        return name, i

    print("Produto não encontrado!")

def run(products):
  error = ''
  while True:
    print_system(products)
    if error:
      print(error)
      error = ''

    try:
      choice = int(input('Opção: '))
      if choice < 1 or choice > 7:
        error = ('Erro: Opção inválida!')
        continue
    except ValueError:
      error = ('Erro: Digite um número válido!')
      continue

    if choice == 7:
      break
    name, indice = get_name(products, choice)

    if choice == 1:
      products[indice].update_stock(action='venda')

    elif choice == 2:
      products[indice].update_stock(action='devolucao')

    elif choice == 3:
      products[indice].set_discount()

    elif choice == 4:
      products[indice].reset_price()

    elif choice == 5:
      add_product(products, name)

    elif choice == 6:
      products.pop(indice)

  print('Obrigado por usar o sistema!')


if __name__ == '__main__':
  products = [
    Product('Notebook', 2500, 15),
    Product('Mouse', 50, 30),
    Product('Teclado', 100, 25),
    Product('Fone', 250, 20)
  ]
  run(products)
