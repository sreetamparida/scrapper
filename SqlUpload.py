#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import create_engine


class Engine:
    
    #setup database connection
    def __init__(self,dailect,driver,user_name,password,host,db_name):
        self.dailect = dailect
        self.driver = driver
        self.user_name = user_name
        self.password = password
        self.host = host
        self.db_name = db_name
        self.url = str(dailect)+'+'+str(driver)+'://'+str(user_name)+':'+str(password)+'@'+str(host)+'/'+str(db_name)
        self.engine = create_engine(self.url, echo=False)
    
    # Setup sqlite connection
    
    # Upload data to server
    def uploadData(self,data,table_name):
        data.to_sql(str(table_name),con=self.engine)
    # Execute query    
    def executeQuery(self,query):
        return self.engine.executeQuery(query).fetchAll()





