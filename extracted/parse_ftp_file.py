import pandas as pd
import csv


df = pd.read_excel('Customer_data.xlsx')
df2 = pd.read_table("SOA.txt", delimiter="^")    

df.to_csv('D:\development\python\DATAPIPELINEPROJECT\parsed\Customer_data.csv', sep='^', index=False)
df2.to_csv('D:\development\python\DATAPIPELINEPROJECT\parsed\SOA.csv', sep='^', index=False)


with open("CREDTC", "r") as file1:

    file_content = file1.read()

lines = file_content.splitlines()
data_list = []  

for line in lines:
    credit_card_number = line[0:16]
    transaction_date = line[46:56]
    transaction_amount = line[86:94]
    customer_number = line[124:]
    
    data = {
        'Credit_Card_Number': credit_card_number,
        'Transaction_Date': transaction_date,
        'Transaction_Amount': transaction_amount,
        'Customer_Number': customer_number
    }

    data_list.append(data)

fields = ['Credit_Card_Number', 'Transaction_Date', 'Transaction_Amount', 'Customer_Number']
filename = 'D:\development\python\DATAPIPELINEPROJECT\parsed\CREDTC.csv'
     
with open(filename, 'w', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(data_list)


file1.close()