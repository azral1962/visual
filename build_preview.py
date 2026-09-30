"""Build a self-contained HTML reading copy using Pandoc, not the Quarto engine.
The QMD remains authoritative. Replacement is limited to Quarto cross-references.
"""
from pathlib import Path
import re, subprocess

ROOT=Path(__file__).resolve().parent
source=(ROOT/'paper.qmd').read_text()
figs=re.findall(r'\{#(fig-[\w-]+)',source)
tables=re.findall(r'\{#(tbl-[\w-]+)',source)
ids={key:('Gambar' if key.startswith('fig-') else 'Tabel',i+1) for group in [figs,tables] for i,key in enumerate(group)}
for key,(label,n) in ids.items():
    source=source.replace('@'+key,f'[{label} {n}](#{key})')

def figure(match):
    caption,path,attrs=match.groups()
    key=re.search(r'#(fig-[\w-]+)',attrs).group(1)
    label,n=ids[key]
    # These generated figures have meaningful alt text, retained separately.
    return f'![{label} {n}. {caption}]({path}){{{attrs}}}'
source=re.sub(r'!\[([^\n]+)\]\(([^)]+)\)\{([^\n]+)\}',figure,source)

def table_caption(match):
    caption,key=match.groups();label,n=ids[key]
    return f': {label} {n}. {caption} {{#{key}}}'
source=re.sub(r'^: (.+) \{#(tbl-[\w-]+)\}$',table_caption,source,flags=re.M)
lines=source.splitlines()
for i in range(len(lines)-1,-1,-1):
    match=re.match(r'^: (.+) \{#(tbl-[\w-]+)\}$',lines[i])
    if not match: continue
    caption,key=match.groups()
    start=i-1
    while start>=0 and (not lines[start].strip() or lines[start].startswith('|')):
        start-=1
    start+=1
    lines[i]=f': {caption}'
    lines.insert(i+1,'\n:::')
    lines.insert(start,f'\n::: {{#{key}}}\n')
source='\n'.join(lines)+'\n'
source=source.replace('::: {#refs}\n:::','')
preview=ROOT/'.preview.md';preview.write_text(source)
subprocess.run(['/usr/bin/pandoc',str(preview),'--from=markdown','--to=html5','--standalone','--embed-resources','--mathml','--citeproc','--bibliography=references.bib','--css=styles.css','--toc','--toc-depth=2','--number-sections','--metadata=lang:id','--output=paper.html'],cwd=ROOT,check=True)
html=(ROOT/'paper.html').read_text().replace('>Abstract<','>Abstrak<')
(ROOT/'paper.html').write_text(html)
preview.unlink()
print(f'Built paper.html: {len(figs)} figures, {len(tables)} tables')
