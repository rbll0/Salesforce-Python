# Projeto de Gerenciamento de Clientes e Produtos

## Participantes

- Gustavo Rabelo Frere | RM:553326
- Mellina Comelli Koike Tavares | RM:554046
- Marcelo Vieira Junior | RM:553640

## Descrição

Este projeto em Python tem como objetivo gerenciar informações de clientes e produtos em um banco de dados Oracle. Ele oferece funcionalidades para cadastro, alteração, exclusão, consulta e exportação de dados para arquivos JSON.

## Funcionalidades

- **Cadastro de Clientes**:
  - Inserir, alterar, excluir e consultar clientes.
  - Exportar relatório de clientes para JSON.

- **Cadastro de Produtos**:
  - Inserir, alterar, excluir e consultar produtos.
  - Exportar relatório de produtos para JSON.

## Requisitos

- Python 3.x
- Bibliotecas: `oracledb`, `pandas`, `json`

## Como Usar

1. **Configuração do Banco de Dados**: Certifique-se de ter acesso ao banco de dados Oracle com as credenciais corretas especificadas na função `conectar_bd()`.

2. **Execução do Programa**: Execute o script Python. Um menu interativo será exibido onde você pode escolher as operações desejadas para clientes e produtos.

3. **Operações Disponíveis**: Escolha uma das opções numeradas para cadastrar, alterar, excluir, consultar ou exportar dados para JSON.

4. **Exportação para JSON**: Quando solicitado, os relatórios de clientes e produtos serão exportados para arquivos JSON (`clientes.json` e `produtos.json`, respectivamente).

## Observações

- O programa utiliza a biblioteca `pandas` para formatação e exibição dos dados em formato tabular.
- A exportação para JSON é realizada utilizando a biblioteca padrão `json` do Python.

Este readme fornece uma visão geral do projeto e instruções básicas de uso. Certifique-se de ter todas as dependências instaladas e configurar corretamente o acesso ao banco de dados Oracle antes de executar o programa.
