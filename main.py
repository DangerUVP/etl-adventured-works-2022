import pandas as pd
import datetime
from datetime import date
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine
import yaml
#from etl import extract, transform, load
import psycopg2


# PARA DEFINIR EL MAXIMO DE REGISTROS EN FILAS Y COLUMNAS
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)


#ABRIR ARCHIVO DE CONFIGURACION DE CONEXION A BASES DE DATOS
with open('configuracion.yml', 'r') as f:
    configuracion = yaml.safe_load(f)
    configuracionBaseDatos= configuracion['ADVENTURE_WORKS_DB']
    configuracionBodegaDatos= configuracion['ADVENTURE_WORKS_DW']

# CREAR LAS URLs DE CONEXION

from sqlalchemy.engine import URL

urlBaseDatos = URL.create(
    "mssql+pyodbc",
    username=configuracionBaseDatos['user'],
    password=str(configuracionBaseDatos['password']),
    host=configuracionBaseDatos['host'],
    port=configuracionBaseDatos['port'],
    database=configuracionBaseDatos['dbname'],
    query={"driver": "ODBC Driver 17 for SQL Server"}
)

urlBodegaDatos = URL.create(
    "mssql+pyodbc",
    username=configuracionBodegaDatos['user'],
    password=str(configuracionBodegaDatos['password']),
    host=configuracionBodegaDatos['host'],
    port=configuracionBodegaDatos['port'],
    database=configuracionBodegaDatos['dbname'],
    query={"driver": "ODBC Driver 17 for SQL Server"}
)



# CREAR EL MOTOR DE SQLALCHEMY
motorBaseDatos = create_engine(urlBaseDatos)
motorBodegaDatos = create_engine(urlBodegaDatos)

inspector = inspect(motorBodegaDatos)
nombreTablas = inspector.get_table_names()



# if not nombreTablas:
#     conexion = psycopg2.connect(dbname=configuracionBodegaDatos['dbname'], user=configuracionBodegaDatos['user'], password=configuracionBodegaDatos['password'],
#                             host=configuracionBodegaDatos['host'], port=configuracionBodegaDatos['port'])
#     cursor = conexion.cursor()
#     with open('sqlscripts.yml', 'r') as f: #EL ARCHIVO 'sqlscripts.yml' TIENE EL SCRIPT PARA CREAR LAS DIMENIONES Y LOS HECHOS(BODEGA)
#         sql = yaml.safe_load(f)
#         for key, val in sql.items():
#             cursor.execute(val)
#             conexion.commit()


# CODIGO PARA CARGAR DATOS A LA BODEGA SI HAY NUEVOS
# if utils_etl.new_data(motorBodegaDatos):

#     if configuracion['CARGAR_DIMENSIONES']:
#         dim_ips = extract.extract_ips(co_sa)
#         dim_persona = extract.extract_persona(co_sa)
#         dim_medico = extract.extract_medico(co_sa)
#         trans_servicio = extract.extract_trans_servicio(co_sa)
#         dim_demo = extract.extract_demografia(co_sa)
#         dim_diag = extract.extract_enfermedades(co_sa)
#         dim_drug = extract.extract_medicamentos(config['medicamentos'])
#         dim_servicio = extract.extract_servicios(co_sa)


#         # transform
#         dim_ips = transform.transform_ips(dim_ips)
#         dim_persona = transform.transform_persona(dim_persona)
#         dim_medico = transform.transform_medico(dim_medico)
#         trans_servicio = transform.transform_trans_servicio(trans_servicio)
#         dim_fecha = transform.transform_fecha()
#         dim_demo = transform.transform_demografia(dim_demo)
#         dim_diag = transform.transform_enfermedades(dim_diag)



#         load.load(dim_ips, etl_conn, 'dim_ips', True)
#         load.load(dim_fecha, etl_conn, 'dim_fecha', True)
#         load.load(dim_servicio, etl_conn, 'dim_servicio', True)
#         load.load(dim_persona, etl_conn, 'dim_persona', True)
#         load.load(dim_medico, etl_conn, 'dim_medico', True)
#         load.load(trans_servicio, etl_conn, 'trans_servicio', True)
#         load.load(dim_diag, etl_conn, 'dim_diag', True)
#         load.load(dim_demo, etl_conn, 'dim_demografia', True)
#         load.load(dim_drug,etl_conn,'dim_medicamentos',True)


#     #hecho Atencion
#     hecho_atencion = extract.extract_hecho_atencion(etl_conn)
#     hecho_atencion = transform.transform_hecho_atencion(hecho_atencion)
#     load.load_hecho_atencion(hecho_atencion, etl_conn)
#     print('Done atencion fact')
#     # Hecho Entrega medicamentos
#     hecho_entrega = extract.extract_hecho_entrega(co_sa,etl_conn)
#     hecho_entrega, masrecetados = transform.transform_hecho_entrega(hecho_entrega)
#     load.load_hecho_entrega(hecho_entrega, etl_conn)
#     print('Done entrega fact')
#     # medicamentos que mas se recetan juntos
#     masrecetados = masrecetados.astype('string')
#     load.load(masrecetados,etl_conn, 'mas_recetados', False)
#     # Hecho retrios
#     hecho_retiros = extract.extract_retiros(co_sa,etl_conn)
#     hecho_retiros = transform.transform_hecho_retiros(hecho_retiros,1)
#     load.load(hecho_retiros, etl_conn, 'hecho_retiros', False)
#     print('Done retiros fact')

#     print('success all facts loaded')
# else:
#     print('done not new data')
