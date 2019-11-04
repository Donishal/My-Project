import datetime
x = int("3456321231")
print(datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))