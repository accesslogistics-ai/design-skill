# Access Design • 1.0.1

Pacote para criar avisos e sistemas com a identidade visual da Access Global Logistics. Inclui uma skill com duas rotas, fontes locais, cinco logos em PDF/PNG, referência aprovada, gerador de avisos e base de interface responsiva.

## Para quem vai usar

Depois de disponibilizar a skill no Codex, peça:

> Use $access-design para criar um aviso institucional com estas informações: …

> Use $access-design para criar um sistema de solicitações internas. Preserve a logo, as fontes e as cores oficiais da Access.

> Use $access-design para revisar esta tela, principalmente o tamanho da logo, as fontes, os alinhamentos e o espaçamento.

O pacote não requer conta externa, servidor, chave de API ou um plugin de design específico. O ambiente precisa permitir ler arquivos e criar/renderizar a entrega. O gerador de PNG usa Python com Pillow; a base de interface usa HTML/CSS/JavaScript locais.

## Uso local como skill — caminho mais direto

1. Copie a pasta `skills/access-design` inteira deste pacote para `.agents/skills/access-design` dentro do projeto da pessoa. Para todos os projetos do usuário, use a pasta pessoal `~/.agents/skills/access-design` (no Windows, dentro do perfil do usuário).
2. Preserve todos os subdiretórios, inclusive `assets`; copiar só o `SKILL.md` não é suficiente.
3. Abra o projeto no Codex e procure a skill `access-design`. Se não aparecer, reinicie o aplicativo e inicie uma tarefa nova.
4. Não instale ao mesmo tempo a cópia avulsa e a versão plugin, para evitar duas skills de mesmo nome.

Esses locais e o uso de plugins para distribuição estão documentados em [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Uso como plugin

O pacote contém `.codex-plugin/plugin.json` e `skills/`, validados para a estrutura local do Codex. Um administrador pode colocar a pasta `access-design` no catálogo de plugins da equipe e usar o fluxo de instalação/compartilhamento disponível no ambiente. Consulte [Package your plugin](https://developers.openai.com/plugins/build/plugins).

Esta entrega é o pacote fonte e a skill portátil. Não foi publicada num catálogo, instalada na conta de colegas nem ativada globalmente nesta máquina. O ZIP sozinho não instala o plugin ao ser anexado em qualquer chat. A criação de um catálogo corporativo ou instalação global é uma etapa separada, dependente do destino escolhido.

## Identidade preservada

- Azul oficial #023F88 e paleta documentada.
- IBM Plex Mono Regular/Bold para títulos; Inter variável para corpo e controles.
- Cinco logos oficiais com proporção preservada; PNGs derivados dos PDFs sem redesenho.
- Parâmetros de tamanho e respiro para evitar marcas pequenas; revisão visual no tamanho real.
- Prazo em negrito no parágrafo, agrupamento claro e quebra natural de texto.
- Assets acompanhados de inventário SHA-256 para detectar alterações e arquivos ausentes.

Os mínimos de 200 CSS px em interfaces e 30% da largura em avisos são padrões operacionais iniciais deste pacote, não normas medidas do manual. A legibilidade deve prevalecer e pode exigir logo maior.

## Manutenção

A base distribuída tem versão fixa. Ajustes locais vão para o histórico do projeto, não para os assets instalados. A equipe de Marketing mantém e distribui novas versões da identidade. Skills não impedem edição manual nem substituem permissões de repositório. O inventário detecta alterações em relação à versão, mas não é assinatura digital de autoria.

## Arquivos e verificações

- `skills/access-design/SKILL.md`: orientações e rotas.
- `assets/identidade.json`: cores, fontes, variantes e parâmetros.
- `scripts/verificar_assets.py`: integridade dos assets.
- `scripts/criar_aviso.py`: aviso a partir de JSON, com PNG/SVG e medidas.
- `assets/web/exemplo.html`: exemplo de sistema, aberto em navegador.
- `assets/web/auditar.js`: auditoria parcial do DOM; a revisão visual continua necessária.

Os caminhos acima, exceto o primeiro, são relativos à pasta da skill. Não há caminhos absolutos da máquina de Henrique dentro da skill.

As fontes e marcas são de seus respectivos titulares; o pacote não atribui uma nova licença às marcas Access nem aos arquivos de terceiros. Fontes Inter e IBM Plex Mono conservam os metadados originais dos arquivos fornecidos. Referências de origem: [Inter](https://github.com/rsms/inter) e [IBM Plex](https://github.com/IBM/plex).
