import pandas as pd
import pickle
import random

import PySimpleGUI as sg


def invalid_input_missing_fields():
    layout = [
        [sg.Text("Error: All fields must be completed before hitting "
                 "submit.")],
        [sg.Button("Exit")]
        ]
    window_invalid_input = sg.Window("Error: Incomplete Fields", 
                                     layout, 
                                     modal=True)
    while True:
        event, values = window_invalid_input.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window_invalid_input.close()


def validate_input(values):
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

    for field in fields:
        num_entries = 0
        for num in fields[field].values():
            if values[num] is True:
                num_entries += 1
        if num_entries != 1:
            return -1

    return 0


def give_results(prediction, df_input):
    if prediction == 0:
        result = 'edible'
    else:
        result = 'poisonous'

    layout = [
        [sg.Text("Results")],
        [sg.Text(f"This mushroom is {result}.")],
        [sg.Text("Warning: This result may be incorrect. Always consult an "
                 "expert before consuming unidentified mushrooms.")],
        [sg.Text("Your inputs:")],

        [sg.Text(f"cap-shape: {to_feat('cap-shape', df_input.loc[0, 'cap-shape'])}")],
        [sg.Text(f"cap-surface: {to_feat('cap-surface', df_input.loc[0, 'cap-surface'])}")],
        [sg.Text(f"cap-color: {to_feat('cap-color', df_input.loc[0, 'cap-color'])}")],
        [sg.Text(f"bruises: {to_feat('bruises', df_input.loc[0, 'bruises'])}")],
        [sg.Text(f"odor: {to_feat('odor', df_input.loc[0, 'odor'])}")],
        [sg.Text(f"gill-attachment: {to_feat('gill-attachment', df_input.loc[0, 'gill-attachment'])}")],
        [sg.Text(f"gill-spacing: {to_feat('gill-spacing', df_input.loc[0, 'gill-spacing'])}")],
        [sg.Text(f"gill-size: {to_feat('gill-size', df_input.loc[0, 'gill-size'])}")],
        [sg.Text(f"gill-color: {to_feat('gill-color', df_input.loc[0, 'gill-color'])}")],
        [sg.Text(f"stalk-shape: {to_feat('stalk-shape', df_input.loc[0, 'stalk-shape'])}")],
        [sg.Text(f"stalk-root: {to_feat('stalk-root', df_input.loc[0, 'stalk-root'])}")],
        [sg.Text(f"stalk-surface-above-ring: {to_feat('stalk-surface-above-ring', df_input.loc[0, 'stalk-surface-above-ring'])}")],
        [sg.Text(f"stalk-surface-below-ring: {to_feat('stalk-surface-below-ring', df_input.loc[0, 'stalk-surface-below-ring'])}")],
        [sg.Text(f"stalk-color-above-ring: {to_feat('stalk-color-above-ring', df_input.loc[0, 'stalk-color-above-ring'])}")],
        [sg.Text(f"stalk-color-below-ring: {to_feat('stalk-color-below-ring', df_input.loc[0, 'stalk-color-below-ring'])}")],
        [sg.Text(f"veil-type: {to_feat('veil-type', df_input.loc[0, 'veil-type'])}")],
        [sg.Text(f"veil-color: {to_feat('veil-color', df_input.loc[0, 'veil-color'])}")],
        [sg.Text(f"ring-number: {to_feat('ring-number', df_input.loc[0, 'ring-number'])}")],
        [sg.Text(f"ring-type: {to_feat('ring-type', df_input.loc[0, 'ring-type'])}")],
        [sg.Text(f"spore-print-color: {to_feat('spore-print-color', df_input.loc[0, 'spore-print-color'])}")],
        [sg.Text(f"population: {to_feat('population', df_input.loc[0, 'population'])}")],
        [sg.Text(f"habitat: {to_feat('habitat', df_input.loc[0, 'habitat'])}")],

        [sg.Button("Exit")]
        ]
    window_resuls = sg.Window("Results", layout, modal=True)
    while True:
        event, values = window_resuls.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window_resuls.close()


def to_feat(field, num):
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

    for k, v in fields[field].items():
        if v == num:
            return k


def format_input(values):
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

    field_abs_to_rel = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 0,
        7: 1,
        8: 2,
        9: 3,
        10: 0,
        11: 1,
        12: 2,
        13: 3,
        14: 4,
        15: 5,
        16: 6,
        17: 7,
        18: 8,
        19: 9,
        20: 0,
        21: 1,
        22: 0,
        23: 1,
        24: 2,
        25: 3,
        26: 4,
        27: 5,
        28: 6,
        29: 7,
        30: 8,
        31: 0,
        32: 1,
        33: 2,
        34: 3,
        35: 0,
        36: 1,
        37: 2,
        38: 0,
        39: 1,
        40: 0,
        41: 1,
        42: 2,
        43: 3,
        44: 4,
        45: 5,
        46: 6,
        47: 7,
        48: 8,
        49: 9,
        50: 10,
        51: 11,
        52: 0,
        53: 1,
        54: 0,
        55: 1,
        56: 2,
        57: 3,
        58: 4,
        59: 5,
        60: 6,
        61: 0,
        62: 1,
        63: 2,
        64: 3,
        65: 0,
        66: 1,
        67: 2,
        68: 3,
        69: 0,
        70: 1,
        71: 2,
        72: 3,
        73: 4,
        74: 5,
        75: 6,
        76: 7,
        77: 8,
        78: 0,
        79: 1,
        80: 2,
        81: 3,
        82: 4,
        83: 5,
        84: 6,
        85: 7,
        86: 8,
        87: 0,
        88: 1,
        89: 0,
        90: 1,
        91: 2,
        92: 3,
        93: 0,
        94: 1,
        95: 2,
        96: 0,
        97: 1,
        98: 2,
        99: 3,
        100: 4,
        101: 5,
        102: 6,
        103: 7,
        104: 0,
        105: 1,
        106: 2,
        107: 3,
        108: 4,
        109: 5,
        110: 6,
        111: 7,
        112: 8,
        113: 0,
        114: 1,
        115: 2,
        116: 3,
        117: 4,
        118: 5,
        119: 0,
        120: 1,
        121: 2,
        122: 3,
        123: 4,
        124: 5,
        125: 6,
    }

    df_input = pd.DataFrame({
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

    for field in fields:
        for option in fields[field]:
            num_abs = fields[field][option]
            if values[num_abs] is True:
                df_input.loc[0, field] = field_abs_to_rel[num_abs]

    return df_input


def on_submit(values, model):
    # validate input
    validate_success = validate_input(values)

    if validate_success == -1:
        invalid_input_missing_fields()
    else:
        df_input = format_input(values)
        prediction = model.predict(df_input)
        give_results(prediction, df_input)
        clear_input(window_main, values)


def warning_clear():
    layout = [
        [sg.Text("Warning: All fields have an entry. Are you sure you want to "
                 "clear your input?")],
        [sg.Button("Yes"), sg.Button("No")]
        ]
    window_warning_clear = sg.Window("Warning",
                                     layout,
                                     modal=True)
    while True:
        event, values = window_warning_clear.read()
        if event == "No" or event == sg.WIN_CLOSED:
            output = "No"
            break
        elif event == "Yes":
            output = "Yes"
            break

    window_warning_clear.close()
    return output


def clear_input(window_main, values):
    for i in range(126):
        window_main[i].reset_group()


def clear_input_helper(window_main, values):
    # check if all fields are entered
    if validate_input(values) == 0:
        response = warning_clear()
        if response == "Yes":
            clear_input(window_main, values)
    else:
        clear_input(window_main, values)


def load_random(window_main, values):
    # set random values
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

    df_input = pd.DataFrame({
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

    for field in fields:
        k = random.choice([v for v in fields[field].values()])
        df_input.loc[0, field] = k

    prediction = model.predict(df_input)
    give_results(prediction, df_input)
    clear_input(window_main, values)

col_1 = [
    [sg.Text("1. What is the mushroom's cap shape?")],
    [
        sg.Radio('bell', 'cap-shape'),      # 0
        sg.Radio('conical', 'cap-shape'),   # 1
        sg.Radio('convex', 'cap-shape'),    # 2
        sg.Radio('flat', 'cap-shape'),      # 3
        sg.Radio('knobbed', 'cap-shape'),   # 4
        sg.Radio('sunken', 'cap-shape'),    # 5
    ],

    [sg.Text("2. What is the mushroom's cap surface?")],
    [
        sg.Radio('fibrous', 'cap-surface'),
        sg.Radio('grooves', 'cap-surface'),
        sg.Radio('scaly', 'cap-surface'),
        sg.Radio('smooth', 'cap-surface'),
    ],

    [sg.Text("3. What is the mushroom's cap color?")],
    [
        sg.Radio('brown', 'cap-color'),
        sg.Radio('buff', 'cap-color'),
        sg.Radio('cinnamon', 'cap-color'),
        sg.Radio('gray', 'cap-color'),
        sg.Radio('green', 'cap-color'),
        sg.Radio('pink', 'cap-color'),
        sg.Radio('purple', 'cap-color'),
        sg.Radio('red', 'cap-color'),
        sg.Radio('white', 'cap-color'),
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
        sg.Radio('attached', 'gill-attachment'),
        sg.Radio('descending', 'gill-attachment'),
        sg.Radio('free', 'gill-attachment'),
        sg.Radio('notched', 'gill-attachment'),
    ],

    [sg.Text("7. What is the mushroom's gill spacing?")],
    [
        sg.Radio('close', 'gill-spacing'),
        sg.Radio('crowded', 'gill-spacing'),
        sg.Radio('distant', 'gill-spacing'),
    ],

    [sg.Text("8. What is the mushroom's gill size?")],
    [
        sg.Radio('broad', 'gill-size'),
        sg.Radio('narrow', 'gill-size'),
    ],

    [sg.Text("9. What is the mushroom's gill color?")],
    [
        sg.Radio('black', 'gill-color'),
        sg.Radio('brown', 'gill-color'),
        sg.Radio('buff', 'gill-color'),
        sg.Radio('chocolate', 'gill-color'),
        sg.Radio('gray', 'gill-color'),
        sg.Radio('green', 'gill-color'),
        sg.Radio('orange', 'gill-color'),
        sg.Radio('pink', 'gill-color'),
        sg.Radio('purple', 'gill-color'),
        sg.Radio('red', 'gill-color'),
        sg.Radio('white', 'gill-color'),
        sg.Radio('yellow', 'gill-color'),
    ],

    [sg.Text("10. What is the mushroom's stalk shape?")],
    [
        sg.Radio('enlarging', 'stalk-shape'),
        sg.Radio('tapering', 'stalk-shape'),
    ],

    [sg.Text("11. What is the mushroom's stalk root?")],
    [
        sg.Radio('bulbous', 'stalk-root'),
        sg.Radio('club', 'stalk-root'),
        sg.Radio('cup', 'stalk-root'),
        sg.Radio('equal', 'stalk-root'),
        sg.Radio('rhizomorphs', 'stalk-root'),
        sg.Radio('rooted', 'stalk-root'),
        sg.Radio('missing', 'stalk-root'),
    ],

    [sg.Text("12. What is the mushroom's stalk surface, above the ring?")],
    [
        sg.Radio('fibrous', 'stalk-surface-above-ring'),
        sg.Radio('scaly', 'stalk-surface-above-ring'),
        sg.Radio('silky', 'stalk-surface-above-ring'),
        sg.Radio('smooth', 'stalk-surface-above-ring'),
    ],

    [sg.Text("13. What is the mushroom's stalk surface, below the ring?")],
    [
        sg.Radio('fibrous', 'stalk-surface-below-ring'),
        sg.Radio('scaly', 'stalk-surface-below-ring'),
        sg.Radio('silky', 'stalk-surface-below-ring'),
        sg.Radio('smooth', 'stalk-surface-below-ring'),
    ],

    [sg.Text("14. What is the mushroom's stalk color, above the ring?")],
    [
        sg.Radio('brown', 'stalk-color-above-ring'),
        sg.Radio('buff', 'stalk-color-above-ring'),
        sg.Radio('cinnamon', 'stalk-color-above-ring'),
        sg.Radio('gray', 'stalk-color-above-ring'),
        sg.Radio('orange', 'stalk-color-above-ring'),
        sg.Radio('pink', 'stalk-color-above-ring'),
        sg.Radio('red', 'stalk-color-above-ring'),
        sg.Radio('white', 'stalk-color-above-ring'),
        sg.Radio('yellow', 'stalk-color-above-ring'),
    ],

    [sg.Text("15. What is the mushroom's stalk color, below the ring?")],
    [
        sg.Radio('brown', 'stalk-color-below-ring'),
        sg.Radio('buff', 'stalk-color-below-ring'),
        sg.Radio('cinnamon', 'stalk-color-below-ring'),
        sg.Radio('gray', 'stalk-color-below-ring'),
        sg.Radio('orange', 'stalk-color-below-ring'),
        sg.Radio('pink', 'stalk-color-below-ring'),
        sg.Radio('red', 'stalk-color-below-ring'),
        sg.Radio('white', 'stalk-color-below-ring'),
        sg.Radio('yellow', 'stalk-color-below-ring'),
    ],

    [sg.Text("16. What is the mushroom's veil type?")],
    [
        sg.Radio('partial', 'veil-type'),
        sg.Radio('universal', 'veil-type'),
    ],

    [sg.Text("17. What is the mushroom's veil color?")],
    [
        sg.Radio('brown', 'veil-color'),
        sg.Radio('orange', 'veil-color'),
        sg.Radio('white', 'veil-color'),
        sg.Radio('yellow', 'veil-color'),
    ],

    [sg.Text("18. What is the mushroom's ring number?")],
    [
        sg.Radio('none', 'ring-number'),
        sg.Radio('one', 'ring-number'),
        sg.Radio('two', 'ring-number'),
    ],

    [sg.Text("19. What is the mushroom's ring type?")],
    [
        sg.Radio('cobwebby', 'ring-type'),
        sg.Radio('evanescent', 'ring-type'),
        sg.Radio('flaring', 'ring-type'),
        sg.Radio('large', 'ring-type'),
        sg.Radio('none', 'ring-type'),
        sg.Radio('pendant', 'ring-type'),
        sg.Radio('sheathing', 'ring-type'),
        sg.Radio('zone', 'ring-type'),
    ],

    [sg.Text("20. What is the mushroom's spore print color?")],
    [
        sg.Radio('black', 'spore-print-color'),
        sg.Radio('brown', 'spore-print-color'),
        sg.Radio('buff', 'spore-print-color'),
        sg.Radio('chocolate', 'spore-print-color'),
        sg.Radio('green', 'spore-print-color'),
        sg.Radio('orange', 'spore-print-color'),
        sg.Radio('purple', 'spore-print-color'),
        sg.Radio('white', 'spore-print-color'),
        sg.Radio('yellow', 'spore-print-color'),
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
window_main = sg.Window("Mushroom Classifier", layout, size=(1200, 600))

# load in model
with open('model.sav', 'rb') as f:
    model = pickle.load(f)

# main event loop
while True:
    event, values = window_main.read()
    # End program if user closes window_main
    if event == sg.WIN_CLOSED:
        break
    elif event == "Load Random":
        load_random(window_main, values)
    elif event == "Clear Input":
        clear_input_helper(window_main, values)
    elif event == "Submit":
        on_submit(values, model)

window_main.close()
