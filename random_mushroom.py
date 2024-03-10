import random

import socket
import pickle
import pandas as pd


###############################################################
# Get Random Stats (returns DataFrame)                        #
# - Fills in a data frame with random mushroom attributes.    #
# - Helper function for microservice                          #
# - Set debug_prints to 1 in main to print out the field and  #
#   data frames if something doesn't work properly.           #
#                                                             #
###############################################################
def get_random_stats(debug_prints=False):

    # The list of fields and valid values.
    fields = {
        'cap-shape': {
            'bell': 0,
            'conical': 1,
            'convex': 2,
            'flat': 3,
            'knobbed': 4,
            'sunken': 5,
        },

        'cap-surface': {
            'fibrous': 6,
            'grooves': 7,
            'scaly': 8,
            'smooth': 9,
        },

        'cap-color': {
            'brown': 10,
            'buff': 11,
            'cinnamon': 12,
            'gray': 13,
            'green': 14,
            'pink': 15,
            'purple': 16,
            'red': 17,
            'white': 18,
            'yellow': 19,
        },

        'bruises': {
            'Yes': 20,
            'No': 21,
        },

        'odor': {
            'almond': 22,
            'anise': 23,
            'creosote': 24,
            'fishy': 25,
            'foul': 26,
            'musty': 27,
            'none': 28,
            'pungent': 29,
            'spicy': 30,
        },

        'gill-attachment': {
            'attached': 31,
            'descending': 32,
            'free': 33,
            'notched': 34,
        },

        'gill-spacing': {
            'close': 35,
            'crowded': 36,
            'distant': 37,
        },

        'gill-size': {
            'broad': 38,
            'narrow': 39,
        },

        'gill-color': {
            'black': 40,
            'brown': 41,
            'buff': 42,
            'chocolate': 43,
            'gray': 44,
            'green': 45,
            'orange': 46,
            'pink': 47,
            'purple': 48,
            'red': 49,
            'white': 50,
            'yellow': 51,
        },

        'stalk-shape': {
            'enlarging': 52,
            'tapering': 53,
        },

        'stalk-root': {
            'bulbous': 54,
            'club': 55,
            'cup': 56,
            'equal': 57,
            'rhizomorphs': 58,
            'rooted': 59,
            'missing': 60,
        },

        'stalk-surface-above-ring': {
            'fibrous': 61,
            'scaly': 62,
            'silky': 63,
            'smooth': 64,
        },

        'stalk-surface-below-ring': {
            'fibrous': 65,
            'scaly': 66,
            'silky': 67,
            'smooth': 68,
        },

        'stalk-color-above-ring': {
            'brown': 69,
            'buff': 70,
            'cinnamon': 71,
            'gray': 72,
            'orange': 73,
            'pink': 74,
            'red': 75,
            'white': 76,
            'yellow': 77,
        },

        'stalk-color-below-ring': {
            'brown': 78,
            'buff': 79,
            'cinnamon': 80,
            'gray': 81,
            'orange': 82,
            'pink': 83,
            'red': 84,
            'white': 85,
            'yellow': 86,
        },

        'veil-type': {
            'partial': 87,
            'universal': 88,
        },

        'veil-color': {
            'brown': 89,
            'orange': 90,
            'white': 91,
            'yellow': 92,
        },

        'ring-number': {
            'none': 93,
            'one': 94,
            'two': 95,
        },

        'ring-type': {
            'cobwebby': 96,
            'evanescent': 97,
            'flaring': 98,
            'large': 99,
            'none': 100,
            'pendant': 101,
            'sheathing': 102,
            'zone': 103,
        },

        'spore-print-color': {
            'black': 104,
            'brown': 105,
            'buff': 106,
            'chocolate': 107,
            'green': 108,
            'orange': 109,
            'purple': 110,
            'white': 111,
            'yellow': 112,
        },

        'population': {
            'abundant': 113,
            'clustered': 114,
            'numerous': 115,
            'scattered': 116,
            'several': 117,
            'solitary': 118,
        },

        'habitat': {
            'grasses': 119,
            'leaves': 120,
            'meadows': 121,
            'paths': 122,
            'urban': 123,
            'waste': 124,
            'woods': 125,
        }
    }

    if debug_prints:
        print(fields, "\n\n\n")

    # Create an "empty" data frame with no values, and randomly assign values
    random_frame = pd.DataFrame({
                                'cap-shape': [None],
                                'cap-surface': [None],
                                'cap-color': [None],
                                'bruises': [None],
                                'odor': [None],
                                'gill-attachment': [None],
                                'gill-spacing': [None],
                                'gill-size': [None],
                                'gill-color': [None],
                                'stalk-shape': [None],
                                'stalk-root': [None],
                                'stalk-surface-above-ring': [None],
                                'stalk-surface-below-ring': [None],
                                'stalk-color-above-ring': [None],
                                'stalk-color-below-ring': [None],
                                'veil-type': [None],
                                'veil-color': [None],
                                'ring-number': [None],
                                'ring-type': [None],
                                'spore-print-color': [None],
                                'population': [None],
                                'habitat': [None]
                                })

    # Assign random, valid values to each field.
    for field in fields:
        random_field_val = random.choice([v for v in fields[field].values()])
        random_frame.loc[0, field] = random_field_val
    if debug_prints:
        print(random_frame)
    return random_frame


###############################################################
# Start Microservice (no return type)                         #
# - Starts the microservice on the port specified.            #
# - Microservice accepts connections                          #
# - Send "give" to service along socket, service will return  #
#   a mushroom DataFrame with random attributes.              #
#                                                             #
###############################################################
def start_microservice(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", port))  # Host on LOCALHOST
    server_socket.listen(1)                # Wait for connection
    print("Microservice started on port:", port)
    main_socket, addr = server_socket.accept()

    # Main server loop
    # Valid commands: give, close
    while True:

        msg = main_socket.recv(1024).decode()
        print("Message:", msg)
        # Generate random mushroom attributes and send DataFrame
        if msg == "give":
            attr = get_random_stats()  # Set to 1 to enable debug printing.
            pickled_data = pickle.dumps(attr)
            main_socket.sendall(pickled_data)
        elif msg == "close":
            print("Closing connection and stopping microservice")
            main_socket.close()
            break
        else:
            print("Invalid message.")
    main_socket.close()
    print("Microservice stopped.")


def main():
    start_microservice(1100)


if __name__ == "__main__":
    main()
