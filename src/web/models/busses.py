from run import db


class buses_clean_with_timetables_archived(db.Model):
    __tablename__ = 'results'

    time = db.Column(db.DateTime)
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    delay = db.Column(db.Float)

    def __init__(self, time, lon, lat, delay):
        self.time = time
        self.lon = lon
        self.lat = lat
        self.delay = delay

    def __repr__(self):
        return f'Time:{self.time}, lat:{self.lat}, lon:{self.lon}, delay:{self.delay}'
