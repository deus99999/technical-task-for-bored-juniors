import requests
import sqlite3


class APIWrapper:
    url = "http://www.boredapi.com/api/activity/"

    def get_random_act(self, act_type=None, participants=None, price=None, minprice=None, maxprice=None,
                       accessibility=None, minaccessibility=None, maxaccessibility=None):
        params = {}
        if act_type:
            params['type'] = act_type
        if participants:
            params['participants'] = participants
        if price:
            params['price'] = price
        if minprice and maxprice:
            params['minprice'] = minprice
            params['maxprice'] = maxprice
        if accessibility:
            params['accessibility'] = accessibility
        if minaccessibility and maxaccessibility:
            params['minaccessibility'] = minaccessibility
            params['maxaccessibility'] = maxaccessibility

        response = requests.get(APIWrapper.url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch activity from Bored API")


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS activities ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            activity TEXT, \
            type TEXT, \
            participants INTEGER, \
            price FLOAT, \
            accessibility FLOAT)")

    def save_activity(self, activity_data):
        insert_sql = """
            INSERT INTO activities (activity, type, participants, price, accessibility)
            VALUES (?, ?, ?, ?, ?)
            """
        values = (
            activity_data['activity'],
            activity_data.get('type', None),
            activity_data.get('participants', None),
            activity_data.get('price', None),
            activity_data.get('accessibility', None),
        )

        try:
            self.cursor.execute(insert_sql, values)
            self.conn.commit()
            print("Activity saved successfully.")
        except Exception as e:
            self.conn.rollback()
            print(f"Failed to save activity: {str(e)}")

    def get_last_5_data(self):
        try:
            query_last_data = """
            SELECT * FROM activities
            ORDER BY id DESC LIMIT 5
            """

            self.cursor.execute(query_last_data)
            records = self.cursor.fetchall()
            return records

        except Exception as e:
            print(f"Database not exits or invalid query.")

    def close(self):
        self.conn.close()