class TrainArrival:
    def __init__(self, station_name: str, service_direction: str, train_run_number: str, route: str, destination: str, arrival_time: str):
        self.station_name = station_name
        self.service_direction = service_direction
        self.train_run_number = train_run_number
        self.route = route
        self.destination = destination
        self.arrival_time = arrival_time