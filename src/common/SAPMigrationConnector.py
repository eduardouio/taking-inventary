from pymssql import connect, Cursor
from decimal import Decimal

from config.secrets_config import SAP_CONNECTION, MIGRATION_QUERY


class SAPMigrationConnector(object):

    def conect(self):
        try:
            self.conn = connect(**SAP_CONNECTION, login_timeout=5)
        except:
            raise Exception('Error al conectar a SAP')

    def runMigration(self) -> list:
        """Ejecuta la consulta el servidor y retorna un arreglo"""
        self.conect()
        # ejecuramos la consulta en SAP
        cursor = self.conn.cursor(as_dict=True)
        cursor.execute(MIGRATION_QUERY)
        report = [i for i in cursor]

        # generamos el arreglo a retorar
        for item in report:
            for k, v in zip(item.keys(), item.values()):
                if isinstance(v, Decimal):
                    item[k] = int(v)

        # cerramos la conexion
        cursor.close()
        self.conn.close()
        # retornamos el reporte
        return report
