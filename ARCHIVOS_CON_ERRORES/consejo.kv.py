<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        ScrollView:
            BoxLayout:
                id: box
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: 'Salir'
            size_hint_y: None
            height: 50
            on_release: app.stop()

<PracticeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            text: "Escribe el consejo:"
        Label:
            text: root.consejo_actual
            color: (0.3, 0.3, 0.8, 1)
            size_hint_y: None
            height: 80
        TextInput:
            id: input
            multiline: False
            hint_text: "Tu respuesta"
        Button:
            text: 'Verificar'
            on_release: root.verificar()
        Label:
            text: "Progreso: {}/{}".format(root.progreso, len(root.lista) if hasattr(root, 'lista') else 0)
        Button:
            text: 'Volver'
            on_release: app.root.current = "menu"

<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        Label:
            id: resultado
            font_size: 20
            color: (0, 0.6, 0, 1)
        ScrollView:
            BoxLayout:
                id: box
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: 'Volver al menú'
            on_release: app.root.current = "menu"
