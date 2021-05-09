import sqlite3
def setup():
    global conn
    global c
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    conn.row_factory = sqlite3.Row


def insert_watch(prepared_data):
    c.execute("""INSERT INTO watches(watch_name, notes, total_alarms, run_next_alarm_immediately, watch_id, was_last_opened) 
                   VALUES (?, ?, ?, ?, ?, ?)""", (prepared_data))
    conn.commit()


    # self.load_data()