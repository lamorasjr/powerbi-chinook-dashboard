import os
import csv
import sqlite3

def extract_database_tables(db_path:str)->list:
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT IN ('sqlite_stat1', 'sqlite_sequence');")
        rows = cur.fetchall()
        return [ r[0] for r in rows ]

def export_table_to_csv(db_path:str, table_name:str, output_path:str):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {table_name};')
        rows = cur.fetchall()
        headers = [ d[0] for d in cur.description ]

        output_csv = os.path.join(output_path, f'{table_name}.csv')

        with open(output_csv, mode = 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            csv_writer.writerows(rows)
        
        print(f'Exported table {table_name} to {output_csv}.')

if __name__ == '__main__':

    db_path = 'src\chinook.db'      # define path to sqlit database
    output_path = 'data'            # define path to export csv

    tables = extract_database_tables(db_path)
    
    try:
        for t in tables:
            export_table_to_csv(db_path, t, output_path)
    
    except sqlite3.Error as e:
        print(f'SQLite Error: {e}')