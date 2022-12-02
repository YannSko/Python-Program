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
    [sg.B("+", key="-+-")],
    [sg.B("-", key="---")],
    [sg.B("/", key="-/-")],
    [sg.B("=", key="-=-")],
]

printed = [
    [sg.T()]
]

layout = [
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(
        col_2), sg.VerticalSeparator(), sg.Col(col_3), sg.VerticalSeparator(),
        sg.Col(col_4)]
]

window = sg.Window("Calculatrce", layout)
event, values = window.read()
print(event, values)
