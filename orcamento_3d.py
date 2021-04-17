#Desenvolvido por Anderson Xavier 
# https://github.com/andersonlx
import os
os.system('cls') or None

RED   = "\033[1;31m"  
CYAN  = "\033[1;36m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"

print(RESET)

print(BOLD + 'Digite somente números...')
preco_filamento = float(input(BOLD  + 'Entre com o preço do Kg de Filamento (R$):\n ' + CYAN))

print(BOLD + 'Digite somente números...')
qtd_material = float(input(BOLD  + 'Entre com a Qtd. Material Usado (g):\n ' + CYAN))

print(BOLD + 'Digite somente as Horas sem os minutos...')
tempo_impressao = float(input(BOLD  + 'Entre com o Tempo de Impressão em (H):\n ' + CYAN))

print(BOLD + 'Separe os valores com ponto ".". ')
taxa_energia = float(input(BOLD  + 'Entre com a Taxa de Energia em (Kw/h):\n Ver aqui: https://www.aneel.gov.br/ranking-das-tarifas: \n Entre com o valor: \n' + CYAN))

print(BOLD + 'Digite somente números...')
consumo_impressora = float(input(BOLD  + 'Entre com o Consumo da Impressora (W):\n ' + CYAN))

print(BOLD + 'Digite somente números...')
margem_lucro = float(input(BOLD  + 'Entre com Margem Lucro em (%):\n ' + CYAN))

print(BOLD + 'Separe os valores com ponto ".". ')
despesas_avulsas = float(input(BOLD  + 'Entre com Despesas Avulsas em (R$):\n ' + CYAN))
os.system('cls') or None

consumo_filamento = (preco_filamento/1000)*qtd_material

x_tempo_impressao = tempo_impressao*taxa_energia
y_tempo_impressao = (consumo_impressora*x_tempo_impressao)/1000

grama_peca = (consumo_filamento+y_tempo_impressao)/qtd_material
custo_total = consumo_filamento+y_tempo_impressao
margem_lucro = (custo_total*(margem_lucro+100)/100)+despesas_avulsas

print(CYAN + 'O Consumo de Filamento é de: '+ RED + f'R${consumo_filamento:.2f} \n')
print(CYAN + 'O Consumo de energia elétrica é de: '+ RED + f'R${y_tempo_impressao:.2f} \n')
print(CYAN + 'Cada grama da sua peça custará: '+ RED + f'R${grama_peca:.2f} \n')
print(CYAN + 'O Custo Total é de: '+ RED + f'R${custo_total:.2f} \n')
print(CYAN + 'Valor a ser cobrado pela impressão é de: '+ RED + f'R${margem_lucro:.2f} \n')
print(RESET)

