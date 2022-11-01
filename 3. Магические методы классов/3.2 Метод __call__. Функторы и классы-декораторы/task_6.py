class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, items: dict):
        method = items.get('method', 'GET')
        return f"GET: {self.__fn(items)}" if method == 'GET' else None

@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
