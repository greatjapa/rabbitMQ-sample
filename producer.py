#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.basic_publish(exchange='first_exchange', routing_key='', body=json.dumps({"name": "Japa"}))

connection.close()