# 🤝 Guia de Contribuição (CONTRIBUTING.md)

Agradecemos o seu interesse em contribuir para o **DSE.LearnLab**! Este é um projeto de código aberto mantido por voluntários e entusiastas da comunidade *Data Science Enthusiasts*. Sua ajuda é fundamental para criarmos ferramentas educacionais baseadas em evidências científicas.

Todos os tipos de contribuição são muito bem-vindos: código, documentação, revisão ortográfica, testes de usabilidade, sugestões metodológicas ou novos designs de interface.

---

## 🧭 Fluxo Geral de Contribuição

### 1. Encontre uma Issue para Trabalhar
*   Explore o painel de **Issues** do nosso repositório.
*   Nossas Issues são rotuladas para facilitar a navegação:
    *   **Por Squad**: `squad:ciencia-aprendizagem`, `squad:escrita`, `squad:pesquisa`, `squad:ia-educacional`, `squad:analytics`, `squad:backend`, `squad:frontend`.
    *   **Por Nível**: `good first issue` (ótimo para iniciar), `help wanted` (precisa de ajuda ativa).
*   Antes de começar a trabalhar, deixe um comentário na Issue demonstrando seu interesse (ex: *"Olá! Gostaria de trabalhar nesta issue. Podem atribuí-la a mim?"*), para evitar que duas pessoas desenvolvam a mesma solução simultaneamente.

### 2. Estratégia de Branches e Commits
*   Faça um **Fork** do repositório original para sua conta pessoal.
*   Crie uma branch descritiva a partir da branch `main` seguindo o padrão:
    *   `feat/nome-da-squad/breve-descricao` (para novas funcionalidades).
    *   `fix/nome-da-squad/breve-descricao` (para correção de bugs).
    *   `docs/breve-descricao` (para documentações puras).
*   Exemplo: `git checkout -b feat/pesquisa/integracao-zotero`
*   Recomendamos a convenção de commits descritivos (**Conventional Commits**):
    *   `feat(pesquisa): adiciona cliente para consulta a API do Zotero`
    *   `fix(backend): corrige expiracao de token JWT`

### 3. Setup do Ambiente de Desenvolvimento (Backend)

Você precisará de **Python 3.11+** e **Docker** instalados em sua máquina.

1.  **Clone o seu fork localmente**:
    ```bash
    git clone https://github.com/SEU_USUARIO/dse_learn_lab.git
    cd dse_learn_lab
    ```
2.  **Crie e ative um ambiente virtual**:
    ```bash
    # No Windows (PowerShell):
    python -m venv venv
    .\venv\Scripts\Activate.ps1

    # No Linux/MacOS:
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instale as dependências de desenvolvimento**:
    ```bash
    pip install -r backend/requirements-dev.txt
    ```
4.  **Suba o banco de dados via Docker Compose** (PostgreSQL + pgvector):
    ```bash
    docker-compose up -d db
    ```
5.  **Rode as migrações e inicie o servidor local**:
    ```bash
    cd backend
    uvicorn app.main:app --reload
    ```
    *A API estará acessível em `http://localhost:8000` e a documentação interativa Swagger em `http://localhost:8000/docs`.*

---

## 🎨 Padrões de Código e Qualidade

*   **Formatadores e Linters**: Nós utilizamos o **Ruff** (ou a combinação de **Black** e **Flake8**) para manter o estilo de código Python alinhado com a PEP 8. Certifique-se de formatar seu código antes do commit.
*   **Testes**: Nós usamos o **pytest**. Nenhuma funcionalidade nova deve ser mesclada sem os testes unitários ou de integração correspondentes.
    *   Para rodar os testes localmente:
        ```bash
        pytest backend/tests/
        ```

---

## 📬 Enviando seu Pull Request (PR)

1.  Certifique-se de que sua branch está atualizada com a branch `main` do repositório original.
2.  Submeta seu Pull Request preenchendo o template padrão fornecido pelo GitHub.
3.  O PR passará por testes automatizados de CI e, em seguida, será revisado pelos mantenedores da Squad responsável.
4.  Responda ativamente aos feedbacks dos revisores no code review para acelerar o merge.
