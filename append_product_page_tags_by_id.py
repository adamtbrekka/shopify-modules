import csv
from datetime import datetime
import pandas as pd
import shopify
from initiateShopifySession import initiate_shopify_session
import time

def append_product_page_tags_by_id():
    initiate_shopify_session()
    with open('product_page_tag_updates.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV) #skips top row
        for row in readCSV:
            input0_text = row[0].replace("'", "")
            product_id_0 = int(input0_text)
            new_tag_1 = row[1]
            product = shopify.Product.find(product_id_0)
            old_tags = product.tags
            if len(old_tags) < 1:
                new_tags = new_tag_1
            else:
                new_tags = "{}, {}".format(old_tags, new_tag_1)
            product.tags = new_tags
            time.sleep(2)
            print("{}: {}".format(product_id_0,new_tags))
            time.sleep(2)
            product.save()
    print("Products have been tagged!")

#append_product_page_tags_by_id()
