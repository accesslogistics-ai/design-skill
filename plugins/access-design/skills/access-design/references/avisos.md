# Avisos e artes

Base institucional: fundo azul #023F88, texto branco, títulos IBM Plex Mono e corpo Inter, acentos vermelhos, logo oficial e departamento somente quando informado. Cartões claros ou azul escuro separam informações paralelas. Grafismos de linhas vermelhas ficam nos cantos, longe do texto.

Escolher estrutura pelo conteúdo: comunicado direto; sequência de procedimentos; grupos comparáveis; aviso com ação e prazo. Não acrescentar cabeçalhos, rótulos ou botões sem função.

## Aprendizados aprovados no aviso Marcílio Dias v4

- O nome da seção é o título principal; o detalhe do evento é subordinado. No exemplo: “PRÓXIMO JOGO - 19/09” maior que “MARCÍLIO DIAS × HERCÍLIO LUZ”. Essa ordem é contextual, não regra para todos os títulos.
- Prazo dentro do parágrafo permanece em Inter do mesmo tamanho, apenas em negrito. Não virar outra chamada em caixa alta ou IBM Plex Mono.
- A frase de disponibilidade pertence ao corpo e foi integrada ao mesmo parágrafo, sem ficar solta entre subtítulo e instruções.
- Título e subtítulo formam um grupo. A separação desse grupo para o corpo é maior que a entrelinha do texto.
- Depois de reduzir ou reagrupar texto, ajustar a altura do cartão e a posição dos blocos seguintes. Não deixar um vazio grande herdado da versão anterior.
- Deixar o texto preencher naturalmente cada linha. Não deslocar palavras para acompanhar um trecho em negrito quando ainda cabem na linha anterior.

## Dimensões e leitura

Começar com margens de 6–8% e um ritmo curto de espaçamentos. Ajustar o formato ao canal; 1414 px de largura não significa leitura garantida em celular. Para conteúdo longo, propor páginas ou sequência de cards em vez de comprimir fontes. Não omitir informações silenciosamente para encaixar.

Logo: consultar mínimos operacionais da identidade; conferir o rodapé no tamanho de exibição. O gerador usa 30% da largura e reserva espaço exclusivo para a marca.

## Gerador incluído

`python scripts/criar_aviso.py briefing.json pasta-saida`

Executar usando o caminho real do script. Requer Python e Pillow; o ambiente Codex pode ter o runtime pronto. O JSON contém `title`, `intro`, `sections` e `department` opcional. Cada seção aceita `heading`, `subtitle` opcional, `paragraphs` e `highlight` opcional. Texto suporta apenas `**negrito**`. Conteúdo sem pares de marcadores é rejeitado para evitar perda de formatação. Sem HTML, comandos ou links inventados.

O gerador não modifica os assets, calcula quebras por largura, mantém o corpo em Inter e dimensiona cartões conforme o texto. Produz PNG, SVG com fontes incorporadas e relatório. SVG inclui logo raster derivada do PDF, com transparência e proporção preservadas. Revisão visual continua necessária.

## Temáticas

Uma data pode ganhar ilustração e ambientação próprias. Preserve as duas famílias de fontes, logo e cores de estrutura da marca. Não repetir selos de aniversário, personagens ou elementos de parceiros de uma referência antiga sem relação com a demanda. Não recriar escudos ou marcas de terceiros por semelhança.
