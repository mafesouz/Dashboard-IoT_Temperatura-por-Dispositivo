from sqlalchemy import create_engine
from ler_csv import df  # Certifique-se de que ler_csv.py está no mesmo diretório

# Conexão com o PostgreSQL
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres_iot')

# Inserir os dados no banco de dados
df.to_sql('temperatura_readings', engine, if_exists='replace', index=False)