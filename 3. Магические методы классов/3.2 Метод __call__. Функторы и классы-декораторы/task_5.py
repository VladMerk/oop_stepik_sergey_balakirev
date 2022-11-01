class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ['ul', 'ol'] else 'ul'

    def __call__(self, lst):
        string = f'<{self.type_list}>\n'
        for item in lst:
            string += f"<li>{item}</li>\n"
        string += f"</{self.type_list}>"
        return string

# Test
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html.replace(' ', '').replace('\n', ''))
