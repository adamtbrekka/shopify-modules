import csv
from datetime import datetime
import shopify
from initiateShopifySession import initiate_shopify_session
import time

def replace_product_page_tags_by_id():
    initiate_shopify_session()
    print("Replacing tags...")
    with open('product_page_tag_replacements - export.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV) #skips top row
        for row in readCSV:
            input0_text = row[0].replace("'", "")
            product_id_0 = int(input0_text)
            new_tag_1 = row[1]
            product = shopify.Product.find(product_id_0)
            product.tags = new_tag_1
            time.sleep(2)
            print("{}: {}".format(product_id_0,new_tag_1))
            time.sleep(2)
            product.save()
    print("Products have been tagged!")

#replace_product_page_tags_by_id()
