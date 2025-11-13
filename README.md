# Automação com PyAutoGUI para Preenchimento de Formulário

![Automação](https://img.shields.io/badge/automation-pyautogui-blue)

## Descrição

Este projeto contém um script em Python que automatiza a abertura do navegador Chrome, acessa um site, preenche um formulário com dados fornecidos e envia o formulário automaticamente. É uma automação simples para demonstrar como interagir com a interface gráfica usando a biblioteca PyAutoGUI.

## Motivação

Automatizar tarefas repetitivas pode economizar tempo e evitar erros. Este script é ótimo para aprendizado e pequenos processos que envolvem interação com a tela.

## Funcionalidades

- Abre o navegador Google Chrome via menu iniciar do Windows.
- Acessa um site específico.
- Preenche campos de formulário (nome, e-mail, telefone).
- Envia o formulário automaticamente.
- Retorna ao terminal após a automação.

## Pré-requisitos

- Python 3 instalado
- Biblioteca PyAutoGUI  
  Para instalar use:  


- Sistema operacional Windows
- Navegador Google Chrome instalado

## Como usar

1. Clone este repositório ou baixe o script.
2. Edite o script para inserir seu nome, e-mail e telefone (substitua os valores `XXXXXXXX`).
3. Execute o script no seu ambiente Windows:  

4. Aguarde a automação executar as ações no navegador.

## Observações importantes

- As coordenadas do clique (`py.click(x=276, y=484)`) podem precisar ser ajustadas conforme a resolução do seu monitor.
- As pausas (`time.sleep`) são essenciais para garantir o carregamento correto de páginas e evitar falhas.
- Recomendado não usar o computador durante a execução para evitar interferências.

## Estrutura do projeto


## Contribuindo

Fique à vontade para enviar sugestões, melhorias e reportar problemas. Use pull requests e issues para colaborar neste projeto.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

Feito com 💙 para facilitar seu aprendizado em automação com Python!

