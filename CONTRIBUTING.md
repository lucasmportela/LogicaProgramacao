# Contribuindo

Este repositório reúne exercícios e projetos de estudo. Para manter o histórico organizado e facilitar a revisão das alterações, utilize mensagens de commit claras e padronizadas.

## Padrão de mensagens

Adotamos o formato **Conventional Commits**:

```text
tipo(escopo): descrição objetiva
```

- **tipo:** categoria da alteração.
- **escopo:** área afetada, quando ajudar a contextualizar.
- **descrição:** resume a mudança em poucas palavras.

Escreva em português, use letras minúsculas no tipo e na descrição e não finalize a linha com ponto. Prefira verbos no presente, indicando a ação realizada.

## Tipos recomendados

| Tipo | Quando utilizar | Exemplo |
|---|---|---|
| `feat` | Nova funcionalidade ou exercício | `feat(python): adiciona busca binária` |
| `fix` | Correção de erro | `fix(python): corrige limite do quick sort` |
| `test` | Criação ou ampliação de testes | `test(python): amplia testes de ordenação` |
| `docs` | README e documentação | `docs(readme): documenta execução dos projetos` |
| `refactor` | Reorganização sem mudar comportamento | `refactor(python): separa funções auxiliares` |
| `perf` | Melhoria de desempenho | `perf(python): reduz comparações na busca` |
| `ci` | GitHub Actions e automações | `ci(github-actions): valida sintaxe Python` |
| `build` | Dependências e processo de build | `build(python): atualiza dependências de teste` |
| `chore` | Manutenção geral | `chore(repo): remove arquivos temporários` |
| `style` | Formatação sem alterar lógica | `style(python): padroniza espaçamento` |

## Boas práticas

1. Descreva o objetivo da alteração, não apenas o nome do arquivo modificado.
2. Faça commits pequenos, com uma finalidade principal.
3. Evite mensagens genéricas como `update`, `changes`, `modified`, `correções` ou `atualização de arquivos`.
4. Não misture documentação, correções e funcionalidades sem necessidade.
5. Quando a mudança exigir contexto, acrescente um corpo explicando o motivo e os impactos.
6. Informe os testes executados quando forem relevantes.

## Exemplos

**Evite:**

```text
modified: BubbleSort.py
update files
corrigido
```

**Prefira:**

```text
fix(python): corrige ordenação de elementos repetidos
test(python): cobre listas vazias e valores negativos
docs(python): adiciona instruções de execução
```

## Usar o modelo de commit

Na raiz deste repositório, execute uma vez:

```bash
git config commit.template .gitmessage
```

A partir daí, o Git abrirá o modelo de mensagem ao criar um commit sem a opção `-m`. Edite os campos, remova as instruções e salve a mensagem.

Para desativar o modelo neste repositório:

```bash
git config --unset commit.template
```

Consulte também o arquivo [`.gitmessage`](.gitmessage).
