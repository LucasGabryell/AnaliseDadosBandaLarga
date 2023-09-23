# Análise de Dados da Banda Larga

## Introdução

Este projeto consiste em uma análise dos dados de banda larga disponíveis na Base dos Dados. Os dados incluem registros de contratos de banda larga fixa realizados entre 2007 e 2023 (Abril). O objetivo deste projeto é responder a várias perguntas sobre os acessos de banda larga e suas características ao longo do tempo.

## Estrutura do Projeto

- `results/`: Pasta que armazena as visualizações e resultados gerados.
- `README.md`: Este arquivo com informações sobre o projeto.

## Instruções para Executar o Código

Para executar a análise e reproduzir os resultados, siga estas etapas:

1. Clone este repositório: https://github.com/LucasGabryell/AnaliseDadosBandaLarga

2. Instale as dependências Python:
   - streamlit
   - pandas
   - matplotlib
   - seaborn
   - plotly

3. Execute o processo.

## Resultados

### 1. Distribuição de Acessos

O mês com maior acesso foi: Maio. Esse mês se destacou com o maior número de acessos, representando um pico significativo na atividade.

Por outro lado, o mês com menor acesso foi: Fevereiro. Este mês registrou o menor número de acessos, indicando uma diminuição na atividade em comparação com os demais meses.

O total de acessos ao longo do período analisado foi de: 8984744.0.

A média de acessos mensais gerais foi de: 748728.6666666666.

### 2. Características Tecnológicas e de Velocidade

Por quase uma década, o cabo metálico tem uma dominância. Isso porque, devido à infraestrutura existente, tecnologias DSL, disponibilidade em áreas remotas e velocidades suficientes para a maioria dos usuários. Perdendo um pouco de sua relevância em 2010, mas nada muito alarmante. Entretanto, o mesmo iria a decair em 2018 para a fibra que proporciona alta velocidade, confiabilidade e imunidade a interferências, sendo ideal para transmissões de dados de alta qualidade em longas distâncias. Sendo ela, a atual dominante.

### 3. Evolução ao Longo do Tempo

Analisamos como essas características mudaram ao longo dos anos. [Inserir visualizações aqui.]

### 4. Empresas com Maior Número de Contratos

Listamos as empresas com o maior número de contratos, considerando o porte da empresa, se aplicável.

Dentre as empresas de grande porte, a OI é a líder, tendo o uma média do dobro de contratos do segundo colocado, a Claro. A Vivo vem logo atrás com valores que são bem abaixo da claro também e por fim SKY e TIM muito próximos, com valores que em média são parelhos.

### 5. Perfil do Tipo de Empresa por Ano

Analisamos como o perfil do tipo de empresa mudou ao longo dos anos nos estados. Verificamos se houve crescimento ou redução em relação a um tipo de porte específico. [Inserir visualizações aqui.]

### 6. Perfil Atual da Distribuição de Banda Larga

Analisamos o perfil da distribuição de banda larga com base nos dados mais recentes da base. [Inserir visualizações aqui.]

## Referências

- [Link para a Base dos Dados](https://basedosdados.org/dataset/4ba41417-ba19-4022-bc24-6837db973009?table=26f41ddd-3b01-492a-9119-6255b3cdcf72)
- [Biblioteca de análise de dados utilizada](https://pandas.pydata.org/)



