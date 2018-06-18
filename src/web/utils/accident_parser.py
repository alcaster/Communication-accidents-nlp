import csv
import datetime
import psycopg2


class Accident:

    def __init__(self, start_date, end_date, x_cord, y_cord, s_hour, s_min, e_hour, e_min):
        self.start_date = start_date
        self.end_date = end_date
        self.stat_time_hour = s_hour
        self.start_time_min = s_min
        self.end_time_hour = e_hour
        self.end_time_min = e_min
        self.x = x_cord
        self.y = y_cord


class AccidentParser:

    def __init__(self, filename):
        self.filename = filename
        self.list_of_accidents = []

    def create_list_of_database_entries(self):
        list_of_accident_entries = []
        with open(self.filename, 'rt') as file:
            reader = csv.reader(file, delimiter=' ')
            for i, row in enumerate(reader):
                if i == 0: continue
                start_date = row[0]
                end_date = row[1]
                s_day, s_month, s_year = start_date.split('.')
                e_day, e_month, e_year = end_date.split('.')
                if end_date == '2.017.':
                    e_day = s_day
                    e_month = s_month
                    e_year = s_year
                if len(e_year) == 0:
                    e_year = s_year
                if len(e_day) == 1:
                    e_day = '0' + e_day

                start_time = row[2]
                if len(start_time) == 3: start_time = '0' + start_time
                start_hour = start_time[0:2]
                start_min = start_time[2:4]

                end_time = row[3]
                if len(end_time) == 3: end_time = '0' + end_time
                end_hour = end_time[0:2]
                end_min = end_time[2:4]

                x = float(row[4])
                y = float(row[5])

                start_date_str = s_day + s_month + s_year
                end_date_str = e_day + e_month + e_year

                start_date = datetime.datetime.strptime(start_date_str, "%d%m%Y").date()

                end_date = datetime.datetime.strptime(end_date_str, "%d%m%Y").date()

                entry = Accident(start_date=start_date, end_date=end_date, x_cord=x, y_cord=y, s_hour=start_hour,
                                 s_min=start_min, e_hour=end_hour, e_min=end_min)
                list_of_accident_entries.append(entry)

        self.list_of_accidents = list_of_accident_entries

    def create_accident_table(self):
        conn = psycopg2.connect(host="localhost", dbname='nlp', user='postgres', password='password')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE ACCIDENT(
                START_DATE DATE NOT NULL,
                END_DATE DATE NOT NULL,
                START_TIME_H smallint NOT NULL,
                START_TIME_M smallint NOT NULL,
                END_TIME_H smallint NOT NULL,
                END_TIME_M smallint NOT NULL,
                X REAL  NOT NULL,
                Y REAL NOT NULL
        )""")
        conn.commit()

    def populate_database(self):
        connection = psycopg2.connect(host="localhost", dbname='nlp', user='postgres', password='password')
        # connection.autocommit = True
        cur = connection.cursor()
        sql = """INSERT INTO ACCIDENT VALUES (\'{}\'::date,\'{}\'::date,{}::int2,{}::int2,{}::int2,{}::int2,{}::real,{}::real)"""
        for counter, accident in enumerate(self.list_of_accidents):
            cur.execute(
                sql.format(accident.start_date.strftime("%Y-%m-%d"), accident.end_date.strftime("%Y-%m-%d"),
                           accident.stat_time_hour, accident.start_time_min,
                           accident.end_time_hour, accident.end_time_min, accident.x, accident.y))
            connection.commit()
