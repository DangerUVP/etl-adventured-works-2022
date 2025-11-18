#%%
# import datetime
# from datetime import timedelta, date, datetime
# from typing import Tuple, Any

# import holidays
# import numpy as np
# from mlxtend.frequent_patterns import apriori
# from mlxtend.preprocessing import TransactionEncoder
from pandas import DataFrame
import pandas as pd


def transformarCurrency(dimensionCurrency: DataFrame) -> DataFrame:
    
    dimensionCurrency.rename(columns={
    'Name' : 'CurrencyName',
    'CurrencyCode' : 'CurrencyAlternateKey'
    }, inplace=True)


    dimensionCurrency.drop('ModifiedDate', axis=1, inplace=True)

    print(f"Transformacion de dimension Currency Completa")

    return dimensionCurrency


def transformarSalesTerritory(tablaSalesTerritory: DataFrame,tablaCountryRegion: DataFrame) -> DataFrame:
    

    tablaSalesTerritory = tablaSalesTerritory.merge(tablaCountryRegion, on='CountryRegionCode')



    tablaSalesTerritory.rename(columns={
        'TerritoryID'  : 'SalesTerritoryKey',
        'Name_x' : 'SalesTerritoryRegion',
        'Name_y' : 'SalesTerritoryCountry',
        'Group' : 'SalesTerritoryGroup',
    }, inplace=True)

    tablaSalesTerritory["SalesTerritoryAlternateKey"] = tablaSalesTerritory["SalesTerritoryKey"]
    tablaSalesTerritory["SalesTerritoryImage"] = None



    tablaSalesTerritory.drop(columns={
        'CountryRegionCode'
    }, inplace=True)

    print(f"Transformacion de dimension SalesTerritory Completa")


    return tablaSalesTerritory



def transformarDate(df: DataFrame) -> DataFrame:
    
    
        # Clave numérica estilo YYYYMMDD
    df["DateKey"] = df["FullDateAlternateKey"].dt.strftime("%Y%m%d").astype(int)

    # Día de la semana (1=Monday, 7=Sunday según ISO, ajustamos si quieres que 7 sea sábado como tu ejemplo)
    df["DayNumberOfWeek"] = df["FullDateAlternateKey"].dt.dayofweek + 1  # Monday=1 ... Sunday=7

    
    # Nombres de días
    days_en = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    days_es = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    days_fr = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

    df["EnglishDayNameOfWeek"] = df["DayNumberOfWeek"].apply(lambda x: days_en[x-1])
    df["SpanishDayNameOfWeek"] = df["DayNumberOfWeek"].apply(lambda x: days_es[x-1])
    df["FrenchDayNameOfWeek"]  = df["DayNumberOfWeek"].apply(lambda x: days_fr[x-1])

    # Día del mes y del año
    df["DayNumberOfMonth"] = df["FullDateAlternateKey"].dt.day
    df["DayNumberOfYear"]  = df["FullDateAlternateKey"].dt.dayofyear

    # Semana del año
    df["WeekNumberOfYear"] = df["FullDateAlternateKey"].dt.isocalendar().week


    # Meses
    months_en = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    months_es = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    months_fr = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]

    df["MonthNumberOfYear"] = df["FullDateAlternateKey"].dt.month
    df["EnglishMonthName"]  = df["MonthNumberOfYear"].apply(lambda x: months_en[x-1])
    df["SpanishMonthName"]  = df["MonthNumberOfYear"].apply(lambda x: months_es[x-1])
    df["FrenchMonthName"]   = df["MonthNumberOfYear"].apply(lambda x: months_fr[x-1])


    # Trimestres y semestres calendario
    df["CalendarQuarter"]  = df["FullDateAlternateKey"].dt.quarter
    df["CalendarYear"]     = df["FullDateAlternateKey"].dt.year
    df["CalendarSemester"] = ((df["MonthNumberOfYear"]-1)//6)+1


    
    df["FiscalYear"]     = df["FullDateAlternateKey"].apply(lambda d: d.year if d.month>=4 else d.year-1)
    df["FiscalQuarter"]  = ((df["FullDateAlternateKey"].dt.month-4)%12)//3 + 1
    df["FiscalSemester"] = ((df["FiscalQuarter"]-1)//2)+1

    print(f"Transformacion de dimension Date Completa")


    return df


def transformarPromotion(dimensionPromotion: DataFrame) -> DataFrame:
    
    dimensionPromotion.rename(columns={
        'SpecialOfferID': 'PromotionKey',
        'Type' : 'EnglishPromotionType',
        'Category' : 'EnglishPromotionCategory'
    },inplace=True)


    dimensionPromotion["PromotionAlternateKey"] = dimensionPromotion["PromotionKey"]

    dimensionPromotion["EnlishPromotionName"] = None


    dimensionPromotion["SpanishPromotionName"] = None
    dimensionPromotion["FrenchPromotionName"] = None


    dimensionPromotion["SpanishPromotionType"] = None
    dimensionPromotion["FrenchPromotionType"] = None

    dimensionPromotion["SpanishPromotionCategory"] = None
    dimensionPromotion["FrenchPromotionCategory"] = None

    dimensionPromotion.drop(columns=[
        'rowguid',
        'ModifiedDate'
    ] ,inplace=True)

    print(f"Transformacion de dimension Promotion Completa")

    return dimensionPromotion



def transformarGeography(tablaAddress: DataFrame,tablaStateProvince: DataFrame,tablaCountryRegion: DataFrame) -> DataFrame:



    dimensionGeography = tablaAddress.merge(tablaStateProvince, on='StateProvinceID')
    dimensionGeography.rename(columns=
        {
            'Name' : 'StateProvinceName'
        }, inplace=True)

    dimensionGeography.drop(columns=
    {
        'StateProvinceID'
    }, inplace=True)


    dimensionGeography = dimensionGeography.merge(tablaCountryRegion, on='CountryRegionCode')
    dimensionGeography.rename(columns=
    {
        'Name' : 'EnglishCountryRegionName'
    }, inplace=True)

    dimensionGeography["SpanishCountryRegionName"] = None
    dimensionGeography["FrenchCountryRegionName"] = None
    dimensionGeography["IpAddressLocator"] = None

    dimensionGeography.rename(columns=
    {
        'TerritoryID' : 'SalesTerritoryKey'
    }, inplace=True)

    print(f"Transformacion de dimension Currency Completa")

    return dimensionGeography



def transformarProductCategory(dimensionProductCategory: DataFrame) -> DataFrame:

    dimensionProductCategory.rename(columns={
    'ProductCategoryID': 'ProductCategoryKey',
    'Name' : 'EnglishProductCategoryName'
    }, inplace=True)

    dimensionProductCategory["ProductCategoryAlternateKey"] = dimensionProductCategory["ProductCategoryKey"]
    dimensionProductCategory["SpanishProductCategoryName"] = None
    dimensionProductCategory["FrenchProductCategoryName"] = None


    dimensionProductCategory.drop(columns=[
        'rowguid',
        'ModifiedDate',
    ], inplace=True)
    print(f"Transformacion de dimension ProductCategory Completa")

    return dimensionProductCategory



def transformarProductSubCategory(dimensionProductSubCategory: DataFrame) -> DataFrame:

    dimensionProductSubCategory.rename(columns={
        'ProductSubcategoryID': 'ProductSubcategoryKey',
        'Name' : 'EnglishProductSubcategoryName',
        'ProductCategoryID' : 'ProductCategoryKey'

    }, inplace=True)

    dimensionProductSubCategory["ProductSubcategoryAlternateKey"] = dimensionProductSubCategory["ProductSubcategoryKey"]
    dimensionProductSubCategory["SpanishProductCategoryName"] = None
    dimensionProductSubCategory["FrenchProductCategoryName"] = None


    dimensionProductSubCategory.drop(columns=[
        'rowguid',
        'ModifiedDate',
    ], inplace=True)


    print(f"Transformacion de dimension ProductSubCategory Completa")

    return dimensionProductSubCategory


def transformarCustomer(dimensionCustomer: DataFrame) -> DataFrame:


    # AGREGAR LAS COLUMNAS NUEVAS

    dimensionCustomer["EnglishEducation"] = None
    dimensionCustomer["SpanishEducation"] = None
    dimensionCustomer["FrenchEducation"] = None
    dimensionCustomer["EnglishOccupation"] = None
    dimensionCustomer["SpanishOccupation"] = None
    dimensionCustomer["FrenchOccupation"] = None
    dimensionCustomer["YearlyIncome"] = None
    dimensionCustomer["TotalChildren"] = None
    dimensionCustomer["NumberChildrenAtHome"] = None
    dimensionCustomer["HouseOwnerFlag"] = None
    dimensionCustomer["NumberCarsOwned"] = None
    dimensionCustomer["DateFirstPurchase"] = None
    dimensionCustomer["CommuteDistance"] = None

    dimensionCustomer.rename(columns={
    "CustomerID":"CustomerKey",
    "AccountNumber":"CustomerAlternateKey",
    }, inplace=True)

    dimensionCustomer.drop(columns=[
        'BusinessEntityID'
    ], inplace=True)


    print(f"Transformacion de dimension Customer Completa")

    return dimensionCustomer


def transformarProduct(dimensionProducto: DataFrame) -> DataFrame:
    

    # Crear columnas nuevas con None y truncar, cuando tengan data asignada luego será necesario
    for col, length in {
        "SpanishProductName": 50,
        "FrenchProductName": 50,
        "FrenchDescription": 400,
        "ChineseDescription": 400,
        "ArabicDescription": 400,
        "HebrewDescription": 400,
        "ThaiDescription": 400,
        "GermanDescription": 400,
        "JapaneseDescription": 400,
        "TurkishDescription": 400,
        "SizeRange": 50,
        "DealerPrice": 50,
    }.items():
        dimensionProducto[col] = None
        dimensionProducto[col] = dimensionProducto[col].str[:length]

    dimensionProducto.loc[dimensionProducto["SellEndDate"].isnull(), "Status"] = "Current"
    dimensionProducto.loc[dimensionProducto["SellEndDate"].notnull(), "Status"] = None

    dimensionProducto.rename(columns={
        'ProductID' : 'ProductKey',
        'ProductNumber': 'ProductAlternateKey',
        'SellStartDate' : 'StartDate',
        'SellEndDate' : 'EndDate',
        'ProductSubcategoryID' : 'ProductSubcategoryKey'
    }, inplace=True)

    print(f"Transformacion de dimension Product Completa")

    return dimensionProducto




def transformarHechoInternetSales(tablaSales:DataFrame) -> DataFrame:


    tablaSales.rename(columns={
        'TerritoryID': 'SalesTerritoryKey',
        'CustomerID': 'CustomerKey',
        'UnitPriceDiscount': 'UnitPriceDiscountPct',
        'SpecialOfferID': 'PromotionKey',
        'OrderQty': 'OrderQuantity',
        'LineTotal' : 'ExtendedAmount',
        'StandardCost' : 'ProductStandardCost',
        'ProductID' : 'ProductKey'
    }, inplace=True)


    tablaSales["DiscountAmount"] = tablaSales["UnitPrice"] * tablaSales["UnitPriceDiscountPct"] * tablaSales["OrderQuantity"] 

    tablaSales["TotalProductCost"] = tablaSales["ProductStandardCost"] * tablaSales["OrderQuantity"] 

    tablaSales["SalesAmount"] = tablaSales["ExtendedAmount"]

    tablaSales["CustomerPONumber"] = None
    tablaSales["CurrencyKey"] = None
    tablaSales["SalesOrderLineNumber"] = None

    tablaSales["OrderDateKey"] = pd.to_datetime(tablaSales["OrderDate"]).dt.strftime('%Y%m%d')
    tablaSales["DueDateKey"] = pd.to_datetime(tablaSales["DueDate"]).dt.strftime('%Y%m%d')
    tablaSales["ShipDateKey"] = pd.to_datetime(tablaSales["ShipDate"]).dt.strftime('%Y%m%d')

    tablaSales.drop(columns=[
        'SalesOrderID',
        'SalesPersonID',
    ], inplace=True)


    print(f"Transformacion de Hecho Internet Sales Completa")


    return tablaSales







# PARA EL DATAMART DE RESELLER SALES


def transformarEmployee(dimensionEmployee: DataFrame) -> DataFrame:
    

    dimensionEmployee.rename(columns={
        'BusinessEntityID' : 'EmployeeKey',
        'NationalIDNumber' : 'EmployeeNationalIDAlternateKey',
        'PhoneNumber' :'Phone',
        'Rate' : 'BaseRate'
    }, inplace=True)



    dimensionEmployee["ParentEmployeeKey"] = None
    dimensionEmployee["ParentEmployeeNationalIDAlternateKey"] = None
    dimensionEmployee["EmergencyContactName"] = dimensionEmployee["FirstName"] + " "+ dimensionEmployee["LastName"]
    dimensionEmployee["EmergencyContactPhone"] = dimensionEmployee["Phone"]
    dimensionEmployee["EmployeePhoto"] = None
    dimensionEmployee["SalesPersonFlag"] = None

    dimensionEmployee.loc[dimensionEmployee["EndDate"].isnull(), "Status"] = "Current"
    dimensionEmployee.loc[dimensionEmployee["EndDate"].notnull(), "Status"] = None






    print(f"Transformacion de dimension Employee Completa")

    return dimensionEmployee



def transformarReseller(dimensionReseller: DataFrame) -> DataFrame:



    dimensionReseller["OrderFrequency"] = None
    dimensionReseller["OrderMonth"] = None
    dimensionReseller["FirstOrderYear"] = None
    dimensionReseller["LastOrderYear"] = None
    dimensionReseller["MinPaymentType"] = None
    dimensionReseller["MinPaymentAmount"] = None


    # DICCIONARIO PARA ORDER-FRECUENCY
    diccionarioOrderFrecuency = {
        'OS' : 'Q',
        'BM' : 'S',
        'BS' : 'A'
    }

    # DICCIONARIO PARA BUSINESS-TYPE
    diccionarioBusinessType = {
        'OS' : 'Warehouse',
        'BM' : 'Value Added Reseller',
        'BS' : 'Specialty Bike Shop'
    }

    dimensionReseller["OrderFrequency"] = dimensionReseller["BusinessType"].replace(diccionarioOrderFrecuency)
    dimensionReseller["BusinessType"] = dimensionReseller["BusinessType"].replace(diccionarioBusinessType)



    print(f"Transformacion de dimension Reseller Completa")

    return dimensionReseller



def transformarHechoResellerSales(tablaPurchaseSales:DataFrame) -> DataFrame:


    tablaPurchaseSales.rename(columns={
        'StandardCost': 'ProductStandardCost',
        'TerritoryID': 'SalesTerritoryKey',
        'CustomerID': 'CustomerKey',
        'UnitPriceDiscount': 'UnitPriceDiscountPct',
        'SpecialOfferID': 'PromotionKey',
        'OrderQty': 'OrderQuantity',
        'LineTotal' : 'ExtendedAmount',
        'EmployeeID' : 'EmployeeKey',
        'ProductID' : 'ProductKey',
        'DiscountPct' : 'UnitPriceDiscountPct'
    }, inplace=True)

    tablaPurchaseSales["OrderDateKey"] = pd.to_datetime(tablaPurchaseSales["OrderDate"]).dt.strftime('%Y%m%d')
    tablaPurchaseSales["DueDateKey"] = pd.to_datetime(tablaPurchaseSales["DueDate"]).dt.strftime('%Y%m%d')
    tablaPurchaseSales["ShipDateKey"] = pd.to_datetime(tablaPurchaseSales["ShipDate"]).dt.strftime('%Y%m%d')


    tablaPurchaseSales["SalesAmount"] = tablaPurchaseSales["ExtendedAmount"] 
    tablaPurchaseSales["CustomerPONumber"] = None
    tablaPurchaseSales["ResellerKey"] = None
    tablaPurchaseSales["CurrencyKey"] = None
    tablaPurchaseSales["CarrierTrackingNumber"] = None
    tablaPurchaseSales["CustomerPONumber"] = None
    tablaPurchaseSales["SalesOrderLineNumber"] = None
    tablaPurchaseSales["SalesOrderNumber"] = None
    tablaPurchaseSales["SalesTerritoryKey"] = None



    tablaPurchaseSales["DiscountAmount"] = tablaPurchaseSales["UnitPrice"] *  tablaPurchaseSales["UnitPriceDiscountPct"] * tablaPurchaseSales["OrderQuantity"]
    tablaPurchaseSales["TotalProductCost"] = tablaPurchaseSales["ProductStandardCost"] *  tablaPurchaseSales["OrderQuantity"]


    tablaPurchaseSales.drop(columns=[
        'PurchaseOrderDetailID',
        'PurchaseOrderID'
    ], inplace=True)





    print(f"Transformacion de Hecho Reseller Sales Completa")
    return tablaPurchaseSales





