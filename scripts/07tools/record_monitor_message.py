import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import mysql.connector

def store_result(category, result):
    connection = mysql.connector.connect(
        host='your_mysql_host',
        user='your_mysql_user',
        password='your_mysql_password',
        database='your_mysql_database'
    )

    cursor = connection.cursor()

    # Insert the result into a table
    insert_query = "INSERT INTO monitoring_results (category, result) VALUES (%s, %s)"
    cursor.execute(insert_query, (category, result))

    # Commit the changes and close the connection
    connection.commit()
    cursor.close()
    connection.close()

# Monitoring function




