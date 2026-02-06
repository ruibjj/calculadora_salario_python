nome = input('Digite seu nome')
salario = float(input('Digite seu salario mensal'))
gastos_a = float(input('Digite seus gastos mensais com alimentação'))
gastos_t = float(input('Digite seus gastos mensais com vale transporte'))
gastos_l = float(input('Digite seus gastos mensais com lazer'))
saldo_final = salario - gastos_a - gastos_t - gastos_l

if saldo_final >= 0:
    print(f'{nome} seus gastos com alimentação foram de R${gastos_a:.2f}')
    print(f'{nome} seus gastos com vale transporte foram de R${gastos_t:.2f}')
    print(f'{nome} seus gastos com lazer foram de R${gastos_l:.2f}')
    print(f'{nome} seu saldo no final do mes foi de R${saldo_final:,.2f}' .replace(',','x').replace('.',',').replace('x','.'))
else:
    print(f'{nome} seus gastos ultrapassaram o seu rendimento mensal e seu saldo final foi de {saldo_final:,.2f}' .replace (',','x') .replace('.',',') .replace('x' ,'.'))
