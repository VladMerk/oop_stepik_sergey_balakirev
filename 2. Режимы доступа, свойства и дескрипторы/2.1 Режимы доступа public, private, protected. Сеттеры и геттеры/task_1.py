class Clock:
    def __init__(self, tm=0) -> None:
        if self.__check_time(tm):
            self.__time = tm

    def __check_time(self, tm):
        if type(tm) == int and 0 < tm < 100_000:
            return True
        else:
            False

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)

# Test
if __name__ == "__main__":

    assert isinstance(clock, Clock) and hasattr(Clock, 'set_time') and hasattr(
        Clock, 'get_time'), "в классе Clock присутствуют не все методы"

    assert clock.get_time() == 4530, "текущее время в объекте clock не равно 4530"

    clock.set_time(10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(-10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(1000001)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
