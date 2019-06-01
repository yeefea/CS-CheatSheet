#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
while True:
    try:
        msg = input('>>>')
        channel.basic_publish(exchange='', routing_key='hello', body=msg)
        print("Sent:", msg)
    except EOFError:
        break
connection.close()