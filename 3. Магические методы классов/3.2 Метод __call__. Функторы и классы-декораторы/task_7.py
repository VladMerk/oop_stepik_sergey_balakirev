class Handler:
    def __init__(self, methods = ('GET')):
        self.__methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            m = request.get('method', 'GET')
            if m in self.__methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

    def post(self, func, request, *args, **kwargs):
        return f"POST: {func(request)}"

if __name__ == "__main__":
    @Handler(methods=('GET', 'POST'))
    def contact2(request):
        return "контакты"

    assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
    assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"

    @Handler(methods=('POST'))
    def index(request):
        return "index"

    assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
    assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
    assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
