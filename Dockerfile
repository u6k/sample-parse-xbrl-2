FROM python:3

RUN pip install git+https://github.com/sawadyrr5/UfoDataReader
RUN sed -i -e 's/from pandas.core.common/from pandas.api.types/g' /usr/local/lib/python3.7/site-packages/pandas_datareader/fred.py

VOLUME /var/myapp
WORKDIR /var/myapp

CMD ["python", "parse-xbrl.py"]

