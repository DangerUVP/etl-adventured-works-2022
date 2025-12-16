import pandas as pd
from sqlalchemy.engine import Engine



def extraerDimensionCurrency(conexion: Engine):
    dimensionCurrency = pd.read_sql_table("Currency", conexion, "Sales")
    print(f"Datos para dimension Currency Extraidos")

    return dimensionCurrency

def extraerDimensionSalesTerritory(conexion: Engine):

    querySalesTerritory = """
    SELECT 
    [TerritoryID]
        ,[Name]
        ,[CountryRegionCode]
        ,[Group]
    FROM Sales.SalesTerritory
    """

    tablaSalesTerritory = pd.read_sql_query(querySalesTerritory, conexion)


    queryCountryRegion = """
    SELECT 
    [CountryRegionCode]
        ,[Name]
    FROM Person.CountryRegion
    """
    tablaCountryRegion = pd.read_sql_query(queryCountryRegion, conexion)
    print(f"Datos para dimension SalesTerritory Extraidos")


    return tablaSalesTerritory,tablaCountryRegion

def extraerDimensionDate():
    dates = pd.date_range(start="2005-01-01", end="2010-12-31", freq="D")

    df = pd.DataFrame({"FullDateAlternateKey": dates})
    print(f"Datos para dimension Date Extraidos")

    return df

def extraerDimensionPromotion(conexion: Engine):
    dimensionPromotion = pd.read_sql_table("SpecialOffer", conexion, "Sales")
    print(f"Datos para dimension Promotion Extraidos")

    return dimensionPromotion

def extraerDimensionGeography(conexion: Engine):

    
    queryAddress="""
    SELECT 
        [City], 
        [StateProvinceID], 
        [PostalCode]
    FROM Person.Address
    """
    tablaAddress = pd.read_sql_query(queryAddress, conexion)


    queryStateProvince= """
    SELECT 
        [StateProvinceID],
        [StateProvinceCode],
        [CountryRegionCode],
        [Name],
        [TerritoryID]
    FROM Person.StateProvince
    """
    tablaStateProvince = pd.read_sql_query(queryStateProvince, conexion)

    queryCountryRegion= """
    SELECT 
    [CountryRegionCode]
        ,[Name]
    FROM Person.CountryRegion
    """
    tablaCountryRegion = pd.read_sql_query(queryCountryRegion, conexion)

    return tablaAddress,tablaStateProvince,tablaCountryRegion

def extraerDimensionProductCategory(conexion: Engine):
    dimensionProductCategory = pd.read_sql_table("ProductCategory", conexion, "Production")
    print(f"Datos para dimension ProductCategory Extraidos")
    return dimensionProductCategory

def extraerDimensionProductSubCategory(conexion: Engine):
    dimensionSubProductCategory = pd.read_sql_table("ProductSubcategory", conexion, "Production")
    print(f"Datos para dimension ProductSubCategory Extraidos")
    return dimensionSubProductCategory

def extraerDimensionCustomer(conexion: Engine):
    
    queryPerson = """
    SELECT 
    [BusinessEntityID],
    [NameStyle],
    [Title],
    [FirstName],
    [MiddleName],
    [LastName],
    [Suffix]
    FROM Person.Person
    """
    tablaPerson = pd.read_sql_query(queryPerson, conexion)

    queryPersonPhone = """
    SELECT 
    [BusinessEntityID],
    [PhoneNumber]
    FROM Person.PersonPhone
    """
    tablaPersonPhone = pd.read_sql_query(queryPersonPhone, conexion)

    queryEmailAddress = """
    SELECT 
    [BusinessEntityID],
    [EmailAddress]
    FROM Person.EmailAddress
    """
    tablaEmailAddress = pd.read_sql_query(queryEmailAddress, conexion)

    query = """
    SELECT 
    [AddressID],
    [AddressLine1],
    [AddressLine2],
    [StateProvinceID]
    FROM Person.Address
    """
    tablaAddress = pd.read_sql_query(query, conexion)

    queryBusinessEntityAddress = """
    SELECT 
    [BusinessEntityID],
    [AddressID]
    FROM Person.BusinessEntityAddress
    """
    tablaBusinessEntityAddress = pd.read_sql_query(queryBusinessEntityAddress, conexion)

    queryStateProvince = """
    SELECT 
    [StateProvinceID]
        ,[StateProvinceCode]
    FROM Person.StateProvince
    """
    tablaStateProvince = pd.read_sql_query(queryStateProvince, conexion)


    queryEmployee = """
    SELECT 
    [BusinessEntityID],
    [BirthDate],
    [MaritalStatus],
    [Gender]
    FROM HumanResources.Employee
    """
    tablaEmployee = pd.read_sql_query(queryEmployee, conexion)

    
    queryCustomer = """
    SELECT 
    [CustomerID],
    [AccountNumber]
    FROM Sales.Customer
    """
    tablaCustomer = pd.read_sql_query(queryCustomer, conexion)




    customer = tablaBusinessEntityAddress.merge(tablaCustomer, left_on='BusinessEntityID', right_on='CustomerID')

    customer.drop(columns=[
        'AccountNumber',
        'CustomerID'
    ],inplace=True)

    customer = customer.merge(tablaAddress, on='AddressID')
    customer = customer.merge(tablaStateProvince, on='StateProvinceID')

    dimensionCustomer = tablaCustomer.merge(tablaPerson, left_on='CustomerID', right_on='BusinessEntityID')
    dimensionCustomer = dimensionCustomer.merge(tablaEmployee, on='BusinessEntityID')

    dimensionCustomer = dimensionCustomer.merge(tablaPersonPhone, on='BusinessEntityID')
    dimensionCustomer = dimensionCustomer.merge(tablaEmailAddress, on='BusinessEntityID')
    dimensionCustomer = dimensionCustomer.merge(customer, on='BusinessEntityID')


    print(f"Datos para dimension Customer Extraidos")

    return dimensionCustomer

def extraerDimensionProduct(conexion: Engine):


    
    queryProduct = """
    SELECT 
        [ProductID],
        [Name],
        [ProductNumber],
        [WeightUnitMeasureCode]
        ,[FinishedGoodsFlag]
        ,[Color]
        ,[SafetyStockLevel]
        ,[ReorderPoint]
        ,[StandardCost]
        ,[ListPrice]
        ,[Size]
        ,[Weight]
        ,[DaysToManufacture]
        ,[ProductLine]
        ,[Class]
        ,[Style]
        ,[ProductSubcategoryID]
        ,[ProductModelID]
        ,[SellStartDate]
        ,[SellEndDate]
    FROM Production.Product
    """

    dimensionProducto = pd.read_sql_query(queryProduct, conexion)



    queryProductModel = """
    SELECT 
    [ProductModelID],
    [Name]
    FROM Production.ProductModel
    """

    tablaProductModel = pd.read_sql_query(queryProductModel, conexion)



    queryProductPhoto = """
    SELECT 
        [ProductPhotoID],
        [LargePhoto]
    FROM Production.ProductPhoto
    """
    tablaProductPhoto = pd.read_sql_query(queryProductPhoto, conexion)



    queryProductDescription = """
    SELECT 
    [ProductDescriptionID]
        ,[Description]
    FROM Production.ProductDescription
    """
    tablaProductDescription = pd.read_sql_query(queryProductDescription, conexion)

    queryProductModelProductDescriptionCulture = """
    SELECT 
    [ProductModelID]
        ,[ProductDescriptionID]
    FROM Production.ProductModelProductDescriptionCulture
    """
    tablaProductModelProductDescriptionCulture = pd.read_sql_query(queryProductModelProductDescriptionCulture, conexion)



    queryProductProductPhoto = """
    SELECT 
        [ProductID]
        ,[ProductPhotoID]
    FROM Production.ProductProductPhoto
    """
    tablaProductProductPhoto = pd.read_sql_query(queryProductProductPhoto, conexion)

    description = tablaProductModelProductDescriptionCulture.merge(tablaProductDescription, on='ProductDescriptionID')
    
    productPhoto = tablaProductProductPhoto.merge(tablaProductPhoto, on='ProductPhotoID')
    productPhoto.drop(columns=[
        'ProductPhotoID'
    ], inplace=True)


    dimensionProducto = dimensionProducto.merge(productPhoto, on='ProductID')


    dimensionProducto.rename(columns={
        'Name' : ' EnglishProductName',
    }, inplace=True)


    dimensionProducto = dimensionProducto.merge(description, on='ProductModelID')


    dimensionProducto.rename(columns={
        'Description' : 'EnglishDescription',
    }, inplace=True)


    dimensionProducto.drop(columns={
        'ProductDescriptionID'
    }, inplace=True)

    dimensionProducto = dimensionProducto.merge(tablaProductModel, on='ProductModelID', how='left')
    dimensionProducto.rename(columns={
        'Name' : 'ModelName',
    }, inplace=True)

    print(f"Datos para dimension Product Extraidos")

    return dimensionProducto

def extraerDatosHechoInternetSales(conexion: Engine):
    # Consulta SalesOrderDetail
    queryOrderDetail = """
        SELECT 
            [SalesOrderID],
            [SalesOrderDetailID],
            [CarrierTrackingNumber],
            [OrderQty],
            [ProductID],
            [SpecialOfferID],
            [UnitPrice],
            [UnitPriceDiscount],
            [LineTotal]
        FROM Sales.SalesOrderDetail
    """
    
    tablaResultadoOrderDetail = pd.read_sql_query(queryOrderDetail, conexion)
    
    # Consulta SalesOrderHeader
    queryOrderHeader = """
        SELECT 
            [SalesOrderID],
            [RevisionNumber],
            [OrderDate],
            [DueDate],
            [ShipDate],
            [SalesOrderNumber],
            [CustomerID],
            [SalesPersonID],
            [TerritoryID],
            [TaxAmt],
            [Freight],
            [OnlineOrderFlag]
        FROM Sales.SalesOrderHeader
    """
    
    tablaResultadoOrderHeader = pd.read_sql_query(queryOrderHeader, conexion)
    
    # Consulta Product
    queryProduct = """
        SELECT 
            [ProductID],
            [StandardCost]
        FROM Production.Product
    """
    
    tablaProduct = pd.read_sql_query(queryProduct, conexion)
    
    tablaCombinada = pd.merge(
        tablaResultadoOrderDetail,
        tablaResultadoOrderHeader,
        on='SalesOrderID',
        how='inner'
    )

    # Condición Internet Sales: onlineflag debe ser 1
    flag = tablaCombinada['OnlineOrderFlag'] == 1

    # Aplicar ambas condiciones (A AND B) usando el operador '&'
    tablaResultado = tablaCombinada[
        flag
    ]


    tablaResultado = tablaResultado.merge(tablaProduct, on='ProductID')




    print("Datos para Hecho Internet Sales Extraídos")
    
    return tablaResultado



# PARA EL DATAMART DE RESELLER SALES
def extraerDimensionEmployee(conexion: Engine):

    queryEmployee = """
    SELECT 
    [BusinessEntityID]
        ,[NationalIDNumber]
        ,[LoginID]
        ,[BirthDate]
        ,[MaritalStatus]
        ,[Gender]
        ,[HireDate]
        ,[SalariedFlag]
        ,[VacationHours]
        ,[SickLeaveHours]
        ,[CurrentFlag]
    FROM HumanResources.Employee
    """

    tablaEmployee = pd.read_sql_query(queryEmployee, conexion)



    queryEmployeePayHistory = """
    SELECT 
    [BusinessEntityID]
        ,[Rate]
        ,[PayFrequency]
    FROM HumanResources.EmployeePayHistory
    """
    tablaEmployeePayHistory = pd.read_sql_query(queryEmployeePayHistory, conexion)



    queryEmployeeDepartmentHistory = """
    SELECT 
    [BusinessEntityID]
        ,[DepartmentID]
        ,[StartDate]
        ,[EndDate]
    FROM HumanResources.EmployeeDepartmentHistory
    """
    tablaEmployeeDepartmentHistory = pd.read_sql_query(queryEmployeeDepartmentHistory, conexion)

    queryDepartment = """
    SELECT 
    [DepartmentID]
        ,[Name]
    FROM HumanResources.Department
    """
    tablaDeparment = pd.read_sql_query(queryDepartment, conexion)




    queryPerson = """
    SELECT 
        [BusinessEntityID],
        [NameStyle],
        [Title],
        [FirstName],
        [MiddleName],
        [LastName]
    FROM Person.Person
    """
    tablaPerson = pd.read_sql_query(queryPerson, conexion)


    queryPersonPhone = """
    SELECT 
    [BusinessEntityID]
        ,[PhoneNumber]
    FROM Person.PersonPhone
    """
    tablaPersonPhone = pd.read_sql_query(queryPersonPhone, conexion)


    queryEmailAddress = """
    SELECT 
    [BusinessEntityID]
        ,[EmailAddress]
    FROM Person.EmailAddress
    """
    tablaEmailAddress = pd.read_sql_query(queryEmailAddress, conexion)



    queryAddress = """
    SELECT 
    [AddressID]
        ,[StateProvinceID]
    FROM Person.Address
    """
    tablaAddress = pd.read_sql_query(queryAddress, conexion)


    queryBusinessEntityAddress = """
    SELECT 
    [BusinessEntityID]
        ,[AddressID]
    FROM Person.BusinessEntityAddress
    """
    tablaBusinessEntityAddress = pd.read_sql_query(queryBusinessEntityAddress, conexion)



    queryStateProvince = """
    SELECT 
    [StateProvinceID]
        ,[TerritoryID]
    FROM Person.StateProvince
    """
    tablaStateProvince = pd.read_sql_query(queryStateProvince, conexion)



    # PARA OBTENER EL NOMBRE DEL DEPARTAMENTO DE LA PERSONAS

    # SE UNE LA TABLA EmployeeDepartmentHistory CON LA TABLA Department PARA UNIR StartDate,EndDate,Name(Nombre del departamento)
    department = tablaEmployeeDepartmentHistory.merge(tablaDeparment, on='DepartmentID')


    department.rename(columns={
        'Name' :'DepartmentName'
    }, inplace=True)


    # LA COLUMNA DepartmentID  YA NO ES NECESARIA
    department.drop(columns=[
        'DepartmentID'
    ], inplace=True)



    # PARA OBTENER EL TERRITORY-ID DE LA PERSONAS

    # SE UNE LA TABLA BusinessEntityAddress CON LA TABLA Address PARA RELACIONAR EL AddresID CON LA PERSONA
    address = tablaBusinessEntityAddress.merge(tablaAddress, on='AddressID')

    # LA COLUMNA AddressID  YA NO ES NECESARIA
    address.drop(columns=[
        'AddressID'
    ], inplace=True)



    # SE UNE LA NUEVA TABLA address CON COLUMNAS (BusinessEntityID,StateProvinceID) CON LA TABLA StateProvince PARA RELACIONAR EL TerritoryID CON LA PERSONA
    address = address.merge(tablaStateProvince, on='StateProvinceID')


    address.rename(columns={
        'TerritoryID' : 'SalesTerritoryKey'
    }, inplace=True)


    # LA COLUMNA StateProvinceID  YA NO ES NECESARIA
    address.drop(columns=[
        'StateProvinceID'
    ], inplace=True)


    dimensionEmployee = tablaEmployee.merge(tablaPerson, on='BusinessEntityID')
    dimensionEmployee = dimensionEmployee.merge(tablaPersonPhone, on='BusinessEntityID')
    dimensionEmployee = dimensionEmployee.merge(tablaEmailAddress, on='BusinessEntityID')
    dimensionEmployee = dimensionEmployee.merge(tablaEmployeePayHistory, on='BusinessEntityID')
    dimensionEmployee = dimensionEmployee.merge(department, on='BusinessEntityID')
    dimensionEmployee = dimensionEmployee.merge(address, on='BusinessEntityID')


    print(f"Datos para dimension Employee Extraidos")
    return dimensionEmployee

def extraerDimensionReseller(conexion: Engine):

    # PARA MANEJO DE ARCHIVOS XML
    import xml.etree.ElementTree as ET
    queryStore = """
    SELECT
        [Name],
        [BusinessEntityID],
        [SalesPersonID],
        [Demographics]
    FROM Sales.Store
    """

    tablaStore = pd.read_sql_query(queryStore, conexion)


    queryPersonPhone = """
    SELECT 
    [BusinessEntityID]
        ,[PhoneNumber]
    FROM Person.PersonPhone
    """
    tablaPersonPhone = pd.read_sql_query(queryPersonPhone, conexion)

    queryPersonAddress = """
    SELECT 
    [AddressID]
        ,[AddressLine1]
        ,[AddressLine2]
    FROM Person.Address
    """
    tablaPersonAddress = pd.read_sql_query(queryPersonAddress, conexion)




    queryPersonBusinessEntityAddress = """
    SELECT 
    [BusinessEntityID]
        ,[AddressID]
    FROM Person.BusinessEntityAddress
    """
    tablaBusinessEntityAddress = pd.read_sql_query(queryPersonBusinessEntityAddress, conexion)





    queryCustomer = """
    SELECT 
        [StoreID],
        [AccountNumber],
        [TerritoryID]
    FROM Sales.Customer
    """
    tablaCustomer = pd.read_sql_query(queryCustomer, conexion)




    # Namespace del XML
    NS = {'ns': 'http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey'}

    def parse_store_survey(xml_str):
        root = ET.fromstring(xml_str)
        # Extraer cada campo del XML usando el namespace
        return {
            'AnnualSales': root.find('ns:AnnualSales', NS).text if root.find('ns:AnnualSales', NS) is not None else None,
            'AnnualRevenue': root.find('ns:AnnualRevenue', NS).text if root.find('ns:AnnualRevenue', NS) is not None else None,
            'BankName': root.find('ns:BankName', NS).text if root.find('ns:BankName', NS) is not None else None,
            'BusinessType': root.find('ns:BusinessType', NS).text if root.find('ns:BusinessType', NS) is not None else None,
            'YearOpened': root.find('ns:YearOpened', NS).text if root.find('ns:YearOpened', NS) is not None else None,
            'Specialty': root.find('ns:Specialty', NS).text if root.find('ns:Specialty', NS) is not None else None,
            'SquareFeet': root.find('ns:SquareFeet', NS).text if root.find('ns:SquareFeet', NS) is not None else None,
            'Brands': root.find('ns:Brands', NS).text if root.find('ns:Brands', NS) is not None else None,
            'Internet': root.find('ns:Internet', NS).text if root.find('ns:Internet', NS) is not None else None,
            'NumberEmployees': root.find('ns:NumberEmployees', NS).text if root.find('ns:NumberEmployees', NS) is not None else None,
        }

    # Supón que df es tu DataFrame y la columna se llama 'Demographics'
    # Aplica la función para crear un DataFrame expandido con esos campos
    df_expanded = tablaStore['Demographics'].apply(parse_store_survey).apply(pd.Series)

    # Combinar con el DataFrame original si lo deseas
    store = pd.concat([tablaStore, df_expanded], axis=1)

    dimensionReseller = store


    dimensionReseller.rename(columns={
        'Name' : 'ResellerName',
        'Specialty' : 'ProductLine',
        'BusinessEntityID': 'StoreID'
    }, inplace=True)

    dimensionReseller =  dimensionReseller.merge(tablaCustomer, on='StoreID')

    dimensionReseller = dimensionReseller.merge(tablaPersonPhone, left_on='SalesPersonID', right_on='BusinessEntityID') 

    dimensionReseller.drop(columns=[
        'BusinessEntityID',
        'Demographics',
    ], inplace=True)



    dimensionReseller.drop(columns=[
        'SquareFeet',
        'Brands',
        'Internet',
    ], inplace=True)



    address = tablaBusinessEntityAddress.merge(tablaPersonAddress, on='AddressID')

    address.drop(columns=[
        'AddressID',
    ], inplace=True)

    dimensionReseller = dimensionReseller.merge(address, left_on='SalesPersonID', right_on='BusinessEntityID')

    dimensionReseller.drop(columns=[
        'BusinessEntityID'
    ], inplace=True)


    print(f"Datos para dimension Reseller Extraidos")
    return dimensionReseller

def extraerDatosHechoResellerSales(conexion: Engine,conexionDW: Engine,):
    queryOderDetail = """
        SELECT 
        [SalesOrderID]
            ,[SalesOrderDetailID]
            ,[CarrierTrackingNumber]
            ,[OrderQty]
            ,[ProductID]
            ,[SpecialOfferID]
            ,[UnitPrice]
            ,[UnitPriceDiscount]
            ,[LineTotal]
        FROM Sales.SalesOrderDetail
    """

    tablaResultadoOrderDetail = pd.read_sql_query(queryOderDetail, conexion)


    queryOderHeader = """
        SELECT 
        [SalesOrderID]
            ,[RevisionNumber]
            ,[OrderDate]
            ,[DueDate]
            ,[ShipDate]
            ,[SalesOrderNumber]
            ,[CustomerID]
            ,[SalesPersonID]
            ,[TerritoryID]
            ,[TaxAmt]
            ,[Freight]
            ,[OnlineOrderFlag]
        FROM Sales.SalesOrderHeader
    """

    tablaResultadoOrderHeader = pd.read_sql_query(queryOderHeader, conexion)


    queryProduct = """
            SELECT 
                [ProductID]
                ,[StandardCost]
            FROM Production.Product
    """

    tablaProduct = pd.read_sql_query(queryProduct, conexion)


    tablaCombinada = pd.merge(
        tablaResultadoOrderDetail,
        tablaResultadoOrderHeader,
        on='SalesOrderID',
        how='inner'
    )

    # Condición reseller salies : onlineflag debe ser 0
    flag = tablaCombinada['OnlineOrderFlag'] == 0

    tablaResultado = tablaCombinada[
        flag
    ]


    tablaResultado = tablaResultado.merge(tablaProduct, on='ProductID')


    print(f"Datos para Hecho Reseller Sales Extraidos")
    return tablaResultado
