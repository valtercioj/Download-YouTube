from pytube import YouTube

def youtube_download(url):
	try:
		print('Seu video está baixando. Aguarde alguns segundos')
		YouTube(url).streams.first().download()
		print('Seu Download terminou')
	except:
		print('erro na tentativa')
