import pandas as pd
from sqlalchemy.engine import Engine





def extract(tables : list,conection: Engine)-> pd.DataFrame:
    """
    :param conection: the conectionnection to the database
    :param tables: the tables to extract
    :return: a list of tables in df format
    """
    a = []
    for i in tables:
        aux = pd.read_sql_table(i, conection)
        a.append(aux)
    return a

def extraerDimensionCurrency(conexion: Engine):
    dimensionCurrency = pd.read_sql_table("Currency",conexion)
    return dimensionCurrency

def extraerDimensionSalesTerritory(conexion: Engine):
    dimensionSalesTerritory = pd.read_sql_table("SalesTerritory",conexion)
    return dimensionSalesTerritory


def extraerDimensionDate(conexion: Engine):
    dimensionDate = pd.read_sql_table("Date",conexion)
    return dimensionDate


def extraerDimensionCustomer(conexion: Engine):
    dimensionCustomer = pd.read_sql_table("Customer",conexion)
    return dimensionCustomer

def extraerDimensionProduct(conexion: Engine):
    dimensionProduct = pd.read_sql_table("Product",conexion)
    return dimensionProduct

def extraerDimensionPromotion(conexion: Engine):
    dimensionPromotion = pd.read_sql_table("Promotion",conexion)
    return dimensionPromotion
