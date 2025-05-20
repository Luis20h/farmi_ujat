import flet as ft
import consulta_airtable as cat


def main (page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)

    page.title ="Farma UJAT"
    page.theme_mode = "light"
    page.appbar = ft.AppBar(
        title=ft.Text("Farmacia-UJAT", size=48),
        center_title = True
    )
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication",size=40, color="black"),
                    ft.Text("Interacciones medicamentosas",text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=18
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=19),
            side=ft.BorderSide(1,"orange")
        ),
        bgcolor="orange100",
        color="black",
        width=200,
        on_click=mostrar_interacciones
    )
    btn_altas = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add_box",size=40, color="black"),
                    ft.Text("Altas de medicamentos",text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=18
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=19),
            side=ft.BorderSide(1,"ogreen")
        ),
        bgcolor="green100",
        color="black",
        width=200,
    

    )
    btn_listar = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("VIEW_LIST",size=40, color="black"),
                    ft.Text("Listar medicamentos",text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=18
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=19),
            side=ft.BorderSide(1,"blue")
        ),
        bgcolor="blue100",
        color="black",
        width=200
    )
    row_botones = ft.Row(
        controls=[btn_interacciones, btn_altas, btn_listar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30
    )
    
    page.add(ft.Divider(color="black"))
    page.add( row_botones)
    page.update()

ft.app(target=main,view=ft.AppView.WEB_BROWSER)