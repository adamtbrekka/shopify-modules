import csv
from datetime import datetime
import shopify
from initiateShopifySession import initiate_shopify_session
import datetime

def export_product_data():
    initiate_shopify_session()
    products_count = shopify.Product.count()
    limit = 50
    pages = 30
    variants_data = []
    for i in range(1, pages + 1):
        products = shopify.Product.find(limit=limit, page=i)
        for product in products:
            for variant in product.variants:
                upc = "'{}".format(variant.barcode)
                product_id = "'{}".format(product.id)
                variant_id = "'{}".format(variant.id)
                if product.published_at is not None:
                    published_status_final = "TRUE"
                elif product.published_at is None:
                    published_status_final = "FALSE"
                shopify_URL = "/admin/products/"+str(product.id)
                variants_data.append([product.handle, product.title, product.body_html, product.vendor, product.product_type, product.tags, published_status_final, variant.option1, variant.option1, variant.option2, variant.option2, variant.option3, variant.option3, variant.sku, variant.grams, variant.inventory_management, variant.inventory_quantity, variant.inventory_policy, variant.fulfillment_service, variant.price, variant.compare_at_price, variant.requires_shipping, variant.taxable, upc, product_id, variant_id, shopify_URL])
    product_export_file_name = 'products_export {:%Y-%m-%d %H:%M:%S}.csv'.format(datetime.datetime.now())
    with open(product_export_file_name, 'w') as csvfile:
        output = csv.writer(csvfile)
        output.writerow(["Handle","Title","Body (HTML)","Vendor","Type","Tags","Published","Option1 Name","Option1 Value","Option2 Name","Option2 Value","Option3 Name","Option3 Value","Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty","Variant Inventory Policy","Variant Fulfillment Service","Variant Price","Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Variant_Barcode","Product_Id","Variant_Id","shopify_URL"])
        for variant_data in variants_data:
            output.writerow(variant_data)
    print("Product export csv has been created!")

def extract_product_data():
    initiate_shopify_session()
    products_count = shopify.Product.count()
    limit = 50
    pages = 30
    variants_data = []
    for i in range(1, pages + 1):
        products = shopify.Product.find(limit=limit, page=i)
        for product in products:
            for variant in product.variants:
                upc = "'{}".format(variant.barcode)
                product_id = "'{}".format(product.id)
                variant_id = "'{}".format(variant.id)
                if product.published_at is not None:
                    published_status_final = "TRUE"
                elif product.published_at is None:
                    published_status_final = "FALSE"
                shopify_URL = "/admin/products/"+str(product.id)
                variants_data.append([product.handle, product.title, product.body_html, product.vendor, product.product_type, product.tags, published_status_final, variant.option1, variant.option1, variant.option2, variant.option2, variant.option3, variant.option3, variant.sku, variant.grams, variant.inventory_management, variant.inventory_quantity, variant.inventory_policy, variant.fulfillment_service, variant.price, variant.compare_at_price, variant.requires_shipping, variant.taxable, upc, product_id, variant_id, shopify_URL])
    return variants_data

#export_product_data()
#extract_product_data()
