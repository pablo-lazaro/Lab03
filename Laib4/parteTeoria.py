import flet as ft


def main(page: ft.Page):
    def handle_button(e):
        page.add(ft.Text(f"Ciao {name.value}!"))
        page.update()

    name = ft.TextField(label="Your name")

    page.add(
        ft.Row(controls=[
            name,
            # Qui usiamo il testo come primo argomento posizionale, senza 'text='
            ft.ElevatedButton("Say my name!", on_click=handle_button)
        ])
    )


ft.app(target=main)


