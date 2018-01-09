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
    potential_fraud_orders = []
    for i in range(1, pages + 1):
        time.sleep(2)
        orders = shopify.Order.find(limit=limit, page=i, fulfillment_status='unfulfilled')
        for order in orders:
            unfulfilled_orders_data.append(order.id)
    wait_time = 0
    for order_id_number in unfulfilled_orders_data:
        order_risk = shopify.OrderRisk.find(order_id = order_id_number)
        wait_time += 2
        for risk in order_risk:
            risk_message = risk.message
            risk_recommendation = risk.recommendation
            if risk_message == "Shopify recommendation":
                if risk_recommendation != "accept":
                    potential_fraud_orders.append(order_id_number)
        if wait_time % 5 == 0:
            time.sleep(2)
    return potential_fraud_orders

def tag_potential_fraud_orders():
    initiate_shopify_session()
    print("Fetching unfulfilled order data...")
    potential_fraud_orders = comb_unfulfilled_orders()
    print("Potential Fraud Order data fetched...")
    tag_orders(potential_fraud_orders, "Potential Fraud")
    print("\n{} potential fraud order(s) tagged!".format(len(potential_fraud_orders)))

#tag_potential_fraud_orders()
