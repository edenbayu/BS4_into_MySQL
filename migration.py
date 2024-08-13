import mysql.connector

# Configuration
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'testing',
    'raise_on_warnings': True
}

def migrate_data(judul_komik):
    try:
        #Connect to the database
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        #Query to the table
        select_query = "SELECT * FROM testing_scraping"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        # Prepare data for insertion
        data_to_insert = [(komik_title,) for komik_title in judul_komik]

        #Update Query
        insert_query = "INSERT INTO testing_scraping (judul_komik) VALUES(%s)"
        cursor.executemany(insert_query, data_to_insert)
        conn.commit()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
