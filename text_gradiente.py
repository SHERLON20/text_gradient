import flet as ft 
def main(page:ft.Page):
    page.bgcolor=ft.colors.BLACK
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    text=ft.Text(
        value='SHERLON',
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        size=50,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(blur_radius=40,color=ft.colors.AMBER),
            foreground=ft.Paint(
                gradient=ft.PaintLinearGradient(
                    colors=[ft.colors.BLUE,ft.colors.GREEN,ft.colors.PINK],
                    begin=ft.Offset(x=0,y=0),
                    end=ft.Offset(x=400,y=0),
                    color_stops=[0,0.6,1]
                )
            )
        )
    )
    text2=ft.ShaderMask(
        content=ft.Text(
            value='shadermask',
            size=30,
            weight=ft.FontWeight.BOLD,
        ),
        shader=ft.LinearGradient(
            colors=[ft.colors.PINK,ft.colors.GREEN,ft.colors.CYAN],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            stops=[0,0.4,1]
        )
    )
    page.add(text2,text)
if __name__=='__main__':
    ft.app(target=main)