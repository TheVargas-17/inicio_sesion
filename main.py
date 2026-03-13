import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Participantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    USUARIO_D = "admin"
    CONTRASEÑA_D = "12345"

    def mostrar_snackbar(mensaje):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            duration=2000
        )
        page.snack_bar.open = True
        page.update()

    def cambiar(e):
        if e.control.selected_index == 0:
            contenido.value = "Pantalla Inicio"
        elif e.control.selected_index == 1:
            contenido.value = "Pantalla Perfil"
        elif e.control.selected_index == 2:
            contenido.value = "Pantalla Ajustes"
        page.update()

    def cargar_app():
        page.clean()

        global contenido
        contenido = ft.Text("Bienvenido al sistema", size=30)
        contenido = ft.Text("has iniciado sesion correctamente", size=15)

        page.add(
            ft.Column(
                [contenido],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        )

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Ajustes"),
            ],
            on_change=cambiar
        )

        mostrar_snackbar("Inicio exitoso")

 
    def login_click(e):
        if txt_usuario.value == USUARIO_D and txt_contraseña.value == CONTRASEÑA_D:
            cargar_app()
        else:
            mostrar_snackbar("Datos incorrectos")

    def recuperar_click(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                "Se han enviado instrucciones a tu correo",
                color="white"
            ),
            bgcolor="black",
            behavior=ft.SnackBarBehavior.FLOATING,
            margin=ft.Margin(10, 0, 0, 10),
            duration=3000
        )
        page.snack_bar.open = True
        page.update()

    
    titulo = ft.Text(
        "Inicio de sesión",
        size=30,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    txt_usuario = ft.TextField(label="Usuario", width=300)
    txt_contraseña = ft.TextField(label="Contraseña", password=True, width=300)

    btn = ft.Button(
        content=ft.Text("Iniciar sesión"),
        on_click=login_click,
        width=200
    )

    btn_recuperar = ft.Button(
        content=ft.Text("Recuperar contraseña"),
        on_click=recuperar_click,
        width=200
    )

    page.add(
        ft.Container(
            padding=20,
            bgcolor="white",
            border_radius=15,
            shadow=ft.BoxShadow(
            blur_radius=15,
            color="black26",
            offset=ft.Offset(0, 4)
        ),
            content=ft.Column(
                [
                    titulo,
                    txt_usuario,
                    txt_contraseña,
                    btn,
                    btn_recuperar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )

ft.run(main)