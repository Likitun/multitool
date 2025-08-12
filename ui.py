import flet as ft
from dotenv import load_dotenv
import os
from config import APPCFG
import json
import re

def main(page: ft.Page):
    CFG = APPCFG()
    lang = CFG.lang
    main_menu=None
    def dropdown_change(e):
        if e.control.value == "English":
            CFG.set("lang","en")
        else:
            CFG.set("lang","ru")
        update_interface()
    def settings(e):
        page.clean()
        page.add(ft.Column([
            ft.Dropdown(label=lang['lang'],editable=True,options=[ft.dropdown.Option("Русский"),ft.dropdown.Option("English")],on_change=dropdown_change)
        ],ft.padding.all(50)))
    def update_interface():
        lang = CFG.lang
        serveses = [(lang['download'],"WHITE",""),(lang['convert'],"CYAN",""),(lang['resize'],"LIGHT_GREEN",""),(lang['ASCII'],"LIGHT_BLUE",""),(lang['joke'],"ORANGE",""),(lang['qrcreatefunc'],"GREEN",""),(lang['qrread'],"BLUE",""),(lang['settings'],"PURPLE",settings)]
        buttons = [ft.TextButton(x,on_click=z,style = ft.ButtonStyle(color=eval(f"ft.Colors.{y}"),bgcolor={ft.ControlState.HOVERED:ft.Colors.BLACK},animation_duration=500,overlay_color=ft.Colors.TRANSPARENT,shape=ft.RoundedRectangleBorder(radius=10))) for x,y,z in serveses]
        nonlocal main_menu
        main_menu = ft.Column(buttons,ft.padding.all(50))
        if page.controls and isinstance(page.controls[0], ft.Column):
            page.controls[0] = main_menu
            page.update()
    page.title = "MultiTool"
    page.theme_mode = 'dark'
    update_interface()
    page.add(main_menu)
ft.app(main)