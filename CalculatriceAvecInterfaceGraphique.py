import PySimpleGUI as sg

col_1 = [
    [sg.B("1", key="-1-")],
    [sg.B("2", key="-2-")],
    [sg.B("3", key="-3-")],
]
col_2 = [
    [sg.B("4", key="-4-")],
    [sg.B("5", key="-5-")],
    [sg.B("6", key="-6-")],
]
col_3 = [
    [sg.B("7", key="-7-")],
    [sg.B("8", key="-8-")],
    [sg.B("9", key="-9-")],
]

col_4 = [
    [sg.B("+", key="-PLUS-")],
    [sg.B("-", key="-MINUS-")],
    [sg.B("/", key="-DEVID-")],
    [sg.B("=", key="-EQUAL-")],
    [sg.B("-->", key="-CLEAR-")],
]

# printed = [
#   [sg.T()]
# ]

layout = [
    [sg.I(font=(None, 30), size=(13, 1), key="-INPUT-")],
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(
        col_2), sg.VerticalSeparator(), sg.Col(col_3), sg.VerticalSeparator(),
        sg.Col(col_4)]
]

num = [str(i) for i in range(10)]
window = sg.Window("Calculatrce", layout)
history = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        window.close()
    elif event in num:
        history += num
        window["-INPUT-"].update(event)
