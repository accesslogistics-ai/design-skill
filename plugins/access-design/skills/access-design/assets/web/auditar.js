// Auditoria parcial de identidade; complementar com inspeção visual e hashes dos assets.
async function auditAccessBrand() {
  await document.fonts.ready;
  const errors=[];
  const headings=[...document.querySelectorAll('h1,h2,h3,[data-access-heading]')];
  for(const el of headings){if(!el.getClientRects().length)continue;if(!getComputedStyle(el).fontFamily.startsWith('"IBM Plex Mono"')&&!getComputedStyle(el).fontFamily.startsWith('IBM Plex Mono'))errors.push('Título com fonte diferente de IBM Plex Mono: '+el.textContent.slice(0,60));}
  for(const el of document.querySelectorAll('p,button,input,textarea,select,label,nav a')){if(!el.getClientRects().length)continue;if(!getComputedStyle(el).fontFamily.startsWith('Inter'))errors.push('Corpo/controle sem Inter: '+el.tagName);}
  const loaded=[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family.replaceAll('"',''));
  for(const name of ['Inter','IBM Plex Mono'])if(!loaded.includes(name))errors.push('Arquivo da fonte não carregado: '+name);
  const logos=[...document.querySelectorAll('[data-access-logo]')].filter(el=>el.getClientRects().length);
  if(!logos.length)errors.push('Logo visível não encontrada com data-access-logo.');
  for(const logo of logos){const b=logo.getBoundingClientRect(),c=getComputedStyle(logo);if(!logo.complete||!logo.naturalWidth)errors.push('Logo não carregada.');else if(Math.abs((b.width/b.height)/(logo.naturalWidth/logo.naturalHeight)-1)>.01)errors.push('Logo deformada.');if(b.width<200)errors.push('Logo abaixo de 200 CSS px.');if(c.filter!=='none'||c.transform!=='none'||c.objectFit==='cover')errors.push('Logo com filtro, transformação ou recorte.');}
  if(document.documentElement.scrollWidth>innerWidth+1)errors.push('Overflow horizontal na página.');
  return {ok:errors.length===0,errors,scope:'Fontes carregadas/computadas, presença, proporção e dimensão de logos marcadas; overflow. Não valida autenticidade dos pixels nem toda a qualidade visual.'};
}
if(typeof window!=='undefined')window.auditAccessBrand=auditAccessBrand;
