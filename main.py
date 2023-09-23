import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import plotly.express as px

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

# Título do aplicativo
st.title("Análise de Dados de Banda Larga")

# Substitua 'seu_arquivo.csv' pelo caminho real do seu arquivo CSV
caminho_arquivo_csv = 'testeDados.csv'

# Use o método 'read_csv' do pandas para ler o arquivo CSV
dados = pd.read_csv(caminho_arquivo_csv)

# Exibir os dados no Streamlit
st.write("### Dados do arquivo CSV:")
st.write(dados)

# Barra de seleção para escolher o gráfico
opcao_grafico = st.selectbox("Escolha o Gráfico", ["Gráfico de Acessos", "Gráfico de Tipo de Transmissão/Tempo",
                                                   "Gráfico de Tipo de Transmissão/Velocidade", "Gráfico de empresas"])


# Função para criar e mostrar o gráfico de Acessos

def plot_acessos(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Filtrar os dados com base no ano selecionado
    if ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados
        titulo = 'Acessos por Mês (Todos os Anos)'
    else:
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Acessos por Mês em {ano_selecionado}'

    acessos_por_mes = dados_filtrados.groupby('mes')['acessos'].sum().reset_index()

    # Crie o gráfico de barras
    fig = px.bar(acessos_por_mes, x='mes', y='acessos', labels={'mes': 'Mês', 'acessos': 'Acessos'})
    fig.update_layout(title=titulo, xaxis_title='Mês', yaxis_title='Acessos')
    st.write("### Gráfico de Acessos por Mês:")
    st.plotly_chart(fig)

    # Identificar o mês com maior e menor acesso
    mes_maior_acesso = meses[acessos_por_mes.loc[acessos_por_mes['acessos'].idxmax()]['mes']]
    mes_menor_acesso = meses[acessos_por_mes.loc[acessos_por_mes['acessos'].idxmin()]['mes']]

    # Calcular o total de acessos e a média de acessos gerais
    total_acessos = acessos_por_mes['acessos'].sum()
    media_acessos = acessos_por_mes['acessos'].mean()

    # Texto com informações sobre os acessos
    st.write("### Análise dos Acessos Mensais")
    st.write(f"O mês com maior acesso foi: {mes_maior_acesso}. Esse mês se destacou com o maior número de acessos, representando um pico significativo na atividade.")
    st.write(f"Por outro lado, o mês com menor acesso foi: {mes_menor_acesso}. Este mês registrou o menor número de acessos, indicando uma diminuição na atividade em comparação com os demais meses.")
    st.write(f"O total de acessos ao longo do período analisado foi de: {total_acessos}.")
    st.write(f"A média de acessos mensais gerais foi de: {media_acessos}.")



# Função para criar e mostrar o gráfico de Tipo de Transmissão
def plot_transmissao(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Filtrar os dados com base no ano selecionado
    if ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados
        titulo = 'Contagem de Tipo de Transmissão de Rede ao Longo do Tempo (Todos os Anos)'
    else:
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Contagem de Tipo de Transmissão de Rede em {ano_selecionado}'

    # Agrupe os dados por mês e tipo de transmissão e conte as ocorrências
    dados_agrupados = dados_filtrados.groupby(['mes', 'transmissao']).size().reset_index(name='contagem')

    # Crie o gráfico de barras empilhadas
    fig = px.bar(dados_agrupados, x='mes', y='contagem', color='transmissao',
                 labels={'mes': 'Mês', 'contagem': 'Contagem', 'transmissao': 'Tipo de Transmissão'},
                 title=titulo)
    fig.update_xaxes(title='Mês')
    fig.update_yaxes(title='Contagem')
    st.write("### Gráfico de Tipo de Transmissão de Rede ao Longo do Tempo:")
    st.plotly_chart(fig)


# Função para criar e mostrar o gráfico de Tipo de Transmissão/Velocidade/Tecnologia
def plot_transmissao_velocidade_tecnologia(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Adicione uma barra de seleção para filtrar a velocidade
    velocidades = dados['velocidade'].unique()
    velocidades = ['Todas as Velocidades'] + list(velocidades)  # Adiciona a opção "Todas as Velocidades"
    velocidade_selecionada = st.selectbox('Selecione a Velocidade', velocidades)

    # Filtrar os dados com base no ano e velocidade selecionados
    if ano_selecionado == 'Todos os Anos' and velocidade_selecionada == 'Todas as Velocidades':
        dados_filtrados = dados
        titulo = 'Contagem de Tipo de Transmissão de Rede ao Longo do Tempo (Todos os Anos, Todas as Velocidades)'
    elif ano_selecionado == 'Todos os Anos':
        dados_filtrados = dados[dados['velocidade'] == velocidade_selecionada]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em Todas as Velocidades ({velocidade_selecionada})'
    elif velocidade_selecionada == 'Todas as Velocidades':
        dados_filtrados = dados[dados['ano'] == ano_selecionado]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em {ano_selecionado} (Todas as Velocidades)'
    else:
        dados_filtrados = dados[(dados['ano'] == ano_selecionado) & (dados['velocidade'] == velocidade_selecionada)]
        titulo = f'Contagem de Tipo de Transmissão de Rede por Tecnologia em {ano_selecionado} ({velocidade_selecionada})'

    # Agrupe os dados por transmissao, tecnologia e conte as ocorrências
    dados_agrupados = dados_filtrados.groupby(['transmissao', 'tecnologia']).size().reset_index(name='contagem')

    # Crie o gráfico de barras empilhadas 2D com cores para representar a tecnologia
    fig = px.bar(dados_agrupados, x='transmissao', y='contagem', color='tecnologia',
                 labels={'transmissao': 'Tipo de Transmissão', 'contagem': 'Contagem'},
                 title=titulo)
    fig.update_xaxes(title='Tipo de Transmissão')
    fig.update_yaxes(title='Contagem')
    st.write("### Gráfico de Tipo de Transmissão de Rede por Tecnologia:")
    st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_empresas(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + list(anos)  # Adiciona a opção "Todos os Anos"
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Adicione um multiselect para escolher o porte da empresa
    portes = dados['porte_empresa'].unique()
    portes_selecionados = st.multiselect('Selecione o Porte da Empresa', portes)

    # Filtrar os dados com base no ano selecionado e portes selecionados
    dados_filtrados = dados
    if ano_selecionado != 'Todos os Anos':
        dados_filtrados = dados_filtrados[dados_filtrados['ano'] == ano_selecionado]

    if portes_selecionados:
        dados_filtrados = dados_filtrados[dados_filtrados['porte_empresa'].isin(portes_selecionados)]

    # Crie uma lista de empresas com base nos filtros
    empresas_disponiveis = dados_filtrados['empresa'].unique()

    # Adicione um multiselect para escolher as empresas a serem incluídas no gráfico
    empresas_selecionadas = st.multiselect('Selecione as Empresas', empresas_disponiveis)

    # Defina o título com base nos filtros aplicados
    titulo = f'Contagem de Empresas'
    if ano_selecionado != 'Todos os Anos':
        titulo += f' em {ano_selecionado}'
    if empresas_selecionadas:
        titulo += f' ({", ".join(empresas_selecionadas)})'
    if portes_selecionados:
        titulo += f' (Portes: {", ".join(portes_selecionados)})'

    # Agrupe os dados por mês e empresa e conte as ocorrências
    dados_agrupados = dados_filtrados.groupby(['ano', 'mes', 'empresa']).size().reset_index(name='contagem')

    # Crie um DataFrame pivot para o gráfico de calor
    pivot_data = dados_agrupados.pivot_table(index='mes', columns='empresa', values='contagem', aggfunc='sum',
                                             fill_value=0)

    # Verifique se pivot_data não está vazio
    if not pivot_data.empty:
        # Crie o gráfico de calor
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_data, annot=True, fmt='d', cmap='YlGnBu')
        plt.xlabel('Empresa')
        plt.ylabel('Mês')
        plt.title(titulo)
        st.write("### Gráfico de Contagem de Empresas ao Longo do Tempo:")
        st.pyplot(plt)  # Passe a figura plt como argumento para st.pyplot()
    else:
        st.warning("Não há dados para exibir com os filtros selecionados.")


# Mostrar o gráfico selecionado com base na escolha do usuário
if opcao_grafico == "Gráfico de Acessos":
    plot_acessos(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Tempo":
    plot_transmissao(dados)
elif opcao_grafico == "Gráfico de Tipo de Transmissão/Velocidade":
    plot_transmissao_velocidade_tecnologia(dados)
elif opcao_grafico == "Gráfico de empresas":
    plot_empresas(dados)