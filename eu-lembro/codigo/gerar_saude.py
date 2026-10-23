import html, pathlib
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).resolve().parent
OUT = BASE.parent / "stories" / "saude"
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
.cita.gigante { font-size: 92px; line-height: 104px; border-left-width: 12px; margin-top: 56px; }
.cita.gigante small { font-size: 36px; }
.lista p { margin-top: 0; }
.lista p b { font-weight: 800; color: var(--giz); }
.risco { display: inline; background: var(--sangue); color: #fff; padding: 0 10px; margin-left: -10px; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
"""

def furos():
    return '<div class="furos">' + '<i></i>' * 5 + '</div>'

def cartao(n, total, data, titulo, numero=None, textos=(), citacao=None, fonte="", menor=False, ordem="ntc", depois=(), h1=None, citaclasse="cita"):
    partes = [f'<h1 style="font-size:{h1}px">{titulo}</h1>' if h1 else f'<h1>{titulo}</h1>']
    for k in ordem:
        if k == "n" and numero:
            partes.append(f'<div class="num{" menor" if menor else ""}">{numero}</div>')
        if k == "t":
            for t in textos:
                partes.append(t if t.startswith('<') else f'<p>{t}</p>')
        if k == "c" and citacao:
            txt, quem = citacao
            partes.append(f'<p class="{citaclasse}">{txt}<small>{quem}</small></p>')
    for t in depois:
        partes.append(t if t.startswith('<') else f'<p>{t}</p>')
    return f"""<section class="pg">{furos()}
      <div class="cab"><div class="eu">Eu lembro…</div><div class="data">{data}</div></div>
      <div class="corpo">{''.join(partes)}</div>
      <div class="fonte">{fonte}</div><div class="pag">{n}/{total}</div></section>"""

T = 8
paginas = []

paginas.append(f"""<section class="pg capa">{furos()}
  <div class="corpo" style="top: 330px">
    <div class="grande">Eu<br>lembro.</div>
    <h1 style="margin-top: 112px">O que aconteceu com a saúde no Brasil entre <span class="risco">2019 e 2022</span>.</h1>
    <p>Seis fatos. Todos com fonte.</p>
  </div>
  <div class="pag">1/{T}</div></section>""")

paginas.append(cartao(2, T, "abril de 2020",
    "O Brasil passou a China em mortes por COVID. O presidente respondeu:", h1=96,
    citacao=("“E daí? Lamento. Quer que eu faça o quê?”", "Jair Bolsonaro, 28/04/2020, dia de 474 mortes em 24 horas"),
    citaclasse="cita gigante",
    numero="693.853 mortos",
    depois=['<p class="ctx">Óbitos por COVID notificados no Brasil de 2020 a 2022.</p>'],
    ordem="cn",
    fonte="Fontes: Poder360, Folhapress e Ministério da Saúde"))

paginas.append(cartao(3, T, "2020 → 2021",
    "O presidente fez propaganda de remédios sem eficácia contra a COVID.", h1=92,
    textos=['<p class="cita">“Quem é de direita toma cloroquina. Quem é de esquerda toma Tubaína.”<small>Live, 19/05/2020, véspera do protocolo da cloroquina</small></p>',
            '<p class="cita">“Eu mesmo fui um desses que fez tratamento inicial.”<small>Discurso na ONU, 21/09/2021</small></p>',
            '<p class="ctx" style="margin-top: 48px !important">Em 2025, o TCU anulou as notas do Ministério sobre o “tratamento precoce”.</p>'],
    ordem="t",
    fonte="Fontes: Folhapress, Jovem Pan, Poder360 e TCU"))

paginas.append(cartao(4, T, "janeiro de 2021",
    "Manaus ficou sem oxigênio.",
    numero="7 dias",
    textos=["Foi o tempo entre o alerta e a falta de oxigênio nos hospitais.",
            "No mesmo mês, o Ministério da Saúde lançou em Manaus um aplicativo que receitava cloroquina.",
            '<p class="ctx">O TCU classificou a conduta do Ministério como “reativa”, sem apontar dolo.</p>'],
    ordem="nt",
    fonte="Fontes: TCU, Poder360 e Correio Braziliense"))

paginas.append(cartao(5, T, "2020",
    "Três ministros da Saúde em um ano de pandemia.",
    textos=['<div class="lista" style="margin-top: 64px"><p><b>Mandetta</b>, médico: demitido em abril, depois de divergir sobre a condução da pandemia.</p>'
            '<p style="margin-top: 32px"><b>Teich</b>, médico: pediu demissão em 28 dias.</p>'
            '<p style="margin-top: 32px"><b>Pazuello</b>, general do Exército: em 5 dias, assinou o protocolo da cloroquina.</p></div>'],
    numero="O terceiro nem era médico", menor=True, ordem="tn",
    fonte="Fontes: Agência Brasil, G1, Poder360 e Folhapress"))

paginas.append(cartao(6, T, "fev. de 2021",
    "A Covaxin foi a vacina mais cara comprada pelo governo.", h1=100,
    numero="US$&nbsp;15 por dose",
    textos=["Pfizer e Janssen saíram por US$ 10. O contrato de R$ 1,6 bilhão foi assinado antes do aval da Anvisa.",
            '<p style="margin-top: 32px">Uma fatura de uma empresa de Cingapura, que nem estava no contrato, cobrou US$ 45 milhões adiantados.</p>',
            '<p class="ctx">O contrato foi cancelado depois da CPI, sem nenhum pagamento. A fabricante diz que o preço estava na menor faixa praticada no mundo.</p>'],
    ordem="nt",
    fonte="Fontes: Estadão, Poder360, InfoMoney e CNN Brasil"))

paginas.append(cartao(7, T, "out. de 2020",
    "Meses antes, Flávio Bolsonaro levou o dono da empresa da Covaxin ao presidente do BNDES.", h1=92,
    numero="O filho do presidente", menor=True,
    textos=["Francisco Maximiano é dono da Precisa Medicamentos, que intermediou a compra da vacina indiana.",
            '<p class="ctx">Flávio diz que a reunião tratou de outra empresa do dono e nega ligação com a vacina. O TCU apontou a inidoneidade da empresa intermediária.</p>'],
    ordem="nt",
    fonte="Fontes: Poder360, Metrópoles, Estadão e TCU"))

paginas.append(f"""<section class="pg capa">{furos()}
  <div class="corpo" style="top: 230px">
    <div class="grande" style="font-size: 165px">Eu lembro.<br><em>E você?</em></div>
    <h1 style="margin-top: 96px; font-size: 100px">Não vamos deixar que isso ocorra <span class="risco">novamente.</span></h1>
    <p style="margin-top: 64px">Todos os fatos vêm de atos oficiais, auditorias e imprensa de referência.</p>
    <p class="ctx" style="margin-top: 40px !important; max-width: 660px">Dados e fontes: github.com/gavelino/pesquisa-politica</p>
  </div>
  <div class="pag">{T}/{T}</div></section>""")

doc = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(paginas)}</body></html>"
(BASE / "stories_saude.html").write_text(doc, encoding="utf-8")

nomes = ["01-capa", "02-mortes-e-dai", "03-cloroquina", "04-manaus", "05-ministros", "06-covaxin", "07-covaxin-flavio", "08-fechamento"]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    pg.goto((BASE / "stories_saude.html").as_uri())
    pg.wait_for_timeout(600)
    for i, el in enumerate(pg.query_selector_all("section.pg")):
        el.screenshot(path=str(OUT / f"{nomes[i]}.png"))
    b.close()
print("ok")
