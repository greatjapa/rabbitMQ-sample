import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(queue="first_queue", on_message_callback=callback, auto_ack=True)

channel.start_consuming()