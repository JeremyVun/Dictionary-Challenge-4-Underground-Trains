"""
Dictionary Challenge 4 - Underground Trains

Description:
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Example:
Input:
  actions = [
    "checkin","checkin","checkin","checkout","checkout","checkout","get_avg_time","get_avg_time","checkin","get_avg_time","checkout","get_avg_time"
  ]
  args: [
    [45,"Leyton",3],
    [32,"Paradise",8],
    [27,"Leyton",10],
    [45,"Waterloo",15],
    [27,"Waterloo",20],
    [32,"Cambridge",22],
    ["Paradise","Cambridge"],
    ["Leyton","Waterloo"],
    [10,"Leyton",24],
    ["Leyton","Waterloo"],
    [10,"Waterloo",38],
    ["Leyton","Waterloo"]
  ]

Correct outputs from get_avg_time:
  [
    14.00, # (Paradise, Cambridge)
    11.00, # (Leyton, Waterloo)
    11.00, # (Leyton, Waterloo)
    12.00 # (Leyton, Waterloo)
  ]
"""

from solution import UndergroundSystem


########
# This code wil run your solution against a bunch of test cases
########
from tests.runner import run_tests

if __name__ == "__main__":
  run_tests(UndergroundSystem)