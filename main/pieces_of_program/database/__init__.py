import sqlite3
from ..database import watches
from ..database import alarms
class Database:
    def data_setup(self):
        self.conn = sqlite3.connect("data.db")
        self.c = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

        watches.setup()
        alarms.setup()

        # Making table if it the program hasn't been run before
        self.c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='watches'")
        if self.c.fetchone()[0] != 1:
            self.create_db()
        else:
            self.load_data()

    def create_db(self):
        print("creating")
        self.c.execute("""CREATE TABLE watches (
                            watch_name text,
                            notes text,
                            total_alarms integer,
                            run_next_alarm_immediately text,
                            watch_id integer,
                            was_last_opened text
                        )""")
        self.c.execute("""CREATE TABLE alarms (
                        positionx integer,
                        positiony integer,
                        name text,
                        beginning_time text,
                        remaining_time text,
                        is_time_specific_checked integer,
                        notify_dropdown_time text,
                        specific_notify_time text,
                        alarm_sound text,
                        watch_id integer
                    )""")
        self.conn.commit()

    def load_data(self):
        print("loading")

    def closing_program(self):
        self.c.execute("SELECT * from alarms")
        self.c.execute("DROP TABLE alarms")
        self.c.execute("SELECT * from watches")
        self.c.execute("DROP TABLE watches")
        self.conn.commit()
        self.conn.close()