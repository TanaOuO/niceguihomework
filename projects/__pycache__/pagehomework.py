from nicegui import ui

with ui.header():
        ui.button(icon='home',on_click=ui.navigate.back)
        ui.button('page1',on_click=lambda:ui.navigate.to('/page1'))
        ui.button('page2',on_click=lambda:ui.navigate.to('/page2'))
        ui.button('page3',on_click=lambda:ui.navigate.to('/page3'))
        ui.button('page4',on_click=lambda:ui.navigate.to('/page4'))
        ui.button('page5',on_click=lambda:ui.navigate.to('/page5'))


@ui.page('/page1')
def page1():
    ui.button(icon='home',on_click=ui.navigate.back)
    ui.label('here is page1')

@ui.page('/page2')
def page2():
    with ui.row().classes('w-full'):
         ui.button('page1',on_click=lambda:ui.navigate.to('/page1')).classes('w-20')
         ui.button('page2',on_click=lambda:ui.navigate.to('/page2')).classes('w-20')
         ui.button('page3',on_click=lambda:ui.navigate.to('/page3')).classes('w-20')
         ui.button('page4',on_click=lambda:ui.navigate.to('/page4')).classes('w-20')
         ui.button('page5',on_click=lambda:ui.navigate.to('/page5')).classes('w-20')

@ui.page('/page3')
def page3():
     with open('/root/projects/__pycache__/README.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()
     with ui.row(align_items='center').style('width:100% ; background-color: #f0f0f0'):
          ui.image('/root/projects/__pycache__/guanwei1mao6.png').style('width: 50px ; height: 50px') #'width: 50px; height: 50px;
          ui.label('guanwei1mao6')
          ui.markdown(markdown_content)
     with ui.row():
          ui.label('段落一')
     with ui.row():
          ui.label('段落二')
     with ui.row():
          ui.label('段落三')

@ui.page('/page4')
def page4():
    with ui.tabs().classes('w-full') as tabs:
         one = ui.tab('Tab1')
         two = ui.tab('Tab2')
         there = ui.tab('Tab3')
    with ui.tab_panels(tabs, value=one).classes('w-full'):
        with ui.tab_panel(one):
             ui.label('Tab1')
        with ui.tab_panel(two):
             ui.label('Tab2')
        with ui.tab_panel(there):
             ui.label('Tab3')

@ui.page('/page5')
def page5():
     v = ui.video('/root/projects/__pycache__/bancho轟はじめreglosshololivedevis--shorts--vtuber.mp4')
     v.on('ended', lambda _: ui.notify('Video playback completed'))
     
ui.run()