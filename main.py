from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('banda-larga.json')

# Sua consulta SQL
query = """
SELECT *
FROM `basedosdados.br_anatel_banda_larga_fixa.microdados`
LIMIT 100
"""

# Execute a consulta
query_job = client.query(query)

# Obtenha os resultados
results = query_job.result()

# Itere sobre os resultados
for row in results:
    print(row)
