MAJORITY = 18

age = int(input("Digite a sua idade: "))

if age >= MAJORITY:
    print("Você é maior de idade.")
if age < MAJORITY:
    print("Você é menor de idade.")


if age >= MAJORITY:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


if age >= MAJORITY:
    print("Você é maior de idade.")
elif age == MAJORITY:
    print("Você tem exatamente a idade da maioridade.")
else:
    print("Você é menor de idade.")