#!/usr/bin/env python

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(1000000):
    message = "message " + str(i)
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)

connection.close()

