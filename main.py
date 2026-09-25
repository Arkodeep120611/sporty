import flet as ft
from google import genai

client = genai.Client()

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.title = "sporty | Sports Analyst | DPS Megacity CRESCO Event"
    page.bgcolor = "#0F172A"

    def animate_r_up(e: ft.Event[ft.Button]):
        e.control.rotate=-0.1 if e.data else 0

    def create_card(header, content):
        return ft.Card(
            bgcolor="#1E293B",
            content=ft.Column(
                controls=[
                    ft.Text(header, color=ft.Colors.WHITE, size = 30, weight = ft.FontWeight.BOLD),
                    ft.Text(content, color=ft.Colors.WHITE),
                ],
                spacing=10,
                width = page.width * 0.27,
                margin = 20
            )
        )

    hero = ft.Container(
        border=ft.Border.all(1, ft.Colors.BLACK),
        bgcolor = "#0F172A",
        width = float("inf"),
        border_radius=20,
        padding = 20,
        content=ft.Column(
                controls=[
                    ft.Text("sporty", color=ft.Colors.WHITE, size=50, weight=ft.FontWeight.BOLD),
                    ft.Text("Sports Insight - made easy with AI", color=ft.Colors.WHITE, size=20)
                ]
        )
    )

    insights = ft.Container(
        padding = 20,
        border=ft.Border.all(1, ft.Colors.BLACK),
        border_radius=20,
        content = ft.Column(
            controls=[
                ft.Text("Some Very Interesting Insights", color = ft.Colors.WHITE, size=25, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls = [
                        create_card("The Fan Heart Rate Spike", "Watching a tense game is a workout for your ticker. Data shows a fan's heart rate can spike by an average of 41% during an intense match, mimicking the physiological stress of actually playing the sport"),
                        create_card("Immunity on the Move", "Engaging in dynamic sports boosts white blood cell circulation. The temporary rise in core body temperature helps your body efficiently fight off invading bacteria and flush out toxins through sweat."),
                        create_card("Bone Density Adaptation", "High-impact, weight-bearing sports like tennis or basketball place controlled stress on your skeletal system. This signals your bones to build higher density, protecting against osteoporosis as you age")
                    ]
                )
            ]
        )
    )

    question = ft.TextField(label="Ask a question about sports", width=page.width * 0.5, color="#F8FAFC")
    answer = ft.Markdown(
        "AI's answer will appear here",
        selectable=True,
        md_style_sheet = ft.MarkdownStyleSheet(
            p_text_style = ft.TextStyle(color="#F8FAFC")
        )
    )

    def ask_ai(e):
        question_text = question.value

        if not question_text:
            answer.value = "Please enter a question."
            page.update()
            return
        
        try:
            response = client.models.generate_content(
                model = "gemini-3.5-flash",
                contents = f"""
                    You are sporty: a sports analyst. You are an expert in sports, and have a deep understanding of various sports, including their rules. You are always up to date with what is happening in the real world of sports. Your task is to keep the user updated with whatever sports information they ask about, in a short and concise manner.
                    User question:
                    {question_text}
                """
            )

            answer.value = response.text

        except Exception as error:
            answer.value = f"Error: {error}"

        page.update()

    ai = ft.Container(
        bgcolor = "",
        border=ft.Border.all(1, ft.Colors.BLACK),
        border_radius=20,
        padding=5,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Ask Our AI Any Question", size=25, weight=ft.FontWeight.BOLD, color="#F8FAFC"),
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls=[
                        question,
                        ft.Button("Get Answer", on_click=ask_ai, bgcolor="#22C55E", color="#FFFFFF", on_hover=animate_r_up, rotate=0, animate_rotation=100)
                    ]
                ),
                ft.Container(
                    content=answer,
                    border=ft.Border.all(1, ft.Colors.BLACK),
                    border_radius=12,
                    padding=5
                )
            ]
        )
    )

    page.add (
        hero, insights, ai
    )

if __name__ == "__main__":
    ft.run(main)
