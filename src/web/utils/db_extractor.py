import time
from flask import current_app
from dbcore import db

class DbExtractor:
    def __init__(self):
        random_var = 3

    def get_total_delay(lon, lat, radius):
        sql = 'SELECT COUNT(time) FROM buses_clean_with_timetables_archived WHERE ST_DistanceSphere(ST_MakePoint(lon, lat), ST_MakePoint(52.233407, 21.116504)) <= 10;'
        result = db.engine.execute(sql).scalar()
        print(result)

        return result
