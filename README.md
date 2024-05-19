Projeto de Gerenciamento de Clientes e Produtos
Participantes
Gustavo Rabelo Frere | RM:553326
Mellina Comelli Koike Tavares | RM:554046
Marcelo Veira Junior | RM:553640
Este projeto Python visa gerenciar informações de clientes e produtos em um banco de dados Oracle. Ele oferece funcionalidades para cadastro, alteração, exclusão, consulta e exportação de dados para arquivos JSON. Abaixo estão detalhadas as principais funcionalidades e a estrutura do projeto.

Requisitos
Python 3.x
Bibliotecas: oracledb, pandas, json
Estrutura do Projeto
main(): Função principal que controla o fluxo do programa, conectando-se ao banco de dados Oracle e exibindo um menu para operações de clientes e produtos.

Operações com Clientes (menu_clientes()):

Inserir cliente: Permite cadastrar um novo cliente no banco de dados.
Alterar cliente: Permite modificar os dados de um cliente existente.
Excluir cliente: Remove um cliente do banco de dados.
Consultar clientes: Mostra todos os clientes cadastrados em formato tabular.
Exportar relatório de clientes para JSON: Exporta todos os clientes cadastrados em um arquivo JSON.
Operações com Produtos (menu_produtos()):

Inserir produto: Adiciona um novo produto ao banco de dados.
Alterar produto: Permite alterar os detalhes de um produto existente.
Excluir produto: Remove um produto do banco de dados.
Consultar produtos: Exibe todos os produtos cadastrados em formato tabular.
Exportar relatório de produtos para JSON: Exporta todos os produtos cadastrados em um arquivo JSON.
Conexão com o Banco de Dados (conectar_bd()): Estabelece a conexão com o banco de dados Oracle usando oracledb.

Como Usar
Configuração do Banco de Dados: Certifique-se de ter acesso ao banco de dados Oracle com as credenciais corretas especificadas na função conectar_bd().

Execução do Programa: Execute o script Python. Será exibido um menu interativo onde você pode escolher as operações desejadas para clientes e produtos.

Operações Disponíveis: Escolha uma das opções numeradas para cadastrar, alterar, excluir, consultar ou exportar dados para JSON.

Exportação para JSON: Quando solicitado, os relatórios de clientes e produtos serão exportados para arquivos JSON (clientes.json e produtos.json, respectivamente).

Exemplo de Uso
python
Copiar código
# Exemplo de uso básico do programa
if __name__ == "__main__":
    main()
Observações
O programa utiliza a biblioteca pandas para formatar e exibir os dados em formato tabular.
A exportação para JSON é realizada utilizando a biblioteca padrão json do Python.
