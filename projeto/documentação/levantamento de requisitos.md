# Documentação do Projeto: Sistema de Gestão para assistência de informática (Fase 1 - MVP)
## I. Detalhes do Projeto

| Detalhe | Valor |
| :--- | :--- |
| **Papel Assumido** | Analista de Sistemas |
| **Cliente** | Central Tech Assistência de Informática |
| **Fase do Projeto** | Mínimo Produto Viável (MVP) com Integridade de Dados |
| **Foco Principal** | Gestão Unificada de Clientes, Serviços, Estoque/Vendas e Relatórios. |

## II. Escopo e Requisitos

### Objetivo Principal

O objetivo desta fase é criar um sistema que permita que o dono da assistência cadastre novos clientes com suas características, cadastre produtos, serviços e fornecedores, efetue vendas e visualize seu estoque.

### Requisitos Funcionais (RF)

| ID | Requisito |
| :--- | :--- |
| **001** | Gerenciar o Cadastro de Clientes com suas características (Nome, Cpf e Telefone)|
| **002** | Gerenciar o Cadastro de Produtos, Serviços, Fornecedores |
| **003** | Registrar a Entrada de Estoque por meio de Compras e Fornecedores. |
| **004** | Emissão de voucher de desconto em aniversário do cliente |
| **005** | Coleta de Feedback dos clientes |








### Requisitos Não Funcionais (RNF)

| ID | Requisito |
| :--- | :--- |
| **RNF01** | **Desempenho:** As páginas devem carregar em no máximo 3 segundos em conexões padrão. |
| **RNF02** | **Automação de Estoque:** O estoque deve ser atualizado automaticamente usando *Triggers* (Gatilhos) na Entrada de Compras e na Baixa de Vendas. |
| **RNF03** | **Responsividade:** A interface deve ser responsiva e adaptável a diferentes tamanhos de tela (desktop, tablet, smartphone).
| **RNF04** | **Usabilidade:** O sistema deve ser intuitivo e fácil de usar, com uma curva de aprendizado curta.
| **RNF05** | **Compatibilidade:** Deve ser compatível com os principais navegadores modernos (Chrome, Firefox, Edge, Safari).
| **RNF06** | **Disponibilidade:** O aplicativo deve estar disponível 24/7 com exceção de períodos programados de manutenção.

II. Modelo de Dados (Estrutura e Inteligência)
A estrutura do banco de dados relacional (CentralTech) é composta por 5 tabelas.

### 1. Entidades Principais (Tabelas)

| Módulo | Entidades (Tabelas) | Objetivo |
| :--- | :--- | :--- |
| **Pessoas** | `CLIENTE`, FORNECEDOR` | Cadastro de base de clientes e fornecedores. |
| **Logística** | `PRODUTOS`, `SERVICO`, `VENDAS` | Gestão de itens vendáveis, precificação e entrada de estoque. |
