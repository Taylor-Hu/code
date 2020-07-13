import pymysql
from pymysql.cursors import SSDictCursor
from framework.woniucbt.common.utility import UtilityTest as util

class Database:
    def __init__(self):
        self.conn = pymysql.connect(util.get_config_value('db','host'), util.get_config_value('db','user'),
                                    util.get_config_value('db','pass'), util.get_config_value('db','dbname'),
                                    charset='utf8')
        self.cursor = self.conn.cursor(cursor=SSDictCursor)

    def query_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def query_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result


