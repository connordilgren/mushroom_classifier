import socket
import pickle


###############################################################
# Example client interaction with service                     #
# - Sends "give" to microservice, microservice will respond   #
#   with pandas DataFrame.                                    #
#                                                             #
###############################################################
def get_mushroom_data(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", port))
    # print("Connected to microservice on port", port)

    # Valid commands
    request_msg = "give"
    close_msg = "close"

    # Send "give" to receive DataFrame
    client_socket.sendall(request_msg.encode())
    response = client_socket.recv(2048)
    full_response = pickle.loads(response)
    # Print DataFrame to prove it survived transit
    print(full_response)
    # Close the connection by sending "close"
    client_socket.sendall(close_msg.encode())
    client_socket.close()


def main():
    get_mushroom_data(1100)


if __name__ == "__main__":
    main()
