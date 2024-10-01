'''import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres_iot')

df = pd.read_sql('SELECT * FROM temperatura_readings', engine)

st.title('Média de Temperatura por Dispositivo')

st.write(df)'''

import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres_iot')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Exibindo dados da tabela de leituras de temperatura
st.header('Leituras de Temperatura')
df_temperatura = load_data('temperatura_readings')
st.write(df_temperatura)

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')

# Calculando a média de temperatura por dispositivo
df_avg_temp = df_temperatura.groupby('room_id/id').agg(avg_temp=('temp', 'mean')).reset_index()

# Mostrando as colunas disponíveis para depuração
st.write("Colunas disponíveis em temperatura_readings:", df_temperatura.columns.tolist())

# Aqui você deve ajustar 'room_id/id' e 'avg_temp' de acordo com os nomes reais das colunas.
try:
    fig1 = px.bar(df_avg_temp, x='room_id/id', y='avg_temp', title='Média de Temperatura por Dispositivo')
    st.plotly_chart(fig1)
except ValueError as e:
    st.error(f"Ocorreu um erro ao criar o gráfico: {e}")

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')

# Ajuste aqui para usar o formato correto
df_leituras_hora = df_temperatura.copy()
df_leituras_hora['hora'] = pd.to_datetime(df_leituras_hora['noted_date'], format="%d-%m-%Y %H:%M").dt.hour
df_leituras_hora = df_leituras_hora.groupby('hora').size().reset_index(name='contagem')

fig2 = px.line(df_leituras_hora, x='hora', y='contagem', title='Leituras por Hora do Dia')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')

# Agrupando por data e calculando max/min
df_temp_max_min = df_temperatura.copy()
df_temp_max_min['data'] = pd.to_datetime(df_temp_max_min['noted_date'], format="%d-%m-%Y %H:%M").dt.date
df_temp_max_min = df_temp_max_min.groupby('data').agg(temp_max=('temp', 'max'), temp_min=('temp', 'min')).reset_index()

fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], title='Temperaturas Máximas e Mínimas por Dia')
st.plotly_chart(fig3)
