"""Generate terminal banners using only Python's standard library.
Run: py scripts/profile_banner.py
"""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def banner(light=False):
    bg, panel, border, text, muted, purple = (
        ('#f6f3fc', '#ffffff', '#ded5ee', '#241c35', '#71657e', '#7553b8')
        if light else
        ('#0b0a12', '#12101d', '#30283f', '#ede6fc', '#9488aa', '#aa9bef')
    )
    rows = [
        ('name', 'Leandro Silva'),
        ('role', 'Full Stack Software Engineer'),
        ('focus', 'Legacy modernization + BFF'),
        ('frontend', 'React / Next.js / TypeScript'),
        ('backend', 'NestJS / Node.js / FastAPI'),
        ('work', 'OCA / ePak / Fulfillment'),
        ('personal', 'github.com/leeansilva'),
        ('oca', 'github.com/lsilva-oca'),
    ]
    lines = []
    theme = 'light' if light else 'dark'
    portrait_path = ROOT / 'assets' / f'portrait-{theme}.svg'
    portrait = portrait_path.read_text(encoding='utf-8')
    portrait = portrait.replace('<svg ', '<svg x="748" y="93" ', 1)
    portrait = re.sub(r'width="[^"]+" height="[^"]+"', 'width="330" height="330"', portrait, count=1)
    for i, (key, value) in enumerate(rows):
        y = 173 + i * 31
        lines.append(f'<text x="57" y="{y}" fill="{muted}">{key}</text>'
                     f'<text x="187" y="{y}" fill="{text}">{escape(value)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="510" viewBox="0 0 1180 510" role="img" aria-labelledby="title desc">
<title id="title">Leandro Silva · Full Stack Software Engineer</title>
<desc id="desc">React, Next.js, TypeScript, NestJS. Personal: leeansilva. OCA: lsilva-oca.</desc>
<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{border}"/></pattern></defs>
<rect width="1180" height="510" rx="20" fill="{bg}"/>
<rect width="1180" height="510" rx="20" fill="url(#grid)"/>
<rect x="25" y="26" width="1130" height="458" rx="14" fill="{panel}" stroke="{border}"/>
<path d="M25 76H1155" stroke="{border}"/>
<circle cx="51" cy="51" r="6" fill="#ff5f57"/><circle cx="73" cy="51" r="6" fill="#febc2e"/><circle cx="95" cy="51" r="6" fill="#28c840"/>
<g font-family="ui-monospace, SFMono-Regular, Consolas, monospace" font-size="16">
<text x="132" y="57" fill="{muted}">lean@github: ~/profile</text>
<text x="57" y="120" fill="{purple}">$ ./profile.sh --live</text>
{''.join(lines)}
<text x="57" y="455" fill="{purple}">$ building what comes next</text>
<rect x="370" y="440" width="9" height="19" fill="{purple}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.49;0.5;1" dur="1.2s" repeatCount="indefinite"/></rect>
<path d="M680 106V445" stroke="{border}"/>
{portrait}
<text x="913" y="421" text-anchor="middle" font-size="13" fill="{muted}">FRONTEND · BACKEND · WHAT'S NEXT</text>
</g></svg>'''


if __name__ == '__main__':
    for theme in ('dark', 'light'):
        path = ROOT / 'assets' / f'banner-{theme}.svg'
        path.write_text(banner(light=theme == 'light'), encoding='utf-8')
        print(f'Generated {path.name}')
