from statistics import mean

class UndergroundSystem:
  # Constructor
  def __init__(self):
    self.activity = {}
    self.travel_times = {}

  # check in the passenger to the station at specified time
  def checkin(self, id, station, time):
    self.activity[id] = (station, time)

  # check out the passenger from station
  def checkout(self, id, station, time):
    start = self.activity[id]
    path = (start[0], station)

    if path not in self.travel_times:
      self.travel_times[path] = []

    self.travel_times[path].append(time - start[1])

  # Returns the average time it takes to travel between two stations if the data is available
  def get_avg_time(self, start_station, end_station):
    path = (start_station, end_station)
    if path in self.travel_times:
      return mean(self.travel_times[path])
    else:
      return None