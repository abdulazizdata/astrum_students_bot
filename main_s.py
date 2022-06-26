import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO persons_data (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM persons_data WHERE user_id = ?", (user_id,)).fetchall()
            # print(bool(len(result)))
            return bool(len(result))

    def add_quser(self, user_id, qwasar_user):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET q_user = ? WHERE user_id = ?",
                                       (qwasar_user, user_id,))

    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET Full_name = ? WHERE user_id = ?",
                                       (name, user_id,))

    def set_path(self, user_id, path):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET path = ? WHERE user_id = ?", (path, user_id,))

    def set_t_user(self, user_id, t_user):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET t_user = ? WHERE user_id = ?", (t_user, user_id,))

    def set_phone_number(self, user_id, phone_number):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET phone_number = ? WHERE user_id = ?",
                                       (phone_number, user_id,))

    def set_season(self, user_id, season):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET season = ? WHERE user_id = ?", (season, user_id,))

    def set_stay(self, user_id, stay):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET stay = ? WHERE user_id = ?", (stay, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM persons_data WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE persons_data SET signup = ? WHERE user_id = ?", (signup, user_id,))
