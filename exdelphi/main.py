import client


if __name__ == "__main__":
    client.authorize(username="USERNAME", password="PASSWORD")
    print(client.get_product_list())
    print(client.get_data_sets_for_product(1))
    print(client.get_data(1))
