def fetchAllSQL(sql,placeholder,db):
    with db:
        # create a cursor
        cursor=db.cursor()
        # execute sql
        cursor.execute(sql,placeholder)
        # fetch
        data = cursor.fetchall()
        # cursor close 
        cursor.close()
        
    return data

    pass
def getAllQuestionRecByUid(
                        mysql:pymysql.Connection,
                        uid:str,
                        table=config.mysql["table-questionForm"],
                        ):
    sql = f""" 
                select * from {table} WHERE uid=%(uid)s
            """
    with mysql:
        # create a cursor
        cursor=mysql.cursor()
        # execute sql
        cursor.execute(sql,{"uid":uid})
        # fetch
        data = cursor.fetchall()
        # cursor close 
        cursor.close()
        
    return data
