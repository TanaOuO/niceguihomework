from nicegui import ui


with ui.header():
        ui.button(icon = 'home', on_click= ui.navigate.back)
        ui.button('page1', on_click = lambda: ui.open('/page1'))
        ui.button('page2', on_click = lambda: ui.navigate('/page2'))
        ui.button('page3', on_click = lambda: ui.navigate.to(page3))
        ui.button('page4', on_click = lambda: ui.navigate.to(page4))
        ui.button('page5', on_click = lambda: ui.navigate.to(page5))

ui.page('/page1')
def page1():
    ui.button(icon = 'home' , on_click= ui.navigate.back)
    ui.label('1')

ui.page('/page2')
def page2():
    ui.button(icon = 'home' , on_click= ui.navigate.back)
    ui.label('2')

ui.page('/page3')
def page3():
    ui.button(icon = 'home' , on_click= ui.navigate.back)
    ui.label('3')

ui.page('/page4')
def page4():
    ui.button(icon = 'home' , on_click= ui.navigate.back)
    ui.label('4')

ui.page('/page5')
def page5():
    ui.button(icon = 'home' , on_click= ui.navigate.back)
    ui.label('5')


ui.run()