from datetime import datetime


def load_message(db_conn, message):
    if not message:
        return

    try:
        cursor = db_conn.cursor()

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(now)

        cursor.execute('''
            INSERT INTO arinc_429_messages 
            (timestamp,
            channel,
            raw_message,
            raw_parity_field,
            raw_data_field,
            raw_label_field,
            processed_label_field,
            message_group,
            processed_data_field)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            now,
            message['channel'],
            message['raw_message'],
            message['raw_fields']['parity'],
            message['raw_fields']['data'],
            message['raw_fields']['label'],
            message['processed_fields']['label'],
            message['message_group'],
            message['processed_fields']['data']
        ))
        db_conn.commit()

    except Exception as e:
        print(f"[ERROR] Database insertion: {e}")
