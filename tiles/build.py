import subprocess, os, pathlib
S = pathlib.Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
tiles = [
 dict(n=1, slug="corporate-gifting", img="t1.jpg", pos="28% 50%", h="Need to send a lot of gifts?", s="Corporate gifting, without the scramble.", cta="Explore corporate gifting", logo=True),
 dict(n=2, slug="holiday-2026", img="t2.jpg", pos="50% 50%", h="Planning holiday gifts? Start here.", s="December is decided in October.", cta="2026 holiday gifting", logo=True),
 dict(n=3, slug="build-your-own", img="t3.jpg", pos="50% 30%", h="Build a gift they’ll actually want.", s="Choose the products. We’ll make it beautiful.", cta="Build your own gift box", logo=True),
 dict(n=4, slug="meet-martha", img="t4.jpg", pos="50% 18%", h="75,000+ gifts later, I have opinions.", s="Founder notes on gifting that actually gets used.", cta="Meet Martha", logo=False),
]
tpl = """<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=DM+Sans:wght@300;500&display=block" rel="stylesheet">
<style>
html,body{{margin:0;padding:0}}
body{{width:1200px;height:627px;overflow:hidden;background:#F5EFE1;font-family:'DM Sans',Helvetica,Arial,sans-serif;color:#051C2C}}
.wrap{{display:flex;width:1200px;height:627px}}
.photo{{width:600px;height:627px;overflow:hidden;flex:none}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:{pos};display:block}}
.panel{{width:600px;box-sizing:border-box;padding:52px 60px 52px 60px;display:flex;flex-direction:column;justify-content:space-between}}
.logo{{height:44px}} .logo img{{height:44px;width:auto;display:block}}
h1{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:{hs}px;line-height:1.0;letter-spacing:-0.01em;margin:0 0 22px 0}}
.rule{{width:48px;height:2px;background:#C39B82;margin:0 0 18px 0}}
p{{font-weight:300;font-size:28px;line-height:1.3;margin:0}}
.btn{{display:inline-block;align-self:flex-start;background:#051C2C;color:#F5EFE1;font-weight:500;font-size:21px;letter-spacing:0.18em;text-transform:uppercase;padding:20px 30px;border-radius:3px}}
</style></head><body><div class="wrap">
<div class="photo"><img src="src/{img}"></div>
<div class="panel"><div class="logo">{logo}</div>
<div><h1>{h}</h1><div class="rule"></div><p>{s}</p></div>
<div class="btn">{cta}</div></div></div></body></html>"""
for t in tiles:
    hs = 80 if len(t["h"]) < 34 else 74
    html = tpl.format(pos=t["pos"], img=t["img"], logo='<img src="src/logo.png">' if t["logo"] else "", h=t["h"], s=t["s"], cta=t["cta"], hs=hs)
    f = S / f"tile{t['n']}.html"; f.write_text(html)
    out2x = S / "out" / f"giften-market-linkedin-featured-tile-{t['n']}-{t['slug']}@2x.png"
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2","--window-size=1200,627","--virtual-time-budget=10000",f"--screenshot={out2x}",f"file://{f}"],capture_output=True)
    out1x = S / "out" / f"giften-market-linkedin-featured-tile-{t['n']}-{t['slug']}.jpg"
    subprocess.run(["sips","-s","format","jpeg","-s","formatOptions","88","-Z","1200",str(out2x),"--out",str(out1x)],capture_output=True)
    print(t["n"], out2x.exists(), out1x.exists())
