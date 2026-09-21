# Núcleo de identidade — versão 1.0.0

## Fontes oficiais

IBM Plex Mono para títulos, Inter para parágrafos, formulários, navegação, tabelas e botões. Fontes locais inclusas. Pesos Regular, Medium, SemiBold e Bold resolvem a maioria das demandas. Não utilizar Arial, Montserrat, Poppins, Roboto ou outra substituta como fonte final. Fallback técnico pode existir para carregamento, mas exportar ou aprovar somente após conferir as fontes corretas.

Itálico e caixa alta são recursos de hierarquia, não obrigatórios em todo texto. A interface não deve usar caixa alta em parágrafos. Parágrafos em Inter usam negrito seletivo sem mudar de família, tamanho ou entrelinha.

## Paleta

| Uso | Cor |
|---|---|
| Principal | #023F88 |
| Acento vermelho | #ED1B34 |
| Cinza | #6D6E71 |
| Azul escuro | #1E3662 |
| Vinho | #A01731 |
| Azul vivo | #1859B7 |
| Rosado | #E9465F |
| Branco | #FFFFFF |

O azul principal foi confirmado por Henrique. A legenda duplicada #6D6E71 na amostra azul do manual original é incorreta. Não recuperar essa legenda como azul nem amostrar uma tela para substituir o código confirmado.

Para texto, preferir azul sobre branco ou branco sobre azul. Cor de marca não garante contraste em todo uso: conferir a combinação real. Fotos e ilustrações podem conter cores próprias, sem redefinir os tokens da interface ou a identidade institucional.

## Logos oficiais

Arquivos `assets/logos/`: `azul-vermelho`, `vermelho-branco`, `azul-branco`, `branco` e `preto`, cada um em PDF e PNG. Preferir azul-vermelho sobre branco e vermelho-branco sobre azul. As outras variantes dependem de contraste real.

Os PNGs foram renderizados diretamente dos PDFs e recortados somente na margem transparente. Para impressão ou exportação vetorial, usar o PDF original em ferramenta que preserve seus vetores. Nunca declarar um PNG embutido em SVG como logo vetorial.

### Evitar marca pequena ou deformada

- Medir a largura do desenho visível, não a largura da prancheta do PDF.
- Manter `height: auto`, não esticar para preencher caixas. Proibidos filtros CSS de cor e `object-fit: cover` na logo.
- Ponto de partida do pacote: logo com 30% da largura de um aviso vertical, ou no mínimo 200 CSS px para o conjunto horizontal numa interface. Na peça aprovada anterior, a marca ocupava aproximadamente 26%; o padrão inicial foi ampliado aqui para responder à preocupação com logos pequenas.
- Esses números são parâmetros operacionais do pacote, não medidas oficiais do manual. Se “LOGISTICS” não for legível, aumentar mesmo que o mínimo tenha sido atingido.
- Reservar área livre ao redor equivalente a pelo menos metade da altura visível da logo, como padrão operacional.
- Em telas estreitas, reorganizar cabeçalho e navegação em linhas; não encolher a marca até perder leitura. Não criar símbolo isolado recortando a logo para caber num menu. Favicon depende de asset apropriado autorizado.

## O que é fixo e o que se adapta

Fixos: arquivos da marca, proporções, cores documentadas e famílias tipográficas. Adaptáveis: layout, quantidade de páginas, composição de cartões, imagens de apoio e distribuição do conteúdo. Este pacote adota tipografia estrita inclusive em temas, conforme o pedido de impedir fontes não usadas pela Access. Fontes decorativas de referências antigas não autorizam novas substituições.

Feedback de usuários deve melhorar a composição sem modificar os arquivos de marca. Atualização oficial exige nova versão do pacote mantida pela equipe responsável; esta regra de processo não equivale a um controle técnico de permissões sobre arquivos locais.
