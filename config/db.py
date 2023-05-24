from sqlalchemy import create_engine , MetaData

engine = create_engine("mysql+pymysql://pma:123456@localhost:3306/users")

meta_data = MetaData()
