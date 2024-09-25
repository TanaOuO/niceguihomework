from nicegui import ui

@ui.page('/page_layout')
def page_layout():

        ui.label('page')
        ui.label('hello!!')
        
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):ui.label('HEADER')
        with ui.left_drawer(fixed=False).style('background-color: #696969'):ui.label('LEFT DRAWER')
        with ui.right_drawer(fixed=False).style('background-color: #696969').props('bordered') as right_drawer:ui.label('RIGHT DRAWER')

ui.link('show page with fancy layout', page_layout)        
ui.run()