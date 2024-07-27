dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos quilometros forma rodados? "))

aluguel = (60 * dias) + (0.15 * km)

print(f"O valor do aluguel é R$ {aluguel}")