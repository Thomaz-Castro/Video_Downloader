from pytube import YouTube

url = str(input('Insira o link do video: '))

youtube = YouTube(url)

print('Titulo: {}'.format(youtube.title))

stream= youtube.streams.get_highest_resolution()

stream.download()
