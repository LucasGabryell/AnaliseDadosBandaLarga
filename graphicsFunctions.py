import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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

def plot_acessos(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + sorted(list(anos))  # Adiciona a opção "Todos os Anos" e ordena a lista
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

    # Adicione o filtro de mês
    meses_selecionados = st.selectbox('Selecione um Mês para Detalhes', [meses[i] for i in range(1, 13)])

    # Verifique se um mês foi selecionado e mostre informações sobre os acessos para esse mês
    if meses_selecionados:
        numero_mes = [k for k, v in meses.items() if v == meses_selecionados][0]
        acessos_mes_selecionado = acessos_por_mes[acessos_por_mes['mes'] == numero_mes]['acessos'].values[0]
        st.write(f"Para o mês de {meses_selecionados}, o número de acessos foi de: {acessos_mes_selecionado}.")
    else:
        st.write("Nenhum mês selecionado.")

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
    anos = ['Todos os Anos'] + sorted(list(anos))  # Adiciona a opção "Todos os Anos" e ordena a lista
    ano_selecionado = st.selectbox('Selecione o Ano', anos)

    # Calcular o tipo de transmissão mais usado para o ano selecionado
    if ano_selecionado == 'Todos os Anos':
        tipo_transmissao_mais_usado_total = dados.groupby('transmissao').size().idxmax()
        tipo_transmissao_menos_usada_total = dados.groupby('transmissao').size().idxmin()
    else:
        dados_ano_selecionado = dados[dados['ano'] == ano_selecionado]
        tipo_transmissao_mais_usado_total = dados_ano_selecionado.groupby('transmissao').size().idxmax()
        tipo_transmissao_menos_usada_total = dados_ano_selecionado.groupby('transmissao').size().idxmin()

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

    # Adicione informações sobre o tipo de transmissão mais e menos usados ao título
    #fig.update_layout(title_text=f"{titulo}\n(Mais Usado: {tipo_transmissao_mais_usado_total}, Menos Usado: {tipo_transmissao_menos_usada_total})")

    st.write("### Gráfico de Tipo de Transmissão de Rede ao Longo do Tempo:")
    st.plotly_chart(fig)

    # Adicione o filtro de mês com a opção de selecionar todos
    selecionar_meses = st.radio('Selecione o(s) Mês(es)', ['Todos os Meses', 'Meses Específicos'])
    if selecionar_meses == 'Todos os Meses':
        st.write(f"O tipo de transmissão mais usado para o ano selecionado é: {tipo_transmissao_mais_usado_total}")
        st.write(f"O tipo de transmissão menos usado para o ano selecionado é: {tipo_transmissao_menos_usada_total}")
    else:
        meses_selecionados = st.multiselect('Selecione o(s) Mês(es) desejado(s)', [meses[i] for i in range(1, 13)])  # Use o dicionário 'meses'

        # Verifique se algum mês foi selecionado e mostre o tipo de transmissão menos usado para o(s) mês(es)
        if meses_selecionados:
            for mes in meses_selecionados:
                numero_mes = [k for k, v in meses.items() if v == mes]
                if numero_mes:
                    numero_mes = numero_mes[0]
                    dados_mes = dados_agrupados[dados_agrupados['mes'] == numero_mes]
                    if not dados_mes.empty:
                        tipo_transmissao_menos_usada_mes = dados_mes[dados_mes['contagem'] == dados_mes['contagem'].min()]['transmissao'].values[0]
                        st.write(f"Para o mês de {mes}, o tipo de transmissão menos usado é: {tipo_transmissao_mais_usado_total}")
                        st.write(f"Para o mês de {mes}, o tipo de transmissão menos usado é: {tipo_transmissao_menos_usada_mes}")
                    else:
                        st.write(f"Não há dados para o mês de {mes}.")
        else:
            st.write("Nenhum mês selecionado.")

    st.write("### Evolução das Tecnologias de Transmissão de Rede")
    st.write("""
    Por quase uma década, o cabo metálico tem uma dominância. Isso porque, devido à infraestrutura existente, 
    tecnologias DSL, disponibilidade em áreas remotas e velocidades suficientes para a maioria dos usuários. 
    Perdendo um pouco de sua relevância em 2010, mas nada muito alarmante. Entretanto, o mesmo iria a decair em 2018 
    para a fibra que proporciona alta velocidade, confiabilidade e imunidade a interferências, sendo ideal para 
    transmissões de dados de alta qualidade em longas distâncias. Sendo ela, a atual dominante.
    """)

def plot_transmissao_velocidade_tecnologia(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + sorted(list(anos))  # Adiciona a opção "Todos os Anos" e ordena a lista
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

    # Crie uma contagem das ocorrências de tecnologia
    dados_agrupados = dados_filtrados['tecnologia'].value_counts().reset_index()
    dados_agrupados.columns = ['tecnologia', 'contagem']

    # Crie um gráfico de treemap
    fig = px.treemap(dados_agrupados, path=['tecnologia'], values='contagem',
                     title=titulo)
    st.write("### Gráfico de Treemap de Tipo de Transmissão de Rede por Tecnologia:")
    st.plotly_chart(fig)

    # Encontre a tecnologia mais usada e menos usada
    tecnologia_mais_usada = dados_agrupados['tecnologia'].iloc[0]
    tecnologia_menos_usada = dados_agrupados['tecnologia'].iloc[-1]

    # Escreva o texto informativo
    st.write(f"**Tecnologia mais usada (com base na velocidade):** {tecnologia_mais_usada}")
    st.write(f"**Tecnologia menos usada (com base na velocidade):** {tecnologia_menos_usada}")


def plot_empresas(dados):
    # Adicione uma barra de seleção para filtrar o ano
    anos = dados['ano'].unique()
    anos = ['Todos os Anos'] + sorted(list(anos))  # Adiciona a opção "Todos os Anos" e ordena a lista
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

    # Amostragem de Dados - Adicione uma amostra aleatória de 50% dos dados
    dados_filtrados = dados_filtrados.sample(frac=0.2)

    # Crie uma lista de empresas com base nos filtros
    empresas_disponíveis = dados_filtrados['empresa'].unique()

    # Adicione um multiselect para escolher as empresas a serem incluídas no gráfico
    empresas_selecionadas = st.multiselect('Selecione as Empresas', empresas_disponíveis)

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

        # Identifique a empresa mais contratada e a menos contratada
        empresa_mais_contratada = pivot_data.sum(axis=0).idxmax()
        empresa_menos_contratada = pivot_data.sum(axis=0).idxmin()
        contratacoes_empresa_mais = pivot_data.sum(axis=0).max()
        contratacoes_empresa_menos = pivot_data.sum(axis=0).min()

        st.write(f"**Empresa mais contratada:** {empresa_mais_contratada} ({contratacoes_empresa_mais} contratações)")
        st.write(f"**Empresa menos contratada:** {empresa_menos_contratada} ({contratacoes_empresa_menos} contratações)")
    else:
        st.warning("Não há dados para exibir com os filtros selecionados.")