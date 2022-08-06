import client
import pandas as pd


if __name__ == '__main__':
    client.authorize(username="USERNAME", password="PASSWORD")
    product_list = client.get_product_list()
    print(product_list)
    print(client.get_data_sets_for_product(1))
    print(client.get_data(1))

    data = pd.DataFrame([1, 2, 3, 4])
    data.columns = ['v']
    data.index = [100000000, 100100000, 100200000, 100300000]
    data['t'] = data.index
    print(client.convert_to_timestamp(data))
    client.upload_data(product_id=1, start_time=100000000, data=data)

