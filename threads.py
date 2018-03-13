import threading


class iam_not_understanding(threading.Thread):
    def run(self):
        for _ in range(10):
            may_be=print(threading.currentThread().getName())
            print(may_be)

x = iam_not_understanding(name='i can\n')
y = iam_not_understanding(name='may be let\'s see')
x.start()
y.start()
