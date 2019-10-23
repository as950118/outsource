from rx import Observable, Observer

class PrintObserver(Observer):
    def on_next(self, value):
        print("Value :", value)
    def on_error(self, error):
        print("Error :", error)
    def on_completed(self):
        print("Completed")

if __name__ == '__main__':
    source = Observable.from_iterable(range(10))
    source.filter(lambda x: x%2).subscribe(PrintObserver())