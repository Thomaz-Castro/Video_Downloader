from os import getenv, listdir, remove
from os.path import isfile, join
import moviepy.editor as mp
from emoji import emojize
from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube, Playlist

tit = ('YOUTUBE DOWNLOADER')
dmsg = ('Baixado com sucesso!')
ll = emojize(str(':magnifying_glass_tilted_left:'))


#layout
sg.theme('DarkBlue17')
layout_column = [
    [sg.Text('YOUTUBE DOWNLOADER', justification='center')],
    [sg.Text('Insira o link'),sg.Input(key='url'), sg.Button(ll)],
    [sg.Checkbox('É playlist?', default=False, key='playlist') ,sg.Text('===================================', key='tiltulu', background_color='#655A80', size=(35, 1), border_width=5)],
    [sg.Text('Download:')],
    [sg.Button('MP3', size=(10,3)), sg.Button('MP4 - MAX', size=(10,3)), sg.Button('MP4 - MIN', size=(10,3))],
    [sg.ProgressBar(100, orientation="h", size=(50,17), key='barrr', border_width=(1))],
    [sg.Text('', key='douloadi')]
]
layout = [[sg.Column(layout_column, element_justification='center')]]

useerr = getenv("USERNAME")


#janela
janela = sg.Window('Video Downloader', layout)

#eventos

jjj = 0

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    

    if valores['playlist'] == False:

        youtube = YouTube((valores['url']))
        
        vdtt = youtube.title

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

            janela['douloadi'].update('50% - Convertendo...')
            janela['barrr'].update(50)
            
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
            for i in range(100):
                if i == 0:
                    i += 50
                eventos, valores =janela.read(20)
                janela['barrr'].update(i+20)
            remove(cc)
            janela['douloadi'].update(dmsg)

            for i in range(125):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)
            

        elif eventos == 'MP4 - MAX':
            janela['douloadi'].update('')
            janela['barrr'].update(0)
            stream = youtube.streams.get_highest_resolution()
            cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
            for i in range(100):
                eventos, valores =janela.read(20)
                janela['barrr'].update(i+20)
            stream.download(cam)

            janela['douloadi'].update(dmsg)
            for i in range(125):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)

        elif eventos == 'MP4 - MIN':
            janela['douloadi'].update('')
            janela['barrr'].update(0)
            stream = youtube.streams.get_lowest_resolution()
            cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
            for i in range(100):
                eventos, valores =janela.read(20)
                janela['barrr'].update(i+20)
            stream.download(cam)
            janela['douloadi'].update(dmsg)
            for i in range(125):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)

            
    else:
    
        playmus = Playlist(valores['url'])
        bartot = 100/(len(playmus.video_urls))
        progresso = bartot
        blockcc = 0
        percenti = 0

        vdtt = playmus.title

        if eventos == ll:
            vdtt = playmus.title
            vdttd = ['TÍTULO:  ', vdtt]
            vdttd = ''.join(vdttd)

            janela['tiltulu'].update(vdttd)

        if eventos == 'MP3':
            for urlss in playmus.video_urls:
                linkurl = str(urlss)
                if blockcc != 0:
                    progresso += bartot
                youtube = YouTube(linkurl)

                vdtt = youtube.title
                janela['tiltulu'].update(vdtt)

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
                janela['barrr'].update(progresso)
                blockcc = blockcc + 1
                percenti = round((blockcc/len(playmus.video_urls)*100),2)
                perstr = (str(percenti)+'%')
                janela['douloadi'].update(perstr)


            
            blockcc = 0
            janela['douloadi'].update(dmsg)
            for i in range(150):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)

        if eventos == 'MP4 - MAX':
            for urlss in playmus.video_urls:
                linkurl = str(urlss)
                if blockcc != 0:
                    progresso += bartot
                youtube = YouTube(linkurl)

                vdtt = youtube.title
                janela['tiltulu'].update(vdtt)

                stream = youtube.streams.get_highest_resolution()
                cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
                stream.download(cam)
                janela['barrr'].update(progresso)
                blockcc = blockcc + 1
                percenti = round((blockcc/len(playmus.video_urls)*100),2)
                perstr = (str(percenti)+'%')
                janela['douloadi'].update(perstr)

            blockcc = 0
            janela['douloadi'].update(dmsg)
            for i in range(150):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)
            
        if eventos == 'MP4 - MIN':
            for urlss in playmus.video_urls:
                linkurl = str(urlss)
                if blockcc != 0:
                    progresso += bartot
                youtube = YouTube(linkurl)

                vdtt = youtube.title
                janela['tiltulu'].update(vdtt)

                stream = youtube.streams.get_lowest_resolution()
                cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
                stream.download(cam)
                janela['barrr'].update(progresso)
                blockcc = blockcc + 1
                percenti = round((blockcc/len(playmus.video_urls)*100),2)
                perstr = (str(percenti)+'%')
                janela['douloadi'].update(perstr)

            blockcc = 0
            janela['douloadi'].update(dmsg)
            for i in range(150):
                eventos, valores =janela.read(100)
            janela['douloadi'].update('')
            janela['tiltulu'].update('===================================')
            janela['barrr'].update(0)
