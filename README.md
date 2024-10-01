#Dashboard IoT - Média de Temperatura por Dispositivo

##Explicação do projeto

Este projeto tem como objetivo, apresentar um dashboard interativo.
Onde podemos visualizar as leituras de temperatura de dispositivos IoT. 
Nele apresentamos gráficos que mostram a média de temperatura por dispositivo, 
a contagem de leituras por hora do dia e as temperaturas máximas e mínimas por dia.


##Instalação
- Python (versção atualizada)
bibliotecas:
	-pandas
	-sqlalchemy
	-streamlit
	-plotly 
	-psycopg2
- PostgreSQL
- Docker

##Criando o Ambiente
-Instalação das bibliotecas necessarias.
pip instal - pandas / sqlalchemy / streamlit / plotly / psycopg2

______________________________//__________________________________

Execução do Projeto

Após criar o ambiente,
execute o contêiner PostgreSQL:

''docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres''

Execute a script (ultilizei no vsc) Python para carregar e criar os dados/views.

Apos a criação, iniciamos o dashboard:

''streamlit run dashboard.py''

______________________________//__________________________________

Views SQL

Média de temperatura para cada dispositivo IoT.

CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;

Número de leituras de temperatura por hora do dia.

CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM noted_date) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;

Temperaturas máximas e mínimas por dia.

CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(noted_date) AS data, MAX(temperature) AS temp_max, MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY data;
