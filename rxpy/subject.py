from rx import Observable, Observer
from rx.subjects import Subject

class PrintObserver(Observer):
    def on_next(self, value):
        print("Value :", value)
    def on_error(self, error):
        print("Error :", error)
    def on_completed(self):
        print("Completed")

subject = Subject()
subject.subscribe(PrintObserver())
for i in range(10):
    subject.on_next(i)
subject.on_completed()