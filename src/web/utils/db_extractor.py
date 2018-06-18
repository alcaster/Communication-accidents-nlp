from dbcore import db


def get_total_delay(lon, lat, radius, date):
    # robust to string/long format of input
    # lon = "52.233407"
    # lat = "21.116504"
    # radius = "10"
    open_sql = 'SELECT COUNT(time) FROM buses_clean_with_timetables_archived WHERE time=\'{}\'::date AND ST_DistanceSphere(ST_MakePoint(lon, lat), ST_MakePoint({}, {})) <= {};'
    sql = open_sql.format(date, lon, lat, radius)
    result = db.engine.execute(sql).scalar()

    return result
