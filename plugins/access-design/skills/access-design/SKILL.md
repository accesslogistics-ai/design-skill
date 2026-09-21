---
name: access-design
description: Crie ou revise avisos, peças gráficas e interfaces de sistemas da Access Global Logistics usando as fontes, cores e logos oficiais incluídas. Use para demandas explicitamente da Access; não aplique a identidade a outras marcas.
---

# Access Design

O resultado deve ser reconhecível como Access, com conteúdo legível e hierarquia coerente. Este pacote reúne a matriz e as correções aprovadas por Henrique em 16/09/2026. Não depende de acesso à pasta original nem de um histórico de conversa.

## Antes de criar

Leia [identidade](references/identidade.md). Resolva os caminhos a partir da pasta desta skill, nunca do diretório de trabalho do usuário. Execute `python scripts/verificar_assets.py` com o caminho completo do script para conferir os assets. Isso usa apenas a biblioteca padrão do Python.

- Para **avisos e artes**, leia [avisos](references/avisos.md) e examine `assets/exemplos/aviso-aprovado.png`. Para temas comemorativos, mantenha o núcleo da marca e use a seção temática da referência.
- Para **sistemas e interfaces**, leia [sistemas](references/sistemas.md). Use a base de estilos `assets/web/access.css` e logos incluídas. Adapte ao framework existente; não recrie o projeto sem necessidade.
- Para **revisões e ajustes**, consulte também [qualidade e aprendizado](references/qualidade.md).

Pergunte apenas pelos dados ausentes que mudem a entrega: conteúdo essencial, destino/formato, prazo e ação desejada. Aproveite o briefing existente. Não invente datas, canais de solicitação, links ou regras de negócio.

## Núcleo da marca

- Azul principal **#023F88**, vermelho **#ED1B34**, títulos **IBM Plex Mono**, corpo e controles **Inter**. As demais cores autorizadas estão em `assets/identidade.json`.
- Use os arquivos locais de `assets/fontes`; não substitua por uma fonte parecida, CDN ou fonte padrão do sistema. Se as fontes não carregarem, corrija antes da exportação.
- Use as logos oficiais em `assets/logos`: PDFs vetoriais preservados e PNGs transparentes derivados sem redesenho. Não gerar logo com IA, redigitar, recortar letras, mudar cores, deformar, adicionar contorno/sombra ou aplicar filtros.
- Dimensione pela área visível da marca, não pela página em branco do PDF. Preserve a proporção. Confira a legibilidade de “LOGISTICS” no tamanho de uso. A presença do arquivo não basta para considerar a marca legível.
- Conteúdo e layout podem variar. Não alterar o pacote ou seus assets para atender um pedido comum de arte/sistema. Pedidos de atualização oficial da identidade são uma tarefa separada de manutenção, com versão e origem da decisão registradas.

## Produção

Faça a composição tipográfica de forma determinística, com texto real, fontes oficiais e logo como asset. Geração de imagem pode fornecer apenas ilustrações/fundos de apoio; não delegue a ela textos exatos nem marca. Evite ilustrações que disputem espaço com regras e prazos.

Para aviso simples, o gerador `scripts/criar_aviso.py` aceita um JSON conforme `references/briefing-exemplo.json` e produz PNG, SVG e relatório com medidas. Requer Pillow. Ele é uma base adaptável, não uma obrigação de usar sempre o mesmo layout. Não reaproveite o texto histórico do exemplo aprovado como informação vigente.

Em interfaces, mantenha textos, formulários e ações como elementos funcionais. Não converter uma arte em imagem de interface. Teste a fonte carregada e a logo nos tamanhos desktop e celular.

## Antes de entregar

Examine o resultado renderizado completo e no tamanho de exibição. Corrija cortes, sobreposições, grafismos invadindo conteúdo, marca pequena, substituição de fonte e texto comprimido. Recalcule a altura dos cartões depois de qualquer mudança no texto. Parágrafos preenchem a largura disponível naturalmente; negrito não cria quebra de linha.

Execute as verificações da rota escolhida e relate apenas o que foi realmente verificado. Assets íntegros e metadados corretos não garantem qualidade visual nem provam as fontes de uma imagem externa. Se não puder inspecionar uma renderização, identifique a revisão visual como pendente.

Entregue prévia visível e arquivos utilizáveis, com fonte editável quando disponível. Guarde decisões locais no projeto de destino. Não modificar silenciosamente o plugin instalado, nem propagar uma preferência de uma peça para toda a equipe.
