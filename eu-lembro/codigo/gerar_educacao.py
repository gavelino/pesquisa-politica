import html, pathlib
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE.parent / "stories" / "educacao"
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
@font-face { font-family: 'Archivo'; src: url('fonts/Archivo.ttf'); font-weight: 100 900; font-stretch: 62% 125%; }
@font-face { font-family: 'Kalam'; src: url('fonts/Kalam-Bold.ttf'); font-weight: 700; }
@font-face { font-family: 'Kalam'; src: url('fonts/Kalam-Regular.ttf'); font-weight: 400; }
:root {
  --fundo: #0D121F; --pauta: rgba(150,175,215,.10); --margem: #E1323C;
  --giz: #F4F2EC; --cinza: #98A1B3; --sangue: #E1323C;
  --r: 64px; --topo: 320px;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
.pg {
  width: 1080px; height: 1920px; position: relative; overflow: hidden;
  background-color: var(--fundo);
  background-image:
    radial-gradient(ellipse 120% 80% at 50% 40%, transparent 40%, rgba(0,0,0,.55) 100%),
    linear-gradient(90deg, transparent 154px, var(--margem) 154px, var(--margem) 158px, transparent 158px),
    repeating-linear-gradient(180deg, transparent 0, transparent calc(var(--r) - 2px), var(--pauta) calc(var(--r) - 2px), var(--pauta) var(--r));
  background-position: 0 0, 0 0, 0 var(--topo);
  background-repeat: no-repeat, no-repeat, repeat;
  background-size: 100% 100%, 100% 100%, 100% calc(100% - var(--topo));
  color: var(--giz); font-family: 'Archivo', sans-serif;
}
.pg::after { content: ''; position: absolute; inset: 0; pointer-events: none; opacity: .16; mix-blend-mode: screen;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
.furos { position: absolute; left: 52px; top: 0; bottom: 0; width: 44px; display: flex; flex-direction: column; justify-content: space-around; padding: 140px 0; }
.furos i { display: block; width: 40px; height: 40px; border-radius: 50%; background: #04060B; box-shadow: inset 0 3px 6px rgba(0,0,0,.9), 0 1px 0 rgba(255,255,255,.06); }
.cab { position: absolute; left: 196px; right: 70px; top: 150px; display: flex; justify-content: space-between; align-items: baseline; z-index: 2; }
.eu { font-family: 'Kalam'; font-weight: 700; font-size: 96px; line-height: 1; color: var(--sangue); transform: rotate(-2deg); transform-origin: left bottom; }
.data { font-family: 'Kalam'; font-weight: 400; font-size: 46px; color: var(--cinza); }
.corpo { position: absolute; left: 196px; right: 72px; top: calc(var(--topo) + var(--r) * 1); z-index: 2; }
h1 { font-weight: 900; font-stretch: 72%; font-size: 112px; line-height: calc(var(--r) * 2); letter-spacing: -1px; margin-top: calc(var(--r) * -0.62); color: var(--giz); }
.num { display: inline-block; margin-top: calc(var(--r) * 0.9); font-weight: 900; font-stretch: 70%; font-size: 92px; line-height: calc(var(--r) * 1.9);
  padding: 4px 26px 0; margin-left: -10px; background: var(--sangue); color: #fff; transform: rotate(-2.5deg); transform-origin: left center;
  box-shadow: 0 12px 30px rgba(225,50,60,.25); }
.num.menor { font-size: 84px; }
p { font-size: 46px; line-height: var(--r); font-weight: 450; font-stretch: 92%; margin-top: var(--r); max-width: 800px; color: #DCDDE3; }
p + p { margin-top: 0; }
.cita { font-family: 'Kalam'; font-weight: 700; font-size: 58px; line-height: 72px; color: var(--giz); border-left: 8px solid var(--sangue); padding-left: 28px; margin-left: -36px; margin-top: calc(var(--r) * 1.2); }
.cita small { display: block; font-family: 'Archivo'; font-size: 34px; line-height: 48px; color: var(--cinza); font-weight: 450; margin-top: 12px; }
.ctx { font-size: 34px; line-height: 48px; color: var(--cinza); margin-top: 32px !important; }
.cita + p { margin-top: 40px; }
.num + p { margin-top: 48px; }
.fonte { position: absolute; left: 196px; right: 170px; bottom: 96px; font-family: 'Kalam'; font-size: 36px; line-height: 46px; color: var(--cinza); z-index: 2; }
.pag { position: absolute; right: 64px; bottom: 92px; font-family: 'Kalam'; font-size: 40px; color: var(--cinza); z-index: 2;
  width: 96px; height: 96px; border: 3px solid var(--cinza); border-radius: 50% 46% 52% 48%; display: grid; place-items: center; transform: rotate(-6deg); }
.grande { font-family: 'Kalam'; font-weight: 700; font-size: 240px; line-height: .95; color: var(--giz); transform: rotate(-3deg); transform-origin: left bottom; margin-top: 40px; }
.grande em { font-style: normal; color: var(--sangue); }
.capa h1 { font-size: 96px; }
.risco { display: inline; background: var(--sangue); color: #fff; padding: 0 10px; margin-left: -10px; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
"""

# --- formato de saída -------------------------------------------------------
# whatsapp: 1080x1920 (padrão)
# instagram-stories: 1080x1920 com margens livres para a interface do Instagram
# instagram-carrossel: 1080x1350 (4:5), para posts no feed
import os
FORMATO = os.environ.get("FORMATO", "whatsapp")
if FORMATO == "instagram-stories":
    _z = 0.85
    CSS += f"""
.pg {{ zoom: {_z}; width: {1080/_z:.1f}px; height: {1920/_z:.1f}px; --topo: 470px; }}
.cab {{ top: 310px; }}
.fonte {{ bottom: 400px; }}
.pag {{ bottom: 396px; }}
p {{ max-width: 1000px; }}
"""
elif FORMATO == "instagram-carrossel":
    _z = 0.8
    CSS += f"""
.pg {{ zoom: {_z}; width: {1080/_z:.1f}px; height: {1350/_z:.1f}px; }}
p {{ max-width: 1080px; }}
"""
if FORMATO != "whatsapp":
    OUT = OUT.parent / f"{OUT.name}-{FORMATO}"
    OUT.mkdir(parents=True, exist_ok=True)
# -----------------------------------------------------------------------------

def furos():
    return '<div class="furos">' + '<i></i>' * 5 + '</div>'

def cartao(n, total, data, titulo, numero=None, textos=(), citacao=None, fonte="", menor=False, ordem="ntc", depois=(), h1=None):
    partes = [f'<h1 style="font-size:{h1}px">{titulo}</h1>' if h1 else f'<h1>{titulo}</h1>']
    for k in ordem:
        if k == "n" and numero:
            partes.append(f'<div class="num{" menor" if menor else ""}">{numero}</div>')
        if k == "t":
            for t in textos:
                partes.append(t if t.startswith('<') else f'<p>{t}</p>')
        if k == "c" and citacao:
            txt, quem = citacao
            partes.append(f'<p class="cita">{txt}<small>{quem}</small></p>')
    for t in depois:
        partes.append(t if t.startswith('<') else f'<p>{t}</p>')
    return f"""<section class="pg">{furos()}
      <div class="cab"><div class="eu">Eu lembro…</div><div class="data">{data}</div></div>
      <div class="corpo">{''.join(partes)}</div>
      <div class="fonte">{fonte}</div><div class="pag">{n}/{total}</div></section>"""

T = 7
paginas = []

paginas.append(f"""<section class="pg capa">{furos()}
  <div class="corpo" style="top: 330px">
    <div class="grande">Eu<br>lembro.</div>
    <h1 style="margin-top: 112px">O que aconteceu com a educação no Brasil entre <span class="risco">2019 e 2022</span>.</h1>
    <p>Cinco fatos. Todos com fonte.</p>
  </div>
  <div class="pag">1/{T}</div></section>""")

paginas.append(cartao(2, T, "2019 → 2021",
    "Em dois anos, o dinheiro das universidades federais encolheu 30%.",
    numero="R$&nbsp;2,6&nbsp;bi a menos",
    textos=["De R$ 8,6 bi para R$ 6,0 bi por ano, já descontada a inflação.",
            '<p class="ctx">Valores de dez/2025 (IPCA), com emendas. Período de Teto de Gastos e pandemia.</p>'],
    fonte="Fonte: SIOP, Ministério do Planejamento (dados abertos do orçamento)"))

paginas.append(cartao(3, T, "abril de 2019",
    "O MEC bloqueou 30% da verba de universidades acusadas de “balbúrdia”.",
    citacao=("“Universidades que (...) estiverem fazendo balbúrdia, terão verbas reduzidas.”",
             "Abraham Weintraub, ministro da Educação, ao Estadão"),
    textos=["UnB, UFF e UFBA foram as primeiras. Depois, o bloqueio chegou a todas as universidades federais."],
    ordem="ct",
    fonte="Fontes: Estadão, Metrópoles, Folhapress e Agência Senado"))

paginas.append(cartao(4, T, "2019 → 2020",
    "O governo nomeou reitores que a universidade não escolheu.", h1=96,
    numero="14 de 25 reitores",
    textos=["nomeados até set/2020 não lideravam a lista. Por décadas, o mais votado foi sempre nomeado.",
            '<p style="margin-top: 32px"><span class="risco">Na UFPI</span>, em nov/2020, o nomeado ficou em 3º lugar na consulta à comunidade.</p>',
            '<p class="ctx" style="font-size: 38px; line-height: 52px; color: #DCDDE3">Em março de 2026, a Lei 15.367 acabou com a lista tríplice. Agora, o presidente é obrigado a nomear o mais votado.</p>'],
    ordem="nt",
    fonte="Fontes: Gazeta do Povo, Congresso em Foco, Brasil de Fato, Andes-SN e Lei 15.367/2026"))

paginas.append(cartao(5, T, "junho de 2020",
    "Bolsonaro nomeou um ministro da Educação com doutorado que não existia.", h1=92,
    numero="Currículo falso", ordem="nt",
    textos=["As universidades de Rosário e Wuppertal negaram os títulos de Carlos Decotelli, que o MEC divulgava desde 2019. A nomeação caiu em 6 dias, antes da posse.",
            '<p class="ctx" style="margin-top: 32px !important; font-size: 36px; line-height: 50px; color: #DCDDE3"><b style="font-weight:800; color: var(--giz)">5 nomeados para o MEC em 4 anos:</b> Vélez, Weintraub, Decotelli, Milton Ribeiro e Victor Godoy.</p>'],
    fonte="Fontes: Agência Brasil, Folhapress, Estadão e CartaCapital"))

paginas.append(cartao(6, T, "março de 2021",
    "Bolsonaro vetou internet para alunos na pandemia.", h1=100,
    numero="18,6 milhões de alunos sem conexão", menor=True,
    textos=["Alunos de baixa renda (CadÚnico) e 1,6 milhão de professores ficariam sem a internet prevista na lei."],
    citacao=("“Decidi vetar integralmente.”", "Mensagem de veto, 19/03/2021. Meses depois, o Congresso derrubou o veto."),
    ordem="ntc",
    fonte="Fontes: Diário Oficial da União, Exame e Estadão"))

paginas.append(f"""<section class="pg capa">{furos()}
  <div class="corpo" style="top: 230px">
    <div class="grande" style="font-size: 165px">Eu lembro.<br><em>E você?</em></div>
    <h1 style="margin-top: 96px; font-size: 100px">Não vamos deixar que isso ocorra <span class="risco">novamente.</span></h1>
    <p style="margin-top: 64px">Todos os fatos vêm de atos oficiais, auditorias e imprensa de referência.</p>
    <p class="ctx" style="margin-top: 40px !important; max-width: 660px">Dados e fontes: github.com/gavelino/pesquisa-politica</p>
  </div>
  <div class="pag">{T}/{T}</div></section>""")

doc = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(paginas)}</body></html>"
(BASE / "stories.html").write_text(doc, encoding="utf-8")

nomes = ["01-capa", "02-universidades", "03-bloqueio", "04-reitores", "05-ministro-curriculo", "06-internet-veto", "07-fechamento"]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1400, "height": 2400}, device_scale_factor=1)
    pg.goto((BASE / "stories.html").as_uri())
    pg.wait_for_timeout(600)
    for i, el in enumerate(pg.query_selector_all("section.pg")):
        el.screenshot(path=str(OUT / f"{nomes[i]}.png"))
    b.close()
print("ok")
