"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os.path
import csv

customers_data = os.path.join('north_data', 'customers_data.csv')
employees_data = os.path.join('north_data', 'employees_data.csv')
orders_data = os.path.join('north_data', 'orders_data.csv')

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='658311')


def writing_to_table(filename, table_name):
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            quantity_el = '%s, ' * len(row)
            cur.execute(f"INSERT INTO {table_name} VALUES({quantity_el[:-2]})", (row[::]))


try:
    with conn:
        with conn.cursor() as cur:
            writing_to_table(customers_data, 'customers')

            writing_to_table(employees_data, 'employees')

            writing_to_table(orders_data, 'orders')
finally:
    conn.close()