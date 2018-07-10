from UfoDataReader.util.parser import UfoXBRLParser

ufoparser = UfoXBRLParser()
xbrl = ufoparser.parse('sample.xbrl')

dei = ufoparser.parseDEI(xbrl)
print(dei.__dict__)

gaap = ufoparser.parseGAAP(xbrl)
print(gaap.__dict__)

