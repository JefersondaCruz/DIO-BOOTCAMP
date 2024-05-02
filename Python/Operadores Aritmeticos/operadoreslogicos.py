# and , exemplo saldo >= saque AND saque <= limite  PARA SER TRUE TUDO TEM QUE SER TRUE
# OR,  exmplo  saldo >= saque OR saque <= limite     PARA SER TRUE APENAS UM TEM QUE SER TRUE
# not, operador de negação   not 1000 > 1500 = true, falso com falso e true
# () 
print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True and True)
print(True or False and False)
print(False or False and False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True



exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2= (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)