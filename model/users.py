from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table("data_users",meta_data,
              Column("id", Integer, primary_key=True),
              Column("first_surname",String(20)),
              Column("first_name",String(20)),
              Column("other_name",String(50)),
              Column("country",String(20)),
              Column("email",String(300))
            )


meta_data.create_all(engine)