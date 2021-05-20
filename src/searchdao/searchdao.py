from model.connection import BasicDAO, ConnectionDecorator
from datetime import datetime

class SearchesDAO(BasicDAO):

    def __init__(self) -> None:
        super().__init__()

    @ConnectionDecorator.open_conn
    def add_search_to_db(self, data=None):

        description = data.get('description', None)
        location = data.get('location', None)
        ipaddress = "666.666.666.666"
        time = datetime.now()

        location = location.replace(" ", "_")

        values = [time, description, location, ipaddress]
        cur = self.conn.cursor()

        query = """INSERT INTO searches (time, description, location, ipaddress)
                    VALUES (?, ?, ?, ?);"""
        
        cur.execute(query, values) 

        return "ok"


    @ConnectionDecorator.open_conn    
    def initialize_search_table(self):

        query = """CREATE TABLE IF NOT EXISTS searches (
                    id SERIAL PRIMARY KEY,
                    time DATETIME,
                    description VARCHAR(20) NOT NULL,
                    location VARCHAR (20),
                    ipaddress DATETIME
                );"""

        cur = self.conn.cursor()

        cur.execute(query)

