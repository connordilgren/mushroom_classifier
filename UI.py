import pandas as pd
import PySimpleGUI as sg


def invalid_input_missing_fields():
    layout = [
        [sg.Text("Error: All fields must be completed before hitting submit.")],
        [sg.Button("Exit")]
        ]
    window = sg.Window("Error: Incomplete Fields", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def validate_input(values):
    fields = {
        'cap shape': {
            'bell': 0,
            'conical': 1,
            'convex': 2,
            'flat': 3,
            'knobbed': 4,
            'sunken': 5,
        },
        'cap surface': {
            'fibrous': 6,
            'grooves': 7,
            'scaly': 8,
            'smooth': 9,
        },
        'cap color': {
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
        'gill attachment': {
            'attached': 31,
            'descending': 32,
            'free': 33,
            'notched': 34,
        },
        'gill spacing': {
            'close': 35,
            'crowded': 36,
            'distant': 37,
        },
        'gill size': {
            'broad': 38,
            'narrow': 39,
        },
        'gill color': {
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
        'stalk shape': {
            'enlarging': 52,
            'tapering': 53,
        },
        'stalk root': {
            'bulbous': 54,
            'club': 55,
            'cup': 56,
            'equal': 57,
            'rhizomorphs': 58,
            'rooted': 59,
            'missing': 60,
        },
        'stalk surface above ring': {
            'fibrous': 61,
            'scaly': 62,
            'silky': 63,
            'smooth': 64,
        },
        'stalk surface below ring': {
            'fibrous': 65,
            'scaly': 66,
            'silky': 67,
            'smooth': 68,
        },
        'stalk color above ring': {
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
        'stalk color below ring': {
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
        'veil type': {
            'partial': 87,
            'universal': 88,
        },
        'veil color': {
            'brown': 89,
            'orange': 90,
            'white': 91,
            'yellow': 92,
        },
        'ring number': {
            'none': 93,
            'one': 94,
            'two': 95,
        },
        'ring type': {
            'cobwebby': 96,
            'evanescent': 97,
            'flaring': 98,
            'large': 99,
            'none': 100,
            'pendant': 101,
            'sheathing': 102,
            'zone': 103,
        },
        'spore print color': {
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

    for field in fields:
        num_entries = 0
        for num in fields[field].values():
            if values[num] is True:
                num_entries += 1
        if num_entries != 1:
            invalid_input_missing_fields()
            break


def on_submit(values):
    # validate input
    validate_input(values)
    
    # if bad, say that they need to fill out all fields


# user input, to be filled out
df_user = pd.DataFrame({'cap-shape': [None],
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
                        'habitat': [None]})

col_1 = [
    [sg.Text("1. What is the mushroom's cap shape?")],
    [
        sg.Radio('bell', 'cap shape'),      # 0
        sg.Radio('conical', 'cap shape'),   # 1
        sg.Radio('convex', 'cap shape'),    # 2
        sg.Radio('flat', 'cap shape'),      # 3
        sg.Radio('knobbed', 'cap shape'),   # 4
        sg.Radio('sunken', 'cap shape'),    # 5
    ],

    [sg.Text("2. What is the mushroom's cap surface?")],
    [
        sg.Radio('fibrous', 'cap surface'),
        sg.Radio('grooves', 'cap surface'),
        sg.Radio('scaly', 'cap surface'),
        sg.Radio('smooth', 'cap surface'),
    ],

    [sg.Text("3. What is the mushroom's cap color?")],
    [
        sg.Radio('brown', 'cap color'),
        sg.Radio('buff', 'cap color'),
        sg.Radio('cinnamon', 'cap color'),
        sg.Radio('gray', 'cap color'),
        sg.Radio('green', 'cap color'),
        sg.Radio('pink', 'cap color'),
        sg.Radio('purple', 'cap color'),
        sg.Radio('red', 'cap color'),
        sg.Radio('white', 'cap color'),
        sg.Radio('yellow', 'cap color'),
    ],

    [sg.Text("4. Does the mushroom have bruises?")],
    [
        sg.Radio('Yes', 'bruises'),
        sg.Radio('No', 'bruises'),
    ],

    [sg.Text("5. What is the mushroom's odor?")],
    [
        sg.Radio('almond', 'odor'),
        sg.Radio('anise', 'odor'),
        sg.Radio('creosote', 'odor'),
        sg.Radio('fishy', 'odor'),
        sg.Radio('foul', 'odor'),
        sg.Radio('musty', 'odor'),
        sg.Radio('none', 'odor'),
        sg.Radio('pungent', 'odor'),
        sg.Radio('spicy', 'odor'),
    ],

    [sg.Text("6. What is the mushroom's gill attachment?")],
    [
        sg.Radio('attached', 'gill attachment'),
        sg.Radio('descending', 'gill attachment'),
        sg.Radio('free', 'gill attachment'),
        sg.Radio('notched', 'gill attachment'),
    ],

    [sg.Text("7. What is the mushroom's gill spacing?")],
    [
        sg.Radio('close', 'gill spacing'),
        sg.Radio('crowded', 'gill spacing'),
        sg.Radio('distant', 'gill spacing'),
    ],

    [sg.Text("8. What is the mushroom's gill size?")],
    [
        sg.Radio('broad', 'gill size'),
        sg.Radio('narrow', 'gill size'),
    ],

    [sg.Text("9. What is the mushroom's gill color?")],
    [
        sg.Radio('black', 'gill color'),
        sg.Radio('brown', 'gill color'),
        sg.Radio('buff', 'gill color'),
        sg.Radio('chocolate', 'gill color'),
        sg.Radio('gray', 'gill color'),
        sg.Radio('green', 'gill color'),
        sg.Radio('orange', 'gill color'),
        sg.Radio('pink', 'gill color'),
        sg.Radio('purple', 'gill color'),
        sg.Radio('red', 'gill color'),
        sg.Radio('white', 'gill color'),
        sg.Radio('yellow', 'gill color'),
    ],

    [sg.Text("10. What is the mushroom's stalk shape?")],
    [
        sg.Radio('enlarging', 'stalk shape'),
        sg.Radio('tapering', 'stalk shape'),
    ],

    [sg.Text("11. What is the mushroom's stalk root?")],
    [
        sg.Radio('bulbous', 'stalk root'),
        sg.Radio('club', 'stalk root'),
        sg.Radio('cup', 'stalk root'),
        sg.Radio('equal', 'stalk root'),
        sg.Radio('rhizomorphs', 'stalk root'),
        sg.Radio('rooted', 'stalk root'),
        sg.Radio('missing', 'stalk root'),
    ],

    [sg.Text("12. What is the mushroom's stalk surface, above the ring?")],
    [
        sg.Radio('fibrous', 'stalk surface above ring'),
        sg.Radio('scaly', 'stalk surface above ring'),
        sg.Radio('silky', 'stalk surface above ring'),
        sg.Radio('smooth', 'stalk surface above ring'),
    ],

    [sg.Text("13. What is the mushroom's stalk surface, below the ring?")],
    [
        sg.Radio('fibrous', 'stalk surface below ring'),
        sg.Radio('scaly', 'stalk surface below ring'),
        sg.Radio('silky', 'stalk surface below ring'),
        sg.Radio('smooth', 'stalk surface below ring'),
    ],

    [sg.Text("14. What is the mushroom's stalk color, above the ring?")],
    [
        sg.Radio('brown', 'stalk color above ring'),
        sg.Radio('buff', 'stalk color above ring'),
        sg.Radio('cinnamon', 'stalk color above ring'),
        sg.Radio('gray', 'stalk color above ring'),
        sg.Radio('orange', 'stalk color above ring'),
        sg.Radio('pink', 'stalk color above ring'),
        sg.Radio('red', 'stalk color above ring'),
        sg.Radio('white', 'stalk color above ring'),
        sg.Radio('yellow', 'stalk color above ring'),
    ],

    [sg.Text("15. What is the mushroom's stalk color, below the ring?")],
    [
        sg.Radio('brown', 'stalk color below ring'),
        sg.Radio('buff', 'stalk color below ring'),
        sg.Radio('cinnamon', 'stalk color below ring'),
        sg.Radio('gray', 'stalk color below ring'),
        sg.Radio('orange', 'stalk color below ring'),
        sg.Radio('pink', 'stalk color below ring'),
        sg.Radio('red', 'stalk color below ring'),
        sg.Radio('white', 'stalk color below ring'),
        sg.Radio('yellow', 'stalk color below ring'),
    ],

    [sg.Text("16. What is the mushroom's veil type?")],
    [
        sg.Radio('partial', 'veil type'),
        sg.Radio('universal', 'veil type'),
    ],

    [sg.Text("17. What is the mushroom's veil color?")],
    [
        sg.Radio('brown', 'veil color'),
        sg.Radio('orange', 'veil color'),
        sg.Radio('white', 'veil color'),
        sg.Radio('yellow', 'veil color'),
    ],

    [sg.Text("18. What is the mushroom's ring number?")],
    [
        sg.Radio('none', 'ring number'),
        sg.Radio('one', 'ring number'),
        sg.Radio('two', 'ring number'),
    ],

    [sg.Text("19. What is the mushroom's ring type?")],
    [
        sg.Radio('cobwebby', 'ring type'),
        sg.Radio('evanescent', 'ring type'),
        sg.Radio('flaring', 'ring type'),
        sg.Radio('large', 'ring type'),
        sg.Radio('none', 'ring type'),
        sg.Radio('pendant', 'ring type'),
        sg.Radio('sheathing', 'ring type'),
        sg.Radio('zone', 'ring type'),
    ],

    [sg.Text("20. What is the mushroom's spore print color?")],
    [
        sg.Radio('black', 'spore print color'),
        sg.Radio('brown', 'spore print color'),
        sg.Radio('buff', 'spore print color'),
        sg.Radio('chocolate', 'spore print color'),
        sg.Radio('green', 'spore print color'),
        sg.Radio('orange', 'spore print color'),
        sg.Radio('purple', 'spore print color'),
        sg.Radio('white', 'spore print color'),
        sg.Radio('yellow', 'spore print color'),
    ],

    [sg.Text("21. What is the mushroom's population?")],
    [
        sg.Radio('abundant', 'population'),
        sg.Radio('clustered', 'population'),
        sg.Radio('numerous', 'population'),
        sg.Radio('scattered', 'population'),
        sg.Radio('several', 'population'),
        sg.Radio('solitary', 'population'),
    ],

    [sg.Text("22. What is the mushroom's habitat?")],
    [
        sg.Radio('grasses', 'habitat'),
        sg.Radio('leaves', 'habitat'),
        sg.Radio('meadows', 'habitat'),
        sg.Radio('paths', 'habitat'),
        sg.Radio('urban', 'habitat'),
        sg.Radio('waste', 'habitat'),
        sg.Radio('woods', 'habitat'),
    ],
]

col_2 = [
    [sg.Button("Load Random")],
    [sg.Button("Clear Input")],
    [sg.Button("Submit")],
]

layout = [
    [sg.Text("Welcome to the Mushroom Classifier!")],
    [sg.Text("Please answer the following questions about your mushroom, and "
             "this program will classify it as either edible or poisonous.")],
    [
        sg.Column(col_1, scrollable=True),
        sg.Column(col_2)
    ],
]

# Create the window
window = sg.Window("Mushroom Classifier", layout, size=(1200, 600))

# main event loop
while True:
    event, values = window.read()
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break
    elif event == "Submit":
        on_submit(values)

    print(values)

window.close()
