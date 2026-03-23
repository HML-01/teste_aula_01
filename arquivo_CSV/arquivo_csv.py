# Arquivo CSV - Valores separados por vírgula (Comma-Separated Values)

import csv
dados=[
    ['nome', 'nota ', 'turma'],
    ['Angela', 10, '3°E'],
    ['Tiana', 9.5, '2°E'],
    ['Yana', 8.7, '1°E'],
]

with open('turma.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)
