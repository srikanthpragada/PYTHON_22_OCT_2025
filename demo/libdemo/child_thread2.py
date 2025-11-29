from threading import Thread
import threading

def numbers(num = 10):
    for n in range(1, num + 1):
        print(n)


t = Thread(target = numbers, args = (5,))
t.start()

#t.join()
print(threading.active_count())
print("The End!")
# t = Thread(target = numbers)
# t.start()
