from timeit import Timer
from statistics import mean
from .tests import build_tests

# Run a single test
def run_test(clazz, test):
  obj = clazz()
  actions = test.data["actions"]
  args = test.data["args"]
  
  actual = []

  for i in range(len(actions)):
    if actions[i] == "checkin":
      obj.checkin(args[i][0], args[i][1], args[i][2])
    elif actions[i] == "checkout":
      obj.checkout(args[i][0], args[i][1], args[i][2])
    else:
      avg_time = obj.get_avg_time(args[i][0], args[i][1])
      if avg_time != None:
        avg_time = round(avg_time, 2)
        actual.append(avg_time)

  expected = test.answer
  if len(actual) == len(expected):
    for i in range(len(actual)):
      if actual[i] != expected[i]:
        raise Exception(f" expected={expected}, actual={actual}")
  else:
    raise Exception(f" expected={expected}, actual={actual}")
    
  

# Run all the tests
def run_tests(clazz, runs=1000):
  testNum = 0
  test_times = []

  try:
    for test in build_tests():
      testNum += 1
      print(f"[RUNNING] Test {testNum}...", end="\r")

      timer = Timer(lambda: run_test(clazz, test))
      ms = timer.timeit(runs) * 1000 / runs
      
      test_times.append(ms)
      print(f"[PASS] Test {testNum}: {ms:.5f}ms")

    print(f"Average time: {mean(test_times):.5f}ms")

  except Exception as e:
    print(f"[FAIL] Test {testNum}: {e}")