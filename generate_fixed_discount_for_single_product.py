import csv
from datetime import datetime
import shopify
from initiateShopifySession import initiate_shopify_session
from datetime import datetime, date, time, timedelta

def generate_fixed_discount_for_single_product(discount_value_float, product_id_int, code_name):
    initiate_shopify_session()
    discounted_value = -discount_value_float
    date_now = datetime.now()
    start_date_strf = date_now.strftime("%Y-%m-%d %H:%M:%S")
    expiration_date = date_now + timedelta(days=365)
    expiration_date_strf = expiration_date.strftime("%Y-%m-%d %H:%M:%S")
    print(expiration_date)
    price_rule = shopify.PriceRule.create({
        'title': code_name,
        'target_type': 'line_item',
        'target_selection': 'entitled',
        'allocation_method': 'across',
        'value_type': 'fixed_amount',
        'value': discounted_value,
        'once_per_customer': True,
        'usage_limit': 1,
        'customer_selection': 'all',
        'entitled_product_ids': [ product_id_int ],
        'starts_at': start_date_strf,
        'ends_at': expiration_date_strf
    })
    print(price_rule.id)
    print(price_rule.title)
    discount = shopify.DiscountCode.create({
        'price_rule_id': price_rule.id,
        'code': code_name
    })
    print(discount.id)
    print(discount.code)

#generate_fixed_discount_for_single_product(discount_value_float, product_id_int, code_name)
