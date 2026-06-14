# 📝 Registro de Decisões de Arquitetura (ADRs)

Este diretório contém os **Architectural Decision Records (ADRs)** para o DSE.LearnLab.

## O que é um ADR?

Um ADR é um documento curto que descreve uma decisão de design ou arquitetura significativa que foi tomada, incluindo o contexto da decisão, os fatores que a influenciaram, a alternativa escolhida e as suas consequências. 

Nosso objetivo é manter este registro transparente para que qualquer colaborador (atual ou futuro) possa entender o porquê de certas decisões técnicas terem sido tomadas.

---

## 📄 Template de ADR

Sempre que propor uma nova decisão de arquitetura, utilize o seguinte template (crie como `docs/adr/YYYY-ADR-XXXX-titulo-curto.md`):

```markdown
# ADR-XXXX: [Título Curto e Descritivo]

*   **Status**: [Proposed | Accepted | Rejected | Superseded]
*   **Data**: [AAAA-MM-DD]
*   **Autor(es)**: [Seu Nome ou Usuário do GitHub]
*   **Decisão Relacionada**: [Se houver, ex: "Substitui ADR-0002"]

## Contexto e Problema

Descreva o cenário atual, o problema técnico que precisa ser resolvido e as restrições ou requisitos associados.

## Opções Consideradas

Quais alternativas foram analisadas? (Forneça detalhes curtos sobre as vantagens e desvantagens de cada uma).

*   **Opção 1**: ...
*   **Opção 2**: ...

## Decisão Selecionada

Explique qual opção foi escolhida e o motivo técnico, conceitual ou metodológico que sustentou essa escolha.

## Consequências

Quais são os impactos dessa decisão no sistema?
*   **Pontos Positivos (Ganhos)**: ...
*   **Pontos Negativos (Riscos ou Dívida Técnica)**: ...
```

---

## 🏛️ Índice de ADRs Aprovados

| Código | Título | Data | Status |
| :--- | :--- | :--- | :--- |
| **[ADR-0001](#adr-0001-estrutura-inicial-e-fundacoes-do-projeto)** | Estrutura Inicial e Fundações do Projeto | 2026-06-14 | Accepted |

---

# ADR-0001: Estrutura Inicial e Fundações do Projeto

*   **Status**: Accepted
*   **Data**: 2026-06-14
*   **Autor(es)**: Antigravity (AI Assistant)

## Contexto e Problema

O **DSE.LearnLab** está sendo iniciado do zero como um projeto open source voltado para a comunidade. Como ele se diferencia de outras plataformas educacionais por se posicionar como um *laboratório baseado em evidências de aprendizagem*, é crucial que a fundação do repositório comunique claramente essa filosofia, divida as frentes de desenvolvimento (squads) e estabeleça regras de convivência, ética e segurança desde o primeiro commit.

## Opções Consideradas

*   **Opção 1: Iniciar diretamente pelo código** (criar o boilerplate FastAPI e pastas sem documentação).
    *   *Prós*: Código funcional mais rápido.
    *   *Contras*: Risco alto de desalinhamento de squads, falta de clareza conceitual na modelagem de dados educacionais, e ausência de diretrizes éticas sobre o uso de IA.
*   **Opção 2: Iniciar pela fundação documental estruturada** (criar README, LEARNING_PHILOSOPHY, ARCHITECTURE, ROADMAP, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, ETHICS e o diretório de ADRs).
    *   *Prós*: Garante alinhamento imediato sobre os objetivos científicos do produto, define a arquitetura técnica antes da codificação, estrutura o backlog por squads e incentiva contribuições qualificadas desde o início.
    *   *Contras*: Requer esforço inicial de escrita de documentação antes de ver o código rodando.

## Decisão Selecionada

Escolhemos a **Opção 2**. A criação prévia de documentos conceituais e estruturais fortes serve como o "coração" e a "bússola" do DSE.LearnLab. A filosofia de aprendizagem detalhada serve como a especificação de produto para as squads de código (Ciência da Aprendizagem, Escrita, Pesquisa, IA, etc.).

## Consequências

*   **Pontos Positivos (Ganhos)**:
    *   Facilidade no onboarding de novos colaboradores de qualquer squad.
    *   Clareza teórica baseada em Anders Ericsson, Barbara Oakley e Scott Young.
    *   Arquitetura de software planejada usando Clean Architecture e Docker/PostgreSQL/pgvector.
    *   Regras éticas explícitas sobre IA e portabilidade de dados.
*   **Pontos Negativos (Riscos ou Dívida Técnica)**:
    *   A documentação precisará ser ativamente atualizada no ROADMAP e CONTRIBUTING à medida que o projeto progredir para evitar obsolescência.
