from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.animation import Animation
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.core.window import Window
from kivy.lang import Builder
import json
import random

# Paleta de colores art decó
COLORS = {
    'background': [0.96, 0.96, 0.94, 1],
    'primary': [0.35, 0.65, 0.82, 1],
    'secondary': [0.93, 0.33, 0.33, 1],
    'accent': [0.98, 0.85, 0.37, 1]
}

Builder.load_string('''
<ArtButton>:
    background_color: [0,0,0,0]
    canvas.before:
        Color:
            rgba: self.bg_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]
        Color:
            rgba: self.border_color
        Line:
            rounded_rectangle: [self.x, self.y, self.width, self.height, 20]
            width: 1.5

<AnimatedLabel>:
    canvas.before:
        Color:
            rgba: COLORS.primary
        RoundedRectangle:
            pos: self.pos[0]-10, self.pos[1]-5
            size: self.size[0]+20, self.size[1]+10
            radius: [15,]

<GradientWidget>:
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Ellipse:
            pos: self.pos[0]-self.width/2, self.pos[1]-self.height/4
            size: self.width*2, self.height*1.5
            angle_start: 180
            angle_end: 360
        Color:
            rgba: COLORS.primary
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [40,]

<ExampleItem>:
    orientation: 'horizontal'
    spacing: 20
    padding: 20
    size_hint_y: None
    height: 80
    canvas.before:
        Color:
            rgba: COLORS.background
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
        Color:
            rgba: COLORS.primary
        Line:
            rounded_rectangle: [self.x, self.y, self.width, self.height, 15]
            width: 1.5
''')

class ArtButton(Button):
    bg_color = ListProperty(COLORS['primary'])
    border_color = ListProperty(COLORS['secondary'])
    
    def on_press(self):
        anim = Animation(bg_color=COLORS['accent'] + [0.5], duration=0.1) + \
               Animation(bg_color=self.bg_color, duration=0.3)
        anim.start(self)

class AnimatedLabel(Label):
    pass

class GradientWidget(BoxLayout):
    title = StringProperty("")
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*COLORS['accent'], mode='rgba', group='effect')
                self.ellipse = Ellipse(pos=(touch.x-25, touch.y-25), size=(50,50))
                anim = Animation(size=(200,200), opacity=0, duration=0.5)
                anim.start(self.ellipse)
        return super().on_touch_down(touch)

class ExampleItem(BoxLayout):
    verb = StringProperty("")
    conjugation = StringProperty("")
    sentence = StringProperty("")

class VerbosArtApp(App):
    def build(self):
        Window.clearcolor = COLORS['background']
        self.root = MainScreen()
        return self.root

class MainScreen(GradientWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20
        
        # Header
        header = BoxLayout(size_hint_y=0.15)
        header.add_widget(AnimatedLabel(text="VERBOS ART", font_size=40, bold=True))
        self.add_widget(header)
        
        # Controles principales
        controls = BoxLayout(size_hint_y=0.1, spacing=20)
        self.spinner = Spinner(
            text='Epéntesis',
            values=CATEGORIAS.values(),
            background_color=COLORS['secondary'],
            font_size=20
        )
        controls.add_widget(self.spinner)
        
        btn_add = ArtButton(text="➕ NUEVO", bg_color=COLORS['secondary'])
        btn_add.bind(on_release=self.show_editor)
        controls.add_widget(btn_add)
        
        self.add_widget(controls)
        
        # Lista con efecto parallax
        self.scroll = ScrollView()
        self.list_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        self.list_layout.bind(minimum_height=self.list_layout.setter('height'))
        self.scroll.add_widget(self.list_layout)
        self.add_widget(self.scroll)
        
        # Cargar ejemplos
        self.load_examples()
    
    def load_examples(self):
        self.list_layout.clear_widgets()
        for _ in range(10):
            item = ExampleItem(
                verb="Agradecer",
                conjugation="agradezco",
                sentence="Yo agradezco tu ayuda siempre"
            )
            item.bind(on_touch_down=self.item_effect)
            self.list_layout.add_widget(item)
    
    def item_effect(self, instance, touch):
        if instance.collide_point(*touch.pos):
            anim = Animation(opacity=0.5, duration=0.1) + \
                   Animation(opacity=1, duration=0.3)
            anim.start(instance)
    
    def show_editor(self, instance):
        content = BoxLayout(orientation='vertical', spacing=20)
        popup = Popup(
            title="Nuevo Verbo",
            content=content,
            size_hint=(0.8, 0.6),
            separator_color=COLORS['accent'],
            title_color=COLORS['primary']
        )
        
        inputs = GridLayout(cols=1, spacing=10)
        inputs.add_widget(Label(text="Verbo:", color=COLORS['primary']))
        verb_input = ArtButton(text="Ingresar verbo", bg_color=[1,1,1,0.9])
        inputs.add_widget(verb_input)
        
        # ... (resto de inputs y botones)
        
        content.add_widget(inputs)
        popup.open()

if __name__ == '__main__':
    VerbosArtApp().run()
