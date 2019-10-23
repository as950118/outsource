from rx import Observable, Observer
from rx.testing import marbles

class PrintObserver(Observer):
    def on_next(self, value):
        print("Value :", value)
    def on_error(self, error):
        print("Error :", error)
    def on_completed(self):
        print("Completed")

if __name__ == '__main__':
    source_1 = Observable.from_marbles("1-2-3-|")
    source_2 = Observable.from_marbles("-a-b-c|")
    print(source_1.merge(source_2).to_blocking().to_marbles())
