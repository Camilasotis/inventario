produto1 = {
      "id":1,"nome":"Vestido","preço":50.00,"quantidade":10,"categoria":"Vestuário"
      }
produto2 = {
      "id":2,"nome":"Mouse","preço":80.00,"quantidade":5,"categoria":"Eletrônicos"
      }
produto3 = {
      "id":3,"nome":"Banana","preço":2.00,"quantidade":50,"categoria":"Alimentos"
      }

inventario = []
inventario.append(produto1)
inventario.append(produto2)
inventario.append(produto3)

def menu():
    print("1-Adicionar um novo produto ao inventário.")
    print("2-Remover um produto do inventário.")
    print("3-Atualizar informações de um produto existente.")
    print("4-Listar todos os produtos de uma categoria específica.")
    print("5-Calcular o valor total em estoque.")
    print("6-Verificação de produtos. ")

def adicionar(): 
    id=input("Digite o id do produto: ")
    nome=input("Digite o nome do produto: ")
    preço=input("Digite o preço do produto: ")
    quantidade=input("Digite a quantidade do produto: ")
    categoria=input("Digite a categoria do produto:")

    inventario.append({"id":id,"nome":nome,"preço":preço,"quantidade":quantidade,"categoria":categoria}) 
    print(inventario)

def remover():
   id=input("Digite o ID do produto que deseja remover: ")
   for i in range(len(inventario)):
      if(inventario[i]["id"]==id):
       inventario.pop(i)
       print(inventario)
         
while(True):
    menu()
    op=input("Digite a opção desejada: ")
    
    match op:
       case "1": adicionar()
       case "2": remover()
       
