# Documentação Técnica do Sistema de Gestão de Estoque (SGE)

## 1. Introdução

O Sistema de Gestão de Estoque (SGE) é uma aplicação web desenvolvida em Django e Django REST Framework, projetada para gerenciar produtos, fornecedores, categorias, marcas, entradas e saídas de estoque. A aplicação oferece uma interface administrativa, funcionalidades de API RESTful e um dashboard com métricas de estoque e vendas.

## 2. Tecnologias Utilizadas

A aplicação SGE é construída com as seguintes tecnologias:

| Tecnologia | Versão |
|---|---|
| Python | 3.13.2 |
| Django | 6.0.4 |
| Django REST Framework | 3.17.1 |
| Django REST Framework Simple JWT | 5.5.1 |
| PostgreSQL | 17 |
| Docker | Latest |
| Docker Compose | Latest |
| openpyxl | 3.1.5 |
| psycopg2-binary | 2.9.12 |
| python-dotenv | 1.2.2 |

## 3. Estrutura do Projeto

A estrutura do projeto segue o padrão de aplicações Django, com módulos (`apps`) dedicados a funcionalidades específicas. A seguir, uma visão geral dos principais diretórios e arquivos:

```
/sge
├── app/                  # Configurações globais, URLs principais, views e métricas do dashboard
├── authentication/       # Módulo de autenticação JWT
├── brands/               # Módulo para gestão de marcas
├── categories/           # Módulo para gestão de categorias
├── inflows/              # Módulo para gestão de entradas de estoque
├── outflows/             # Módulo para gestão de saídas de estoque
├── products/             # Módulo para gestão de produtos
├── suppliers/            # Módulo para gestão de fornecedores
├── Dockerfile            # Definição da imagem Docker da aplicação
├── docker-compose.yml    # Configuração do Docker Compose para orquestração de serviços
├── manage.py             # Utilitário de linha de comando do Django
├── requirements.txt      # Dependências do projeto
├── requirements_dev.txt  # Dependências de desenvolvimento
└── .env                  # Variáveis de ambiente (não versionado)
```

## 4. Funcionalidades Principais

### 4.1. Autenticação

O sistema utiliza autenticação baseada em JWT (JSON Web Tokens) através do `djangorestframework_simplejwt`. Os endpoints de API para autenticação são:

*   `api/v1/authentication/token/`: Obtenção de tokens de acesso e refresh.
*   `api/v1/authentication/token/refresh/`: Renovação do token de acesso.
*   `api/v1/authentication/token/verify/`: Verificação da validade de um token.

Além disso, a aplicação possui views de login e logout baseadas no sistema de autenticação padrão do Django.

### 4.2. Gestão de Produtos

O módulo de produtos (`products`) é central para o SGE, permitindo o gerenciamento completo dos itens em estoque. As funcionalidades incluem:

*   **CRUD Completo:** Criação, leitura, atualização e exclusão de produtos via interface web e API RESTful.
*   **Filtros:** Listagem de produtos com filtros por título, número de série, categoria e marca.
*   **Exportação:** Exportação de dados de produtos para arquivos Excel (`.xlsx`), incluindo categoria, marca, preços, quantidade e data de criação.
*   **Modelagem de Dados:** Cada produto possui título, categoria, marca, descrição, número de série, preço de custo, preço de venda, quantidade em estoque, e timestamps de criação/atualização.

### 4.3. Gestão de Entradas (Inflows)

O módulo de entradas (`inflows`) registra a entrada de produtos no estoque. As principais características são:

*   **Registro de Entradas:** Criação de registros de entrada, associando um fornecedor e um produto a uma quantidade específica.
*   **Atualização Automática de Estoque:** Após a criação de uma entrada, a quantidade do produto correspondente é automaticamente incrementada no estoque.
*   **Exportação:** Exportação de dados de entradas para arquivos Excel (`.xlsx`).

### 4.4. Gestão de Saídas (Outflows)

O módulo de saídas (`outflows`) gerencia a retirada de produtos do estoque, representando vendas ou outras movimentações. As funcionalidades incluem:

*   **Registro de Saídas:** Criação de registros de saída, associando um produto a uma quantidade específica.
*   **Atualização Automática de Estoque:** Após a criação de uma saída, a quantidade do produto correspondente é automaticamente decrementada no estoque.
*   **Exportação:** Exportação de dados de saídas para arquivos Excel (`.xlsx`).

### 4.5. Gestão de Marcas, Categorias e Fornecedores

Os módulos `brands`, `categories` e `suppliers` fornecem funcionalidades CRUD completas para gerenciar as entidades de apoio do sistema. Eles incluem:

*   **CRUD Completo:** Criação, leitura, atualização e exclusão de marcas, categorias e fornecedores via interface web e API RESTful.
*   **Tratamento de Erros:** O módulo de marcas, por exemplo, trata `ProtectedError` ao tentar excluir uma marca associada a produtos, exibindo uma mensagem amigável.
*   **Exportação:** Exportação de dados para arquivos Excel (`.xlsx`).

## 5. Arquitetura

O SGE é uma aplicação monolítica baseada no framework Django, seguindo o padrão MVT (Model-View-Template). A camada de API é implementada com Django REST Framework, fornecendo uma interface RESTful para interação programática.

### 5.1. Banco de Dados

O banco de dados principal utilizado é o PostgreSQL, configurado para ser executado em um contêiner Docker separado. Há também uma configuração para SQLite para desenvolvimento local.

### 5.2. Dockerização

A aplicação é dockerizada para facilitar o desenvolvimento, implantação e escalabilidade. O `Dockerfile` define o ambiente de execução da aplicação Python, e o `docker-compose.yml` orquestra os serviços da aplicação (web e banco de dados PostgreSQL).

## 6. Configuração e Instalação

Para configurar e executar o projeto localmente usando Docker Compose, siga os passos abaixo:

1.  **Clonar o Repositório:**
    ```bash
    git clone -b develop https://github.com/pombinhagab/sge.git
    cd sge
    ```

2.  **Configurar Variáveis de Ambiente:**
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```env
    SECRET_KEY=sua_chave_secreta_aqui
    DEBUG=True
    ```
    *Substitua `sua_chave_secreta_aqui` por uma chave secreta forte.*

3.  **Iniciar os Serviços com Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    Este comando irá construir as imagens Docker, criar os contêineres e iniciar a aplicação web e o banco de dados PostgreSQL.

4.  **Acessar a Aplicação:**
    A aplicação estará disponível em `http://localhost:8000`.

## 7. Métricas e Dashboard

O dashboard da aplicação, acessível na página inicial (`/`), exibe métricas importantes para a gestão de estoque e vendas, calculadas no módulo `app.metrics`:

*   **Métricas de Produtos:** Custo total em estoque, valor potencial de venda, quantidade total de produtos e lucro potencial.
*   **Métricas de Vendas:** Total de saídas, quantidade total de produtos vendidos, valor total das vendas e lucro total das vendas.
*   **Dados Diários de Vendas:** Séries históricas dos últimos 7 dias para o valor total das vendas e a quantidade de produtos vendidos.
*   **Gráficos:** Contagem de produtos por categoria e por marca, para visualização rápida da distribuição do estoque.

## 8. APIs RESTful

Além da interface web, o SGE expõe uma série de endpoints RESTful para cada módulo, permitindo a integração com outras aplicações. Todos os endpoints de API estão sob o prefixo `api/v1/` e exigem autenticação JWT.

| Módulo | Endpoints (Exemplos) |
|---|---|
| Autenticação | `/api/v1/authentication/token/`, `/api/v1/authentication/token/refresh/`, `/api/v1/authentication/token/verify/` |
| Produtos | `/api/v1/products/`, `/api/v1/products/{id}/` |
| Entradas | `/api/v1/inflows/` |
| Saídas | `/api/v1/outflows/` |
| Marcas | `/api/v1/brands/`, `/api/v1/brands/{id}/` |
| Categorias | `/api/v1/categories/`, `/api/v1/categories/{id}/` |
| Fornecedores | `/api/v1/suppliers/`, `/api/v1/suppliers/{id}/` |

## 9. Considerações Finais

O projeto SGE demonstra uma implementação robusta de um sistema de gestão de estoque utilizando as melhores práticas do Django e Django REST Framework, com foco em modularidade, segurança (JWT) e facilidade de implantação (Docker). A inclusão de um dashboard com métricas e a capacidade de exportar dados para Excel adicionam valor significativo para o gerenciamento do negócio.

---
