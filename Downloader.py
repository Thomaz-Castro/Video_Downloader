from pytube import YouTube
from os import getenv, remove
import moviepy.editor as mp

useerr = getenv("USERNAME")

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
'obs - ler README\n'
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
        print('Baixado com sucesso!')
    
    elif qld == '2':
        stream = youtube.streams.get_lowest_resolution()
        cam = ('C:\\Users\\{}\\Downloads'.format(useerr))
        stream.download(cam)
        print('Baixado com sucesso!')
    else:
        print('Opção invalida')
elif ex == '2':
    stream = youtube.streams.get_audio_only()
    cam = str('C:\\Users\\{}\\Downloads'.format(useerr))
    stream.download(cam)
    cc = [cam,'\\' , vdtt,'.mp4']
    cc = ''.join(cc)
    clip = mp.AudioFileClip(cc)
    ccdd = [cam,'\\' , vdtt, '\\' ,  '.mp3']
    ccdd = ''.join(ccdd)
    clip.write_audiofile(ccdd)
    remove(cc)
    print('Baixado com sucesso!')

else:
    print('Opção invalida')
