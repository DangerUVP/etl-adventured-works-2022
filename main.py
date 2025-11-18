import pandas as pd
import datetime
from datetime import date
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import Engine
import yaml
#from etl import extract, transform, load
import psycopg2
from etl import extract
from etl import transform
from etl import load


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


# CODIGO PARA CARGAR DATOS A LA BODEGA SI HAY NUEVOS


def runDimensionCurrency():
    print("Inicio de extraccion de datos para Currency")
    dimensionCurrency = extract.extraerDimensionCurrency(motorBaseDatos)
    dimensionCurrencyTransformado = transform.transformarCurrency(dimensionCurrency)
    load.cargarDatosCurrency(dimensionCurrency,motorBodegaDatos)


def runDimensionSalesTerritory():
    print("Inicio de extraccion de datos para SalesTerritory")
    tablaSalesTerritory,tablaCountryRegion = extract.extraerDimensionSalesTerritory(motorBaseDatos)
    dimensionSalesTerritoryTransformado = transform.transformarSalesTerritory(tablaSalesTerritory,tablaCountryRegion)
    load.cargarDatosSalesTerritory(dimensionSalesTerritoryTransformado,motorBodegaDatos)


def runDimensionDate():
    print("Inicio de extraccion de datos para Date")
    dimensionDate = extract.extraerDimensionDate()
    dimensionDateTransformado = transform.transformarDate(dimensionDate)
    load.cargarDatosDate(dimensionDateTransformado,motorBodegaDatos)

def runDimensionPromotion():
    print("Inicio de extraccion de datos para Promotion")
    dimensionPromotion = extract.extraerDimensionPromotion(motorBaseDatos)
    dimensionPromotionTransformado = transform.transformarPromotion(dimensionPromotion)
    load.cargarDatosPromotion(dimensionPromotionTransformado,motorBodegaDatos)

def runDimensionGeography():
    print("Inicio de extraccion de datos para Geography")
    tablaAddress,tablaStateProvince,tablaCountryRegion = extract.extraerDimensionGeography(motorBaseDatos)
    dimensionGeographyTransformado = transform.transformarGeography(tablaAddress,tablaStateProvince,tablaCountryRegion)
    load.cargarDatosGeography(dimensionGeographyTransformado,motorBodegaDatos)

def runDimensionProductCategory():
    print("Inicio de extraccion de datos para ProductCategory")
    dimensionProductCategory= extract.extraerDimensionProductCategory(motorBaseDatos)
    dimensionProductCategoryTransformado = transform.transformarProductCategory(dimensionProductCategory)
    load.cargarDatosProductCategory(dimensionProductCategoryTransformado,motorBodegaDatos)

def runDimensionProductSubCategory():
    print("Inicio de extraccion de datos para ProductSubCategory")
    dimensionProductSubCategory= extract.extraerDimensionProductSubCategory(motorBaseDatos)
    ProductSubCategoryTransformado = transform.transformarProductSubCategory(dimensionProductSubCategory)
    load.cargarDatosProductSubCategory(ProductSubCategoryTransformado,motorBodegaDatos)

def runDimensionCustomer():
    print("Inicio de extraccion de datos para Customer")
    dimensionCustomer= extract.extraerDimensionCustomer(motorBaseDatos)
    dimensionCustomerTransformado = transform.transformarCustomer(dimensionCustomer)
    load.cargarDatosCustomer(dimensionCustomerTransformado,motorBodegaDatos)



def runDimensionProduct():
    print("Inicio de extraccion de datos para Prouct")
    dimensionProduct= extract.extraerDimensionProduct(motorBaseDatos)
    dimensionProductTransformado = transform.transformarProduct(dimensionProduct)
    load.cargarDatosProduct(dimensionProductTransformado,motorBodegaDatos)

def runHechoInternetSales():
    print("Inicio de extraccion de datos para HechoInternetSales")
    hechoInternetSales= extract.extraerDatosHechoInternetSales(motorBaseDatos)
    hechoInternetSalesTransformado = transform.transformarHechoInternetSales(hechoInternetSales)
    load.cargarHechoInternetSales(hechoInternetSalesTransformado,motorBodegaDatos)




# PARA EL DATAMART DE RESELLER SALES 

def runDimensionEmployee():
    print("Inicio de extraccion de datos para Employee")
    dimensionEmployee= extract.extraerDimensionEmployee(motorBaseDatos)
    dimensionEmployeeTransformado = transform.transformarEmployee(dimensionEmployee)
    load.cargarDimensionEmployee(dimensionEmployeeTransformado,motorBodegaDatos)

def runDimensionReseller():
    print("Inicio de extraccion de datos para Reseller")
    dimensionReseller= extract.extraerDimensionReseller(motorBaseDatos)
    dimensionResellerTransformado = transform.transformarReseller(dimensionReseller)
    load.cargarDimensionReseller(dimensionResellerTransformado,motorBodegaDatos)

def runHechoResellerSales():
    print("Inicio de extraccion de datos para ResellerSales")
    dimensionResellerSales= extract.extraerDatosHechoResellerSales(motorBaseDatos,motorBodegaDatos)
    dimensionResellerSalesTransformado = transform.transformarHechoResellerSales(dimensionResellerSales)
    load.cargarHechoResellerSales(dimensionResellerSalesTransformado,motorBodegaDatos)



def main():
    print("Inicio de extraccion de datos")
    runDimensionCurrency()
    runDimensionSalesTerritory()
    runDimensionDate()
    runDimensionPromotion()
    runDimensionGeography()
    runDimensionProductCategory()
    runDimensionProductSubCategory()
    runDimensionCustomer()
    runDimensionProduct()
    runHechoInternetSales()

    # PARA LE DATAMART DE RESELLER SALES
    runDimensionEmployee()
    runDimensionReseller()
    runHechoResellerSales()
    print("Todos los procesos ETL completados con éxito")

if __name__ == "__main__":
    main()