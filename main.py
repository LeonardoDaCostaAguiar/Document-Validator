from document_generator import generate_valid_document
from document_validator import is_cpf_valid, get_document_state


request = int(input("Digite:\n1 - Para gerar um novo número de CPF.\n2 - Para verificar a validade de um número de CPF.\n"))

if request == 1:
    new_document = generate_valid_document()
    print(f"IMPORTANTE: Esse serviço gera um número de CPF aleatório.\n"
          f"Este número pode estar em uso (ativo) e foi desenvolvido para ser usado apenas em testes de softwares.\n"
          f"CPF: {new_document}")

elif request == 2:
    document = input("Digite o número do CPF:\n")
    if is_cpf_valid(cpf=document):
        print("✅ CPF válido")
        print(get_document_state(list(document)))
    else:
        print("❌ CPF inválido. Por favor, verifique o número informado.")
else:
    print("Operação não identificada. Por favor, verifique as opções e tente novamente.")


