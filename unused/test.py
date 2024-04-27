import requests


url = "https://tiktok-download-video-no-watermark.p.rapidapi.com/tiktok/info"

querystring = {"url":"https://vt.tiktok.com/ZGJBQHoHA/"}

headers = {
	"X-RapidAPI-Key": "60cfa0ace3msh565a0aa5168d429p1ce973jsnf886a97a90a7",
	"X-RapidAPI-Host": "tiktok-download-video-no-watermark.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())