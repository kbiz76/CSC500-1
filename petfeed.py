feed_types = ["treat", "meal"]
feed_times = ["morning", "night"]

for i in range(len(feed_times)):
  for j in range(len(feed_types)):
    print(f"{feed_times[i]} : {feed_types[j]}")
