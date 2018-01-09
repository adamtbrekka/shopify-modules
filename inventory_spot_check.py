import csv
import time
from datetime import datetime
import shopify
from initiateShopifySession import initiate_shopify_session

def inventory_spot_check():
    initiate_shopify_session()
    with open('inventory_spot_check.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV) #skips top row
        for row in readCSV:
            input0_text = row[0].replace("'", "")
            input0 = int(input0_text)
            input1_text = row[1].replace("'", "")
            input1 = int(input1_text)
            input2raw = float(row[2])
            input2 = int(input2raw) + 0
            product = shopify.Variant.find(input1, product_id = input0)
            product.inventory_quantity = input2
            output1 = product.inventory_quantity
            time.sleep(2)
            print("{}/{}: {}".format(input0,input1,output1))
            product.save()

#inventory_spot_check()
