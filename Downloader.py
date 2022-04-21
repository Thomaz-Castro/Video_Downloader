from pytube import YouTube
from os import getenv, remove, listdir
import moviepy.editor as mp
from os.path import isfile, join

useerr = getenv("USERNAME")

print(('\033[1;31m'), ('-='*15),'YOUTUBE DOWNLOADER', ('=-'*15), ('\033[m'))

url = str(input('Insira o link do video: '))
youtube = YouTube(url)

vdtt = youtube.title

print('')
print('-'*35)
print('Titulo: {}'.format(youtube.title))
print('')

ex = input('Selecione um formato: \n'
'[ 1 ] - mp4 (video normal)\n'
'[ 2 ] - mp3 (apenas audio)\n'
'Selecione: ')


print('')
print('-'*35)
print('')

if ex == '1':
    qld = input('escolha a qualidade: \n'
    '[ 1 ] - Qualidade Maxima\n'
    '[ 2 ] - Qualidade Minima\n'
    'Selecione: ')

    if qld == '1':
        stream = youtube.streams.get_highest_resolution()
        cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)
        print('')
        print('-'*35)
        print('\033[1;32mBaixado com sucesso!')
    
    elif qld == '2':
        stream = youtube.streams.get_lowest_resolution()
        cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)
        print('')
        print('-'*35)
        print('\033[1;32mBaixado com sucesso!')
    else:
        print('Opção invalida')
elif ex == '2':
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
    print('')
    print('\033[1;32mBaixado com sucesso!')

else:
    print('Opção invalida')