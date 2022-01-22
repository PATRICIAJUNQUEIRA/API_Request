# Exercío sobre API request com GitHub repositorio 
import requests

repositorio = requests.get('https://api.github.com/users/PATRICIAJUNQUEIRA/repos') # Recebe o nome do usuário e a lista dos repositorios 

if repositorio.status_code == 200:
  print('Repositorios Disponiveis: ')
  for x in repositorio.json():
    print(x['name']) 
else:
  print('Usuário não encontrado! ')   