import client

if __name__ == '__main__':
    client.authorize(username=USERNAME, password=PASSWORD)
    product_list = client.get_product_list()
    print(product_list)
