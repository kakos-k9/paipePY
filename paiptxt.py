arquivo = open("plan.txt", encoding="utf-8")

lista = []

for a in arquivo:
    ba = a.split("|")
    lista.append(ba)

for b in lista:
    COD = b[0].strip()
    NOME = b[1].strip()
    TELEFONE = b[2].strip()
    ENDERECO = b[3].strip()
    UF = b[4].strip()

    #print(COD)
    print(NOME)
    #print(TELEFONE)
    #print(ENDERECO)
    #print(UF)
    #print(f"Código: {COD}")
    #print(f"Nome: {NOME}")
    #print(f"Telefone: {TELEFONE}")
    #print(f"Endereço: {ENDERECO}")
    #print(f"UF: {UF}")

arquivo.close()

