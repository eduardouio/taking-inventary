from unittest import result
from Con import Con

QUERY = """
    --CORDOVEZ
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand , T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_CORDOVEZ_PROD].DBO.[OITM] T0 INNER JOIN [DB_CORDOVEZ_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_CORDOVEZ_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
      , [DB_CORDOVEZ_PROD].DBO.[OADM] T2
      WHERE T1.WhsCode IN('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16') AND T0.validFor = 'Y'
    UNION ALL
    --VINESA
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_VINESA_PROD].DBO.[OITM] T0 INNER JOIN [DB_VINESA_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_VINESA_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
      , [DB_VINESA_PROD].DBO.[OADM] T2
      WHERE T1.WhsCode IN('1','2','3','4','5','6','7','8','9','10','11') AND T0.validFor = 'Y'
    UNION ALL
    --VINLITORAL
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_VINLITORAL_PROD].DBO.[OITM] T0 INNER JOIN [DB_VINLITORAL_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_VINLITORAL_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
  , [DB_VINLITORAL_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('01','02','03','04','05') AND T0.validFor = 'Y'
    UNION ALL
    --PLUSBRAND
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_PLUSBRAND_PROD].DBO.[OITM] T0 INNER JOIN [DB_PLUSBRAND_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_PLUSBRAND_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_PLUSBRAND_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','98','99') AND T0.validFor = 'Y'
    UNION ALL
    --IMNAC
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_IMNAC_PROD].DBO.[OITM] T0 INNER JOIN [DB_IMNAC_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_IMNAC_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_IMNAC_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('01','02','03','04','05','06','07','08') AND T0.validFor = 'Y'
    UNION ALL
    --PANIAGUA
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_PANIAGUA_PROD].DBO.[OITM] T0 INNER JOIN [DB_PANIAGUA_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_PANIAGUA_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_PANIAGUA_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('01','02','03','04','05','06','07','08') AND T0.validFor = 'Y'
    UNION ALL
    --SERVMULTIMARC
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_SERVMULTIMARC_PROD].DBO.[OITM] T0 INNER JOIN [DB_SERVMULTIMARC_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_SERVMULTIMARC_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_SERVMULTIMARC_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('1','2','3','4','5','6','7','8','9','10','11','12','14','15','16','98','99') AND T0.validFor = 'Y'
    UNION ALL
    --VIDINTERNACIONAL
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_VID_PROD].DBO.[OITM] T0 INNER JOIN [DB_VID_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_VID_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_VID_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('01','02','03','04','05','06','07','08','93') AND T0.validFor = 'Y'
    UNION ALL
    --REVECUADOR
    SELECT T2.COMPNYNAME, T0.ITEMCODE, T0.ITEMNAME,T0.ITEMCODE+' '+ T0.ITEMNAME AS ItemDesc, T1.WHSCODE,T3.WhsName, T1.OnHand, T1.OnOrder, T1.IsCommited,  T1.ONHAND+ T1.OnOrder- T1.IsCommited AS Available
    FROM [DB_REVECUADOR_PROD].DBO.[OITM] T0 INNER JOIN [DB_REVECUADOR_PROD].DBO.OITW T1 ON T0.ItemCode=T1.ITEMCODE
    INNER JOIN [DB_REVECUADOR_PROD].DBO.[OWHS] T3 ON T3.WhsCode=T1.WhsCode
    , [DB_REVECUADOR_PROD].DBO.[OADM] T2
    WHERE T1.WhsCode IN('01','02','03','04','05','06','07','08','10') AND T0.validFor = 'Y'
"""

class ModelInventary():
    """Usamos los mismo datos de cordovez"""
    def __init__(self):
        self.conn = Con('cordovez')
    
    def get_all(self):
        data = self.conn.run_query(QUERY)
        products = []
        
        for item in data:
            products.append({
                'enterprise': item[0],
                'cod_contable': item[1],
                'product_name': item[2],
                'warenhouse_number': item[3],
                'warenhouse_name': item[4],
                'on_hand': int(item[5]),
                'on_order': int(item[6]),
                'is_commited': int(item[7]),
                'avaliable': int(item[8])
            })

        return products
