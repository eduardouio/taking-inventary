from pymssql import connect, Cursor
from decimal import Decimal

from config.secrets_config import SAP_CONNECTION, MIGRATION_QUERY

class SAPMigrationConnector(object):

	def __init__(self):
		try:
			self.conn = connect(**SAP_CONNECTION, login_timeout=5)
		except:
			self.conn = False

	def runMigration(self):
		if self.conn == False:
			return False

		cursor = self.conn.cursor(as_dict=True)
		cursor.execute(MIGRATION_QUERY)
		report = [i for i in cursor] 
		for item in report:
			for k,v in zip(item.keys(),item.values()):
				if isinstance(v, Decimal):
					item[k] = int(v)
			
		cursor.close()
		self.conn.close()
		return report
		