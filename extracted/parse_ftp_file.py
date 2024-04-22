import pandas as pd
import csv

# Parsing of excel file 
df = pd.read_excel('Customer_data.xlsx')
 
df_field_names = ['Customer Id', 'First Name', 'Last Name', 'Middle Name', 'Birthdate', 'Gender', 'Marital Status']
df_excel_cols  = df.columns

df_column_validation = len(df_field_names) == len(df_excel_cols) and (df_field_names == df_excel_cols).all()
if not df_column_validation:
    raise Exception("Customer_data columns do not match the fields.")

df.to_csv('D:\development\python\DATAPIPELINEPROJECT\parsed\Customer_data.csv', sep='^', index=False)

# Parsing of CSV file
df2 = pd.read_table("SOA.txt", delimiter="^") 

df2_field_names = ['SOA Date', 'Customer Number', 'Address', 'Envelop Type']
df2_csv_cols  = df2.columns

df2_column_validation = len(df2_field_names) == len(df2_csv_cols) and (df2_field_names == df2_csv_cols).all()
if not df2_column_validation:
    raise Exception("SOA columns do not match the fields.")

df2.to_csv('D:\development\python\DATAPIPELINEPROJECT\parsed\SOA.csv', sep='^', index=False)


# with open("CREDTC", "r") as file1:

#     file_content = file1.read()

# lines = file_content.splitlines()
# data_list = []  

# for line in lines:
#     credit_card_number = line[0:16]
#     transaction_date = line[46:56]
#     transaction_amount = line[86:94]
#     customer_number = line[124:]
    
#     data = {
#         'Credit_Card_Number': credit_card_number,
#         'Transaction_Date': transaction_date,
#         'Transaction_Amount': transaction_amount,
#         'Customer_Number': customer_number
#     }

#     data_list.append(data)

# fields = ['Credit_Card_Number', 'Transaction_Date', 'Transaction_Amount', 'Customer_Number']
# filename = 'D:\development\python\DATAPIPELINEPROJECT\parsed\CREDTC.csv'
     
# with open(filename, 'w', newline = '') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)

#     writer.writeheader()
#     writer.writerows(data_list)


# file1.close()