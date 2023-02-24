def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (dd/mm/aaaa): ")
    return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento}

def cadastrar_conta_bancaria(usuario):
    numero_conta = input("Informe o número da conta bancária: ")
    agencia = input("Informe a agência da conta bancária: ")
    saldo = float(input("Informe o saldo inicial da conta bancária: "))
    limite = float(input("Informe o limite de saque da conta bancária: "))
    return {"usuario": usuario, "numero_conta": numero_conta, "agencia": agencia, "saldo": saldo, "limite": limite, "extrato": "", "numero_saques": 0, "LIMITE_SAQUES": 3}

def depositar(conta_bancaria):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta_bancaria["saldo"] += valor
        conta_bancaria["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return conta_bancaria

def sacar(conta_bancaria):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta_bancaria["saldo"]
    excedeu_limite = valor > conta_bancaria["limite"]
    excedeu_saques = conta_bancaria["numero_saques"] >= conta_bancaria["LIMITE_SAQUES"]
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta_bancaria["saldo"] -= valor
        conta_bancaria["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta_bancaria["numero_saques"] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return conta_bancaria

def extrato(conta_bancaria):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta_bancaria["extrato"] else conta_bancaria["extrato"])
    print(f"\nSaldo: R$ {conta_bancaria['saldo']:.2f}")
    print("==========================================")
    return conta_bancaria
