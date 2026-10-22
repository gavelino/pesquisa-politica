# Eu lembro: stories sobre educação e saúde (2019–2022)

Dois stories para o Status do WhatsApp (1080×1920) com fatos documentados sobre educação e saúde no governo Jair Bolsonaro (2019–2022). Cada cartão traz as suas fontes, e cada fonte está listada com link na pasta [`fontes/`](fontes/).

> **Transparência.** Estes stories são uma **seleção** de fatos sobre um dos governos. Eles derivam de dois estudos comparativos que analisam o governo Bolsonaro (2019–2022) e o atual governo Lula (2023–), com as mesmas regras para os dois. Os estudos completos, com achados favoráveis e desfavoráveis a ambos, estão nos links da seção [Estudos de origem](#estudos-de-origem).

## Stories

### Educação (7 cartões)

| # | Arquivo | Fato |
|---|---|---|
| 1 | [01-capa.png](stories/educacao/01-capa.png) | Capa |
| 2 | [02-universidades.png](stories/educacao/02-universidades.png) | O orçamento das universidades federais encolheu 30% em valores reais (2019→2021) |
| 3 | [03-bloqueio.png](stories/educacao/03-bloqueio.png) | Bloqueio de 30% da verba de universidades acusadas de "balbúrdia" (abr/2019) |
| 4 | [04-reitores.png](stories/educacao/04-reitores.png) | Nomeação de reitores que não lideravam a lista; caso da UFPI; Lei 15.367/2026 |
| 5 | [05-ministro-curriculo.png](stories/educacao/05-ministro-curriculo.png) | Ministro anunciado com doutorado que não existia; 5 nomeados para o MEC em 4 anos |
| 6 | [06-internet-veto.png](stories/educacao/06-internet-veto.png) | Veto à internet para 18,6 milhões de alunos e 1,6 milhão de professores na pandemia (mar/2021) |
| 7 | [07-fechamento.png](stories/educacao/07-fechamento.png) | Fechamento |

### Saúde (8 cartões)

| # | Arquivo | Fato |
|---|---|---|
| 1 | [01-capa.png](stories/saude/01-capa.png) | Capa |
| 2 | [02-mortes-e-dai.png](stories/saude/02-mortes-e-dai.png) | "E daí? Lamento. Quer que eu faça o quê?" e os óbitos por COVID 2020–2022 |
| 3 | [03-cloroquina.png](stories/saude/03-cloroquina.png) | Falas do presidente sobre remédios sem eficácia contra a COVID |
| 4 | [04-manaus.png](stories/saude/04-manaus.png) | Falta de oxigênio em Manaus e o aplicativo TrateCOV (jan/2021) |
| 5 | [05-ministros.png](stories/saude/05-ministros.png) | Três ministros da Saúde em 2020 |
| 6 | [06-covaxin.png](stories/saude/06-covaxin.png) | Contrato da Covaxin: preço, aval da Anvisa e fatura de pagamento antecipado |
| 7 | [07-covaxin-flavio.png](stories/saude/07-covaxin-flavio.png) | Reunião do dono da Precisa com o presidente do BNDES, levada por Flávio Bolsonaro |
| 8 | [08-fechamento.png](stories/saude/08-fechamento.png) | Fechamento |

## Regras de checagem

Os fatos seguem a hierarquia de evidência dos estudos de origem:

- **A:** dado oficial ou ato publicado (Diário Oficial, SIOP, Ministério da Saúde, leis).
- **B:** órgão de controle (TCU, CGU) ou literatura revisada por pares.
- **C:** entidade ou associação, com a posição institucional registrada.
- **D:** imprensa de referência, sempre com link e data de acesso.

Fatos contestados ou sobre investigações exigem pelo menos dois veículos independentes. Investigações são descritas com o status exato, sem equivaler a condenação. Quando a pessoa citada contesta o fato, a versão dela aparece no próprio cartão. Os números de mortes são apresentados sem atribuição causal a governo.

## Estudos de origem

- Ações efetivas em Educação: Lula 3 × governo Bolsonaro. [Relatório técnico](https://claude.ai/code/artifact/11a701ec-1831-4fb4-b2cc-714e44ba818e)
- Ações efetivas em Saúde: Lula 3 × governo Bolsonaro. [Relatório técnico](https://claude.ai/code/artifact/7b715472-226a-4b81-ba92-f840f411d9c2)

Veja também o [README principal](../README.md) deste repositório.

## Como reproduzir os cartões

Requer Python 3 e Playwright (Chromium).

```bash
pip install playwright
playwright install chromium
cd codigo
./baixar_fontes_tipograficas.sh
python3 gerar_educacao.py   # gera stories/educacao/*.png
python3 gerar_saude.py      # gera stories/saude/*.png
```

Os textos de cada cartão estão no próprio script. As fontes tipográficas (Kalam e Archivo) têm licença SIL OFL 1.1 e não são redistribuídas aqui; o script as baixa do repositório oficial do Google Fonts.

## Autoria e método

Seleção e validação final dos fatos: Guilherme (UFPI). Redação dos cartões, checagem das fontes de imprensa e geração das imagens feitas com assistência de IA (Claude, Anthropic). Fontes consultadas até 22/10/2026.

## Licença

Conteúdo (imagens e textos) sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br). Pode compartilhar e adaptar, desde que cite a autoria e este repositório. Detalhes em [LICENSE.md](../LICENSE.md).
