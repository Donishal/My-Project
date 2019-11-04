import queue
l = queue.Queue(maxsize=10)
l.put(5)
l.put(6)
l.put(7)
print(l.get())