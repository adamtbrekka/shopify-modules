import shopify

def initiate_shopify_session():
    shop_url = "https://%s:%s@PASTE_SHOPNAME_HERE.myshopify.com/admin" % ("PASTE_KEY_HERE", "PASTE_SECRET_HERE")

    shopify.ShopifyResource.set_site(shop_url)

    shopify.Session.setup(api_key="PASTE_KEY_HERE", secret="PASTE_SECRET_HERE")

    # Get the current shop
    shop = shopify.Shop.current()
