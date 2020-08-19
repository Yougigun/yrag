import yaml
import pymysql
import pymysql
import aioredis
from  fastapi import HTTPException
def mysqlConnec(host,user,password,database,port):
    async def mysqlConnec():
        try :
            db = pymysql.connect(host = host,
                                user = user,
                                password = password,
                                database = database,
                                cursorclass=pymysql.cursors.DictCursor,
                                port=port
                                )
        except:
            # logger.error("cannot connect mysql database")
            raise HTTPException(424 , "cannot connect mysql database")
        try:
            yield db
        finally:
            db.close()
    return mysqlConnec

def db_engine(file_:str ="db.yml"):
    with open(f'./{file_}') as f:
        db_config = yaml.load(f, Loader=yaml.FullLoader)
    db = dict()
    for db_name in db_config:
        if db_config[db_name]["type"] == "mysql":
            db[db_name] = mysqlConnec(
                                        host=db_config[db_name]["host"],
                                        user=db_config[db_name]["user"],
                                        password=db_config[db_name]["password"],
                                        database=db_config[db_name]["database"],
                                        port=db_config[db_name]["port"],
                                        )

    return db
