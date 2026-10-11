# AGENTS.md

Este arquivo é o **mapa operacional** do repositório. Mantenha-o curto. Detalhes vivem em `docs/`, `templates/` e na documentação específica do projeto que adotar este modelo.

## Idioma

- Interações, feedbacks, estados, relatórios, findings e resumos para usuários: **português do Brasil**.
- Preserve nomes de código, APIs, comandos, paths e termos técnicos quando a tradução piorar a precisão.
- Seja objetivo: estado atual, evidência relevante, próximo passo.

## Fonte de verdade

- GitHub e arquivos versionados do repositório são a fonte de verdade.
- Antes de agir, atualize o estado relevante: branch base, branch da tarefa, PR, CI, review threads, `work/BOARD.md`, `TASK.md`, `STATUS.md` e dependências.
- Não presuma estado de conversas anteriores quando puder consultá-lo.

## Tarefa atômica

- Trabalhe exclusivamente no escopo da tarefa ativa.
- Não implemente tarefas futuras ou adjacentes.
- Não corrija falhas não relacionadas somente para deixar o CI global verde.
- Se uma dependência impedir diretamente a tarefa, registre `BLOCKED_BY=<referência>`.
- Se um gate herdado/externo falhar sem ser causado pela tarefa, registre `DEFERRED_GATE=<referência>`.
- Uma regressão causada pela tarefa nunca pode ser classificada como `DEFERRED_GATE`.

## Ciclo obrigatório

Para mudanças não triviais, seguir:

`PLANNED → INTAKE → PLANNING → READY → IMPLEMENTING → VERIFYING → IN_REVIEW → SECURITY_REVIEW → READY_TO_MERGE → MERGED → CLOSEOUT → DONE`

Estados excepcionais: `BLOCKED`, `CANCELLED`.

Regras de transição: `docs/ESTADOS.md`.

## Planejamento antes de código

Antes de implementar mudança não trivial:

1. ler `TASK.md` e contratos relevantes;
2. identificar estado atual e dependências;
3. produzir/atualizar `PLAN.md`;
4. definir arquivos/superfícies afetadas, testes, riscos e rollback quando aplicável;
5. somente então iniciar a implementação.

Fluxo completo: `docs/FLUXO-DE-TRABALHO.md`.

## Economia de tokens

Contexto é recurso escasso. Seguir `docs/ECONOMIA-DE-TOKENS.md`.

Princípios mínimos:

- pesquisar antes de ler arquivos inteiros;
- ler primeiro índices, contratos, diffs e trechos relevantes;
- não reabrir conteúdo imutável sem motivo;
- usar testes focados antes de suítes globais;
- buscar somente passos/logs de CI necessários para diagnosticar a falha;
- não repetir no feedback informações já registradas e inalteradas;
- fornecer a subagentes apenas o contrato e contexto necessários;
- ampliar o contexto quando segurança, migração, compatibilidade ou incerteza exigirem;
- nunca economizar tokens sacrificando correção.

## Multiagente

- Paralelizar somente subescopos realmente independentes.
- Definir contrato antes de iniciar trabalho paralelo.
- Evitar agentes concorrendo sobre a mesma superfície mutável.
- Cada agente deve ter objetivo, limites, entradas, saída esperada e critério de conclusão.
- O Orquestrador integra e verifica; não apenas concatena resultados.

Detalhes: `docs/MULTIAGENTE.md`.

## Testes e evidências

- Começar pela menor validação capaz de detectar regressão no escopo alterado.
- Expandir para integração/global somente nos gates previstos.
- Não declarar `PASS` sem evidência verificável.
- Registrar evidências progressivamente em `EVIDENCE.md`.
- Preferir resumo do comando + resultado + identificador do run/commit; não copiar logs enormes.

Qualidade: `docs/REVISAO-E-QUALIDADE.md`.

## Revisão e segurança

- A autorrevisão do implementador é obrigatória, mas não substitui revisão independente quando exigida pelo risco da tarefa.
- Findings devem apontar impacto, evidência e localização concreta.
- Avaliar segurança proporcionalmente à superfície alterada.
- Findings críticos/altos não resolvidos impedem merge.

Segurança: `docs/SEGURANCA.md`.

## Arquivos por tarefa

Cada tarefa deve manter:

- `TASK.md` — contrato de escopo e aceite;
- `PLAN.md` — estratégia aprovada;
- `STATUS.md` — estado atual e classificações;
- `EVIDENCE.md` — evidências acumuladas;
- `REVIEW.md` — revisão e findings quando houver implementação.

Use `templates/` como base.

## ZimaOS Customized App

Se a tarefa envolver implantação como app customizado no ZimaOS, ler também `docs/ZIMAOS-CUSTOM-APP.md` e aplicar seus gates adicionais de persistência, portas, healthcheck, backup, atualização, rollback e pós-reboot.

## Fechamento

Uma tarefa só pode chegar a `DONE` quando, conforme aplicável:

- implementação e documentação estão integradas;
- testes/gates requeridos passaram ou gates herdados foram corretamente classificados;
- findings efetivos estão resolvidos;
- PR foi mesclado;
- merge SHA foi registrado;
- `EVIDENCE.md`, `STATUS.md` e `BOARD.md` refletem o estado final.


## Status integrado dos projetos

Todo projeto novo deve nascer com `PROJECT_STATUS.json`. Manter o arquivo no mesmo PR das entregas; seguir `PROJECT_STATUS.md` e validar com `python3 scripts/project_status.py PROJECT_STATUS.json`. Sem escopo mensurável: 0%. Preservar os gates de conclusão locais e publicar somente nome e agregados autorizados.
