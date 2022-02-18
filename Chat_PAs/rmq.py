from multiprocessing import connection
import pika

GET_ALL_MESSAGES = -1
RMQ_HOST = 'cps-devops.gonzaga.edu'
RMQ_PORT = 5672
RMQ_USER = 'class'
RMQ_PASSWORD = 'CPSC313'
# RMQ_USER = 'bhigley'
# RMQ_PASSWORD = 'CPSC313'
RMQ_DEFAULT_PUBLIC_QUEUE = 'general'
RMQ_DEFAULT_PRIVATE_QUEUE = 'bhigley'

class MessageServer():
    """
    """
    def __init__(self, type: int) -> None:
        """ Need to set up all my RMQ settings
            Create and setup connection, channels, queues, exchanges, etc
        """
        if type == 0: # is a private message
            pass
        else: # is a public message
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST, port=RMQ_PORT))
            self.channel = self.connection.channel()
            self.channel.queue_declare(RMQ_DEFAULT_PUBLIC_QUEUE)
            self.channel.exchange_declare('fanout-exchange', ExchangeType.fanout.'fanout-exchange', True)
            self.messages = []
            
    
    def send_message(self, message: str, target_queue: str) -> bool:
        """
        """
        self.channel.basic_publish(exchange='',
                            routing_key=target_queue,
                            body=message)
        print(" [x] Sent ", message)

    def recieve_messages(self, target_queue: str, num_messages: int): #: int = GET_ALL_MESSAGES) -> list:
        """ Get a set of messages and return them in a list
            messages will be strings, so return a list of strings
        """
        self.channel.queue_declare(target_queue)
        # message_number = 0
        # while (message_number < num_messages):
        #     method, properties, body = self.channel.basic_get(target_queue)
        #     if method:
        #         print(method, properties, body)
        #         self.messages.append(body)
        #         self.channel.basic_ack(method.delivery_tag)
        #     else:
        #         print("No message returned")
        #     message_number += 1

        # def callback(channel, method, properties, body):
        #     print("Received %r" % body)

        # self.channel.basic_consume(queue='general', on_message_callback=callback, auto_ack=True)
        # print("Waiting for messages")
        # self.channel.start_consuming()

        # Get ten messages and break out
        for method_frame, properties, body in self.channel.consume(target_queue):

            # Display the message parts
            print(method_frame)
            print(properties)
            print(body)
            self.messages.append(body)

            # Acknowledge the message
            self.channel.basic_ack(method_frame.delivery_tag)

            # Escape out of the loop after 10 messages
            if method_frame.delivery_tag == 2:
                break

        # Cancel the consumer and return any pending messages
        requeued_messages = self.channel.cancel()
        print('Requeued %i messages' % requeued_messages)

        # Close the channel and the connection
        self.channel.close()
        self.connection.close()