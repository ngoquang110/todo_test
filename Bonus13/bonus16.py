import FreeSimpleGUI as sg
import shutil
import os

layout = [[sg.Text('Select file to compress: '),sg.Input(tooltip='path to file',key='in_path'),sg.FilesBrowse('Choose')],
          [sg.Text('Select destination folder: '),sg.Input(tooltip='path to folder',key='out_path'),sg.FolderBrowse('Choose')],
          [sg.Button('Compress'),sg.Text(key='notice')]]

window = sg.Window('File Zipper',layout)
while True:
    event, values = window.read()
    if event == 'Compress':
        path_compress = values['in_path']
        path_for_save = values['out_path']
        print(path_compress)
        print(path_for_save)
        if os.path.exists(path_compress) and os.path.exists(path_for_save):
            shutil.make_archive(path_for_save,'zip',path_compress)
            window['notice'].update('File compressed successfully!')
        else:
            window['notice'].update('Please select valid file and folder paths.')
    if event == sg.WINDOW_CLOSED():
        break

window.close()



