import mysql.connector
import cx_Oracle
import psycopg2
from pyhive import hive
from kafka import KafkaConsumer
from pymongo import MongoClient
import pyodbc
import psycopg2
import happybase
import ibm_db
import vertica_python
import cassandra.cluster
import clickhouse_driver
import pyhdb
import psycopg2

# 数据源类型
# mysql
# oracle
# postgresql
# hive
# kafka
# sqlserver
# tbase
# mongodb
# hbase
# gbase
# dm
# db2
# vertica
# cassandra
# clickhouse
# hana
# gaussdb200


def test_mysql_connection(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        conn.close()
        print(f"Successfully connected to MySQL database: {database}")
    except mysql.connector.Error as e:
        print(f"Failed to connect to MySQL database: {database}. Error: {str(e)}")


def test_oracle_connection(user, password, dsn):
    try:
        conn = cx_Oracle.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        conn.close()
        print(f"Successfully connected to Oracle database: {dsn}")
    except cx_Oracle.Error as e:
        print(f"Failed to connect to Oracle database: {dsn}. Error: {str(e)}")


def test_postgresql_connection(host, port, user, password, database):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        conn.close()
        print(f"Successfully connected to PostgreSQL database: {database}")
    except psycopg2.Error as e:
        print(f"Failed to connect to PostgreSQL database: {database}. Error: {str(e)}")


def test_hive_connection(host, port, user, password, database):
    try:
        conn = hive.Connection(
            host=host,
            port=port,
            username=user,
            password=password,
            database=database
        )
        conn.close()
        print(f"Successfully connected to Hive database: {database}")
    except Exception as e:
        print(f"Failed to connect to Hive database: {database}. Error: {str(e)}")


def test_kafka_connection(bootstrap_servers, topic):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers
        )
        consumer.close()
        print(f"Successfully connected to Kafka broker: {bootstrap_servers}")
    except Exception as e:
        print(f"Failed to connect to Kafka broker: {bootstrap_servers}. Error: {str(e)}")


def test_sqlserver_connection(server, user, password, database):
    try:
        conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        conn = pyodbc.connect(conn_str)
        conn.close()
        print(f"Successfully connected to SQL Server database: {database}")
    except pyodbc.Error as e:
        print(f"Failed to connect to SQL Server database: {database}. Error: {str(e)}")


def test_tbase_connection(host, port, user, password, database):
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=database)
        print(f"Successfully connected to TBase data source: {host}:{port}/{database}")
        conn.close()
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to TBase data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_mongodb_connection(host, port, username, password, database):
    try:
        client = MongoClient(host, port, username=username, password=password)
        db = client[database]
        db.command("ping")
        client.close()
        print(f"Successfully connected to MongoDB database: {database}")
    except Exception as e:
        print(f"Failed to connect to MongoDB database: {database}. Error: {str(e)}")


def test_hbase_connection(host, port):
    try:
        conn = happybase.Connection(host=host, port=port)
        print(f"Successfully connected to HBase data source: {host}:{port}")
        conn.close()
    except happybase.ConnectionError as e:
        print(f"Failed to connect to HBase data source: {host}:{port}")
        print(f"Error message: {str(e)}")


def test_gbase_connection(host, port, user, password, database):
    try:
        conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
        print(f"Successfully connected to GBase data source: {host}:{port}/{database}")
        conn.close()
    except psycopg2.Error as e:
        print(f"Failed to connect to GBase data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_dm_connection(host, port, user, password, database):
    try:
        connection_string = f"DRIVER={{DM ODBC DRIVER}};SERVER={host},{port};DATABASE={database};UID={user};PWD={password}"
        conn = pyodbc.connect(connection_string)
        print(f"Successfully connected to DM data source: {host}:{port}/{database}")
        conn.close()
    except pyodbc.Error as e:
        print(f"Failed to connect to DM data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_db2_connection(database, hostname, port, username, password):
    conn_string = f"DATABASE={database};HOSTNAME={hostname};PORT={port};PROTOCOL=TCPIP;UID={username};PWD={password};"
    try:
        conn = ibm_db.connect(conn_string, '', '')
        print(f"Successfully connected to DB2 data source: {hostname}:{port}/{database}")
        ibm_db.close(conn)
    except Exception as e:
        print(f"Failed to connect to DB2 data source: {hostname}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_vertica_connection(host, port, database, username, password):
    try:
        conn_info = {"host": host, "port": port, "database": database, "user": username, "password": password}
        conn = vertica_python.connect(**conn_info)
        print(f"Successfully connected to Vertica data source: {host}:{port}/{database}")
        conn.close()
    except vertica_python.Error as e:
        print(f"Failed to connect to Vertica data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_cassandra_connection(host, port, username, password):
    try:
        cluster = cassandra.cluster.Cluster(contact_points=[host], port=port, auth_provider=cassandra.auth.PlainTextAuthProvider(username=username, password=password))
        session = cluster.connect()
        print(f"Successfully connected to Cassandra data source: {host}:{port}")
        session.shutdown()
        cluster.shutdown()
    except cassandra.cluster.NoHostAvailable as e:
        print(f"Failed to connect to Cassandra data source: {host}:{port}")
        print(f"Error message: {str(e)}")


def test_clickhouse_connection(host, port, database, username, password):
    try:
        conn = clickhouse_driver.connect(host=host, port=port, database=database, user=username, password=password)
        print(f"Successfully connected to ClickHouse data source: {host}:{port}/{database}")
        conn.disconnect()
    except clickhouse_driver.Error as e:
        print(f"Failed to connect to ClickHouse data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


def test_hana_connection(host, port, username, password):
    try:
        conn = pyhdb.connect(host=host, port=port, user=username, password=password)
        print(f"Successfully connected to HANA data source: {host}:{port}")
        conn.close()
    except pyhdb.exceptions.DatabaseError as e:
        print(f"Failed to connect to HANA data source: {host}:{port}")
        print(f"Error message: {str(e)}")


def test_gaussdb_connection(host, port, database, username, password):
    try:
        conn = psycopg2.connect(host=host, port=port, database=database, user=username, password=password)
        print(f"Successfully connected to GaussDB200 data source: {host}:{port}/{database}")
        conn.close()
    except psycopg2.Error as e:
        print(f"Failed to connect to GaussDB200 data source: {host}:{port}/{database}")
        print(f"Error message: {str(e)}")


# 测试 MySQL 数据源
mysql_data_source = {"host": "localhost", "user": "root", "password": "password", "database": "db1"}
test_mysql_connection(**mysql_data_source)

# 测试 Oracle 数据源
oracle_data_source = {"user": "user1", "password": "password1", "dsn": "localhost/orcl1"}
test_oracle_connection(**oracle_data_source)

# 测试 PostgreSQL 数据源
# 测试 PostgreSQL 数据源
postgresql_data_source = {"host": "localhost", "port": 5432, "user": "user1", "password": "password1", "database": "db1"}
test_postgresql_connection(**postgresql_data_source)

# 测试 Hive 数据源
hive_data_source = {"host": "localhost", "port": 10000, "user": "user1", "password": "password1", "database": "db1"}
test_hive_connection(**hive_data_source)

# 测试 TBase 数据源
tbase_data_source = {"host": "localhost", "port": 5432, "user": "user1", "password": "password1", "database": "db1"}
test_tbase_connection(**tbase_data_source)

# 测试 Kafka 数据源
kafka_data_source = {"bootstrap_servers": "localhost:9092", "topic": "test_topic"}
test_kafka_connection(**kafka_data_source)


# 测试 MongoDB 数据源
mongodb_data_source = {"host": "localhost", "port": 27017, "username": "user1", "password": "password1", "database": "db1"}
test_mongodb_connection(**mongodb_data_source)


# 测试 GBase 数据源
gbase_data_source = {"host": "localhost", "port": 5258, "user": "user1", "password": "password1", "database": "db1"}
test_gbase_connection(**gbase_data_source)


# 测试 SQL Server 数据源
sqlserver_data_source = {"server": "localhost", "user": "user1", "password": "password1", "database": "db1"}
test_sqlserver_connection(**sqlserver_data_source)

# 测试 HBase 数据源
hbase_data_source = {"host": "localhost", "port": 9090}
test_hbase_connection(**hbase_data_source)

# 测试 DM 数据源
dm_data_source = {"host": "localhost", "port": 5236, "user": "user1", "password": "password1", "database": "db1"}
test_dm_connection(**dm_data_source)

# 测试 DB2 数据源
db2_data_source = {"database": "your_database", "hostname": "your_hostname", "port": "your_port", "username": "your_username", "password": "your_password"}
test_db2_connection(**db2_data_source)

# 测试 Vertica 数据源
vertica_data_source = {"host": "your_host", "port": "your_port", "database": "your_database", "username": "your_username", "password": "your_password"}
test_vertica_connection(**vertica_data_source)

# 测试 cassandra 数据源
cassandra_data_source = {"host": "your_host", "port": 9042, "username": "your_username", "password": "your_password"}
test_cassandra_connection(**cassandra_data_source)

# 测试 ClickHouse 数据源
clickhouse_data_source = {"host": "your_host", "port": "your_port", "database": "your_database", "username": "your_username", "password": "your_password"}
test_clickhouse_connection(**clickhouse_data_source)

# 测试 HANA 数据源
hana_data_source = {"host": "your_host", "port": "your_port", "username": "your_username", "password": "your_password"}
test_hana_connection(**hana_data_source)

# 测试 GaussDB200 数据源
gaussdb_data_source = {"host": "your_host", "port": "your_port", "database": "your_database", "username": "your_username", "password": "your_password"}
test_gaussdb_connection(**gaussdb_data_source)
