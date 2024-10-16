# Write your code here
import tkinter as tk
import services.ctaservice as ctaservice



window = tk.Tk()
# greeting = tk.Label(text="Hello, world!", background="purple", width = 100, height = 100)
# greeting.pack()

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SAVA&apikey=demo'
#r  = requests.get(url)
#data = r.json()

myTrainArrivals = ctaservice.getTrainArrivals()

# Display the parsed data
for train in myTrainArrivals:
    trainString = f"Station: {train.station_name}, Service: {train.service_direction}, Train: {train.train_run_number}, "
    trainString += f"Route: {train.route}, Destination: {train.destination}, Arrival: {train.arrival_time}"
    
    print(train.route)
    widgetBackground = "red"
    if (train.route == "Brn"):
        widgetBackground = "brown"
    elif (train.route == "Purple"):
        #need to check this condition train.route will be something else
        widgetBackground = "purple"
    trainUi = tk.Label(text=trainString, background=widgetBackground, width = 100, height = 10)
    trainUi.pack()


window.mainloop()
