from UfoDataReader.io.data import DataReader
from datetime import datetime

start = datetime(2017, 6, 23)
end = datetime(2017, 6, 23)
ufos = DataReader('7203', 'ufo', start, end, fetch_xbrl=False)
print(ufos)



from UfoDataReader.util.parser import UfoXBRLParser

ufoparser = UfoXBRLParser()
xbrl = ufoparser.parse('sample.xbrl')
dei = ufoparser.parseDEI(xbrl)
print(dei.__dict__)
gaap = ufoparser.parseGAAP(xbrl)
print(gaap.__dict__)

