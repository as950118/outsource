from rx import Observable, Observer

class PrintObserver(Observer):
    def on_next(self, value):
        print("Value :", value)
    def on_error(self, error):
        print("Error :", error)
    def on_completed(self):
        print("Completed")

if __name__ == '__main__':
    source_1 = Observable.from_iterable(range(100))
    source_2 = Observable.from_iterable("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    source_1.merge(source_2).subscribe(PrintObserver())
