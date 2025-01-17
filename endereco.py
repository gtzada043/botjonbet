import openpyxl
from openpyxl.styles import Alignment
from faker import Faker
import os

# Configurando o gerador de dados Faker
fake = Faker('pt_BR')

# Função para gerar um CEP no formato brasileiro
def gerar_cep():
    return fake.postcode()

def criar_planilha_ceps():
    # Solicitar ao usuário a quantidade de registros
    try:
        quantidade = int(input("Digite a quantidade de registros desejada: "))
        if quantidade <= 0:
            print("A quantidade deve ser um número inteiro positivo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return

    # Nome do arquivo da planilha
    nome_arquivo = "enderecos_ceps.xlsx"

    # Verificar se o arquivo já existe e apagá-lo
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)

    # Criar uma nova planilha
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Endereços"

    # Adicionar cabeçalhos
    cabecalhos = ["CEP", "Rua", "Cidade", "Estado", "País"]
    ws.append(cabecalhos)

    # Gerar dados fictícios e adicioná-los na planilha
    for _ in range(quantidade):
        cep = gerar_cep()
        rua = fake.street_name()
        cidade = fake.city()
        estado = fake.estado_sigla()
        pais = "Brasil"
        ws.append([cep, rua, cidade, estado, pais])

    # Ajustar alinhamento dos cabeçalhos
    for cell in ws[1]:
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Salvar a planilha
    wb.save(nome_arquivo)
    print(f"Planilha '{nome_arquivo}' criada com sucesso!")

# Executar o programa
if __name__ == "__main__":
    criar_planilha_ceps()
4