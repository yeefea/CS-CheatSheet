#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))  # 建立连接
channel = connection.channel()

channel.queue_declare(queue='hello')  # 申明queue才能发送消息，否则消息会被丢弃
while True:
    try:
        msg = input('>>>')
        channel.basic_publish(exchange='',  # 默认exchange
                              routing_key='hello',   # queue的名字
                              body=msg)
        print("Sent:", msg)
    except EOFError:
        break
connection.close()