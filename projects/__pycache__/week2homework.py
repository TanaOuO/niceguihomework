from nicegui import ui

with ui.header(elevated=True).style('backgroud-color:#A9A9A9').classes('items-center justify-between'):
    
    ui.button('home', on_click=lambda: ui.notify('Home'))

    ui.button_group()
    ui.button('page1', on_click=lambda: ui.notify('1'))
    ui.button('2', on_click=lambda: ui.notify('2'))
    ui.button('3', on_click=lambda: ui.notify('3'))
    ui.button('4', on_click=lambda: ui.notify('4'))
    ui.button('5', on_click=lambda: ui.notify('5'))
    ui.button('6', on_click=lambda: ui.notify('6'))
ui.run()