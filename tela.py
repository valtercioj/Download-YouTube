from main import youtube_download
import PySimpleGUI as sg
sg.theme('DarkRed1')
layout = [
	[sg.Text('Coloque o link do video'), sg.Input(key='url', justification='center')],
	[sg.Button('enviar',size=(10,1))]
	,
	[sg.Output(size=(70,10))]
]

window = sg.Window('Download YouTube', layout, element_justification='center')

while True:
	event, values = window.read()

	url = values['url']
	youtube_download(url)