from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import urllib
import pyodbc
from Querys import *
    
class Database:
    # Configuración de los parámetros de conexión
    def __init__(self):

        user = "root"
        password = "My:S3cr3t4"
        host = "localhost"  # Nombre del servicio MySQL en Docker
        port = "30306"        # Puerto del servidor MySQL
        database = "AMSA"

        connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(connection_string)
        self.session = sessionmaker(bind=self.engine)
       
        # connection_string = (
        #     "mysql+pyodbc:///?odbc_connect=" +
        #     urllib.parse.quote_plus(
        #         f"DRIVER={{MySQL ODBC 9.1 Unicode Driver}};SERVER={host};PORT={port};DATABASE={database};UID={user};PWD={password}"
        #     )
        # )
        # return connection_string
    
    # def selmateriales(self):
    #     mi_conexion = Servicio.conectar()
    #     engine = create_engine(mi_conexion)
    #     with engine.connect() as connection:
    #         result = connection.execute(text(Querys.QUERY_MATERIALES))
    #     return result
    
    def get_materiales(self):
        with self.engine.connect() as connection:
            query = text(Querys.QUERY_MATERIALES)
            result = connection.execute(query)
            
            # Convierte cada fila en un diccionario usando `mappings()`
            materiales = [dict(row) for row in result.mappings()]
        return materiales

