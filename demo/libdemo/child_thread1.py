from threading import Thread


class PrintThread(Thread):
    def run(self):
        for n in range(1,11):
            print(n)

t = PrintThread()
t.start()
