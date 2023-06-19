import webbrowser
url = 'https://steam.oxxostudio.tw/category/python/ai/opencv-read-video.html'
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(url)