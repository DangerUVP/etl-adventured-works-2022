import pandas as pd
from pandas import DataFrame
from sqlalchemy.engine import Engine
from sqlalchemy import text
import yaml
from sqlalchemy.dialects.postgresql import insert




def cargarDatosCurrency(dimensionCurrency : DataFrame, conexionEtl: Engine):
    dimensionCurrency.to_sql('dimensionCurrency',conexionEtl, if_exists='append',index_label='CurrencyKey')


def cargarDatosSalesTerritory(dimensionSalesTerritory: DataFrame, conexionEtl: Engine):
    dimensionSalesTerritory.to_sql('dimensionSalesTerritory',conexionEtl,if_exists='append',index_label='SalesTerritoryKey')


def cargarDatosCustomer(dimensionCustomer: DataFrame, conexionEtl: Engine):
    dimensionCustomer.to_sql('dimensionCustomer',conexionEtl,if_exists='append',index_label='CustomerKey')


def cargarDatosDate(dimensionDate: DataFrame, conexionEtl: Engine):
    dimensionDate.to_sql('dimensionDate',conexionEtl,if_exists='append',index_label='DateKey')


def cargarDatosProduct(dimensionProuct: DataFrame, conexionEtl: Engine):
    dimensionProuct.to_sql('dimensionProdut',conexionEtl,if_exists='append',index_label='ProductKey')


def cargarDatosPromotion(dimensionPromotion: DataFrame, conexionEtl: Engine):
    dimensionPromotion.to_sql('dimensionPromotion',conexionEtl, if_exists='append',index_label='PromotionKey')

def cargarHechoInternetSales(hechoInternetSales: DataFrame, conexionEtl: Engine):
    hechoInternetSales.to_sql('hechoInternetSales',conexionEtl, if_exists='append', index=False)




def load(table: DataFrame, etl_conn: Engine, tname, replace: bool = False):
    """

    :param table: table to load into the database
    :param etl_conn: sqlalchemy engine to connect to the database
    :param tname: table name to load into the database
    :param replace:  when true it deletes existing table data(rows)
    :return: void it just load the table to the database
    """
    # statement = insert(f'{table})
    # with etl_conn.connect() as conn:
    #     conn.execute(statement)
    if replace :
        with etl_conn.connect() as conn:
            conn.execute(text(f'Delete from {tname}'))
            conn.close()
        table.to_sql(f'{tname}', etl_conn, if_exists='append', index=False)
    else :
        table.to_sql(f'{tname}', etl_conn, if_exists='append', index=False)
