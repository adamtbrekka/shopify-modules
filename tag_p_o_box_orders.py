import csv
from datetime import datetime
import shopify
from initiateShopifySession import initiate_shopify_session
import time

def tag_orders(list_of_order_ids, designated_tag):
    print("\n{}\n".format(list_of_order_ids))
    for order_id in list_of_order_ids:
        order = shopify.Order.find(order_id)
        old_tags = order.tags
        if len(old_tags) > 1:
            new_tags = old_tags + ", " + designated_tag
            order.tags = new_tags
            time.sleep(2)
            order.save()
            print("{}: {}".format(order_id,new_tags))
        elif len(old_tags) == 0:
            new_tags = designated_tag
            order.tags = new_tags
            time.sleep(2)
            order.save()
            print("{}: {}".format(order_id,new_tags))

def comb_unfulfilled_orders():
    orders_count = shopify.Order.count(fulfillment_status="unfulfilled")
    limit = 50
    pages = 30
    unfulfilled_orders_data = []
    p_o_box_orders = []
    for i in range(1, pages + 1):
        time.sleep(2)
        orders = shopify.Order.find(limit=limit, page=i, fulfillment_status='unfulfilled')
        for order in orders:
            order_address = order.shipping_address
            order_address_1 = order_address.address1
            order_address_2 = order_address.address2
            combined_address = "{} / {}".format(order_address_1, order_address_2)
            order_lines = [order.id, combined_address.lower()]
            unfulfilled_orders_data.append(order_lines)
    for order_data in unfulfilled_orders_data:
        if "po box" in order_data[1] or "p o box" in order_data[1] or "p.o. box" in order_data[1]:
            p_o_box_orders.append(order_data[0])
    return p_o_box_orders

def tag_p_o_box_orders():
    initiate_shopify_session()
    print("Fetching unfulfilled order data...")
    p_o_box_orders = comb_unfulfilled_orders()
    print("P.O. Box Order data fetched...")
    tag_orders(p_o_box_orders, "P.O. BOX ORDER")
    print("\n{} P.O. Box order(s) tagged!".format(len(p_o_box_orders)))

#tag_p_o_box_orders()
