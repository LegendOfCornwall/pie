import tkinter as tk
from tkinter.font import Font
import services.ctaservice as ctaservice

class CustomView(tk.Frame):
    def __init__(self, parent, title, number, color, runNumber, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        if (color == "brown"): 
            bgColor = "#A03232"
        else:
            bgColor = "purple"
        # Set background color for the entire frame
        self.configure(bg=bgColor, highlightbackground="black", highlightthickness=1, bd=0)
        self.configure(width="100")

        self.text_frame = tk.Frame(self, bg=bgColor)
        self.text_frame.pack(side="left",fill="both",padx=20, pady=10)
        
        self.description_label = tk.Label(
            self.text_frame,
            text=color.capitalize() + " Line #" + runNumber + " to",
            font=Font(size=16, weight="bold"),
            bg=bgColor,
            fg="white",
            anchor="w",
            justify="left"
        )
        self.description_label.pack(side="top", fill="x")
        # Title
        self.title_label = tk.Label(
            self.text_frame, 
            text=title, 
            font=Font(size=32, weight="bold"), 
            bg=bgColor,  # Set background color
            fg="white", # Set text color
            anchor="w",
            justify="left"
        )
        self.title_label.pack(side="top")
        
        # Number
        self.number_label = tk.Label(
            self, 
            text=str(number) + " min", 
            font=Font(size=32, weight="bold"), 
            bg=bgColor,  # Set background color
            fg="white"  # Set text color
        )
        self.number_label.pack(side="right", padx="20")

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
    
    print(trainString)

    if (train.route == "P"):
        custom_view = CustomView(window, train.destination, train.arrival_time, "purple", train.train_run_number)
    else:
        custom_view = CustomView(window, train.destination, train.arrival_time, "brown", train.train_run_number)

    custom_view.pack(fill="x")  # Fill the width of the window, limit height

    print(train.route)
    widgetBackground = "red"
    if (train.route == "Brn"):
        widgetBackground = "brown"
    elif (train.route == "Purple"):
        #need to check this condition train.route will be something else
        widgetBackground = "purple"
    trainUi = tk.Label(text=trainString, background=widgetBackground, width = 100, height = 10)
    # trainUi.pack()


window.mainloop()
