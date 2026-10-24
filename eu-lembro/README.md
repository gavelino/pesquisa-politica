# Eu lembro: stories sobre educação e saúde (2019–2022)

Dois stories para o Status do WhatsApp e o Instagram com fatos documentados sobre educação e saúde no governo Jair Bolsonaro (2019–2022). Cada cartão traz as suas fontes, e cada fonte está listada com link na pasta [`fontes/`](fontes/).

## Formatos

| Pasta | Formato | Uso |
|---|---|---|
| `stories/educacao/`, `stories/saude/` | 1080×1920 | Status do WhatsApp |
| `stories/educacao-instagram-stories/`, `stories/saude-instagram-stories/` | 1080×1920 | Stories do Instagram, com margens livres no topo e na base para a interface do app |
| `stories/educacao-instagram-carrossel/`, `stories/saude-instagram-carrossel/` | 1080×1350 (4:5) | Carrossel no feed do Instagram |

As tabelas abaixo usam os arquivos do WhatsApp; os nomes dos arquivos são os mesmos nas três versões.

## Stories

### Educação (7 cartões)

| # | Arquivo | Fato |
|---|---|---|
| 1 | [01-capa.png](stories/educacao/01-capa.png) | Capa |
| 2 | [02-universidades.png](stories/educacao/02-universidades.png) | O orçamento das universidades federais encolheu 30% em valores reais (2019→2021) |
| 3 | [03-bloqueio.png](stories/educacao/03-bloqueio.png) | Bloqueio de 30% da verba de universidades acusadas de "balbúrdia" (abr/2019) |
| 4 | [04-reitores.png](stories/educacao/04-reitores.png) | Nomeação de reitores que não lideravam a lista; caso da UFPI; Lei 15.367/2026 |
| 5 | [05-ministro-curriculo.png](stories/educacao/05-ministro-curriculo.png) | Ministro nomeado com currículo falso (doutorado que não existia); 5 nomeados para o MEC em 4 anos |
| 6 | [06-internet-veto.png](stories/educacao/06-internet-veto.png) | Veto à internet para 18,6 milhões de alunos e 1,6 milhão de professores na pandemia (mar/2021) |
| 7 | [07-fechamento.png](stories/educacao/07-fechamento.png) | Fechamento |

### Saúde (9 cartões)

| # | Arquivo | Fato |
|---|---|---|
| 1 | [01-capa.png](stories/saude/01-capa.png) | Capa |
| 2 | [02-mortes-e-dai.png](stories/saude/02-mortes-e-dai.png) | "E daí? Lamento. Quer que eu faça o quê?" e os óbitos por COVID 2020–2022 |
| 3 | [03-cloroquina.png](stories/saude/03-cloroquina.png) | Falas do presidente sobre remédios sem eficácia contra a COVID |
| 4 | [04-manaus.png](stories/saude/04-manaus.png) | Em Manaus, pacientes morreram sem ar nos hospitais; alerta 7 dias antes; aplicativo TrateCOV (jan/2021) |
| 5 | [05-ministros.png](stories/saude/05-ministros.png) | Três ministros da Saúde em 2020; o terceiro sequer era profissional da saúde |
| 6 | [06-pfizer.png](stories/saude/06-pfizer.png) | Oferta de 70 milhões de doses da Pfizer recusada (ago/2020); estimativa de 95 mil a 145 mil mortes evitáveis |
| 7 | [07-covaxin.png](stories/saude/07-covaxin.png) | Contrato da Covaxin: preço, aval da Anvisa e fatura de pagamento antecipado |
| 8 | [08-covaxin-flavio.png](stories/saude/08-covaxin-flavio.png) | Reunião do dono da Precisa com o presidente do BNDES, levada por Flávio Bolsonaro |
| 9 | [09-fechamento.png](stories/saude/09-fechamento.png) | Fechamento |

## Regras de checagem

Os fatos seguem esta hierarquia de evidência:

- **A:** dado oficial ou ato publicado (Diário Oficial, SIOP, Ministério da Saúde, leis).
- **B:** órgão de controle (TCU, CGU) ou literatura revisada por pares.
- **C:** entidade ou associação, com a posição institucional registrada.
- **D:** imprensa de referência, sempre com link e data de acesso.

Fatos contestados ou sobre investigações exigem pelo menos dois veículos independentes. Investigações são descritas com o status exato, sem equivaler a condenação. Quando a pessoa citada contesta o fato, a versão dela aparece no próprio cartão. Os números de mortes são apresentados sem atribuição causal a governo.

## Estudo de origem

Os fatos do story de Educação vêm do estudo comparativo **"Educação: ações efetivas do governo Lula 3 (2023–2026) x grupo Bolsonaro (2019–2022)"**, que segue um protocolo PICOC congelado antes da coleta e aplica as mesmas regras aos dois governos. Dados, fontes, extrações e relatórios: [github.com/gavelino/pesquisa-politica-educacao-2026](https://github.com/gavelino/pesquisa-politica-educacao-2026).

- [Relatório resumido](https://github.com/gavelino/pesquisa-politica-educacao-2026/blob/main/relatorios/relatorio_publico_geral.pdf) (PDF)
- [Relatório técnico completo](https://github.com/gavelino/pesquisa-politica-educacao-2026/blob/main/relatorios/relatorio_tecnico.pdf) (PDF)

## Como reproduzir os cartões

Requer Python 3 e Playwright (Chromium).

```bash
pip install playwright
playwright install chromium
cd codigo
./baixar_fontes_tipograficas.sh
python3 gerar_educacao.py   # gera stories/educacao/*.png (WhatsApp)
python3 gerar_saude.py      # gera stories/saude/*.png (WhatsApp)
FORMATO=instagram-stories   python3 gerar_educacao.py
FORMATO=instagram-carrossel python3 gerar_educacao.py
```

Os textos de cada cartão estão no próprio script. As fontes tipográficas (Kalam e Archivo) têm licença SIL OFL 1.1 e não são redistribuídas aqui; o script as baixa do repositório oficial do Google Fonts.

## Autoria e método

Seleção e validação final dos fatos: Guilherme (UFPI). Redação dos cartões, checagem das fontes de imprensa e geração das imagens feitas com assistência de IA (Claude, Anthropic). Fontes consultadas até 22/10/2026.

## Licença

Conteúdo (imagens e textos) sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br). Pode compartilhar e adaptar, desde que cite a autoria e este repositório. Detalhes em [LICENSE.md](../LICENSE.md).
