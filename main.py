
import flet as ft
def main(page: ft.Page):
    page.title = "Registro de Participantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
   
    titulo=ft.Text(
    value="Inicio de sesion",
    size=30,
    color=ft.Colors.BLUE,
    weight=ft.FontWeight.BOLD,
    italic=False,
    text_align=ft.TextAlign.CENTER,
    max_lines=2,
    overflow=ft.TextOverflow.ELLIPSIS
)
    

    USUARIO_D ="admin"
    CONTRASEÑA_D ="12345"

    def login_click(e):
        usuario= txt_usuario.value
        contraseña= txt_contraseña.value

        if usuario == USUARIO_D and contraseña == CONTRASEÑA_D:
            # mensaje de exito
            page.show_dialog(ft.snackBar(ft.Text("¡Inicio de sesion exitoso!")))
        else:
            #mensaje de error
            page.show_dialog(ft.snackBar(ft.Text("¡Usuario o ocntraseña incorrectos!")))

    def forgot_click(e):
            page.show_dialog(ft.snackBar(ft.Text("¡Se han enviado instrucciones a tu correo!")))

   
    usuario=ft.TextField(
    label="NOMBRE COMPLETO",
    hint_text="Ingresa tu nombre",
    value="",

)

    contraseña=ft.TextField(
    label="CORREO ELECTRONICO",
    hint_text="Ingresa TU CORREO ELECTRONICO",
    value="",

)
    

        
   
    btn=ft.Button(content="Iniciar sesion")     

    page.add(
            ft.Column(
                [
                titulo,
                usuario,
                contraseña,
                btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            
        )



ft.app(target=main)