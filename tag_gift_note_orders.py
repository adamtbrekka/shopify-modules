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
    gift_note_orders = []
    for i in range(1, pages + 1):
        time.sleep(2)
        orders = shopify.Order.find(limit=limit, page=i, fulfillment_status='unfulfilled')
        for order in orders:
            note_attribute_names = []
            for order_note_names in order.note_attributes:
                order_note_attributes = order.note_attributes
                for order_note_names in order_note_attributes:
                    order_lines = [order.id, order_note_names.name]
                    unfulfilled_orders_data.append(order_lines)
    for order_data in unfulfilled_orders_data:
        if 'gift-note' in order_data[1]:
            gift_note_orders.append(order_data[0])
    return gift_note_orders

def tag_gift_note_orders():
    initiate_shopify_session()
    print("Fetching unfulfilled order data...")
    gift_note_orders = comb_unfulfilled_orders()
    print("Gift Note Order data fetched...")
    tag_orders(gift_note_orders, "Gift Note Order")
    print("\n{} gift note order(s) tagged!".format(len(gift_note_orders)))

#tag_gift_note_orders()
