import PySimpleGUI as sg


sg.theme("DarkGrey3")
col_1 = [
        [sg.B('7', size=(8, 4), font="bold"), sg.B('8', size=(8, 4),
                                                   font="bold"), sg.B('9', size=(8, 4), font="bold")],
        [sg.B('4', size=(8, 4), font="bold"), sg.B('5', size=(8, 4),
                                                   font="bold"), sg.B('6', size=(8, 4), font="bold")],
        [sg.B('1', size=(8, 4), font="bold"), sg.B('2', size=(8, 4),
                                                   font="bold"), sg.B('3', size=(8, 4), font="bold")],
        [sg.B('+/-', size=(8, 4), font="bold", key="-OPOSITE-"), sg.B('0', size=(8,
                                                                                 4), font="bold"), sg.B('.', size=(8, 4), font="bold", key="-DOT-")],
]
col_2 = [
        [sg.B('*', size=(8, 4), key="-MULTI-", font="bold")],
        [sg.B('-', size=(8, 4), key="-MINUS-", font="bold")],
        [sg.B('+', size=(10, 5), key="-PLUS-", font="bold")],
]
col_3 = [
        [sg.B('/', size=(8, 4), key="-DEVID-", font="bold")],
        [sg.B('-->', size=(8, 4), key="-CLEAR-", font="bold")],
        [sg.B('CE', size=(8, 4), key="-CEVERY-", font="bold")],
        [sg.B('=', size=(8, 4), key="-EQUAL-", font="bold")],
]

layout = [
    [sg.I(size=(13, 1), font=(None, 60), key="-INPUT-", enable_events=True)],
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2), sg.Col(col_3)],
]
window = sg.Window("Calculator", layout)
num = [str(i) for i in range(10)]
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
    elif event == "-CEVERY-":
        history = ''
        num_1 = 0
        num_2 = 0
        op = ''
        window["-INPUT-"].update(history)
    elif event == "-OPOSITE-":
        history = str(int(history) * -1)
        window["-INPUT-"].update(history)

    print(event, values)
