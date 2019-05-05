from sqlalchemy import String
import luigi
from luigi.contrib import sqla


class SQLATask(sqla.CopyToTable):
    # columns defines the table schema, with each element corresponding
    # to a column in the format (args, kwargs) which will be sent to
    # the sqlalchemy.Column(*args, **kwargs)

    reflect = True
    connection_string = "sqlite://"  # in memory SQLite database
    table = "Author"  # name of the table to store data

    columns = [
        (["First_Name", String(64)], {}),
        (["Last_Name", String(64)], {})
    ]
    
    def rows(self):
        for row in [("First_Name", "Babacar"), ("Last_Name", "Kane")]:
            yield row


if __name__ == '__main__':
    task = SQLATask()
    luigi.build([task], local_scheduler=True)
