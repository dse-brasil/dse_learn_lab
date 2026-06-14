# 📚 DSE.LearnLab — Laboratório de Aprendizagem, Pesquisa e Produção de Conhecimento

![Versão](https://img.shields.io/badge/vers%C3%A3o-v1.0.0-blueviolet)

> **Plataforma Open Source para Aprendizagem Baseada em Prática, Pesquisa, Escrita e Evidências.**

Bem-vindo ao **DSE.LearnLab**, uma iniciativa da comunidade *Data Science Enthusiasts*. O DSE.LearnLab é um laboratório de código aberto focado em construir ferramentas de apoio a estudantes, pesquisadores e profissionais no desenvolvimento acelerado de competências de forma autodirigida e cientificamente fundamentada.

Diferente de sistemas educacionais tradicionais que tratam o aluno como um receptor passivo de informações (assistindo a vídeos e lendo slides), o LearnLab incentiva a **produção intelectual ativa**: praticar de forma deliberada, pesquisar fontes qualificadas, sintetizar ideias por escrito e construir portfólios de conhecimento tangíveis.

---

## 🗺️ Navegação Rápida

Para entender o projeto em profundidade, explore a nossa documentação de fundação:

*   **[Filosofia de Aprendizagem (LEARNING_PHILOSOPHY.md)](file:///c:/Users/ferna/projects/dse_learn_lab/LEARNING_PHILOSOPHY.md)**: O coração conceitual do projeto. Descubra os embasamentos neurocientíficos e metodológicos (Anders Ericsson, Barbara Oakley, Scott Young).
*   **[Arquitetura do Sistema (ARCHITECTURE.md)](file:///c:/Users/ferna/projects/dse_learn_lab/ARCHITECTURE.md)**: Detalhes sobre a arquitetura técnica de microsserviços/módulos, tecnologias planejadas (FastAPI, PostgreSQL, Docker) e integrações.
*   **[Roadmap de Desenvolvimento (ROADMAP.md)](file:///c:/Users/ferna/projects/dse_learn_lab/ROADMAP.md)**: As fases de lançamento do projeto, do MVP (v1.0) até o ecossistema maduro (v3.0).
*   **[Guia de Contribuição (CONTRIBUTING.md)](file:///c:/Users/ferna/projects/dse_learn_lab/CONTRIBUTING.md)**: Como configurar seu ambiente de desenvolvimento local, fluxos de Git e diretrizes para cada Squad.
*   **[Código de Ética (ETHICS.md)](file:///c:/Users/ferna/projects/dse_learn_lab/ETHICS.md)**: Nossos compromissos com o uso responsável da Inteligência Artificial, proteção de dados de aprendizado e equidade no acesso.
*   **[Registro de Decisões de Arquitetura (docs/adr/)](file:///c:/Users/ferna/projects/dse_learn_lab/docs/adr/README.md)**: Histórico documentado das decisões técnicas mais importantes tomadas ao longo do projeto.

---

## 👥 Frentes de Trabalho (Squads)

Nosso desenvolvimento é descentralizado em frentes de especialização:

1.  **📚 Ciência da Aprendizagem**: Responsável pelas mecânicas de estudo ativo, prática deliberada, cronogramas de repetição espaçada, metacognição e evolução de competências.
2.  **✍️ Escrita & Produção Intelectual**: Focada na criação e gestão de notas, resumos, sínteses, artigos e relatórios técnicos usando Markdown, além da exportação de documentos.
3.  **🔬 Pesquisa & Evidências**: Responsável pela curadoria científica, gestão de fontes bibliográficas, integração com o Zotero e motores de busca científica (como arXiv) e sistema de citações.
4.  **🤖 IA para Aprendizagem**: Desenvolvimento de tutores socráticos inteligentes, geradores de perguntas personalizadas e sistemas de avaliação automatizada baseada em IA generativa.
5.  **📊 Analytics Educacional**: Construção de painéis visuais com indicadores reais de estudo (tempo de prática real, calorias cognitivas, mapas de competências).
6.  **⚙️ Backend & Plataforma**: Infraestrutura, APIs, segurança, persistência e integrações core do ecossistema.
7.  **💻 Frontend & UX**: Interfaces limpas, focadas no fluxo de trabalho livre de distrações, responsivas e visualmente deslumbrantes.

---

## 🛠️ Tecnologias Planejadas

*   **Linguagem & Framework**: Python 3.11+ com FastAPI para APIs rápidas e seguras.
*   **Banco de Dados**: PostgreSQL (com extensão `pgvector` para buscas semânticas de anotações e artigos).
*   **Infraestrutura**: Docker e Docker Compose para fácil inicialização local e implantação estável.
*   **IA Generativa**: Integração com LLMs (via APIs do Google Gemini, OpenAI ou modelos locais via Ollama) para tutoria ativa.
*   **Interface**: Desenvolvida de forma moderna, responsiva e com foco em fluidez de escrita.

---

## 🚀 Como Executar o Projeto

Você pode executar o backend do DSE.LearnLab de duas formas: usando **Docker** (com PostgreSQL + pgvector) ou **diretamente na sua máquina** (com fallback automático para SQLite).

### Opção 1: Via Docker (Recomendado para Produção e Testes Completos)
Certifique-se de que o **Docker Desktop** está ativo em sua máquina e execute:
```bash
docker-compose up --build
```
*A API estará disponível em `http://localhost:8000` e o banco PostgreSQL ativo na porta 5432.*

### Opção 2: Localmente via Python (Ambiente de Desenvolvimento Simplificado)
Se preferir rodar de forma leve sem Docker, a aplicação utilizará automaticamente o **SQLite** como banco local caso não encontre o PostgreSQL configurado ou os drivers correspondentes.

1. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   *   **Windows (PowerShell)**: `.\venv\Scripts\Activate.ps1`
   *   **Linux/MacOS**: `source venv/bin/activate`
3. Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Inicie o servidor FastAPI:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```
   *A API estará acessível em `http://localhost:8000`.*

---

## 🤝 Junte-se a Nós!

Procuramos colaboradores de diversos perfis:
*   **Estudantes & Educadores** interessados em testar e validar abordagens de estudo.
*   **Desenvolvedores Backend & Frontend** que querem construir ferramentas eficientes.
*   **Cientistas de Dados & Especialistas em IA** para criar modelos de análise e tutoria.
*   **Pesquisadores** para ajudar com a fundamentação metodológica e gestão de referências.

Consulte o nosso **[Guia de Contribuição](file:///c:/Users/ferna/projects/dse_learn_lab/CONTRIBUTING.md)**, respeite o nosso **[Código de Conduta (CODE_OF_CONDUCT.md)](file:///c:/Users/ferna/projects/dse_learn_lab/CODE_OF_CONDUCT.md)**, e vamos construir o futuro da aprendizagem ativa juntos!

---

## 👥 Colaboradores

Atualmente, o projeto é mantido e desenvolvido por:
* **Fernando Torres Ferreira Silva** ([@fertorresfs](https://github.com/fertorresfs)) — Idealizador e desenvolvedor ativo, responsável pela arquitetura do bot, integração de RAG, segurança e painel administrativo web.

---

## ⚖️ Licença

Este projeto é de uso interno e educacional da comunidade **Data Science Enthusiasts (DSE)**. Consulte as políticas internas de contribuição antes de realizar pull requests.

