class SqlQueries:
    industries_table_insert = ("""
        SELECT DISTINCT INDUSTRY 
        FROM HISTORICALSTOCKSSTAGING 
        ORDER BY INDUSTRY
        """)
    
    historical_stocks_insert = ("""
        SELECT TICKER, EXCHANGE, NAME, S.SECTORID, I.INDUSTRYID 
        FROM HISTORICALSTOCKSSTAGING HSS
        JOIN SECTORS S ON UPPER(HSS.Sector) = UPPER(S.Sector) 
        JOIN INDUSTRIES I ON HSS.Industry = I.IndustryName
        """)
        