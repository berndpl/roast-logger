#!/usr/bin/python
import csv
import os
import datetime
from dateutil.relativedelta import relativedelta
import time

class Logger:

    default_filename = "{} Roast.csv".format("{:%Y-%m-%d %H:%M:%S}.csv".format(datetime.datetime.now()))
    default_columns = ['Time', 'Environment', 'Beans', '1st Crack']
    start_time = datetime.datetime.now()
    last_write_date = datetime.datetime.now()
    write_interval_seconds = 0

    filename = ''
    columns = []

    def __init__(self, **kwargs):
        self.filename = self.default_filename # kwargs.get('filename', self.default_filename)
        self.columns = self.default_columns #kwargs.get('columns', self.default_filename)
        self.start_time = self.start_time
        start_time = datetime.datetime.now()
        self.create_csv(self.filename, self.columns)

    def add_row(self, environment, beans, crack):
        with open(self.filename, 'a') as file:
            csv_writer = csv.DictWriter(file, delimiter='\t', fieldnames=self.columns)
            current_date = datetime.datetime.now()
            diff = relativedelta(current_date, self.start_time)
            seconds_since_last_write = relativedelta(current_date, self.last_write_date)
            row = {
                'Time':"{:0>2}:{:0>2}".format(diff.minutes, diff.seconds),
                'Environment':environment,
                'Beans': beans,
                '1st Crack': crack
            }
            if seconds_since_last_write.seconds > self.write_interval_seconds:
                self.last_write_date = current_date
                csv_writer.writerow(row)
                print(row)
                print(os.path.getsize(self.filename))

    def create_csv(self, filename, columns):
        with open(filename, 'wb') as file:
            csv_writer = csv.DictWriter(file, delimiter='\t', fieldnames=columns)
            csv_writer.writeheader()
            #logging_loop(writer)

if __name__ == '__main__':
    print("Balconia Roast Logger")
    log = Logger()
    log.add_row("e", "b", "c")
    # add_row(filename, columns, "eas", "adb", "sc")
