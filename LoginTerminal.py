# coding=utf-8

# Sistema simples de login em python(terminal), desenvolvido por Everton 2019.

def acesso():
  print("============ Acesso Permitido!!! ===========")
  print('1 - Ver menu.')
  print('2 - Sair.\n')
  perg = int(input("Digite oque deseja fazer: "))
  if perg == 1:
      print("1 - White Hat")
      print("2 - Black Hat")
      print("3 - Grey Hat")
      quit()
  
  elif perg == 2:
      quit()

def quest():
  user = str(raw_input("Digite o usuário: "))
  password = str(raw_input("Digite a senha: "))
  codigo = str(raw_input("Digite o código verificador: "))
  
  if user == "teste" and password == "admin" and codigo == "abcd":
    acesso()

  else:
    print("=========== Acesso negado!!!! ==========\n\n")
    quest()
    while quest() == False:
     quest()

user = str(raw_input("Digite o usuário: "))
password = str(raw_input("Digite a senha: "))
codigo = str(raw_input("Digite o código verificador: "))

if user == "teste" and password == "admin" and codigo == "abcd":
    acesso()

else:
    print("=========== Acesso negado!!!! ============\n\n")
    quest()
    while quest() == False:
     quest()
     

      
    

