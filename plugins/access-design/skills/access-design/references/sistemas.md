# Sistemas e interfaces Access

Use `assets/web/access.css` como base, copiando o diretório `assets` completo para manter caminhos relativos de fontes e logos. Adapte os estilos ao framework existente. `assets/web/exemplo.html` demonstra cabeçalho, formulário e cartão; é uma amostra de identidade, não um sistema de negócio completo.

## Componentes

- Logo horizontal visível no cabeçalho; largura inicial 240 CSS px, nunca inferior a 200 no componente incluído. Em celular, empilhar a navegação.
- Títulos em IBM Plex Mono; corpo, campos, botões e tabelas em Inter. Sem CDN de fontes ou substituição por bibliotecas de UI.
- Azul e branco estruturam a interface. Vermelho é acento; não usar a mesma aparência para erro e ação sem contexto textual.
- Botões, foco, validação e estados devem ser legíveis. Não depender só de cor para indicar erro ou seleção.
- Campos com rótulos reais; ícones com função clara. Evitar imagens decorativas dentro de formulários e tabelas.
- Blocos crescem com o conteúdo. Texto usa quebra natural; não introduzir `<br>` para mover uma expressão destacada ao início de outra linha.
- Logo com `data-access-logo`, títulos com `data-access-heading`; manter esses marcadores para a auditoria incluída.

## Verificação no navegador

Esperar `document.fonts.ready` e confirmar que Inter e IBM Plex Mono carregaram. Executar `await auditAccessBrand()` após carregar `assets/web/auditar.js`. O relatório verifica fontes computadas de títulos e corpo, carregamento das fontes, presença da logo, tamanho, proporção, filtros e overflow horizontal. Usa regras operacionais do pacote.

Executar a 1440 px e 390 px de largura; inspecionar screenshots e estados principais. O script não reconhece pixels de uma marca falsa: conferir o caminho e hash dos assets usados com o inventário. Também não detecta todos os problemas de contraste, sobreposição, palavras ou regras de negócio. Não descrever um relatório sem erros como garantia total.

Só entregar como funcional aquilo que foi implementado e testado. A skill fornece a identidade; autenticação, dados, integrações e autorização são definidos pelo pedido do sistema.
