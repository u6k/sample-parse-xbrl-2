from UfoDataReader.io.data import DataReader
from datetime import datetime

start = datetime(2017, 6, 23)
end = datetime(2017, 6, 23)
ufos = DataReader('7203', 'ufo', start, end, fetch_xbrl=False)
print(ufos)

