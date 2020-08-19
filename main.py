import fastapi
import yrag
from  .models import irisModel
from fastapi import FastAPI,Body, Query, Path, Request,Depends

# create API
app = FastAPI(title="MY AWESOME MODEL")

# database connection
db = yrag.db_engine()

@app.get('./iris-model')
def iris_model( length:Body(...),
                width:Body(...),
                height:Body(...),
                db = Depends(db["iris-mysql"])):
    table = "iris-table"
    sql = f"select * from {table} where uid=%(uid)s"
    ph = {"uid":"10812240"}
    data = yrag.fetchAllSQL(sql,ph)
    result = irisModel(length,width,height,data)

    return result 

    
print(db["iris-mysql"]())