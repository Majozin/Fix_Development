# Guia de adoção

## Objetivo

Aplicar o Fix Development a um projeto novo ou existente sem transformar a adoção em uma refatoração completa do repositório.

## 1. Copie a estrutura mínima

```text
AGENTS.md
docs/
templates/
.agents/skills/
work/BOARD.md
```

Adapte somente o que for específico do projeto.

## 2. Mantenha o AGENTS.md curto

O `AGENTS.md` deve responder:

- qual é a fonte de verdade;
- como tarefas são organizadas;
- quais estados/gates são obrigatórios;
- onde estão os documentos detalhados;
- quais comandos/regras locais são realmente essenciais.

Não copie toda a arquitetura, regras de negócio e documentação para dentro dele.

## 3. Acrescente documentação permanente do projeto

Além dos documentos do Fix Development, um projeto real pode precisar de:

```text
ARCHITECTURE.md
docs/design/
docs/decisions/
docs/contracts/
docs/operations/
docs/product/
```

O importante é que o conhecimento necessário ao agente esteja versionado e seja navegável.

## 4. Defina a convenção de tarefas

Escolha um identificador estável, por exemplo:

```text
ABC-001
APP-042
CORE-017
```

Não dependa de um prefixo específico do Fix Development.

Branch recomendada:

```text
task/<TASK>-<slug>
```

Pasta:

```text
work/<TASK>/
```

## 5. Crie o BOARD

Copie `templates/BOARD.md` para `work/BOARD.md`.

O board deve permitir descobrir rapidamente:
- tarefas planejadas;
- tarefa em andamento;
- dependências;
- estado;
- PR relacionado;
- bloqueios.

Não transforme o board em diário de execução; detalhes ficam na pasta da tarefa.

## 6. Crie a primeira tarefa

Copie:

```text
templates/TASK.md      → work/<TASK>/TASK.md
templates/PLAN.md      → work/<TASK>/PLAN.md
templates/STATUS.md    → work/<TASK>/STATUS.md
templates/EVIDENCE.md  → work/<TASK>/EVIDENCE.md
templates/REVIEW.md    → work/<TASK>/REVIEW.md
```

Preencha `TASK.md` antes de implementação.

## 7. Dê ao Codex um prompt curto

Exemplo:

```text
Inicie exclusivamente a ABC-001.

GitHub e os arquivos versionados são a fonte de verdade.
Siga AGENTS.md integralmente.
Reconsulte o estado fresco antes de agir.

Objetivo: implementar <comportamento>.
Não implemente tarefas adjacentes.

Leia primeiro:
- AGENTS.md
- work/BOARD.md
- work/ABC-001/TASK.md

Conduza a tarefa pelos estados do Fix Development e mantenha o feedback em português do Brasil.
```

Não é necessário repetir todas as regras de governança: elas já estão versionadas.

## 8. Adapte os gates ao tipo de projeto

Exemplos:

### Biblioteca
- testes unitários;
- compatibilidade de API;
- lint/typecheck;
- package build.

### API
- testes unitários e integração;
- migrations;
- contrato HTTP;
- segurança de input/auth;
- smoke test.

### Frontend
- testes de componente;
- build;
- acessibilidade relevante;
- regressão visual quando aplicável.

### Infraestrutura
- validação sintática;
- plan/dry-run;
- rollback;
- least privilege;
- smoke pós-deploy.

### ZimaOS Customized App
- aplicar também `docs/ZIMAOS-CUSTOM-APP.md`.

## 9. Introduza multiagente gradualmente

Comece com um Orquestrador e um fluxo sequencial.

Só introduza subagentes quando houver:
- subescopos independentes;
- contratos claros;
- volume suficiente para justificar coordenação.

A primeira otimização deve ser melhorar contratos e ferramentas, não aumentar o número de agentes.

## 10. Transforme feedback recorrente em sistema

Se o mesmo problema aparece repetidamente:

1. identifique a regra que faltou;
2. escolha o melhor lugar para codificá-la;
3. prefira teste/lint/script quando puder ser verificada mecanicamente;
4. caso contrário, atualize documentação/Skill;
5. remova duplicações e regras antigas conflitantes.

## 11. Migração de projeto existente

Não tente documentar tudo antes de começar.

Adote em camadas:

```text
1. AGENTS.md + estados
2. BOARD + tarefas atômicas
3. TASK/STATUS/EVIDENCE
4. PLAN + review
5. security gate proporcional
6. Skills específicas
7. automações e lints
```

A documentação deve crescer a partir de problemas reais e decisões duráveis.

## 12. Critério de adoção bem-sucedida

O padrão está funcionando quando uma pessoa que não participou da conversa consegue responder, apenas pelo repositório:

- qual tarefa está ativa?
- qual é o escopo?
- em que estado ela está?
- o que a bloqueia?
- qual plano foi escolhido?
- quais testes passaram?
- quais findings existem?
- qual commit/PR representa a entrega?
- o que falta para `DONE`?

## Status obrigatório desde a criação

Inclua `PROJECT_STATUS.json` antes da primeira entrega. Use `templates/PROJECT_STATUS.json` ou `python3 scripts/init_project_status.py /caminho --repository Majozin/nome`. Adote também PROJECT_STATUS.md, scripts/project_status.py e .github/workflows/project-status.yml. O baseline começa em 0%; atualize escopo, evidências e estado no mesmo PR da entrega.

