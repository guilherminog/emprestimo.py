
n = str(input('Nome: '))
v = float(input('Valor da casa: '))
s = float(input('Salário mensal: '))
qa = int(input('Quantos anos de financiamento? '))
min = s * 30 / 100
ptc = v / (qa * 12)
print('Sr. {}, para pagar uma casa de R${:.2f} em {} anos.'.format(n, v, qa))
print('A prestação será de R${:.2f}'.format(ptc))
if ptc <= min:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')



