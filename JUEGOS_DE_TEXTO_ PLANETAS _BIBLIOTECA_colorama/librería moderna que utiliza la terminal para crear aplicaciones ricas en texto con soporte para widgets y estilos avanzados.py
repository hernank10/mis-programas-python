from textual.app import App
from textual.widgets import Header, Footer, Static

class AdventureApp(App):
    def compose(self):
        yield Header()
        yield Static("Bienvenido a la aventura con Textual!", id="main")
        yield Footer()

if __name__ == "__main__":
    AdventureApp.run()
