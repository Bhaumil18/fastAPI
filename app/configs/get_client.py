# from clickhouse_connect import get_client

# def get_clickhouse_client():
#     return get_client(host='localhost',port=8123)

from clickhouse_connect import get_client


def get_clickhouse_client():
    # return get_client(host='192.168.0.10',port=8123)
    return get_client(host='2f27-116-72-8-158.ngrok-free.app', port=80)

