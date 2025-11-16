#%%
import datetime
from datetime import timedelta, date, datetime
from typing import Tuple, Any

import holidays
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from pandas import DataFrame


def transformarCurrency(dimensionCurrency: DataFrame) -> DataFrame:
    dimensionCurrency.rename(columns={'CurrencyCode' : 'CurrencyKey'}, inplace=True)
    dimensionCurrency["CurrencyKey"] = dimensionCurrency["CurrencyKey"].astype("int")

    dimensionCurrency.rename(columns={'Name' : 'CurrencyName'}, inplace=True)

    dimensionCurrency.drop('ModifiedDate', axis=1, inplace=True)


    dimensionCurrency["CurrencyAlternateKey"]  = None
    dimensionCurrency["CurrencyAlternateKey"] = dimensionCurrency["CurrencyKey"].str[:3]


    dimensionCurrency["saved"] = date.today()
    return dimensionCurrency

def transformarSalesTerritory(dimensionSalesTerritory: DataFrame) -> DataFrame: 
    
    dimensionSalesTerritory.rename(columns={'TerritoryID' : 'SalesTerritoryKey'})
    
    dimensionSalesTerritory["SalesTerritoryAlternateKey"] = None
    dimensionSalesTerritory["SalesTerritoryAlternateKey"] = dimensionSalesTerritory['SalesTerritoryAlternateKey'].astype('int')

    dimensionSalesTerritory["SalesTerritoryRegion"] = None
    dimensionSalesTerritory["SalesTerritoryRegion"] = dimensionSalesTerritory['SalesTerritoryRegion'].str[:50]
    
    dimensionSalesTerritory["SalesTerritoryCountry"] = None
    dimensionSalesTerritory["SalesTerritoryCountry"] = dimensionSalesTerritory['SalesTerritoryCountry'].str[:50]
   
    dimensionSalesTerritory["SalesTerritoryGroup"] = None
    dimensionSalesTerritory["SalesTerritoryGroup"] = dimensionSalesTerritory['SalesTerritoryGroup'].str[:50]
    
    dimensionSalesTerritory["SalesTerritoryImage"] = None
    dimensionSalesTerritory["SalesTerritoryImage"] = dimensionSalesTerritory['SalesTerritoryImage'].astype('object')



    dimensionSalesTerritory.drop(
        columns=[
            'Name',
            'CountryRegionCode',
            '[Group]',
            'SalesYTD',
            'SalesLastYear',
            'CostYTD',
            'CostLastYear',
            'rowguid',
            'ModifiedDate'
        ], inplace=True
        
    )


    dimensionSalesTerritory["saved"] = date.today()

    return dimensionSalesTerritory

def transformarCustomer(dimensionCustomer: DataFrame) -> DataFrame:
    dimensionCustomer.rename(columns={'CustomerID' : 'CustomerKey'}, inplace=True)
    dimensionCustomer["GeographyKey"] = None
    dimensionCustomer["GeographyKey"] = dimensionCustomer["GeographyKey"].astype('int')

    dimensionCustomer.drop(
        columns=[
            'PersonID',
            'StoreID',
            'TerritoryID',
            'AccountNumber',
            'rowguid',
            'ModifiedDate'
        ],inplace=True
    )

    
    dimensionCustomer["CustomerAlternateKey"] = None
    dimensionCustomer["CustomerAlternateKey"] = dimensionCustomer["CustomerAlternateKey"].str[:15]


    dimensionCustomer["Title"] = None
    dimensionCustomer["Title"] = dimensionCustomer["Title"].str[:8]


    dimensionCustomer["FirstName"] = None
    dimensionCustomer["FirstName"] = dimensionCustomer["FirstName"].str[:50]
    
    dimensionCustomer["MiddleName"] = None
    dimensionCustomer["MiddleName"] = dimensionCustomer["MiddleName"].str[:50]

    dimensionCustomer["LastName"] = None
    dimensionCustomer["LastName"] = dimensionCustomer["LastName"].str[:50]
    

    dimensionCustomer["NameStyle"] = None
    dimensionCustomer["NameStyle"] = dimensionCustomer["NameStyle"].astype('boolean')
    
    dimensionCustomer["BirthDate"] = None
    dimensionCustomer["BirthDate"] = dimensionCustomer["BirthDate"].astype('datetime')


    dimensionCustomer["MartialStatus"] = None
    dimensionCustomer["MartialStatus"] = dimensionCustomer["MartialStatus"].astype('category')


    dimensionCustomer["Suffix"] = None
    dimensionCustomer["Suffix"] = dimensionCustomer["Suffix"].str[:10]


    dimensionCustomer["Gender"] = None
    dimensionCustomer["Gender"] = dimensionCustomer["Gender"].str[:1]


    dimensionCustomer["EmailAddress"] = None
    dimensionCustomer["EmailAddress"] = dimensionCustomer["EmailAddress"].str[:50]


    dimensionCustomer["YeralyIncome"] = None
    dimensionCustomer["YeralyIncome"] = dimensionCustomer["YeralyIncome"].astype('float')


    dimensionCustomer["TotalChildrens"] = None
    dimensionCustomer["TotalChildrens"] = dimensionCustomer["TotalChildrens"].astype('uint8')


    dimensionCustomer["NumberChildrenAtHome"] = None
    dimensionCustomer["NumberChildrenAtHome"] = dimensionCustomer["NumberChildrenAtHome"].astype('uint8')


    dimensionCustomer["EnglishEducation"] = None
    dimensionCustomer["EmailAddEnglishEducationress"] = dimensionCustomer["EmailAddreEnglishEducationss"].str[:40]


    dimensionCustomer["SpanishEducation"] = None
    dimensionCustomer["SpanishEducation"] = dimensionCustomer["SpanishEducation"].str[:40]

    dimensionCustomer["FrenchEducation"] = None
    dimensionCustomer["FrenchEducation"] = dimensionCustomer["FrenchEducation"].str[:40]


    dimensionCustomer["EnglishOccupation"] = None
    dimensionCustomer["EnglishOccupation"] = dimensionCustomer["EnglishOccupation"].str[:100]


    dimensionCustomer["SpanishOccupation"] = None
    dimensionCustomer["SpanishOccupation"] = dimensionCustomer["SpanishOccupation"].str[:100]

    dimensionCustomer["FrenchOccupation"] = None
    dimensionCustomer["FrenchOccupation"] = dimensionCustomer["FrenchOccupation"].str[:100]


    dimensionCustomer["HouseOwnerFlag"] = None
    dimensionCustomer["HouseOwnerFlag"] = dimensionCustomer["HouseOwnerFlag"].str[:1]
    
    dimensionCustomer["NumberCarsOwned"] = None
    dimensionCustomer["NumberCarsOwned"] = dimensionCustomer["NumberCarsOwned"].astype('uint8')
    


    dimensionCustomer["AddressLine1"] = None
    dimensionCustomer["AddressLine1"] = dimensionCustomer["AddressLine1"].str[:120]


    dimensionCustomer["AddressLine2"] = None
    dimensionCustomer["AddressLine2"] = dimensionCustomer["AddressLine2"].str[:120]

    dimensionCustomer["Phone"] = None
    dimensionCustomer["Phone"] = dimensionCustomer["Phone"].str[:20]
    
    dimensionCustomer["DateFirstPurchase"] = None
    dimensionCustomer["DateFirstPurchase"] = dimensionCustomer["DateFirstPurchase"].astype('datetime')

    dimensionCustomer["CommuteDistance"] = None
    dimensionCustomer["DateFirstPurchase"] = dimensionCustomer["DateFirstPurchase"].str[:15]
    

    dimensionCustomer["Saved"] = date.today()
    return dimensionCustomer

def transformarDate() -> DataFrame:

    dimensionDate = pd.DataFrame({"date": pd.date_range(start='1/1/2005', end='1/1/2009', freq='D')})
    dimensionDate["DateKey"] = None
    dimensionDate["DateKey"] = dimensionDate["DateKey"].astype('int')
    
    dimensionDate["FullDateAlternateKey"] = None
    dimensionDate["FullDateAlternateKey"] = dimensionDate["FullDateAlternateKey"].astype('datetime')
    
    dimensionDate["DayNumberOfWeek"] = None
    dimensionDate["DayNumberOfWeek"] = dimensionDate["DayNumberOfWeek"].astype('uint8')
    
    dimensionDate["EnglishDayNameOfWeek"] = None
    dimensionDate["EnglishDayNameOfWeek"] = dimensionDate["EnglishDayNameOfWeek"].str[:10]
    
    dimensionDate["SpanishDayNameOfWeek"] = None
    dimensionDate["SpanishDayNameOfWeek"] = dimensionDate["SpanishDayNameOfWeek"].str[:10]
    
    dimensionDate["FrenchDayNameOfWeek"] = None
    dimensionDate["FrenchDayNameOfWeek"] = dimensionDate["FrenchDayNameOfWeek"].str[:10]
    
    dimensionDate["DayNumberOfMonth"] = None
    dimensionDate["DayNumberOfMonth"] = dimensionDate["DayNumberOfMonth"].astype('uint8')
    
    dimensionDate["DayNumberOfYear"] = None
    dimensionDate["DayNumberOfYear"] = dimensionDate["DayNumberOfYear"].astype('uint16')

    dimensionDate["WeekNumberOfYear"] = None
    dimensionDate["WeekNumberOfYear"] = dimensionDate["WeekNumberOfYear"].astype('uint8')

    dimensionDate["EnglishMonthName"] = None
    dimensionDate["EnglishMonthName"] = dimensionDate["EnglishMonthName"].str[:10]
    
    dimensionDate["SpanishMonthName"] = None
    dimensionDate["SpanishMonthName"] = dimensionDate["SpanishMonthName"].str[:10]
    
    dimensionDate["FrenchMonthName"] = None
    dimensionDate["FrenchMonthName"] = dimensionDate["FrenchMonthName"].str[:10]

    dimensionDate["MonthNumberOfYear"] = None
    dimensionDate["MonthNumberOfYear"] = dimensionDate["MonthNumberOfYear"].astype('uint8')

    dimensionDate["CalendarQuarter"] = None
    dimensionDate["CalendarQuarter"] = dimensionDate["CalendarQuarter"].astype('uint8')

    dimensionDate["CalendarYear"] = None
    dimensionDate["CalendarYear"] = dimensionDate["CalendarYear"].astype('uint16')

    dimensionDate["CalendarSemester"] = None
    dimensionDate["CalendarSemester"] = dimensionDate["CalendarSemester"].astype('uint8')

    dimensionDate["FiscalQuarter"] = None
    dimensionDate["FiscalQuarter"] = dimensionDate["FiscalQuarter"].astype('uint8')

    dimensionDate["FiscalYear"] = None
    dimensionDate["FiscalYear"] = dimensionDate["FiscalYear"].astype('uint16')

    dimensionDate["FiscalSemester"] = None
    dimensionDate["FiscalSemester"] = dimensionDate["FiscalSemester"].astype('uint8')

    dimensionDate["saved"] = date.today()
    
    return dimensionDate

def transformarPromotion(dimensionPromotion : DataFrame ) -> DataFrame:
    dimensionPromotion["PromotionKey"] = None
    dimensionPromotion["PromotionKey"] = dimensionPromotion["PromotionKey"].astype('int')
    
    dimensionPromotion["PromotionAlternateKey"] = None
    dimensionPromotion["PromotionAlternateKey"] = dimensionPromotion["PromotionAlternateKey"].astype('int')

    dimensionPromotion["EnlishPromotionName"] = None
    dimensionPromotion["EnlishPromotionName"] = dimensionPromotion["EnlishPromotionName"].str[:255]

    dimensionPromotion["SpanishPromotionName"] = None
    dimensionPromotion["SpanishPromotionName"] = dimensionPromotion["SpanishPromotionName"].str[:255]

    dimensionPromotion["FrenchPromotionName"] = None
    dimensionPromotion["FrenchPromotionName"] = dimensionPromotion["FrenchPromotionName"].str[:255]

    dimensionPromotion["DiscountPct"] = None
    dimensionPromotion["DiscountPct"] = dimensionPromotion["DiscountPct"].astype('float')

    dimensionPromotion["EnglishPromotionType"] = None
    dimensionPromotion["EnglishPromotionType"] = dimensionPromotion["EnglishPromotionType"].str[:50]

    dimensionPromotion["SpanishPromotionType"] = None
    dimensionPromotion["SpanishPromotionType"] = dimensionPromotion["SpanishPromotionType"].str[:50]

    dimensionPromotion["FrenchPromotionType"] = None
    dimensionPromotion["FrenchPromotionType"] = dimensionPromotion["FrenchPromotionType"].str[:50]

    dimensionPromotion["EnglishPromotionCategory"] = None
    dimensionPromotion["EnglishPromotionCategory"] = dimensionPromotion["EnglishPromotionCategory"].str[:50]

    dimensionPromotion["SpanishPromotionCategory"] = None
    dimensionPromotion["SpanishPromotionCategory"] = dimensionPromotion["SpanishPromotionCategory"].str[:50]

    dimensionPromotion["FrenchPromotionCategory"] = None
    dimensionPromotion["FrenchPromotionCategory"] = dimensionPromotion["FrenchPromotionCategory"].str[:50]

    dimensionPromotion["StartDate"] = None
    dimensionPromotion["StartDate"] = dimensionPromotion["StartDate"].astype('datetime')
    
    dimensionPromotion["EndDate"] = None
    dimensionPromotion["EndDate"] = dimensionPromotion["EndDate"].astype('datetime')

    dimensionPromotion["MinQty"] = None
    dimensionPromotion["MinQty"] = dimensionPromotion["MinQty"].astype('uint8')

    dimensionPromotion["MaxQty"] = None
    dimensionPromotion["MaxQty"] = dimensionPromotion["MaxQty"].astype('uint8')


    dimensionPromotion["saved"] = date.today()
    return dimensionPromotion

def transformarProducto(dimensionProduct : DataFrame) -> DataFrame:

    dimensionProduct.rename(columns={'ProducID': 'ProductKey','ProductSubcategoryID': 'ProductSubcategoryKey','SellStartDate': 'StartDate', 'SellEndDate' : 'EndDate', 'Name':'ModelName'}, inplace=True)

    dimensionProduct.drop(
        columns=[
            'ProdutNumber',
            'MakeFlag',
            'ProductModelID',
            'DiscontinuedDate',
            'rowguid',
            'ModifiedDate'            

        ], inplace=True
    )

    dimensionProduct["Size"] =  dimensionProduct["Size"].str[:50]


    dimensionProduct["ProductAlternateKey"] = None
    dimensionProduct["ProductAlternateKey"] = dimensionProduct["ProductAlternateKey"].str[:25]

    dimensionProduct["EnglishProductName"] = None
    dimensionProduct["EnglishProductName"] = dimensionProduct["EnglishProductName"].str[:50]

    dimensionProduct["SpanishProductName"] = None
    dimensionProduct["SpanishProductName"] = dimensionProduct["SpanishProductName"].str[:50]

    dimensionProduct["FrenchProductName"] = None
    dimensionProduct["FrenchProductName"] = dimensionProduct["FrenchProductName"].str[:50]

    dimensionProduct["StandardCost"] = None
    dimensionProduct["StandardCost"] = dimensionProduct["StandardCost"].astype('float')

    dimensionProduct["FinishedGoodsFlag"] = None
    dimensionProduct["FinishedGoodsFlag"] = dimensionProduct["FinishedGoodsFlag"].astype('boolean')

    dimensionProduct["SafetyStockLevel"] = None
    dimensionProduct["SafetyStockLevel"] = dimensionProduct["SafetyStockLevel"].astype('uint16')

    dimensionProduct["ReorderPoint"] = None
    dimensionProduct["ReorderPoint"] = dimensionProduct["ReorderPoint"].astype('uint16')

    dimensionProduct["ListPrice"] = None
    dimensionProduct["ListPrice"] = dimensionProduct["ListPrice"].astype('float')

    dimensionProduct["SizeRange"] = None
    dimensionProduct["SizeRange"] = dimensionProduct["SizeRange"].str[:50]

    dimensionProduct["Weight"] = dimensionProduct["Weight"].astype('float')

    dimensionProduct["DealerPrice"] = None
    dimensionProduct["DealerPrice"] = dimensionProduct["DealerPrice"].astype('float')

    dimensionProduct["LargePhoto"] = None
    dimensionProduct["LargePhoto"] = dimensionProduct["LargePhoto"].astype('object')

    dimensionProduct["EnglishDescription"] = None
    dimensionProduct["EnglishDescription"] = dimensionProduct["EnglishDescription"].str[:400]


    dimensionProduct["FrenchDescription"] = None
    dimensionProduct["FrenchDescription"] = dimensionProduct["FrenchDescription"].str[:400]

    dimensionProduct["ChineseDescription"] = None
    dimensionProduct["ChineseDescription"] = dimensionProduct["ChineseDescription"].str[:400]

    dimensionProduct["ArabicDescription"] = None
    dimensionProduct["ArabicDescription"] = dimensionProduct["ArabicDescription"].str[:400]

    dimensionProduct["HebrewDescription"] = None
    dimensionProduct["HebrewDescription"] = dimensionProduct["HebrewDescription"].str[:400]

    dimensionProduct["ThaiDescription"] = None
    dimensionProduct["ThaiDescription"] = dimensionProduct["ThaiDescription"].str[:400]

    dimensionProduct["GermanDescription"] = None
    dimensionProduct["GermanDescription"] = dimensionProduct["GermanDescription"].str[:400]

    dimensionProduct["JapaneseDescription"] = None
    dimensionProduct["JapaneseDescription"] = dimensionProduct["JapaneseDescription"].str[:400]

    dimensionProduct["TurkishDescription"] = None
    dimensionProduct["TurkishDescription"] = dimensionProduct["TurkishDescription"].str[:400]

    dimensionProduct["Status"] = None
    dimensionProduct["Status"] = dimensionProduct["Status"].str[:7]

    dimensionProduct["saved"] =  date.today()

    return dimensionProduct

def transformarHechoInternetSales(hechoInternetSales : DataFrame) -> DataFrame:

    return hechoInternetSales
