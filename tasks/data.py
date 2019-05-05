# these modules are needed for the task
from sqlalchemy import String
import luigi
import psycopg2
from luigi.contrib import sqla
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

reflect = True
connection_string = "sqlite://"  # in memory SQLite database
table = "Author"  # name of the table to store data


class QuerySQL(luigi.Task):
    def output(self):
        # the output will be a .csv file
        return luigi.LocalTarget("/data/ListofAuthors.csv")

    def run(self):
        # these are here for convenience, you'll use
        # environment variables for production code

        conn = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

        cur = conn.cursor()
        cur.execute("""SELECT
          first_name,
          last_name,
         
          FROM Author
        """)
        rows = cur.fetchall()

        with self.output().open("w") as out_file:
            # write a csv header 'by hand'
            out_file.write("first_name, last_name")
            for row in rows:
                out_file.write("\n")
                # without the :%s, the date will be output in year-month-day format
                # the star before row causes each element to be placed by itself into format
                out_file.write("{},  {}".format(*row))


if __name__ == "__main__":
    luigi.build(QuerySQL, worker_scheduler_factory=1, local_scheduler=True)
