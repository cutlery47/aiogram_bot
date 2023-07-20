import psycopg2

class MyBD:

    def add_data(self, latitude: int, longtitude: int) -> bool:
        connect = psycopg2.connect(dbname="doxx_data", port=5432, user="postgres", password="12345", host="localhost")
        cursor = connect.cursor()

        query = "INSERT INTO location(latitude, longtitude) VALUES ("
        query += "'" + str(latitude) + "',"
        query += "'" + str(longtitude) + "');"

        cursor.execute(query)
        connect.commit()

        cursor.close()

        return True

