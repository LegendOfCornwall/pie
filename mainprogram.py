# Write your code here
import tkinter as tk
import requests

window = tk.Tk()
greeting = tk.Label(text="Hello, world!", background="purple", width = 100, height = 100)
greeting.pack()

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SAVA&apikey=demo'
#r  = requests.get(url)
#data = r.json()

baseCtaUrl = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx/query?mapid=2&key="
ctaKey = "38baeaf33f1745baaa96c6fdd45b0820"
fullCtaUrl = baseCtaUrl + ctaKey

ctareq = requests.get(fullCtaUrl)
#ctaData = ctareq.json()

print(ctareq.content)

window.mainloop()
