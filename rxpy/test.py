from rx import Observable, Observer

#observable은 value, error, complete 세가지 이벤트를 가짐
def observable(observer):
    observer.on_next("Hello")
    observer.on_next("World")
    #observer.on_error("error")
    observer.on_completed()

#observer의 값을 출력하는 함수
class PrintObserver(Observer):
    #value
    def on_next(self, value):
        print("Value :", value)
    #error
    def on_error(self, error):
        print("Error :", error)
    # complete
    def on_completed(self):
        print("Completed")

if __name__ == '__main__':
    source = Observable.create(observable)
    source.subscribe(PrintObserver())