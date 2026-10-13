import flet as ft

def main(page: ft.Page):
    page.title = "Dark Crimson Music Player"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0B090A"  # لون داكن فاخر

    # واجهة زجاجية بتصميم Crimson الداكن
    card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Dark Crimson Player", size=24, weight=ft.FontWeight.BOLD, color="#FF165D"),
                ft.Text("مشغل الموسيقى الخاص بك", size=14, color="#A4A0A2"),
                ft.Container(height=20),
                ft.Icon(ft.Icons.MUSIC_NOTE_ROUNDED, size=64, color="#FF165D"),
                ft.Container(height=20),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.SKIP_PREVIOUS_ROUNDED, icon_color="white", icon_size=30),
                        ft.IconButton(icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED, icon_color="#FF165D", icon_size=50),
                        ft.IconButton(icon=ft.Icons.SKIP_NEXT_ROUNDED, icon_color="white", icon_size=30),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=30,
        border_radius=25,
        bgcolor=ft.colors.with_opacity(0.08, "white"),
        border=ft.border.all(1, ft.colors.with_opacity(0.15, "#FF165D")),
        width=320,
        height=400,
    )

    page.add(card)

ft.app(target=main)
