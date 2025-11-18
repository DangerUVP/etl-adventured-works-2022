import pandas as pd
from pandas import DataFrame
from sqlalchemy.engine import Engine
from sqlalchemy import text
import yaml
from sqlalchemy.dialects.postgresql import insert




def cargarDatosCurrency(dimensionCurrency : DataFrame, ConexionBodega: Engine):
    dimensionCurrency.to_sql('dimensionCurrency',ConexionBodega, if_exists='replace',index_label='CurrencyKey')
    print(f"Dimension Currency Cargada")



def cargarDatosSalesTerritory(dimensionSalesTerritory: DataFrame, ConexionBodega: Engine):
    dimensionSalesTerritory.to_sql('dimensionSalesTerritory',ConexionBodega,if_exists='replace',index=False)
    print(f"Dimension SalesTerritory Cargada")




def cargarDatosDate(dimensionDate: DataFrame, ConexionBodega: Engine):
    dimensionDate.to_sql('dimensionDate',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension Date Cargada")
    

def cargarDatosPromotion(dimensionPromotion: DataFrame, ConexionBodega: Engine):
    dimensionPromotion.to_sql('dimensionPromotion',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension Promotion Cargada")


def cargarDatosGeography(dimensionGeography: DataFrame, ConexionBodega: Engine):
    dimensionGeography.to_sql('dimensionGeography',ConexionBodega, if_exists='replace',index_label='GeographyKey')
    print(f"Dimension Geography Cargada")


def cargarDatosProductCategory(dimensionProductCategory: DataFrame, ConexionBodega: Engine):
    dimensionProductCategory.to_sql('dimensionProductCategory',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension ProductCategory Cargada")


def cargarDatosProductSubCategory(dimensionProductSubCategory: DataFrame, ConexionBodega: Engine):
    dimensionProductSubCategory.to_sql('dimensionProductSubCategory',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension ProductSubCategory Cargada")



def cargarDatosCustomer(dimensionCustomer: DataFrame, ConexionBodega: Engine):
    dimensionCustomer.to_sql('dimensionCustomer',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension Customer Cargada")


def cargarDatosProduct(dimensionProuct: DataFrame, ConexionBodega: Engine):
    dimensionProuct.to_sql('dimensionProduct',ConexionBodega, if_exists='replace',index=False)
    print(f"Dimension Product Cargada")




def cargarHechoInternetSales(tablaSales: DataFrame, ConexionBodega: Engine):
    tablaSales.to_sql('hechoInternetSales',ConexionBodega, if_exists='replace',index=False)
    print(f"Hecho Internet Sales Cargado")



# PARA EL DATAMART DE RESELLER SALES


def cargarDimensionEmployee(dimensionEmployee: DataFrame, ConexionBodega: Engine):

    dimensionEmployee.to_sql('dimensionEmployee',ConexionBodega, if_exists='replace',index=False)
    print(f"Hecho Internet Employee Cargado")

def cargarDimensionReseller(dimensionReseller: DataFrame, ConexionBodega: Engine):
    dimensionReseller.to_sql('dimensionReseller',ConexionBodega, if_exists='replace',index_label='ResellerKey')
    print(f"Dimension Reseller Cargado")


def cargarHechoResellerSales(tablaPurchaseSales: DataFrame, ConexionBodega: Engine):
    tablaPurchaseSales.to_sql('hechoResellerSales',ConexionBodega, if_exists='replace',index=False)
    print(f"Hecho Reseller Sales Cargado")











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


















