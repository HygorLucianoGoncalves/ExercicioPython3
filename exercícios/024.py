senha = str(input("Qual e a senha do computador ")).strip()

print(senha[:11].upper() == "SENHA@TESTE")

################
city = str(input("Qual cidade vc naceu? ")).strip()

print(city[:5].upper() == "SANTO")

idade = int(input("Qual e sua idade? ")).strip()

print(idade[:2] < 18)