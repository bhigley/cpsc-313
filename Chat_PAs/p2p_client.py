from rabbit import MessageServer
#from rmq import MessageServer

def main():
    server = MessageServer()

    message = "This is not a message"
    queue = 'general'
    server.send_message(message, queue)
    server.send_message("this is another ben", queue)
    server.recieve_messages(queue, 5)
    print(server.messages)

if __name__ == '__main__':
    main()