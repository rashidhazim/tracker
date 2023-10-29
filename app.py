import streamlit as st
import pandas as pd
import pyodbc

st.title('Discrepancy Tracker')

# Database connection parameters
server = 'INA.MCKESSON.COM'
database = 'INA'
username = 'INA_TEAM'
password = 'ISMCAccount'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# Create a function to load data from SQL Server
def load_data():
    query = """
    SELECT * 
    FROM OPENQUERY(SNOW_SBX, 
                   'SELECT CAST(NATL_GRP_NAM AS VARCHAR(50)) AS NATL_GRP_NAM, 
                           CAST(INA_LOC_ID AS VARCHAR(50)) AS INA_LOC_ID, 
                           CAST(SHIP_TO_GLN AS VARCHAR(50)) AS SHIP_TO_GLN, 
                           CAST(CUST_ACCT_ID AS VARCHAR(50)) AS CUST_ACCT_ID, 
                           CAST(CUST_ACCT_NAM AS VARCHAR(50)) AS CUST_ACCT_NAM, 
                           CAST(ACCT_DLVRY_ADDR AS VARCHAR(50)) AS ACCT_DLVRY_ADDR, 
                           CAST(ACCT_DLVRY_CTY_NAM AS VARCHAR(50)) AS ACCT_DLVRY_CTY_NAM, 
                           CAST(ACCT_DLVRY_ST_ABRV AS VARCHAR(50)) AS ACCT_DLVRY_ST_ABRV, 
                           CAST(ACCT_DLVRY_ZIP AS VARCHAR(50)) AS ACCT_DLVRY_ZIP, 
                           CAST(DEA_NUM AS VARCHAR(50)) AS DEA_NUM, 
                           CAST(CUST_CHN_ID AS VARCHAR(50)) AS CUST_CHN_ID, 
                           CAST(CUST_CHN_NAME AS VARCHAR(50)) AS CUST_CHN_NAME, 
                           CAST(HOME_DC_ID AS VARCHAR(50)) AS HOME_DC_ID, 
                           CAST(REP_NAME AS VARCHAR(50)) AS REP_NAME, 
                           CAST(VPS_NAME AS VARCHAR(50)) AS VPS_NAME, 
                           CAST(NORMALIZED_ADDRESS AS VARCHAR(50)) AS NORMALIZED_ADDRESS, 
                           CAST(DISCREPANCY AS VARCHAR(250)) AS DISCREPANCY, 
                           CAST(DATE_RECORD_PULLED AS VARCHAR(50)) AS DATE_RECORD_PULLED, 
                           CAST(STATUS AS VARCHAR(50)) AS STATUS, 
                           CAST(NOTES AS VARCHAR(50)) AS NOTES 
                   FROM ANALYTICS.CURRENT_DISCREPANCIES')
    """
    data = pd.read_sql(query, cnxn)
    return data

# Load data
data = load_data()

# Display the data in a table
st.dataframe(data)
