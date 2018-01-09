import csv
from datetime import datetime
import datetime
import time
import shopify
from initiateShopifySession import initiate_shopify_session

def export_unfulfilled_orders():
    initiate_shopify_session()
    orders_count = shopify.Order.count(fulfillment_status="unfulfilled")
    limit = 50
    pages = 30
    orders_data = []
    for i in range(1, pages + 1):
        time.sleep(2)
        orders = shopify.Order.find(limit=limit, page=i, fulfillment_status='unfulfilled')
        previous_names = []
        for order in orders:
            for lineitem in order.line_items:
                date_processed = (order.processed_at)[:10]
                date_processed_proper = datetime.datetime.strptime(date_processed,'%Y-%m-%d')
                billed_customer = order.customer
                customer_name = "{} {}".format(billed_customer.first_name,billed_customer.last_name)
                if order.name+" "+customer_name in previous_names:
                    customer_name = ""
                orders_data.append([order.name, order.email, order.financial_status, date_processed_proper, order.fulfillment_status, order.closed_at, order.buyer_accepts_marketing, order.currency, order.subtotal_price, order.shipping_lines, order.tax_lines, order.total_price, order.discount_codes, order.total_discounts, order.shipping_lines, date_processed_proper, lineitem.quantity, lineitem.name, lineitem.price, lineitem.price, lineitem.sku, lineitem.requires_shipping, lineitem.taxable, lineitem.fulfillment_status, customer_name, order.tags])
                previous_names.append(order.name+" "+customer_name)
    with open('orders_export.csv', 'w') as csvfile:
        output = csv.writer(csvfile)
        output.writerow(["Name","Email","Financial Status","Paid at","Fulfillment Status","Fulfilled at","Accepts Marketing","Currency","Subtotal","Shipping","Taxes","Total","Discount Code","Discount Amount","Shipping Method","Created at","Lineitem quantity","Lineitem name","Lineitem price","Lineitem compare at price","Lineitem sku","Lineitem requires shipping","Lineitem taxable","Lineitem fulfillment status","Billing Name","Tags"])
        for order_data in orders_data:
            output.writerow(order_data)

#export_unfulfilled_orders()
