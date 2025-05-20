import flet as ft
import nube as nb

def main(page: ft.Page):
#Configuara pagina
    page.title = "consultas"
    page.window.width =800
    page.window.height = 600
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title= ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("receipt_long"),
        bgcolor="blue",
        center_title=True,
    )

#Compomponentes de la pagina
    encabezado = [
        ft.DataColumn(ft.Text("Medicamento")),
        ft.DataColumn(ft.Text("Interacciones")),
       
    ]
    filas = []
    datos = nb.Receta.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.medicamentos,weight="bold"))
        celda2 = ft.DataCell(ft.Text(d.interacciones))   
        fila = ft.DataRow([celda1,celda2])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_medicamentos)
    page.update()
if __name__ == "__main__":
    ft.app(target=main)