from emoji import emojize
from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
from os import getenv, remove, listdir
import moviepy.editor as mp
from os.path import isfile, join

tit = ('YOUTUBE DOWNLOADER')
dmsg = ('Baixado com sucesso!')
ll = emojize(str(':magnifying_glass_tilted_left:'))

#layout
sg.theme('DarkBlue17')
layout_column = [
    [sg.Text('YOUTUBE DOWNLOADER', justification='center')],
    [sg.Text('Insira o link'),sg.Input(key='url'), sg.Button(ll)],
    [sg.Text('  -- título do vídeo --  ', key='tiltulu', background_color='#655A80')],
    [sg.Text('Download:')],
    [sg.Button('MP3', size=(10,3)), sg.Button('MP4 - MAX', size=(10,3)), sg.Button('MP4 - MIN', size=(10,3))],
    [sg.Text('', key='douloadi')]
]
layout = [[sg.Column(layout_column, element_justification='center')]]

useerr = getenv("USERNAME")


#janela
janela = sg.Window('Video Downloader', layout)

#eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    youtube = YouTube((valores['url']))
    if eventos == ll:
        vdtt = youtube.title
        vdttd = ['TÍTULO:  ', vdtt]
        vdttd = ''.join(vdttd)

        janela['tiltulu'].update(vdttd)

    if eventos == 'MP3':
        stream = youtube.streams.get_audio_only()
        cam = ('mp')
        ddpast = str('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)

        path = 'mp'
        files = list([f for f in listdir(path) if isfile(join(path, f))])
        files = sorted(files)
        nomearq = str(files[1])


        cc = [cam,'\\' , nomearq]
        cc = ''.join(cc)
        clip = mp.AudioFileClip(cc)
        nomearq3 = nomearq.replace('.mp4', '.mp3')
        ccdd = [ddpast,'\\' , nomearq3]
        ccdd = ''.join(ccdd)
        clip.write_audiofile(ccdd)
        remove(cc)
        janela['douloadi'].update(dmsg)

    elif eventos == 'MP4 - MAX':
        stream = youtube.streams.get_highest_resolution()
        cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)
        janela['douloadi'].update(dmsg)
    elif eventos == 'MP4 - MIN':
        stream = youtube.streams.get_lowest_resolution()
        cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)
        janela['douloadi'].update(dmsg)
    
