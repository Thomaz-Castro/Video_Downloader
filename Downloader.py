from pytube import YouTube
from os import getenv

useerr = getenv("USERNAME")

# https://www.youtube.com/watch?v=lac3TYlarFM

url = str(input('Insira o link do video: '))
youtube = YouTube(url)

print('')
print('-'*35)
print('Titulo: {}'.format(youtube.title))
print('')

ex = input('Selecione um formato: \n'
'[ 1 ] - mp4 (video normal)\n'
'[ 2 ] - mp3 (apenas audio)\n'
'Selecione: ')

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
    print('Função sendo desenvolvida')

else:
    print('Opção invalida')
