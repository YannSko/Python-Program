import PySimpleGUI as sg

col_1 = [
    [sg.B('1')],
    [sg.B('2')],
    [sg.B('3', key="-3-")],
]
col_2 = [
    [sg.B('4', key="-4-")],
    [sg.B('5', key="-5-")],
    [sg.B('6', key="-6-")],
]
col_3 = [
    [sg.B('7', key="-7-")],
    [sg.B('8', key="-8-")],
    [sg.B('9', key="-9-")],
]

col_4 = [
    [sg.B('+', key="-PLUS-")],
    [sg.B('-', key="-MINUS-")],
    [sg.B('*', key="-MULTI-")],
    [sg.B('/', key="-DEVID-")],
    [sg.B('=', key="-EQUAL-")],
    [sg.B('-->', key="-CLEAR-")],
]

# printed = [
#   [sg.T()]
# ]

layout = [
    [sg.I(size=(13, 1), font=(None, 30), key="-INPUT-", enable_events=True)],
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(
        col_2), sg.VerticalSeparator(), sg.Col(col_3), sg.VerticalSeparator(),
        sg.Col(col_4)]
]

num = [int(i) for i in range(10)]
window = sg.Window("Calculatrce", layout)

history = ''
operator = ["-DEVID-", "-MULTI-", "-PLUS-", "-MINUS-"]
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break

    elif event in num:
        if len(history) < 12:
            history += event
            window["-INPUT-"].update(int(history))
    elif event in operator:
        op = event
        num_1 = float(history)
        history = ''
    elif event == "-EQUAL-":
        num_2 = int(history)
        if op == "-PLUS-":
            result = num_1 + num_2
        elif op == "-MINUS-":
            result = num_1 - num_2
        elif op == "-MULTI-":
            result = num_1 * num_2
        elif op == "-DEVID-":
            result = num_1 / num_2
        window["-INPUT-"].update(float(result))
    elif event == "-CLEAR-":
        if len(history) > 0:
            history = history[:-1]
            window["-INPUT-"].update(history)

    print(event, values)
