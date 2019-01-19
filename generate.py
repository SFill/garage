from elizabeth import Generic
import mysqlx
from datetime import datetime
from  random import Random


def main():
    mysql_config = {
        "host": "127.0.0.1",
        "port": 33060,
        "user": "root",
        "password": "root1234"
    }

    g = Generic('ru')
    p=g.personal
    a=g.address
    date=datetime.today().strftime("%b %d %Y %H:%M")

    session = mysqlx.get_session(mysql_config)

    if False:
        for i in range(12,14):
            name=p.full_name()

            query = "Insert into garage.user values({4},{0},\"{1}\",\"{2}\",\"{3}\")".format(
                1,
                p.username(),
                p.password(),
                name,
                i

            )
            session.sql(query).execute()

            print(query)
            query="Insert into garage.driver values(\"{0}\",{1},{2},{3},{4})".format(
                name,
                p.age(),
                Random().randint(1,10),
                Random().randint(10000, 30000),
                i,

            )
            print(query)


        session.sql(query).execute()
    rnd=Random()

    for i in range(151):
        try:
            start=a.address()
            finish=a.address()
            plane='не оговорен'
            success=rnd.randint(0,1)
            client=p.full_name()
            id_avto=rnd.choice([1,2,3])
            id_driver=rnd.choice([1,2]+[i for i in range(6,14)])
            id=i

            query = 'Insert into garage.route values("{0}","{1}","{2}",{3},"{4}",{5},{6},{7})'.format(
                start,
                finish,
                plane,
                success,
                client,
                id_avto,
                id_driver,
                id
            )
            session.sql(query).execute()
            print(query)
        except Exception:
            continue

    session.close()


if __name__ == '__main__':
    main()