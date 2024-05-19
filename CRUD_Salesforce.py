import oracledb
import pandas as pd
import json

def main():
    conn = conectar_bd()
    opc = 0
    while opc != 3:
        print("1-Cadastro de Clientes ")
        print("2-Cadastro de Produtos")
        print("3-Sair")

        opc = int(input("Digite a opção (1-3): "))

        if opc == 1:
            menu_clientes(conn)
        elif opc == 2:
            menu_produtos(conn)

    conn.close()

def menu_clientes(conn):
    opc = 0
    while opc != 7:
        print("\nMenu Clientes")
        print("1-Inserir cliente")
        print("2-Alterar cliente")
        print("3-Excluir cliente")
        print("4-Consultar clientes")
        print("5-Exportar relatório de todos os clientes para um arquivo JSON")
        print("6-Voltar para o menu principal")

        opc = int(input("Digite a opção (1-6): "))

        if opc == 1:
            cadastrar_cliente(conn)
        elif opc == 2:
            alterar_cliente(conn)
        elif opc == 3:
            excluir_cliente(conn)
        elif opc == 4:
            relatorio_clientes(conn)
        elif opc == 5:
            exportar_json_clientes(conn)
        elif opc == 6:
            return  # Retorna para o menu principal


def menu_produtos(conn):
    opc = 0
    while opc != 5:
        print("\nMenu Produtos")
        print("1-Inserir produto")
        print("2-Alterar produto")
        print("3-Excluir produto")
        print("4-Consultar produtos")
        print("5-Exportar relatório de todos os produtos para um arquivo JSON")
        print("6-Voltar para o menu principal")

        print("-------------------------")

        opc = int(input("Digite a opção (1-6): "))

        print("-------------------------")

        if opc == 1:
            cadastrar_produto(conn)
        elif opc == 2:
            alterar_produto(conn)
        elif opc == 3:
            excluir_produto(conn)
        elif opc == 4:
            relatorio_produtos(conn)
        elif opc == 5:
            exportar_json_produtos(conn)

def conectar_bd():
    try:
        conn = oracledb.connect(user='rm553326', password='091003', dsn='oracle.fiap.com.br/orcl')
    except oracledb.DatabaseError as e:
        print("Erro ao conectar ao banco de dados:", e)
        exit(1)
    else:
        return conn

def cadastrar_cliente(conn):
    try:
        nome_cliente = input("Digite o nome do cliente: ")
        if not nome_cliente or nome_cliente.isdigit():
            print("Nome do cliente inválido.")
            return

        email_corporativo = input("Digite o email corporativo do cliente: ")
        if not email_corporativo or email_corporativo.isdigit():
            print("Email corporativo inválido.")
            return

        endereco = input("Digite o endereço do cliente: ")
        if not endereco or endereco.isdigit():
            print("Endereço inválido.")
            return

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cliente (nome_cliente, email_corporativo, endereco) VALUES (:1, :2, :3)",
                       (nome_cliente, email_corporativo, endereco))
        conn.commit()
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar cliente:", e)


def alterar_cliente(conn):
    try:
        cd_cliente = int(
            input("Digite o código do cliente que deseja alterar (caso não tenha o código consulte no menu): "))

        # Verifica se o cliente com o código fornecido existe
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Cliente WHERE cd_cliente = :1", (cd_cliente,))
        if not cursor.fetchone():
            print(f"O cliente com o código {cd_cliente} não foi encontrado.")
            return

        novo_nome = input("Digite o novo nome do cliente: ")
        if not novo_nome.isalpha():
            raise ValueError("O novo nome do cliente deve ser uma string.")

        novo_email = input("Digite o novo email corporativo do cliente: ")
        if '@' not in novo_email:
            raise ValueError("O novo email corporativo do cliente deve ser um endereço de email válido.")

        novo_endereco = input("Digite o novo endereço do cliente: ")
        if not novo_endereco:
            raise ValueError("O novo endereço do cliente não pode estar vazio.")

        # Atualiza o cliente
        cursor.execute(
            "UPDATE Cliente SET nome_cliente = :1, email_corporativo = :2, endereco = :3 WHERE cd_cliente = :4",
            (novo_nome, novo_email, novo_endereco, cd_cliente))
        conn.commit()
        print("Cliente alterado com sucesso!")
    except ValueError as ve:
        print("Erro ao alterar cliente:", ve)
    except Exception as e:
        print("Erro ao alterar cliente:", e)


def excluir_cliente(conn):
    try:
        cd_cliente = int(input("Digite o código do cliente que deseja excluir: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cliente WHERE cd_cliente = :1", (cd_cliente,))
        conn.commit()
        print("Cliente excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir cliente:", e)



def relatorio_clientes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

        # Salve as configurações originais
        original_max_columns = pd.get_option('display.max_columns')
        original_max_rows = pd.get_option('display.max_rows')
        original_max_colwidth = pd.get_option('display.max_colwidth')

        # Configure pandas para exibir todas as colunas e linhas
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_colwidth', None)

        print(df)

        # Restaure as configurações originais
        pd.set_option('display.max_columns', original_max_columns)
        pd.set_option('display.max_rows', original_max_rows)
        pd.set_option('display.max_colwidth', original_max_colwidth)
    except Exception as e:
        print("Erro ao gerar relatório de clientes:", e)


def exportar_json_clientes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cliente")
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({"cd_cliente": row[0], "nome_cliente": row[1], "email_corporativo": row[2], "endereco": row[3]})
        with open("clientes.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Relatório de clientes exportado para clientes.json")
    except Exception as e:
        print("Erro ao exportar relatório de clientes para JSON:", e)


def cadastrar_produto(conn):
    try:
        nome_prod = input("Digite o nome do produto: ")
        if not nome_prod.isalpha():
            raise ValueError("O nome do produto é invalido.")

        desc_prod = input("Digite a descrição do produto: ")
        if not desc_prod.isalpha():
            raise ValueError("A descrição do produto está inválida.")

        valor_prod = float(input("Digite o valor do produto: "))
        if valor_prod <= 0:
            raise ValueError("O valor do produto deve ser um número positivo.")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Produto (nome_prod, valor_prod, desc_prod) VALUES (:1, :2, :3)", (nome_prod, valor_prod, desc_prod))
        conn.commit()
        print("Produto cadastrado com sucesso!")
    except ValueError as ve:
        print("Erro ao cadastrar produto:", ve)
    except Exception as e:
        print("Erro ao cadastrar produto:", e)

def alterar_produto(conn):
    try:
        cd_prod = int(
            input("Digite o código do produto que deseja alterar (Caso não tenha o código, consulte no menu): "))

        # Verifica se o produto com o código fornecido existe
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Produto WHERE cd_prod = :1", (cd_prod,))
        if not cursor.fetchone():
            print(f"O produto com o código {cd_prod} não foi encontrado.")
            return

        novo_nome = input("Digite o novo nome do produto: ")
        if not novo_nome.isalpha():
            raise ValueError("O novo nome do produto deve ser uma string.")

        novo_valor = float(input("Digite o novo valor do produto: "))
        if novo_valor <= 0:
            raise ValueError("O novo valor do produto deve ser um número positivo.")

        nova_descricao = input("Digite a nova descrição do produto: ")
        if not nova_descricao.isalpha():
            raise ValueError("A nova descrição do produto deve ser uma string.")

        # Atualiza o produto
        cursor.execute("UPDATE Produto SET nome_prod = :1, valor_prod = :2, desc_prod = :3 WHERE cd_prod = :4",
                       (novo_nome, novo_valor, nova_descricao, cd_prod))
        conn.commit()
        print("Produto alterado com sucesso!")
    except ValueError as ve:
        print("Erro ao alterar produto:", ve)
    except Exception as e:
        print("Erro ao alterar produto:", e)

def excluir_produto(conn):
    try:
        cd_prod = int(input("Digite o código do produto que deseja excluir: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produto WHERE cd_prod = :1", (cd_prod,))
        conn.commit()
        print("Produto excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir produto:", e)


def relatorio_produtos(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

        # Salve as configurações originais
        original_max_columns = pd.get_option('display.max_columns')
        original_max_rows = pd.get_option('display.max_rows')
        original_max_colwidth = pd.get_option('display.max_colwidth')

        # Configure pandas para exibir todas as colunas e linhas
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_colwidth', None)

        print(df)

        # Restaure as configurações originais
        pd.set_option('display.max_columns', original_max_columns)
        pd.set_option('display.max_rows', original_max_rows)
        pd.set_option('display.max_colwidth', original_max_colwidth)
    except Exception as e:
        print("Erro ao gerar relatório de produtos:", e)
import json

def exportar_json_produtos(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produto")
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({
                "cd_prod": row[0],
                "nome_prod": row[1],
                "valor_prod": row[2],
                "desc_prod": row[3]
            })
        with open("produtos.json", "w", encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Relatório de produtos exportado para produtos.json")
    except Exception as e:
        print("Erro ao exportar relatório de produtos para JSON:", e)


if __name__ == "__main__":
    main()
