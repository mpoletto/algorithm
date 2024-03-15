#!/usr/bin/python3
movimentacoes = [
    {"produto": 1, "quantidade": 3}, 
    {"produto": 1, "quantidade": -3},
    {"produto": 2, "quantidade": 2},
    {"produto": 1, "quantidade": 4},
]

c = 0
r = []
for i in range(0, len(movimentacoes)):
    # print(c, movimentacoes[i])
    for j in range(1, len(movimentacoes)):
        print(movimentacoes[i], movimentacoes[j])
        if movimentacoes[i]['produto'] == movimentacoes[j]['produtos']:
            r[c] = {'produto': movimentacoes[i]['produto'], 'quantidade': movimentacoes[i]['quantidade'] + movimentacoes[j]['quantidade']}

    c = c + 1

        

        