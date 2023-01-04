from pymssql import connect, Cursor
from decimal import Decimal

from config.secrets_config import SAP_CONNECTION, MIGRATION_QUERY

class SAPMigrationConnector(object):
    
    def connectDb(self):
        conn = connect(**SAP_CONNECTION)
        cursor = conn.cursor(as_dict=True)
        return cursor

    def runMigration(self):
        cursor = self.connectDb()
        cursor.execute(MIGRATION_QUERY)
        report = [i for i in cursor] 
        for item in report:
            for k,v in zip(item.keys(),item.values()):
                if isinstance(v, Decimal):
                    item[k] = int(v)
        return report
        