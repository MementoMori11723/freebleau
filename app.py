from flet import Page, TextField, Row, IconButton, icons, app
def main(page: Page):
    page.title = "Flet app"
    page.vertical_alignment = "center"
    txt = TextField(value="0",text_align="center",width=100)
    def minus(e):
        txt.value = int(txt.value) - 1
        page.update()
    def plus(e):
        txt.value = int(txt.value) + 1
        page.update()
    page.add(Row([IconButton(icons.REMOVE,on_click=minus),txt,IconButton(icons.ADD,on_click=plus)],alignment="center"))
app(target=main)