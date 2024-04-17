# Verificador de Autômato Finito Determinístico (AFD)

Este repositório contém um algoritmo que realiza a verificação de um Autômato Finito Determinístico (AFD) em uma linguagem específica, que permite a verificação de determinadas palavras.

## Sobre

O objetivo deste algoritmo é fornecer uma forma simples e eficiente para a verificação de palavras em um Autômato Finito Determinístico. O algoritmo implementado é capaz de determinar se o AFD é válido e se uma palavra dada é ou não aceita pelo AFD especificado.

## Funcionamento

O verificador de AFD funciona da seguinte maneira:

1. O usuário define o AFD e uma lista de palavras a serem verificadas.
2. O algoritmo lê a definição do AFD e constrói uma representação interna do mesmo.
3. Para cada palavra fornecida, o algoritmo percorre o AFD de acordo com os símbolos da palavra.
4. Se a palavra for completamente processada e o estado final alcançado estiver entre os estados de aceitação, a palavra é considerada aceita. Caso contrário, é rejeitada.
5. O resultado da verificação para cada palavra é exibido ao usuário.

## Como Usar

Para usar o verificador de AFD, siga estas etapas:

1. Clone este repositório: `git clone https://github.com/ChristianWinguer/verificador-de-AFD.git`.
2. Navegue até o diretório do código: `cd verificador-de-AFD`.
3. Defina o AFD e uma lista de palavras a serem verificadas e execute o programa.
5. Analise os resultados da verificação.

## Contato

Se você tiver alguma dúvida ou sugestão, por favor, entre em contato diretamente ou abra uma issue neste repositório.

