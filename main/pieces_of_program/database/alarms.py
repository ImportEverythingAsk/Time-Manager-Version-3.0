import sqlite3


def setup():
    global conn
    global c
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    conn.row_factory = sqlite3.Row

def insert_alarm(prepared_data):
    c.execute("""INSERT INTO alarms(positionx, positiony, name, beginning_time, remaining_time, is_time_specific_checked, 
                   notify_dropdown_time, specific_notify_time, alarm_sound, watch_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (prepared_data))
    conn.commit()
    alarm_id = c.lastrowid
    return alarm_id
def update_alarm(prepared_data):
    sql_update = ('''\
                UPDATE alarms SET positionx = :value1, positiony = :value2, name = :value3, beginning_time = :value4, 
                remaining_time = :value5, is_time_specific_checked = :value6, notify_dropdown_time = :value7, 
                specific_notify_time = :value8, alarm_sound = :value9, watch_id = :value10 WHERE rowid = ?
                ''')
    c.execute(sql_update, prepared_data)
    conn.commit()

def delete_alarms(watch_id):
    c.execute("DELETE FROM alarms where watch_id =" + str(watch_id))
    conn.commit()