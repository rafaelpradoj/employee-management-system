# 🚀 Sistema de Gestão de Funcionários (CRUD)

Sistema de linha de comando para gerenciamento de funcionários, integrado com PostgreSQL.

## 🛠️ Tecnologias
- Python 3
- PostgreSQL
- Psycopg 3
- Dotenv
- **Hibridismo:** Suporte para execução via Docker ou instalação local.
- **Resiliência:** Sistema de retry que aguarda o banco de dados estar pronto.

## ✨ Funcionalidades
- Cadastro, listagem, atualização e exclusão de funcionários.
- Script de configuração automática de ambiente.
- Criação automática de tabelas no banco de dados.
- Tratamento de erros e validação de entradas.

## 🚀 Como Executar

### Opção A: Via Docker (Recomendado)
1. **Clone o projeto:**
   ```bash
   git clone https://github.com/rafaelpradoj/employee-management-system.git
   ```

2. **Execute o seguinte comando no terminal:**
   ```bash
   docker compose run --rm app && docker compose down -v
   ```

### Opção B: Instalação Local
1. **Clone o projeto:**
   ```bash
   git clone https://github.com/rafaelpradoj/employee-management-system.git
   ```
2. **Configure o ambiente automaticamente:**
   ```bash
   python setup_projeto.py
   ```

3. **Configure sua senha:**
   ```bash
   Edite o arquivo .env gerado e insira suas credenciais do PostgreSQL
   ```
4. **Rode o sistema:**
   ```bash
   python main.py
   ```
## 👨‍💻 Roadmap
- [ ] **Operação Sherlock:** Implementação de relatórios por departamento.
- [ ] **Exportação de dados:** Gerar arquivos em formato CSV/Excel.
- [ ] **Sistema de Logs:** Monitoramento de erros e operações.

## 📫 Contato
- **Nome:** Rafael Jesus
- **LinkedIn:** [Clique aqui para acessar meu perfil](https://www.linkedin.com/in/rafaelpradoj/)
- **E-mail:** [rafaelpradoj@gmail.com](mailto:rafaelpradoj@duck.com)
