#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.
notas = [float(input(f"Digite a nota {i + 1}: ")) for i in range(4)]
media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média:", media)