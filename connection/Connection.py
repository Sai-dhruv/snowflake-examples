import sys

import snowflake.connector as sf

# from Exception.CustomException import CustomException

# it is simple authentication - using user-id & pwd

try:
    conn = sf.connect(
        user='USER NAME ',
        password='PASS_WORD',
        account='ia21722.us-east-2.aws',
        warehouse='COMPUTE_WH',
        database='EDU',
        schema='employee.PUBLIC'
    )
    print("2. Connection established successfully ")
    # Getting the cursor Object
    curser_object = conn.cursor()
    print(conn.database)
    data = curser_object.execute("select * from STUDENT;")
    print(data.fetchone())



except Exception as e:
    print("Error ", e)
    # raise CustomException(e, sys)
