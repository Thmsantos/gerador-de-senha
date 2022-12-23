from random import choice
import string

tamanho_senha = 6
caracteres = string.ascii_letters + string.digits 
senha = ''
for i in range(tamanho_senha):
  senha += choice(caracteres)

print("Senha: ",senha)
