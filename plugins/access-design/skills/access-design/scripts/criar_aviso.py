"""Gerador portátil de avisos Access. Dependência: Pillow. Texto e geometria determinísticos."""
from pathlib import Path
import argparse,base64,html,io,json,re
from PIL import Image,ImageDraw,ImageFont
from verificar_assets import verify

BASE=Path(__file__).resolve().parents[1]
W=1414; M=112; CONTENT=W-2*M; BLUE='#023F88'; NAVY='#1E3662'; RED='#ED1B34'
FILES={
    'body':('Inter-VariableFont_opsz,wght.ttf','Regular',400),
    'bold':('Inter-VariableFont_opsz,wght.ttf','Bold',700),
    'title':('IBMPlexMono-Bold.ttf',None,700),
    'label':('IBMPlexMono-Regular.ttf',None,400),
}
def render(data,out):
    errors=verify()
    if errors: raise ValueError('Assets inconsistentes: '+'; '.join(errors))
    if not isinstance(data,dict) or not isinstance(data.get('title'),str) or not data['title'].strip(): raise ValueError('title deve ser texto não vazio.')
    if not isinstance(data.get('sections'),list): raise ValueError('sections deve ser uma lista.')
    commands=[]; records=[]; fonts={}; measure=ImageDraw.Draw(Image.new('RGB',(1,1)))
    def f(kind,size):
        key=(kind,size)
        if key not in fonts:
            filename,variation,_=FILES[kind]
            font=ImageFont.truetype(str(BASE/'assets/fontes'/filename),size)
            if variation:font.set_variation_by_name(variation)
            fonts[key]=font
        return fonts[key]
    def text(s,x,y,kind,size):commands.append(('text',s,x,y,kind,size))
    def paragraph(s,x,y,width,kind='body',size=32,leading=44):
        if not isinstance(s,str) or not s.strip():raise ValueError('Parágrafo vazio ou não textual.')
        if s.count('**')%2:raise ValueError('Marcadores ** de negrito devem estar em pares.')
        rows=[]; row=[]; advance=0
        for n,run in enumerate(s.split('**')):
            k='bold' if n%2 else kind
            for token in re.findall(r'\s+|\S+',run):
                if token.isspace():
                    if row and row[-1][0]!=' ':row.append((' ',k,measure.textlength(' ',font=f(k,size))));advance+=row[-1][2]
                    continue
                tw=measure.textlength(token,font=f(k,size))
                if tw>width:raise ValueError('Palavra ou endereço longo demais para a coluna; reorganize o conteúdo: '+token)
                if row and advance+tw>width:
                    while row and row[-1][0]==' ':row.pop()
                    rows.append(row);row=[];advance=0
                row.append((token,k,tw));advance+=tw
        if row:rows.append(row)
        for i,row in enumerate(rows):
            xx=x
            for token,k,tw in row:text(token,xx,y+i*leading,k,size);xx+=tw
        records.append({'text':s,'top':y,'bottom':y+len(rows)*leading,'lines':len(rows)})
        return y+len(rows)*leading
    y=110
    y=paragraph(data['title'],M,y,CONTENT,'title',58,72)+42
    if data.get('intro'):y=paragraph(data['intro'],M,y,CONTENT)+64
    for section in data['sections']:
        if not isinstance(section,dict) or not isinstance(section.get('paragraphs'),list):raise ValueError('Cada seção precisa de paragraphs em lista.')
        card=bool(section.get('highlight')); top=y; index=len(commands); x=M+42 if card else M; width=CONTENT-84 if card else CONTENT
        if card:y+=36
        if section.get('heading'):y=paragraph(section['heading'],x,y,width,'title',38,49)
        if section.get('subtitle'):y+=16;y=paragraph(section['subtitle'],x,y,width,'title',30,39)
        y+=32
        for p in section['paragraphs']:y=paragraph(p,x,y,width)+22
        y-=22 if section['paragraphs'] else 0
        if card:
            y+=36;commands.insert(index,('card',M,top,CONTENT,y-top))
        y+=56
    # Marca recebe área própria e 30% da largura, preservando a proporção do asset.
    logo=Image.open(BASE/'assets/logos/vermelho-branco.png').convert('RGBA'); lw=round(W*.30);lh=round(lw*logo.height/logo.width)
    dept=data.get('department','')
    if not isinstance(dept,str):raise ValueError('department deve ser texto.')
    dw=measure.textlength(dept,font=f('label',26)) if dept else 0
    if lw+dw+64>CONTENT:raise ValueError('Departamento muito longo; usar nome abreviado informado pelo usuário.')
    lx=(W-lw-(64+dw if dept else 0))/2;ly=y+24
    commands.append(('logo',lx,ly,lw,lh))
    if dept:commands.append(('line',lx+lw+30,ly,lx+lw+30,ly+lh));text(dept,lx+lw+56,ly+(lh-34)/2,'label',26)
    H=round(ly+lh+90)
    if H>6000:raise ValueError('Conteúdo extenso: dividir o aviso em mais de uma peça.')
    im=Image.new('RGB',(W,H),BLUE);draw=ImageDraw.Draw(im);svg=[f'<rect width="{W}" height="{H}" fill="{BLUE}"/>']
    for c in commands:
        if c[0]=='text':
            _,s,x,yy,k,size=c; baseline=yy+f(k,size).getmetrics()[0]
            draw.text((x,baseline),s,font=f(k,size),fill='white',anchor='ls')
            svg.append(f'<text x="{x}" y="{baseline}" font-family="{k}" font-size="{size}" fill="white">{html.escape(s)}</text>')
        elif c[0]=='card':
            _,x,yy,w,h=c;draw.rounded_rectangle((x,yy,x+w,yy+h),radius=24,fill=NAVY);draw.rectangle((x,yy,x+w,yy+6),fill=RED)
            svg.append(f'<rect x="{x}" y="{yy}" width="{w}" height="{h}" rx="24" fill="{NAVY}"/><rect x="{x}" y="{yy}" width="{w}" height="6" fill="{RED}"/>')
        elif c[0]=='line':
            _,x,y1,x2,y2=c;draw.line((x,y1,x2,y2),fill='white',width=2);svg.append(f'<path d="M{x} {y1}L{x2} {y2}" stroke="white" stroke-width="2"/>')
        else:
            _,x,yy,w,h=c;scaled=logo.resize((w,h),Image.Resampling.LANCZOS);im.paste(scaled,(round(x),round(yy)),scaled);buf=io.BytesIO();scaled.save(buf,format='PNG');svg.append(f'<image x="{x}" y="{yy}" width="{w}" height="{h}" href="data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}"/>')
    css=''.join('@font-face{font-family:'+k+';src:url(data:font/ttf;base64,'+base64.b64encode((BASE/'assets/fontes'/filename).read_bytes()).decode()+');font-weight:'+str(weight)+'}' for k,(filename,_,weight) in FILES.items())
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    for name in ['aviso.png','aviso.svg','relatorio.json']:
        if (out/name).exists():raise FileExistsError('Escolha outra pasta de versão; arquivo já existe: '+str(out/name))
    im.save(out/'aviso.png')
    (out/'aviso.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs><style>{css}</style></defs>'+''.join(svg)+'</svg>',encoding='utf-8')
    (out/'relatorio.json').write_text(json.dumps({'width':W,'height':H,'logo_width':lw,'logo_height':lh,'paragraphs':records,'visual_review':'pendente','brand_version':'1.0.0'},ensure_ascii=False,indent=2),encoding='utf-8')
    return out/'aviso.png'
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('briefing');parser.add_argument('output');args=parser.parse_args()
    print(render(json.loads(Path(args.briefing).read_text(encoding='utf-8')),args.output))
