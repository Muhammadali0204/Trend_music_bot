import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
	            id	INTEGER NOT NULL UNIQUE
            );
        """
        self.execute(sql, commit=True)
       
    def  create_table_data(self):
        sql = """
        CREATE TABLE Data (
            "id"	INTEGER NOT NULL UNIQUE,
            "nomi"	TEXT UNIQUE,
            "file_id"	TEXT,
            "turi"	TEXT,
            "status"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        """
        
        self.execute(sql, commit=True)
        
    
        
    

    



    def add_user(self, id: int):

        sql = """
        INSERT INTO Users(id) VALUES(?)
        """
        self.execute(sql, parameters=(id,), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, id):
        sql = "SELECT * FROM Users WHERE id = ?"
        return self.execute(sql, parameters=(id,), fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
    
    def count_users_data(self):
        return self.execute("SELECT COUNT(*) FROM Data;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
        
        
    def select_data_id(self, id):
        return self.execute(sql="SELECT * FROM Data WHERE id = ?", parameters=(id,), fetchone=True)
    
    def select_data_nom(self, nom):
        return self.execute(sql="SELECT * FROM Data WHERE nomi  = ?",parameters=(nom,), fetchone=True)
        
    def select_data_nomlar(self, nom):
        return self.execute(sql=f"SELECT * FROM Data WHERE nomi LIKE '%{nom}%'", fetchall=True)
        
    def select_data_turi_ordered(self, turi):
        return self.execute(sql="SELECT * FROM Data WHERE turi = ? ORDER BY status DESC", parameters=(turi,), fetchall=True)
        
    def select_top(self):
        return self.execute(sql="SELECT * FROM Data ORDER BY status DESC", fetchall=True)
    
    def add_data(self, nomi, file_id, turi, status):
        self.execute(sql="INSERT INTO Data(nomi, file_id, turi, status) VALUES(?, ?, ?, ?)",parameters=(nomi, file_id, turi, status) ,commit=True)
        
    def update_status(self, id, status):
        self.execute("UPDATE Data SET status = ? WHERE id = ?", parameters=(status, id), commit=True)
        
