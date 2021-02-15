import os

KAFKA_TOPIC = 'order'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'


#############################################
# MySQL
#############################################
def get_mysql_url():
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT', 3306)
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    name = os.environ.get('DB_NAME')
    return f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{name}'
