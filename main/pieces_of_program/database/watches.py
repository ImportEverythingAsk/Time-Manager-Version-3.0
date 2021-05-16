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

def update_data(prepared_data):
    sql_update = ('UPDATE watches SET watch_name = :value1, run_next_alarm_immediately = :value2 WHERE rowid = ?')
    c.execute(sql_update, prepared_data)
    conn.commit()

def delete_watch(watch_id):
    c.execute("DELETE FROM watches WHERE watch_id = " + str(watch_id))
    conn.commit()
def update_was_last_opened_column(watch_id):
    c.execute('UPDATE watches set was_last_opened = ? WHERE was_last_opened = ?', (0, watch_id))
    conn.commit()