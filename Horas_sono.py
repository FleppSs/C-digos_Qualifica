horas_de_sono = [7, 5, 8, 6, 7.5, 8, 7]
horas_semana = 0
diass = 0
diasn = 0
meta = 7
for horas in horas_de_sono:
    horas_semana += horas
    if horas >= meta:
        diass += 1
    else:
        diasn += 1
print(f"Quantidade de dias que alcançaram a meta {diass} dias\nQuantidade de dias que não alcançaram a meta: {diasn} "
  f"dias\n Quantidade de horas totais {horas_semana}""")