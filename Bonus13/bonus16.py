import FreeSimpleGUI as sg
import shutil

layout = [[sg.Text('Select file to compress: '),sg.Input(tooltip='path to file',key='in_path'),sg.Button('Chose')],
          [sg.Text('Select destination folder: '),sg.Input(tooltip='path to file',key='out_path'),sg.Button('Chose')],
          [sg.Button('Compress'),sg.Text(key='notice')]]

window = sg.Window('File Zipper',layout)
while True:
    event, values = window.read()
    path_compress = values['in_path']
    path_for_save = values['out_path']
    if event == 'Compress':
        shutil.make_archive(path_for_save,'zip',path_compress)
    elif event == sg.WINDOW_CLOSED():
        break

window.close()



