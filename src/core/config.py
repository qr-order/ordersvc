import os


#############################################
# Kafka
#############################################
KAFKA_TOPIC = 'order'
KAFKA_HOST = os.environ.get("KAFKA_HOST")
KAFKA_PORT = os.environ.get("KAFKA_PORT")
KAFKA_BOOTSTRAP_SERVERS = f'{KAFKA_HOST}:{KAFKA_PORT}'


#############################################
# Postgresql
#############################################
def get_postgres_url():
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT', 5432)
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    name = os.environ.get('DB_NAME')
    return f'postgresql://{user}:{password}@{host}:{port}/{name}'
