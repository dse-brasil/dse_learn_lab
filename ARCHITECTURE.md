# 🏗️ Arquitetura do Sistema (ARCHITECTURE.md)

Este documento descreve as diretrizes arquiteturais, a estrutura de pastas e as decisões técnicas de alto nível que governam o desenvolvimento do **DSE.LearnLab**.

---

## 📐 Visão Geral do Sistema

O DSE.LearnLab é construído seguindo os princípios de **Clean Architecture** (Arquitetura Limpa), visando desacoplar a lógica de negócio principal (as regras científicas de aprendizagem e competências) dos detalhes de infraestrutura (banco de dados, frameworks web e APIs de IA).

### Diagrama de Blocos da Arquitetura

```mermaid
graph TD
    subgraph Cliente (Frontend & UX)
        UI["Interface do Estudante (SPA Web/Desktop)"]
        EditorMD["Editor Markdown Interno"]
    end

    subgraph Plataforma API (Backend - FastAPI)
        API["Controladores API (Rotas)"]
        UseCase["Casos de Uso (Core Logic)"]
        Domain["Entidades de Domínio (User, Practice, Reference, Note)"]
        Adapters["Adaptadores (DB Repositories, AI Clients)"]
    end

    subgraph Persistência & Serviços Externos
        DB[("PostgreSQL + pgvector")]
        Zotero["Zotero API (Referências)"]
        LLM["Provedores LLM (Gemini, OpenAI, Ollama)"]
    end

    UI --> API
    API --> UseCase
    UseCase --> Domain
    UseCase --> Adapters
    Adapters --> DB
    Adapters --> Zotero
    Adapters --> LLM
```

---

## 💻 Stack Tecnológica

1.  **Backend Core**:
    *   **Python 3.11+**: Linguagem robusta para ciência de dados, IA e desenvolvimento web estruturado.
    *   **FastAPI**: Framework assíncrono de alto desempenho para construção de APIs RESTful com validação automática de dados via Pydantic.
    *   **SQLAlchemy / SQLModel**: ORM para mapeamento objeto-relacional com suporte total a tipagem estática.
2.  **Banco de Dados**:
    *   **PostgreSQL**: Banco relacional robusto e escalável.
    *   **pgvector**: Extensão do PostgreSQL que permite armazenamento e busca de vetores de alta dimensionalidade (embeddings), ideal para pesquisa semântica em resumos e notas de estudo.
3.  **Inteligência Artificial (IA)**:
    *   **LangChain / LlamaIndex**: Frameworks para orquestração de chamadas de LLM, RAG (Geração Aumentada por Recuperação) nas notas e histórico de conversas do tutor.
    *   **Google Gemini SDK** & **OpenAI API**: Conexões nativas para modelos comerciais de ponta.
    *   **Ollama**: Suporte para LLMs locais executando localmente (ex: Llama3, Mistral) para garantir total privacidade dos dados do estudante.
4.  **Desenvolvimento & Infraestrutura**:
    *   **Docker & Docker Compose**: Isolamento de ambiente e simplificação da inicialização do PostgreSQL com suporte a pgvector.

---

## 🗂️ Estrutura de Pastas Sugerida

A estrutura do projeto backend reflete a separação de responsabilidades e a independência dos squads:

```text
dse_learn_lab/
├── docs/                      # Documentação técnica do projeto (ADRs, etc.)
│   └── adr/                   # Architectural Decision Records
├── backend/                   # Código-fonte do Backend (FastAPI)
│   ├── app/
│   │   ├── core/              # Configurações globais, segurança, utilitários
│   │   ├── domain/            # Entidades puras e lógica de negócio
│   │   ├── use_cases/         # Casos de uso (Lógica de orquestração por Squad)
│   │   │   ├── learning/      # Regras da Squad Ciência da Aprendizagem
│   │   │   ├── writing/       # Regras da Squad Escrita & Notas
│   │   │   ├── research/      # Regras da Squad Pesquisa & Referências
│   │   │   ├── ai/            # Regras da Squad IA Educacional
│   │   │   └── analytics/     # Regras da Squad Analytics
│   │   ├── adapters/          # Implementações de banco de dados, clientes HTTP e IA
│   │   └── api/               # Controladores HTTP, rotas e payloads (Pydantic)
│   ├── tests/                 # Testes automatizados (pytest)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                  # Código-fonte do Frontend (A ser definido pela Squad Frontend)
├── docker-compose.yml         # Orquestração do PostgreSQL, pgvector e Backend
└── README.md
```

---

## 💾 Modelagem de Dados Estrutural (Foco v1.0 e v1.5)

Para dar suporte aos pilares científicos do projeto, nossa modelagem relacional prevê as seguintes estruturas principais:

1.  **Usuário (`User`) & Perfil (`Profile`)**:
    *   Credenciais, níveis de experiência e áreas de interesse atuais.
2.  **Trilha de Aprendizagem (`StudyTrail`) & Competências (`Competence`)**:
    *   Estruturação hierárquica de habilidades a serem desenvolvidas pelo estudante.
3.  **Registro de Prática Deliberada (`PracticeLog`)**:
    *   **Meta da sessão**: O que exatamente o estudante planejou praticar (ex: "Criar uma API mockada").
    *   **Nível de Dificuldade Estimado**: Medição de entrada na zona de desconforto.
    *   **Resultado produzido**: Texto do estudante contendo o link do código ou reflexão.
    *   **Feedback recebido**: Resumo do feedback de IA ou autoavaliação guiada.
    *   **Métricas metacognitivas**: Autoavaliação pós-prática (Ex: "Que erros cometi?", "Como posso melhorar?").
4.  **Referência Bibliográfica (`Reference`)**:
    *   Armazena metadados de artigos, livros, URLs.
    *   Conexão direta com chaves de sincronização do Zotero ou DOIs do PubMed/arXiv.
5.  **Anotação de Estudo (`StudyNote`)**:
    *   Documento Markdown escrito pelo estudante.
    *   Vetor associado no `pgvector` para buscas semânticas automáticas durante discussões com o tutor de IA.

---

## 🔒 Princípios de Segurança e Privacidade

*   **Autenticação**: Baseada em OAuth2 com tokens JWT.
*   **Privacidade de Dados de Aprendizagem**: O histórico de estudo, notas e interações do tutor de IA são informações confidenciais do usuário. A arquitetura suporta configurações híbridas de LLM (com opção de usar motores locais via Ollama para evitar envio de resumos e notas a servidores de terceiros).
