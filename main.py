print ("ddd")

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:postgres@172.15.100.222/allparams")
engine.connect()

ins = customers.insert().values(
    first_name = 'Dmitriy',
    last_name = 'Yatsenko',
    username = 'Moseend',
    email = 'moseend@mail.com',
    address = 'Shemilovskiy 2-Y Per., bld. 8/10, appt. 23',
    town = ' Vladivostok'
)

print(ins)
