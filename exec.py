import PySimpleGUI as sg


def tela():
    #layout
    sg.theme('Black')
    layout = [
        [sg.Text('LABIRINTO', font=('',12,), size=(24,0)),sg.Button('START',size=(7)), sg.Button('EXIT', size=(7))],
        [sg.Output(size=(50,20))]
    ]
    return sg.Window('ATIVIDADE', layout=layout, finalize=True)

janela = tela()

while True:
    window,event,values = sg.read_all_windows()
    
    if window == janela and event == sg.WIN_CLOSED:
        break
    if window == janela and event == "START":
        from Labirinto_v2 import *
        labirinto = Labirinto(labirinto_map)
        labirinto.achar_saida()
    elif window == janela and event == "EXIT":
        break