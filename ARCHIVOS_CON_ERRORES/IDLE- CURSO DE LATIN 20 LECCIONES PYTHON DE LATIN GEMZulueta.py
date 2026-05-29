Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.

= RESTART: /Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py
[INFO   ] [Logger      ] Record log in /Users/jhernanacvdo/.kivy/logs/kivy_25-08-04_1.txt
[INFO   ] [Kivy        ] v2.3.1
[INFO   ] [Kivy        ] Installed at "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)]
[INFO   ] [Python      ] Interpreter at "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13"
[INFO   ] [Logger      ] Purge log fired. Processing...
[INFO   ] [Logger      ] Purge finished!
[INFO   ] [Factory     ] 195 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
[INFO   ] [GL          ] Backend used <sdl2>
[INFO   ] [GL          ] OpenGL version <b'2.1 INTEL-14.7.28'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel Inc.'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel HD Graphics 4000 OpenGL Engine'>
[INFO   ] [GL          ] OpenGL parsed version: 2, 1
[INFO   ] [GL          ] Shading version <b'1.20'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <16>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Leaving application in progress...
 Traceback (most recent call last):
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 373, in <module>
     ParaphraseApp().run()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/app.py", line 956, in run
     runTouchApp()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 574, in runTouchApp
     EventLoop.mainloop()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 339, in mainloop
     self.idle()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 383, in idle
     self.dispatch_input()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 334, in dispatch_input
     post_dispatch_input(*pop(0))
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 263, in post_dispatch_input
     listener.dispatch('on_motion', etype, me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1713, in on_motion
     self.dispatch('on_touch_up', me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1750, in on_touch_up
     if w.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/modalview.py", line 281, in on_touch_up
     super().on_touch_up(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 972, in on_touch_up
     if self.dispatch('on_scroll_stop', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 1009, in on_scroll_stop
     self.simulate_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 672, in simulate_touch_down
     ret = super(ScrollView, self).on_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/behaviors/button.py", line 151, in on_touch_down
     self.dispatch('on_press')
   File "kivy/_event.pyx", line 727, in kivy._event.EventDispatcher.dispatch
   File "kivy/_event.pyx", line 1307, in kivy._event.EventObservers.dispatch
   File "kivy/_event.pyx", line 1231, in kivy._event.EventObservers._dispatch
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 287, in <lambda>
     btn.bind(on_press=lambda x, index=i: self.load_for_editing(index))
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 314, in load_for_editing
     self.paraphrase_input.text = self.paraphrases[self.current_exercise_index]
   File "kivy/properties.pyx", line 520, in kivy.properties.Property.__set__
   File "kivy/properties.pyx", line 1662, in kivy.properties.AliasProperty.set
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/textinput.py", line 3646, in _set_text
     text = text.replace(u'\r\n', u'\n')
 AttributeError: 'NoneType' object has no attribute 'replace'

============================= RESTART: Shell =============================

= RESTART: /Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py
[INFO   ] [Logger      ] Record log in /Users/jhernanacvdo/.kivy/logs/kivy_25-08-04_2.txt
[INFO   ] [Kivy        ] v2.3.1
[INFO   ] [Kivy        ] Installed at "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)]
[INFO   ] [Python      ] Interpreter at "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13"
[INFO   ] [Logger      ] Purge log fired. Processing...
[INFO   ] [Logger      ] Purge finished!
[INFO   ] [Factory     ] 195 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
[INFO   ] [GL          ] Backend used <sdl2>
[INFO   ] [GL          ] OpenGL version <b'2.1 INTEL-14.7.28'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel Inc.'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel HD Graphics 4000 OpenGL Engine'>
[INFO   ] [GL          ] OpenGL parsed version: 2, 1
[INFO   ] [GL          ] Shading version <b'1.20'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <16>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Leaving application in progress...
 Traceback (most recent call last):
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 373, in <module>
     ParaphraseApp().run()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/app.py", line 956, in run
     runTouchApp()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 574, in runTouchApp
     EventLoop.mainloop()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 339, in mainloop
     self.idle()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 383, in idle
     self.dispatch_input()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 334, in dispatch_input
     post_dispatch_input(*pop(0))
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 263, in post_dispatch_input
     listener.dispatch('on_motion', etype, me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1713, in on_motion
     self.dispatch('on_touch_up', me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1750, in on_touch_up
     if w.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/modalview.py", line 281, in on_touch_up
     super().on_touch_up(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 972, in on_touch_up
     if self.dispatch('on_scroll_stop', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 1009, in on_scroll_stop
     self.simulate_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 672, in simulate_touch_down
     ret = super(ScrollView, self).on_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/behaviors/button.py", line 151, in on_touch_down
     self.dispatch('on_press')
   File "kivy/_event.pyx", line 727, in kivy._event.EventDispatcher.dispatch
   File "kivy/_event.pyx", line 1307, in kivy._event.EventObservers.dispatch
   File "kivy/_event.pyx", line 1231, in kivy._event.EventObservers._dispatch
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 287, in <lambda>
     btn.bind(on_press=lambda x, index=i: self.load_for_editing(index))
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 314, in load_for_editing
     self.paraphrase_input.text = self.paraphrases[self.current_exercise_index]
   File "kivy/properties.pyx", line 520, in kivy.properties.Property.__set__
   File "kivy/properties.pyx", line 1662, in kivy.properties.AliasProperty.set
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/textinput.py", line 3646, in _set_text
     text = text.replace(u'\r\n', u'\n')
 AttributeError: 'NoneType' object has no attribute 'replace'

============================= RESTART: Shell =============================

= RESTART: /Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py
[INFO   ] [Logger      ] Record log in /Users/jhernanacvdo/.kivy/logs/kivy_25-08-04_3.txt
[INFO   ] [Kivy        ] v2.3.1
[INFO   ] [Kivy        ] Installed at "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)]
[INFO   ] [Python      ] Interpreter at "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13"
[INFO   ] [Logger      ] Purge log fired. Processing...
[INFO   ] [Logger      ] Purge finished!
[INFO   ] [Factory     ] 195 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
[INFO   ] [GL          ] Backend used <sdl2>
[INFO   ] [GL          ] OpenGL version <b'2.1 INTEL-14.7.28'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel Inc.'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel HD Graphics 4000 OpenGL Engine'>
[INFO   ] [GL          ] OpenGL parsed version: 2, 1
[INFO   ] [GL          ] Shading version <b'1.20'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <16>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Leaving application in progress...
 Traceback (most recent call last):
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 373, in <module>
     ParaphraseApp().run()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/app.py", line 956, in run
     runTouchApp()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 574, in runTouchApp
     EventLoop.mainloop()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 339, in mainloop
     self.idle()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 383, in idle
     self.dispatch_input()
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 334, in dispatch_input
     post_dispatch_input(*pop(0))
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/base.py", line 263, in post_dispatch_input
     listener.dispatch('on_motion', etype, me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1713, in on_motion
     self.dispatch('on_touch_up', me)
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/core/window/__init__.py", line 1750, in on_touch_up
     if w.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/modalview.py", line 281, in on_touch_up
     super().on_touch_up(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 611, in on_touch_up
     if child.dispatch('on_touch_up', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 972, in on_touch_up
     if self.dispatch('on_scroll_stop', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 1009, in on_scroll_stop
     self.simulate_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/scrollview.py", line 672, in simulate_touch_down
     ret = super(ScrollView, self).on_touch_down(touch)
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/widget.py", line 589, in on_touch_down
     if child.dispatch('on_touch_down', touch):
   File "kivy/_event.pyx", line 731, in kivy._event.EventDispatcher.dispatch
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/behaviors/button.py", line 151, in on_touch_down
     self.dispatch('on_press')
   File "kivy/_event.pyx", line 727, in kivy._event.EventDispatcher.dispatch
   File "kivy/_event.pyx", line 1307, in kivy._event.EventObservers.dispatch
   File "kivy/_event.pyx", line 1231, in kivy._event.EventObservers._dispatch
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 287, in <lambda>
     btn.bind(on_press=lambda x, index=i: self.load_for_editing(index))
   File "/Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py", line 314, in load_for_editing
     self.paraphrase_input.text = self.paraphrases[self.current_exercise_index]
   File "kivy/properties.pyx", line 520, in kivy.properties.Property.__set__
   File "kivy/properties.pyx", line 1662, in kivy.properties.AliasProperty.set
   File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/uix/textinput.py", line 3646, in _set_text
     text = text.replace(u'\r\n', u'\n')
 AttributeError: 'NoneType' object has no attribute 'replace'

= RESTART: /Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON TKINTER (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py

= RESTART: /Users/jhernanacvdo/Desktop/2000 ejercicios de gramática/100 ejercicios predefinidos sobre la Gramática Histórica del Español,     basados en los principios de Ralph Penny.py
Cargando 100 ejercicios sobre Gramática Histórica del Español (Ralph Penny)...

--- ¡Bienvenido a la Práctica de Gramática Histórica del Español (Ralph Penny)! ---
Para cada pregunta, identifica el concepto clave, el fenómeno o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **latin vulgar:** Base del español.
  - **romanizacion:** Proceso de imposición del latín.
  - **iberas y celtas:** Lenguas prerromanas (sustrato).
  - **patrimoniales:** Palabras con evolución fonética regular.
  - **cultismos:** Palabras latinas reintroducidas sin evolución completa.
  - **sincopa:** Pérdida de vocales átonas internas.
  - **f-:** Consonante inicial latina a 'h' muda.
  - **sonorizacion:** P, T, K > B, D, G intervocálicas.
  - **palatalizacion:** PL, CL, FL > ll; NN > ñ; LL > ll; LI, NI > j; G- > j.
  - **yod:** I semiconsonante que causa cambios.
  - **elision:** Pérdida de -D- intervocálica o -L- intervocálica.
  - **apocope:** Pérdida de sonido al final.
  - **prótesis:** Adición de sonido al principio.
  - **metatesis:** Cambio de lugar de un sonido.
  - **asimilacion:** Sonido se hace más parecido a otro.
  - **disimilacion:** Sonido se hace menos parecido a otro.
  - **casos nominales:** Sistema latino que se perdió.
  - **alfonso x el sabio:** Rey clave en la estandarización.
  - **gallego-portugues:** Origen común de gallego y portugués.
  - **leonés / aragonés:** Dialectos romances diferenciados.
  - **seseo:** Pronunciación de 'c'/'z' como 's'.
  - **ceceo:** Pronunciación de 's' como 'c'/'z'.
  - **distincion:** Diferenciar 's' de 'z/c'.
  - **dialectalizacion:** Proceso de formación de dialectos.
  - **arabe:** Mayor fuente de léxico no latino.
  - **germanico:** Fuente de germanismos (guerra, yelmo).
  - **helenismos:** Palabras de origen griego.
  - **frances:** Fuente de galicismos.
  - **nahuatl y quechua:** Lenguas amerindias (chocolate, tomate).
  - **italianos:** Fuente de italianismos (ópera, soneto).
  - **anglicismos:** Préstamos recientes del inglés.
  - **calcos semanticos:** Préstamos de significado.
  - **diglosia:** Coexistencia de dos lenguas con diferente prestigio.
  - **bilinguismo:** Capacidad individual de usar dos lenguas.
  - **reajuste de las sibilantes:** Cambio en el siglo XVI.
  - **aspiracion de la -s final de silaba:** Rasgo fonético andaluz/americano.
  - **neutralizacion de /l/ y /r/ en posicion implosiva:** Rasgo caribeño.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: La pérdida de la -D- intervocálica (ej. VIDERE > ver) es un fenómeno de:
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/2000 ejercicios de gramática/100 ejercicios predefinidos sobre la Gramática Histórica del Español,     basados en los principios de Ralph Penny.py
Cargando 100 ejercicios sobre Gramática Histórica del Español (Ralph Penny)...

--- ¡Bienvenido a la Práctica de Gramática Histórica del Español (Ralph Penny)! ---
Para cada pregunta, identifica el concepto clave, el fenómeno o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **latin vulgar:** Base del español.
  - **romanización:** Proceso de imposición del latín.
  - **iberas y celtas:** Lenguas prerromanas (sustrato).
  - **patrimoniales:** Palabras con evolución fonética regular.
  - **cultismos:** Palabras latinas reintroducidas sin evolución completa.
  - **sincopa:** Pérdida de vocales átonas internas.
  - **f-:** Consonante inicial latina a 'h' muda.
  - **sonorizacion:** P, T, K > B, D, G intervocálicas.
  - **palatalizacion:** PL, CL, FL > ll; NN > ñ; LL > ll; LI, NI > j; G- > j.
  - **yod:** I semiconsonante que causa cambios.
  - **elision:** Pérdida de -D- intervocálica o -L- intervocálica.
  - **apocope:** Pérdida de sonido al final.
  - **prótesis:** Adición de sonido al principio.
  - **metatesis:** Cambio de lugar de un sonido.
  - **asimilacion:** Sonido se hace más parecido a otro.
  - **disimilacion:** Sonido se hace menos parecido a otro.
  - **casos nominales:** Sistema latino que se perdió.
  - **alfonso x el sabio:** Rey clave en la estandarización.
  - **gallego-portugues:** Origen común de gallego y portugués.
  - **leonés / aragonés:** Dialectos romances diferenciados.
  - **seseo:** Pronunciación de 'c'/'z' como 's'.
  - **ceceo:** Pronunciación de 's' como 'c'/'z'.
  - **distincion:** Diferenciar 's' de 'z/c'.
  - **dialectalizacion:** Proceso de formación de dialectos.
  - **arabe:** Mayor fuente de léxico no latino.
  - **germanico:** Fuente de germanismos (guerra, yelmo).
  - **helenismos:** Palabras de origen griego.
  - **frances:** Fuente de galicismos.
  - **nahuatl y quechua:** Lenguas amerindias (chocolate, tomate).
  - **italianos:** Fuente de italianismos (ópera, soneto).
  - **anglicismos:** Préstamos recientes del inglés.
  - **calcos semanticos:** Préstamos de significado.
  - **diglosia:** Coexistencia de dos lenguas con diferente prestigio.
  - **bilinguismo:** Capacidad individual de usar dos lenguas.
  - **reajuste de las sibilantes:** Cambio en el siglo XVI.
  - **aspiracion de la -s final de silaba:** Rasgo fonético andaluz/americano.
  - **neutralizacion de /l/ y /r/ en posicion implosiva:** Rasgo caribeño.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: La palabra 'aceituna' es un arabismo. ¿Verdadero o Falso?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/2000 ejercicios de gramática/100 ejercicios predefinidos sobre la Gramática Histórica del Español,     basados en los principios de Ralph Penny.py
Cargando 100 ejercicios sobre Gramática Histórica del Español (Ralph Penny)...

--- ¡Bienvenido a la Práctica de Gramática Histórica del Español (Ralph Penny)! ---
Para cada pregunta, identifica el concepto clave, el fenómeno o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **latín vulgar:** Base del español.
  - **romanización:** Proceso de imposición del latín.
  - **iberas y celtas:** Lenguas prerromanas (sustrato).
  - **patrimoniales:** Palabras con evolución fonética regular.
  - **cultismos:** Palabras latinas reintroducidas sin evolución completa.
  - **síncopa:** Pérdida de vocales átonas internas.
  - **f-:** Consonante inicial latina a 'h' muda.
  - **sonorización:** P, T, K > B, D, G intervocálicas.
  - **palatalización:** PL, CL, FL > ll; NN > ñ; LL > ll; LI, NI > j; G- > j.
  - **yod:** I semiconsonante que causa cambios.
  - **elisión:** Pérdida de -D- intervocálica o -L- intervocálica.
  - **apócope:** Pérdida de sonido al final.
  - **prótesis:** Adición de sonido al principio.
  - **metátesis:** Cambio de lugar de un sonido.
  - **asimilación:** Sonido se hace más parecido a otro.
  - **disimilación:** Sonido se hace menos parecido a otro.
  - **casos nominales:** Sistema latino que se perdió.
  - **Alfonso x el sabio:** Rey clave en la estandarización.
  - **gallego-portugues:** Origen común de gallego y portugués.
  - **leonés / aragonés:** Dialectos romances diferenciados.
  - **seseo:** Pronunciación de 'c'/'z' como 's'.
  - **ceceo:** Pronunciación de 's' como 'c'/'z'.
  - **distincion:** Diferenciar 's' de 'z/c'.
  - **dialectalizacion:** Proceso de formación de dialectos.
  - **arabe:** Mayor fuente de léxico no latino.
  - **germanico:** Fuente de germanismos (guerra, yelmo).
  - **helenismos:** Palabras de origen griego.
  - **frances:** Fuente de galicismos.
  - **nahuatl y quechua:** Lenguas amerindias (chocolate, tomate).
  - **italianos:** Fuente de italianismos (ópera, soneto).
  - **anglicismos:** Préstamos recientes del inglés.
  - **calcos semanticos:** Préstamos de significado.
  - **diglosia:** Coexistencia de dos lenguas con diferente prestigio.
  - **bilingüísmo:** Capacidad individual de usar dos lenguas.
  - **reajuste de las sibilantes:** Cambio en el siglo XVI.
  - **aspiracion de la -s final de silaba:** Rasgo fonético andaluz/americano.
  - **neutralización de /l/ y /r/ en posicion implosiva:** Rasgo caribeño.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: La palabra 'aldea' es un arabismo. ¿Verdadero o Falso?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/2000 ejercicios de gramática/100 ejercicios predefinidos sobre la Gramática Histórica del Español,     basados en los principios de Ralph Penny.py
Cargando 100 ejercicios sobre Gramática Histórica del Español (Ralph Penny)...

--- ¡Bienvenido a la Práctica de Gramática Histórica del Español (Ralph Penny)! ---
Para cada pregunta, identifica el concepto clave, el fenómeno o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **latín vulgar:** Base del español.
  - **romanización:** Proceso de imposición del latín.
  - **iberas y celtas:** Lenguas prerromanas (sustrato).
  - **patrimoniales:** Palabras con evolución fonética regular.
  - **cultismos:** Palabras latinas reintroducidas sin evolución completa.
  - **síncopa:** Pérdida de vocales átonas internas.
  - **f-:** Consonante inicial latina a 'h' muda.
  - **sonorización:** P, T, K > B, D, G intervocálicas.
  - **palatalización:** PL, CL, FL > ll; NN > ñ; LL > ll; LI, NI > j; G- > j.
  - **yod:** I semiconsonante que causa cambios.
  - **elisión:** Pérdida de -D- intervocálica o -L- intervocálica.
  - **apócope:** Pérdida de sonido al final.
  - **prótesis:** Adición de sonido al principio.
  - **metátesis:** Cambio de lugar de un sonido.
  - **asimilación:** Sonido se hace más parecido a otro.
  - **disimilación:** Sonido se hace menos parecido a otro.
  - **casos nominales:** Sistema latino que se perdió.
  - **Alfonso x el sabio:** Rey clave en la estandarización.
  - **gallego-portugues:** Origen común de gallego y portugués.
  - **leonés / aragonés:** Dialectos romances diferenciados.
  - **seseo:** Pronunciación de 'c'/'z' como 's'.
  - **ceceo:** Pronunciación de 's' como 'c'/'z'.
  - **distinción:** Diferenciar 's' de 'z/c'.
  - **dialectalización:** Proceso de formación de dialectos.
  - **árabe:** Mayor fuente de léxico no latino.
  - **germánico:** Fuente de germanismos (guerra, yelmo).
  - **helenismos:** Palabras de origen griego.
  - **francés:** Fuente de galicismos.
  - **nahuatl y quechua:** Lenguas amerindias (chocolate, tomate).
  - **italianos:** Fuente de italianismos (ópera, soneto).
  - **anglicismos:** Préstamos recientes del inglés.
  - **calcos semanticos:** Préstamos de significado.
  - **diglosia:** Coexistencia de dos lenguas con diferente prestigio.
  - **bilingüísmo:** Capacidad individual de usar dos lenguas.
  - **reajuste de las sibilantes:** Cambio en el siglo XVI.
  - **aspiración de la -s final de silaba:** Rasgo fonético andaluz/americano.
  - **neutralización de /l/ y /r/ en posicion implosiva:** Rasgo caribeño.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: El dialecto leonés y el aragonés son variedades romances que se mantuvieron diferenciadas del castellano. ¿Verdadero o Falso?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/APLICACIÓN DE ESCRITORIO CON KIVI Y Tkinter Lengua Castellana/APLICACIÓN DE ESCRITORIO CON KIVY LENGUA CASTELLANA/APLICACIÓN DE ESCRITORIO CON KIVY (6to Grado - Lengua Castellana) # 100 EJERCICIOS DE PARÁFRASIS.py
[INFO   ] [Logger      ] Record log in /Users/jhernanacvdo/.kivy/logs/kivy_25-08-04_4.txt
[INFO   ] [Kivy        ] v2.3.1
[INFO   ] [Kivy        ] Installed at "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/kivy/__init__.py"
[INFO   ] [Python      ] v3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)]
[INFO   ] [Python      ] Interpreter at "/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13"
[INFO   ] [Logger      ] Purge log fired. Processing...
[INFO   ] [Logger      ] Purge finished!
[INFO   ] [Factory     ] 195 symbols loaded
[INFO   ] [Image       ] Providers: img_tex, img_imageio, img_dds, img_sdl2, img_pil (img_ffpyplayer ignored)
[INFO   ] [Text        ] Provider: sdl2
[INFO   ] [Window      ] Provider: sdl2
[INFO   ] [GL          ] Using the "OpenGL ES 2" graphics system
[INFO   ] [GL          ] Backend used <sdl2>
[INFO   ] [GL          ] OpenGL version <b'2.1 INTEL-14.7.28'>
[INFO   ] [GL          ] OpenGL vendor <b'Intel Inc.'>
[INFO   ] [GL          ] OpenGL renderer <b'Intel HD Graphics 4000 OpenGL Engine'>
[INFO   ] [GL          ] OpenGL parsed version: 2, 1
[INFO   ] [GL          ] Shading version <b'1.20'>
[INFO   ] [GL          ] Texture max size <16384>
[INFO   ] [GL          ] Texture max units <16>
[INFO   ] [Window      ] auto add sdl2 input provider
[INFO   ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO   ] [Base        ] Start application main loop
[INFO   ] [GL          ] NPOT texture support is available
[INFO   ] [Base        ] Leaving application in progress...

= RESTART: /Users/jhernanacvdo/Desktop/100 ejercicios predefinidos sobre las reglas de redacción     según los principios de María Teresa Serafini2.py
Cargando 100 ejercicios sobre Redacción (María Teresa Serafini)...

--- ¡Bienvenido a la Práctica de Redacción (María Teresa Serafini)! ---
Para cada pregunta, identifica el concepto clave o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **claridad:** Mensaje unívoco y fácil de entender.
  - **precision:** Uso exacto del léxico.
  - **concisión:** Expresar ideas con el mínimo de palabras.
  - **redundancia:** Repetición innecesaria de información.
  - **cohesión (referencia):** Uso de pronombres, adverbios para vincular elementos.
  - **conectores discursivos:** Palabras/frases que unen oraciones/párrafos.
  - **consecuencia:** Tipo de conector ('por lo tanto').
  - **oposición/adversativa:** Tipo de conector ('sin embargo').
  - **secuencia/temporal:** Tipo de conector ('luego').
  - **adición:** Tipo de conector ('además').
  - **causa:** Tipo de conector ('porque').
  - **disyuntiva:** Tipo de conector ('o').
  - **explicación:** Tipo de conector ('es decir').
  - **ejemplificación:** Tipo de conector ('por ejemplo').
  - **cohesión (léxica):** Uso de sinónimos, repeticiones de palabras clave.
  - **cohesión (léxica - sinonimia):** Uso de sinónimos.
  - **cohesión (elipsis):** Omisión de elementos sobrentendidos.
  - **coherencia (unidad temática):** Texto gira en torno a un tema central.
  - **coherencia (progresión temática):** El texto avanza en la información.
  - **coherencia (no contradicción):** Ausencia de contradicciones lógicas.
  - **adecuación:** Adaptación del texto al contexto comunicativo.
  - **registro/adecuación:** Adaptación del nivel de formalidad.
  - **audiencia/adecuación:** Adaptación al receptor.
  - **introducción:** Parte inicial del texto.
  - **desarrollo:** Cuerpo del texto.
  - **conclusión:** Cierre del texto.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: Las palabras o frases que unen oraciones o párrafos, estableciendo relaciones lógicas (causa, consecuencia, adición), se llaman:
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/100 ejercicios predefinidos sobre las reglas de redacción de párrafos     según los principios de María Teresa Serafini.py
Cargando 100 ejercicios sobre Redacción de Párrafos (María Teresa Serafini)...

--- ¡Bienvenido a la Práctica de Redacción de Párrafos (María Teresa Serafini)! ---
Para cada pregunta, identifica el concepto clave o responde Verdadero/Falso.

Conceptos clave a identificar:
  - **párrafo:** Unidad mínima de texto con una idea principal.
  - **oración temática:** Idea principal del párrafo.
  - **oraciones secundarias/de apoyo:** Amplían la idea principal.
  - **párrafo de introducción:** Presenta el tema y capta atención.
  - **párrafo de desarrollo:** Desarrolla ideas principales.
  - **párrafo de conclusión:** Resume y cierra el texto.
  - **párrafo de transición:** Conecta secciones.
  - **párrafo narrativo:** Relata eventos.
  - **párrafo descriptivo:** Presenta cualidades.
  - **párrafo argumentativo:** Defiende una tesis.
  - **párrafo expositivo:** Explica o informa objetivamente.
  - **párrafo instructivo/procedimental:** Da pasos o instrucciones.
  - **párrafo enumerativo:** Presenta una lista.
  - **párrafo expositivo (causa-efecto):** Explica relaciones causales.
  - **párrafo expositivo (comparación/contraste):** Compara ideas.
  - **párrafo expositivo (definición):** Define un concepto.
  - **párrafo argumentativo/expositivo:** Combina defensa y explicación.
  - **unidad:** Todas las oraciones se relacionan con la idea principal.
  - **coherencia:** Conexión lógica y de sentido entre oraciones.
  - **cohesión:** Mecanismos lingüísticos que unen oraciones.
  - **cohesión (referencia):** Uso de pronombres, adverbios para vincular.
  - **cohesión (léxica):** Uso de sinónimos, repeticiones de palabras clave.
  - **cohesión (léxica - sinonimia):** Uso de sinónimos.
  - **cohesión (elipsis):** Omisión de elementos sobrentendidos.
  - **conectores discursivos:** Palabras/frases que unen oraciones.
  - **consecuencia:** Tipo de conector ('por lo tanto').
  - **oposición/adversativa:** Tipo de conector ('sin embargo').
  - **secuencia/temporal:** Tipo de conector ('luego').
  - **adición:** Tipo de conector ('además').
  - **causa:** Tipo de conector ('porque').
  - **disyuntiva:** Tipo de conector ('o').
  - **explicación:** Tipo de conector ('es decir').
  - **ejemplificación:** Tipo de conector ('por ejemplo').
  - **claridad:** Mensaje unívoco y fácil de entender.
  - **precision:** Uso exacto del léxico.
  - **concisión:** Expresar ideas con el mínimo de palabras.
  - **redundancia:** Repetición innecesaria de información.
  - **adecuación:** Adaptación del texto al contexto comunicativo.
  - **registro/adecuación:** Adaptación del nivel de formalidad.
  - **audiencia/adecuación:** Adaptación al receptor.
  - **falta de unidad:** Párrafo con varias ideas principales.
  - **falta de coherencia:** Oraciones no conectadas lógicamente.
  - **claridad/concisión:** Error por párrafo muy largo.
  - **desarrollo/coherencia:** Error por párrafo muy corto.
  - **verdadero / falso:** Para preguntas dicotómicas.

Tienes 100 ejercicios para practicar.


--- Ejercicio 1 de 100 ---
Pregunta: Es recomendable usar conectores para enlazar las oraciones y párrafos. ¿Verdadero o Falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: Mejoran la cohesión y la fluidez.

--- Ejercicio 2 de 100 ---
Pregunta: Un párrafo demasiado corto que debería ser parte de otro más grande es un error de:
Tu respuesta: 
Incorrecto. ❌
La respuesta correcta era: **unidad/desarrollo**
Explicación: No desarrolla completamente una idea y puede fragmentar el texto.

--- Ejercicio 3 de 100 ---
Pregunta: La extensión de los párrafos de desarrollo debe ser uniforme. ¿Verdadero o Falso?
Tu respuesta: falso
¡Correcto! ✅
La respuesta correcta era: **falso**
Explicación: La extensión varía según la complejidad de la idea que desarrollan.

--- Ejercicio 4 de 100 ---
Pregunta: Un párrafo que presenta una opinión y la justifica con datos es de tipo:
Tu respuesta: párrafo argumentativo
¡Correcto! ✅
La respuesta correcta era: **párrafo argumentativo**
Explicación: Combina una tesis con elementos de prueba.

--- Ejercicio 5 de 100 ---
Pregunta: Un párrafo de conclusión siempre debe ser optimista. ¿Verdadero o Falso?
Tu respuesta: falso
¡Correcto! ✅
La respuesta correcta era: **falso**
Explicación: Su tono dependerá del tema y el propósito del texto.

--- Ejercicio 6 de 100 ---
Pregunta: Los párrafos argumentativos deben evitar el uso de conectores lógicos. ¿Verdadero o Falso?
Tu respuesta: falso
¡Correcto! ✅
La respuesta correcta era: **falso**
Explicación: Los conectores son cruciales para enlazar premisas y conclusiones.

--- Ejercicio 7 de 100 ---
Pregunta: ¿Qué tipo de párrafo puede ser una breve transición entre dos secciones?
Tu respuesta: párrafo de proceso 
Incorrecto. ❌
La respuesta correcta era: **párrafo de transición**
Explicación: Ayuda a conectar ideas y mantener la fluidez del texto.

--- Ejercicio 8 de 100 ---
Pregunta: ¿Qué tipo de párrafo defiende una tesis o un punto de vista con argumentos y evidencias?
Tu respuesta: párrafo argumentativo
¡Correcto! ✅
La respuesta correcta era: **párrafo argumentativo**
Explicación: Busca persuadir al lector sobre la validez de una idea.

--- Ejercicio 9 de 100 ---
Pregunta: La sangría al inicio de un párrafo indica un cambio de tema o subtema. ¿Verdadero o Falso?
Tu respuesta: Falso
Incorrecto. ❌
La respuesta correcta era: **verdadero**
Explicación: Visualmente, la sangría marca el inicio de una nueva unidad de sentido.

--- Ejercicio 10 de 100 ---
Pregunta: En un texto, la mayoría de los párrafos son de desarrollo. ¿Verdadero o Falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: Son el 'cuerpo' del escrito, donde se despliega el contenido.

--- Ejercicio 11 de 100 ---
Pregunta: El proceso de redacción de un párrafo termina una vez que lo escribes por primera vez. ¿Verdadero o Falso?
Tu respuesta: falso
¡Correcto! ✅
La respuesta correcta era: **falso**
Explicación: Siempre se requiere revisión y reescritura.

--- Ejercicio 12 de 100 ---
Pregunta: La falta de progresión temática en un párrafo significa que se repite la misma idea sin añadir información. ¿Verdadero o Falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: El párrafo se estanca y no avanza.

--- Ejercicio 13 de 100 ---
Pregunta: La coherencia en un párrafo se refiere a la conexión lógica entre sus oraciones. ¿Verdadero o Falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: Las ideas dentro del párrafo deben tener sentido y fluir lógicamente.

--- Ejercicio 14 de 100 ---
Pregunta: Un párrafo puede ser un solo enunciado. ¿Verdadero o Falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: Especialmente en introducciones o transiciones, un párrafo puede ser muy breve.

--- Ejercicio 15 de 100 ---
Pregunta: La coherencia se establece a nivel de significado, ¿verdadero o falso?
Tu respuesta: verdadero
¡Correcto! ✅
La respuesta correcta era: **verdadero**
Explicación: Es una propiedad semántica que asegura la inteligibilidad.

--- Ejercicio 16 de 100 ---
Pregunta: El párrafo de introducción es siempre el más largo del texto. ¿Verdadero o Falso?
Tu respuesta: verdadero
Incorrecto. ❌
La respuesta correcta era: **falso**
Explicación: Suele ser conciso para no abrumar al lector al principio.

--- Ejercicio 17 de 100 ---
Pregunta: Un 'párrafo frase' (un solo enunciado muy largo) suele ser un error de:
Tu respuesta: 
Incorrecto. ❌
La respuesta correcta era: **claridad/concisión**
Explicación: Dificulta la lectura y la comprensión.

--- Ejercicio 18 de 100 ---
Pregunta: La unidad, coherencia y cohesión son las tres cualidades fundamentales de un buen párrafo. ¿Verdadero o Falso?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/100 ejercicios sobre la primera declinación, funciones sintácticas     (nominativo, vocativo, acusativo), concordancia, primera conjugación activa     (presente e imperfecto de indicativo) y evolución del latín al castellano.py
--- ¡Bienvenido al Taller de Latín! ---
Este programa te ayudará a practicar la primera declinación,
funciones sintácticas, concordancia, primera conjugación activa,
y evolución del latín al castellano.
¡Responde a las preguntas y mejora tus conocimientos!
--------------------------------------

--- Ejercicio 1/100 ---
Tema: Función Sintáctica
Pregunta: Identifica la función sintáctica de 'puer' en 'Veni, puer!'
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: vocativo
Ayuda: Es una interpelación.
------------------------------

--- Ejercicio 2/100 ---
Tema: Primera Conjugación (Presente)
Pregunta: Cuál es la terminación del presente de indicativo, 1ª persona plural, en la primera conjugación?
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: -amus
Ayuda: Ej. 'amamus'.
------------------------------

--- Ejercicio 3/100 ---
Tema: Función Sintáctica
Pregunta: Identifica la función sintáctica de 'puella' en 'Puella cantat.'
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: nominativo
Ayuda: Es el sujeto de la oración, por lo tanto, nominativo.
------------------------------

--- Ejercicio 4/100 ---
Tema: Primera Declinación
Pregunta: Proporciona el acusativo singular de 'puella, -ae f.'
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: puellam
Ayuda: El acusativo singular de 'puella' es 'puellam'.
------------------------------

--- Ejercicio 5/100 ---
Tema: Primera Conjugación (Presente)
Pregunta: Conjuga 'porto, -are' en presente de indicativo, 2ª persona plural.
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: portatis
Ayuda: Vosotros lleváis.
------------------------------

--- Ejercicio 6/100 ---
Tema: Evolución Latín-Castellano
Pregunta: Cuál es la evolución en castellano de 'somnum'?
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: sueño
Ayuda: Vocal 'o' breve tónica diptonga a 'ue', 'mn' a 'ñ'.
------------------------------

--- Ejercicio 7/100 ---
Tema: Función Sintáctica
Pregunta: Identifica la función sintáctica de 'librum' en 'Legimus librum.'
Tu respuesta: libro
Incorrecto. ❌ La respuesta correcta era: acusativo
Ayuda: Es el objeto directo.
------------------------------

--- Ejercicio 8/100 ---
Tema: Primera Declinación
Pregunta: Proporciona el acusativo singular de 'littera, -ae f.'
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: litteram
Ayuda: El acusativo singular de 'littera' es 'litteram'.
------------------------------

--- Ejercicio 9/100 ---
Tema: Concordancia
Pregunta: Completa con la forma correcta de 'bonus, -a, -um': 'Poeta ____ est.'
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: bonus
Ayuda: Poeta es masculino singular, por lo tanto 'bonus'.
------------------------------

--- Ejercicio 10/100 ---
Tema: Concordancia
Pregunta: Completa con la forma correcta de 'altus, -a, -um': 'Silva ____ est.'
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/100  ejercicios sobre la primera declinación (genitivo y ablativo),   .py
--- ¡Bienvenido al Taller Avanzado de Latín! ---
Este programa te ayudará a practicar la primera declinación (genitivo y ablativo),
funciones sintácticas (genitivo y ablativo), complemento circunstancial de lugar,
el verbo 'sum', segunda conjugación activa (presente e imperfecto),
y evolución del latín al castellano.
¡Responde a las preguntas y mejora tus conocimientos!
---------------------------------------------------

--- Ejercicio 1/100 ---
Tema: Complemento Circunstancial de Lugar
Pregunta: Cómo se dice 'por el camino' (lugar por donde)?
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: via
Ayuda: Ablativo sin preposición para 'lugar por donde'.

--- ¡Momento de vocabulario! ---
Escribe una palabra en latín (o 'omitir' para saltar): 
Ahora, escribe la traducción al castellano de '': 
¡Gracias por compartir! Has escrito '' que significa ''.
------------------------------

--- Ejercicio 2/100 ---
Tema: Complemento Circunstancial de Lugar
Pregunta: Cómo se dice 'en casa' (lugar dónde)?
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: domi
Ayuda: Locativo de 'domus'.

--- ¡Momento de vocabulario! ---
Escribe una palabra en latín (o 'omitir' para saltar): 
Ahora, escribe la traducción al castellano de '': 
¡Gracias por compartir! Has escrito '' que significa ''.
------------------------------

--- Ejercicio 3/100 ---
Tema: Verbo Sum
Pregunta: Traduce 'era' (él/ella).
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: erat
Ayuda: 3ª persona singular del imperfecto de indicativo de 'sum'.

--- ¡Momento de vocabulario! ---
Escribe una palabra en latín (o 'omitir' para saltar): 
Ahora, escribe la traducción al castellano de '': 
¡Gracias por compartir! Has escrito '' que significa ''.
------------------------------

--- Ejercicio 4/100 ---
Tema: Primera Declinación (Genitivo/Ablativo)
Pregunta: Cuál es el genitivo singular de 'cura, -ae f.'?
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: curae
Ayuda: El genitivo singular de 'cura' es 'curae'.

--- ¡Momento de vocabulario! ---
Escribe una palabra en latín (o 'omitir' para saltar): 
Ahora, escribe la traducción al castellano de '': 
¡Gracias por compartir! Has escrito '' que significa ''.
------------------------------

--- Ejercicio 5/100 ---
Tema: Complemento Circunstancial de Lugar
Pregunta: Traduce 'desde el bosque' ('silva, -ae f.').
Tu respuesta: 
Incorrecto. ❌ La respuesta correcta era: ex silva
Ayuda: Lugar 'de donde' con 'ex' + ablativo.

--- ¡Momento de vocabulario! ---
Escribe una palabra en latín (o 'omitir' para saltar): 
= RESTART: /Users/jhernanacvdo/Desktop/100 ejercicios de latín. Los ejercicios cubren los siguientes temas- Primera declinación  Casos y funciones del sintagma nominal Sintaxis del ablativo.py
--- 100 EJERCICIOS DE LATÍN ---
------------------------------

1. Identifica el caso, número y función de 'silvae'.

2. Traduce la forma latina para 'a la silva'.

3. Traduce la forma latina para 'a la via'.

4. Traduce la forma latina para 'a la puella'.

5. Identifica el caso, número y función de 'familiae'.

6. Declina el sustantivo 'via' (singular y plural).

7. Declina el sustantivo 'agricola' (singular y plural).

8. Identifica el caso, número y función de 'rosae'.

9. Identifica el caso, número y función de 'silvae'.

10. Declina el sustantivo 'familia' (singular y plural).

11. Identifica el caso, número y función de 'poetae'.

12. Traduce la forma latina para 'a la poeta'.

13. Traduce la forma latina para 'a la agricola'.

14. Traduce la forma latina para 'a la via'.

15. ¿Cuál es el genitivo singular de 'via'? ¿Y su dativo plural?

16. Traduce al latín: 'Las rosas están en los bosques.'. Identifica el caso del sintagma nominal.

17. En la oración 'Puella rosam pulchram videt.', identifica el caso y la función de 'Puella'.

18. En la oración 'Rosae in silvis sunt.', identifica el caso y la función de 'Rosae'.

19. En la oración 'Familia in insula habitat.', identifica el caso y la función de 'Familia'.

20. En la oración 'Poetae agricolas laudant.', identifica el caso y la función de 'Poetae'.

21. Traduce la forma latina para 'de las poetas'.

22. En la oración 'Puella rosam pulchram videt.', identifica el caso y la función de 'Puella'.

23. En la oración 'Poetae agricolas laudant.', identifica el caso y la función de 'agricolas'.

24. Traduce al latín: 'El agricultor muestra el camino largo.'. Identifica el caso del sintagma nominal.

25. En la oración 'Familia in insula habitat.', identifica el caso y la función de 'in'.

26. Traduce al latín: 'El agricultor muestra el camino largo.'. Identifica el caso del sintagma nominal.

27. En la oración 'Agricola viam longam monstrat.', identifica el caso y la función de 'viam'.

28. ¿Cuál es el genitivo singular de 'via'? ¿Y su dativo plural?

29. Traduce al latín: 'El agricultor muestra el camino largo.'. Identifica el caso del sintagma nominal.

30. En la oración 'Agricola viam longam monstrat.', identifica el caso y la función de 'viam'.

31. Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'.

32. En la oración 'magna cum cura' ¿qué tipo de ablativo es? Tradúcela.

33. ¿Qué función sintáctica cumple el ablativo en la frase 'in horto'? Explica el tipo de ablativo.

34. Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'.

35. Identifica el caso, número y función de 'agricolae'.

36. Traduce al latín: 'El agricultor muestra el camino largo.'. Identifica el caso del sintagma nominal.

37. Escribe una oración en latín donde el ablativo cumpla la función de 'complemento de compañía'.

38. En la oración 'magna cum cura' ¿qué tipo de ablativo es? Tradúcela.

39. Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'.

40. Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?

41. ¿Qué función sintáctica cumple el ablativo en la frase 'in horto'? Explica el tipo de ablativo.

42. Declina el sustantivo 'silva' (singular y plural).

43. Traduce al latín: 'Las rosas están en los bosques.'. Identifica el caso del sintagma nominal.

44. Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'.

45. Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?

46. Conjuga el verbo 'habere' (2ª conj.) en presente de indicativo.

47. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

48. Identifica el verbo y su persona/número en la forma 'laudatis'.

49. ¿Cuál es el genitivo singular de 'rosa'? ¿Y su dativo plural?

50. En la oración 'Familia in insula habitat.', identifica el caso y la función de 'insula habitat'.

51. Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?

52. Identifica el verbo y su persona/número en la forma 'laudatis'.

53. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

54. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

55. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

56. Traduce la forma latina para 'de las puellas'.

57. En la oración 'Poetae agricolas laudant.', identifica el caso y la función de 'agricolas'.

58. ¿Qué función sintáctica cumple el ablativo en la frase 'in horto'? Explica el tipo de ablativo.

59. Conjuga el verbo 'videre' (2ª conj.) en presente de indicativo.

60. Traduce al español la forma verbal 'habemus'.

61. Traduce la oración 'Poetae agricolas laudant.' e identifica su sujeto, verbo y objeto directo.

62. Traduce la oración 'Familia in insula habitat.' e identifica su sujeto, verbo y objeto directo.

63. Identifica el caso, número y función de 'puellae'.

64. En la oración 'Puella rosam pulchram videt.', identifica el caso y la función de 'Puella'.

65. Escribe una oración en latín donde el ablativo cumpla la función de 'complemento de compañía'.

66. Traduce al español la forma verbal 'habemus'.

67. Realiza un análisis sintáctico de la oración 'Rosae in silvis sunt.'.

68. Traduce la oración 'Familia in insula habitat.' e identifica su sujeto, verbo y objeto directo.

69. Traduce la oración 'Rosae in silvis sunt.' e identifica su sujeto, verbo y objeto directo.

70. ¿Cuál es el genitivo singular de 'insula'? ¿Y su dativo plural?

71. En la oración 'Poetae agricolas laudant.', identifica el caso y la función de 'Poetae'.

72. En la oración 'magna cum cura' ¿qué tipo de ablativo es? Tradúcela.

73. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

74. Traduce la oración 'Rosae in silvis sunt.' e identifica su sujeto, verbo y objeto directo.

75. Realiza un análisis sintáctico de la oración 'Puella rosam pulchram videt.'.

76. Crea una oración con hiperbatón usando los sustantivos 'silva' y 'puella'.

77. ¿Cuál es el genitivo singular de 'agricola'? ¿Y su dativo plural?

78. En la oración 'Agricola viam longam monstrat.', identifica el caso y la función de 'viam'.

79. Identifica y explica el uso del ablativo en la oración 'Agricola via in agris ambulat'.

80. Conjuga el verbo 'monere' (2ª conj.) en presente de indicativo.

81. Realiza un análisis sintáctico de la oración 'Rosae in silvis sunt.'.

82. Reordena la frase en latín 'Magna pulchra puella est.' para entender mejor su significado en español.

83. Explica qué es el hiperbatón y por qué es común en latín.

84. ¿Cuál es el genitivo singular de 'poeta'? ¿Y su dativo plural?

85. En la oración 'Familia in insula habitat.', identifica el caso y la función de 'insula habitat'.

86. Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?

87. Identifica el verbo y su persona/número en la forma 'laudatis'.

88. Realiza un análisis sintáctico de la oración 'Familia in insula habitat.'.

89. Crea una oración con hiperbatón usando los sustantivos 'silva' y 'puella'.

90. Crea una oración con hiperbatón usando los sustantivos 'silva' y 'puella'.

91. Identifica el caso, número y función de 'poetae'.

92. En la oración 'Agricola viam longam monstrat.', identifica el caso y la función de 'viam'.

93. Traduce la frase 'Con el poeta y la rosa'. ¿En qué caso se usan los sustantivos?

94. Completa la conjugación de 'sum' en presente: 'sum, es, ..., ..., estis, ...'.

95. Crea una oración simple en latín con un verbo de la 2ª conjugación.

96. Reordena la frase en latín 'Magna pulchra puella est.' para entender mejor su significado en español.

97. ¿Qué fenómeno fonético se observa en la evolución de 'OCULUS' a 'ojo'?

98. Declina el sustantivo 'silva' (singular y plural).

99. En la oración 'Rosae in silvis sunt.', identifica el caso y la función de 'Rosae'.

100. ¿Qué función sintáctica cumple el ablativo en la frase 'in horto'? Explica el tipo de ablativo.


= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Genera ejercicios aleatorios y ofrece retroalimentación detallada.py
--- TUTOR INTERACTIVO DE LATÍN ---
-----------------------------------
¡Bienvenido! Te haré una pregunta de latín. Responde y te daré retroalimentación.

--- NUEVO EJERCICIO ---
¿Cuál es la forma de la 3ª persona del plural del verbo 'laudare' en presente de indicativo? Significa 'él/ella alabar'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'laudat'
Retroalimentación: Los verbos de la 1ª conjugación tienen desinencias específicas en cada persona. Por ejemplo, en el presente de indicativo, la tercera persona del plural termina en '-nt'.
Ejemplo: Ejemplo: La tercera persona del plural de 'amare' es 'amant'.
¿Quieres intentarlo de nuevo? (s/n): 

¿Quieres pasar al siguiente ejercicio? (s/n): s

--- NUEVO EJERCICIO ---
¿Cuál es la forma de la 2ª persona del plural del verbo 'amare' en presente de indicativo? Significa 'tú amar'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amas'
Retroalimentación: Los verbos de la 1ª conjugación tienen desinencias específicas en cada persona. Por ejemplo, en el presente de indicativo, la tercera persona del plural termina en '-nt'.
Ejemplo: Ejemplo: La tercera persona del plural de 'amare' es 'amant'.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/100 ejercicios de latín. Los ejercicios cubren los siguientes temas- Segunda declinación (masculino:femenino) Complemento locativo Perfecto de indicativo activo Acusativo de dirección- Evolución del latín al castellano.py
--- 100 EJERCICIOS DE LATÍN ---
------------------------------

1. Encuentra el caso, número y función de la forma 'ager'.

2. Escribe el dativo plural de 'amicus'.

3. Encuentra el caso, número y función de la forma 'populus'.

4. Encuentra el caso, número y función de la forma 'dominum'.

5. Escribe el dativo plural de 'puer'.

6. ¿Cuál es el genitivo singular de 'locus'? ¿Qué significa?

7. Escribe el dativo plural de 'puer'.

8. ¿Cuál es el genitivo singular de 'lupus'? ¿Qué significa?

9. Declina el sustantivo 'locus' (masculino) en singular y plural.

10. Encuentra el caso, número y función de la forma 'amicus'.

11. ¿Cuál es el genitivo singular de 'puer'? ¿Qué significa?

12. Escribe el dativo plural de 'amicus'.

13. Encuentra el caso, número y función de la forma 'amicus'.

14. Encuentra el caso, número y función de la forma 'amicum'.

15. ¿Cuál es el genitivo singular de 'dominus'? ¿Qué significa?

16. Encuentra el caso, número y función de la forma 'locus'.

17. ¿Cuál es el genitivo singular de 'servus'? ¿Qué significa?

18. Encuentra el caso, número y función de la forma 'dominum'.

19. Declina el sustantivo 'servus' (masculino) en singular y plural.

20. ¿Cuál es el genitivo singular de 'amicus'? ¿Qué significa?

21. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

22. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

23. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

24. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

25. Declina el sustantivo 'puer' (masculino) en singular y plural.

26. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

27. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

28. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

29. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

30. Declina el sustantivo 'locus' (masculino) en singular y plural.

31. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

32. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

33. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

34. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

35. Escribe el dativo plural de 'populus'.

36. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

37. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

38. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

39. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

40. Escribe el dativo plural de 'populus'.

41. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

42. Identifica la persona y el número de la forma verbal 'vocavistis'. Tradúcela.

43. Identifica la persona y el número de la forma verbal 'tenuimus'. Tradúcela.

44. Identifica la persona y el número de la forma verbal 'tenuisti'. Tradúcela.

45. Declina el sustantivo 'lupus' (masculino) en singular y plural.

46. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

47. Identifica la persona y el número de la forma verbal 'misit'. Tradúcela.

48. Identifica la persona y el número de la forma verbal 'audiverunt'. Tradúcela.

49. Conjuga el verbo 'tenere' en perfecto de indicativo activo (persona: 'tú').

50. Escribe el dativo plural de 'amicus'.

51. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

52. Identifica la persona y el número de la forma verbal 'tenuisti'. Tradúcela.

53. Identifica la persona y el número de la forma verbal 'misistis'. Tradúcela.

54. Conjuga el verbo 'mittere' en perfecto de indicativo activo (persona: 'yo').

55. ¿Cuál es el genitivo singular de 'servus'? ¿Qué significa?

56. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

57. Identifica la persona y el número de la forma verbal 'vocavit'. Tradúcela.

58. Identifica la persona y el número de la forma verbal 'tenui'. Tradúcela.

59. Conjuga el verbo 'vocare' en perfecto de indicativo activo (persona: 'ellos').

60. Encuentra el caso, número y función de la forma 'amicus'.

61. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

62. Conjuga el verbo 'vocare' en perfecto de indicativo activo (persona: 'nosotros').

63. Traduce al latín la frase 'al campo' y explica el uso del acusativo.

64. En la frase 'ad urbem', ¿por qué se usa la preposición 'ad' con el acusativo?

65. Declina el sustantivo 'dominus' (masculino) en singular y plural.

66. Escribe una oración en latín que use el complemento locativo de 'locus' (lugar).

67. Conjuga el verbo 'audire' en perfecto de indicativo activo (persona: 'yo').

68. Traduce al latín la frase 'al campo' y explica el uso del acusativo.

69. ¿Qué fenómeno gramatical se observa en la frase 'Romam'? ¿Qué significa?

70. Declina el sustantivo 'lupus' (masculino) en singular y plural.

71. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

72. Identifica la persona y el número de la forma verbal 'vocavit'. Tradúcela.

73. ¿Qué fenómeno gramatical se observa en la frase 'Romam'? ¿Qué significa?

74. En la frase 'ad urbem', ¿por qué se usa la preposición 'ad' con el acusativo?

75. Declina el sustantivo 'servus' (masculino) en singular y plural.

76. Explica cómo se forma el complemento locativo para nombres de ciudades y lugares pequeños como 'Roma'.

77. Identifica la persona y el número de la forma verbal 'audivimus'. Tradúcela.

78. ¿Qué fenómeno gramatical se observa en la frase 'Romam'? ¿Qué significa?

79. En la frase 'ad urbem', ¿por qué se usa la preposición 'ad' con el acusativo?

80. Escribe el dativo plural de 'populus'.

81. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

82. Conjuga el verbo 'mittere' en perfecto de indicativo activo (persona: 'ellos').

83. Traduce al latín la frase 'al campo' y explica el uso del acusativo.

84. Explica el cambio fonético en la evolución de 'CAELU' a 'cielo'.

85. Declina el sustantivo 'dominus' (masculino) en singular y plural.

86. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

87. Conjuga el verbo 'tenere' en perfecto de indicativo activo (persona: 'nosotros').

88. En la frase 'ad urbem', ¿por qué se usa la preposición 'ad' con el acusativo?

89. ¿A qué palabra castellana ha evolucionado 'CAELU'? Explica el cambio fonético.

90. Declina el sustantivo 'populus' (masculino) en singular y plural.

91. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

92. Identifica la persona y el número de la forma verbal 'vocaverunt'. Tradúcela.

93. En la frase 'ad urbem', ¿por qué se usa la preposición 'ad' con el acusativo?

94. ¿A qué palabra castellana ha evolucionado 'FILIU'? Explica el cambio fonético.

95. Encuentra el caso, número y función de la forma 'amicum'.

96. En la frase 'domi manet', ¿qué función sintáctica tiene 'domi'? Tradúcela.

97. Identifica la persona y el número de la forma verbal 'audivistis'. Tradúcela.

98. ¿Qué fenómeno gramatical se observa en la frase 'Romam'? ¿Qué significa?

99. ¿A qué palabra castellana ha evolucionado 'HOMO'? Explica el cambio fonético.

100. Escribe el dativo plural de 'populus'.


= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola con un enfoque en temas avanzados- 1. Segunda declinación (masculino:femenino) 2. Complemento locativo 3. Perfecto de indicativo activo 4. Acusativo de dirección 5. Evolución del latín al castellano.py
--- TUTOR INTERACTIVO DE LATÍN AVANZADO ---
------------------------------------------
¡Bienvenido! Te haré una serie de 100 preguntas de latín. Responde y te daré retroalimentación.

--- EJERCICIO 1/100 ---
¿A qué palabra castellana ha evolucionado el vocablo latino 'FILIU' y cuál fue el cambio fonético?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'hijo'
Retroalimentación: La '-L-' intervocálica se palataliza en '-j-'.
Ejemplo: Ejemplo: La palabra 'NOCTE' ha evolucionado a 'noche' debido a que el grupo '-ct-' palatalizó a '-ch-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Cuál es la forma del complemento locativo para 'Roma'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Romae'
Retroalimentación: Para nombres de ciudades pequeñas, el locativo singular de la primera declinación termina en '-ae'.
Ejemplo: Ejemplo: 'Romae manebat' significa 'él se quedaba en Roma'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
En la frase 'Iter ad urbem facio.', ¿cuál es la traducción de la parte que indica dirección?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'hacia la ciudad'
Retroalimentación: Para indicar movimiento 'hacia' un lugar que no es una ciudad, se usa la preposición 'ad' seguida de acusativo.
Ejemplo: Ejemplo: 'Romam ibo' ('iré a Roma').
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
¿A qué palabra castellana ha evolucionado el vocablo latino 'CAPRA' y cuál fue el cambio fonético?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cabra'
Retroalimentación: La vocal '-A-' se mantiene, el grupo '-PR-' se mantiene.
Ejemplo: Ejemplo: La palabra 'NOCTE' ha evolucionado a 'noche' debido a que el grupo '-ct-' palatalizó a '-ch-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿Cuál es la forma del complemento locativo para 'rus'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'ruri'
Retroalimentación: Para 'rus' (campo), la forma locativa es 'ruri', que significa 'en el campo'.
Ejemplo: Ejemplo: 'Romae manebat' significa 'él se quedaba en Roma'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
¿Cuál es la forma del complemento locativo para 'domus'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'domi'
Retroalimentación: Para 'domus' (casa), la forma locativa es 'domi', que significa 'en casa'.
Ejemplo: Ejemplo: 'Romae manebat' significa 'él se quedaba en Roma'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 7/100 ---
En la frase 'Romam veni.', ¿cuál es la traducción de la parte que indica dirección?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'a Roma'
Retroalimentación: Para indicar movimiento 'hacia' una ciudad, se usa el acusativo de lugar sin preposición.
Ejemplo: Ejemplo: 'Romam ibo' ('iré a Roma').
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 8/100 ---
¿A qué palabra castellana ha evolucionado el vocablo latino 'FILIU' y cuál fue el cambio fonético?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'hijo'
Retroalimentación: La '-L-' intervocálica se palataliza en '-j-'.
Ejemplo: Ejemplo: La palabra 'NOCTE' ha evolucionado a 'noche' debido a que el grupo '-ct-' palatalizó a '-ch-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 9/100 ---
¿Cuál es la forma del complemento locativo para 'domus'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'domi'
Retroalimentación: Para 'domus' (casa), la forma locativa es 'domi', que significa 'en casa'.
Ejemplo: Ejemplo: 'Romae manebat' significa 'él se quedaba en Roma'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 10/100 ---
Conjuga el verbo 'mittere' en perfecto de indicativo activo para la persona 'ellos'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'miserunt'
Retroalimentación: El perfecto de indicativo se forma con la raíz de perfecto del verbo ('mis') y las desinencias de perfecto: -i, -isti, -it, -imus, -istis, -erunt.
Ejemplo: Ejemplo: 'Yo amé' se dice 'amavi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 11/100 ---
Conjuga el verbo 'amare' en perfecto de indicativo activo para la persona 'tú'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amavisti'
Retroalimentación: El perfecto de indicativo se forma con la raíz de perfecto del verbo ('amav') y las desinencias de perfecto: -i, -isti, -it, -imus, -istis, -erunt.
Ejemplo: Ejemplo: 'Yo amé' se dice 'amavi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 12/100 ---
¿A qué palabra castellana ha evolucionado el vocablo latino 'CAPRA' y cuál fue el cambio fonético?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cabra'
Retroalimentación: La vocal '-A-' se mantiene, el grupo '-PR-' se mantiene.
Ejemplo: Ejemplo: La palabra 'NOCTE' ha evolucionado a 'noche' debido a que el grupo '-ct-' palatalizó a '-ch-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 13/100 ---
Escribe la forma del gen_p de 'ager'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'agrorum'
Retroalimentación: Las desinencias de la segunda declinación varían. Por ejemplo, el genitivo singular es '-i' y el acusativo plural es '-os'.
Ejemplo: Ejemplo: El genitivo singular de 'servus' es 'servi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 14/100 ---
¿Cuál es la forma del complemento locativo para 'rus'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'ruri'
Retroalimentación: Para 'rus' (campo), la forma locativa es 'ruri', que significa 'en el campo'.
Ejemplo: Ejemplo: 'Romae manebat' significa 'él se quedaba en Roma'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 15/100 ---
¿A qué palabra castellana ha evolucionado el vocablo latino 'CAELU' y cuál fue el cambio fonético?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cielo'
Retroalimentación: La '-AE-' diptonga en '-ie-'.
Ejemplo: Ejemplo: La palabra 'NOCTE' ha evolucionado a 'noche' debido a que el grupo '-ct-' palatalizó a '-ch-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 16/100 ---
Conjuga el verbo 'amare' en perfecto de indicativo activo para la persona 'él/ella'.

Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amavit'
Retroalimentación: El perfecto de indicativo se forma con la raíz de perfecto del verbo ('amav') y las desinencias de perfecto: -i, -isti, -it, -imus, -istis, -erunt.
Ejemplo: Ejemplo: 'Yo amé' se dice 'amavi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 17/100 ---
Conjuga el verbo 'amare' en perfecto de indicativo activo para la persona 'yo'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amavi'
Retroalimentación: El perfecto de indicativo se forma con la raíz de perfecto del verbo ('amav') y las desinencias de perfecto: -i, -isti, -it, -imus, -istis, -erunt.
Ejemplo: Ejemplo: 'Yo amé' se dice 'amavi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 18/100 ---
Escribe la forma del gen_s de 'amicus'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amici'
Retroalimentación: Las desinencias de la segunda declinación varían. Por ejemplo, el genitivo singular es '-i' y el acusativo plural es '-os'.
Ejemplo: Ejemplo: El genitivo singular de 'servus' es 'servi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 19/100 ---
En la frase 'Iter ad urbem facio.', ¿cuál es la traducción de la parte que indica dirección?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'hacia la ciudad'
Retroalimentación: Para indicar movimiento 'hacia' un lugar que no es una ciudad, se usa la preposición 'ad' seguida de acusativo.
Ejemplo: Ejemplo: 'Romam ibo' ('iré a Roma').
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 20/100 ---
Escribe la forma del acu_p de 'ager'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'agros'
Retroalimentación: Las desinencias de la segunda declinación varían. Por ejemplo, el genitivo singular es '-i' y el acusativo plural es '-os'.
Ejemplo: Ejemplo: El genitivo singular de 'servus' es 'servi'.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Flexión de adjetivos de la 1ª clase 2. Función de complemento de un adjetivo 3. El superlativo 4. Posesivos y demostrativos 5. El complemento predicativo 6. Evolución .py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre adjetivos, demostrativos y más.

--- EJERCICIO 1/100 ---
Explica la evolución del concepto 'SUPERLATIVO EN -ISSIMUS' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: '-ísimo'
Retroalimentación: El sufijo latino '-issimus' se simplificó en '-ísimo' en castellano, conservando su función de superlativo absoluto.
Ejemplo: Ejemplo: La palabra 'pulcherrimus' dio lugar al cultismo 'pulquérrimo' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
En la oración 'Senatus consulem dignum creavit.', ¿cuál es el complemento predicativo y con qué palabra concuerda?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'dignum'
Retroalimentación: El adjetivo 'dignum' califica al objeto directo 'consulem'.
Ejemplo: Ejemplo: En 'Senatus consulem dignum creavit.', 'dignum' es el complemento predicativo que califica al sujeto o al objeto directo.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre temas clave del latín.

--- EJERCICIO 1/100 ---
¿Qué le sucede a la consonante final -M (acusativo singular) en la evolución del latín al castellano?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre temas clave del latín.

--- EJERCICIO 1/100 ---
Escribe la forma del nom_p de 'pax' (paz).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'paces'
Retroalimentación: Los sustantivos de la tercera declinación (temas en consonante) se declinan a partir de la raíz ('pac') que se obtiene del genitivo singular. El nominativo singular es a menudo irregular.
Ejemplo: Ejemplo: El genitivo de 'rex' es 'regis'. La raíz es 'reg-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Qué le sucede a la consonante final -M (acusativo singular) en la evolución del latín al castellano?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-m' final del acusativo singular latino se perdió en la evolución al castellano. Por ejemplo, 'amicum' -> 'amigo'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
¿Qué le sucede a la consonante final -R (infinitivo) en la evolución del latín al castellano?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se conserva'
Retroalimentación: La '-r' final del infinitivo se mantiene en castellano. Por ejemplo, 'amare' -> 'amar'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): 
Traceback (most recent call last):
  File "/Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py", line 146, in <module>
    ejecutar_ejercicios()
  File "/Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py", line 122, in ejecutar_ejercicios
    pregunta, respuesta_correcta, explicacion, ejemplo = obtener_ejercicio_aleatorio()
  File "/Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py", line 113, in obtener_ejercicio_aleatorio
    return random.choice(generadores)()
  File "/Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py", line 90, in generar_ejercicio_conjugacion
    pregunta = f"Conjuga el verbo '{verbo['infinitivo']}' ({datos['espanol']}) en {tiempo} de indicativo activo para la persona '{personas[persona_idx]}'."
TypeError: string indices must be integers, not 'str'

= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en consonante) 2. Tercera y cuarta conjugaciones (presente y pretérito imperfecto de indicativo) 3. Evolución del latín al castellano.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre temas clave del latín.

--- EJERCICIO 1/100 ---
¿Qué le sucede a la consonante final -T (3ª persona singular) en la evolución del latín al castellano?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se pierde'
Retroalimentación: La '-t' final de la 3ª persona del singular se perdió. Por ejemplo, 'amat' -> 'ama'.
Ejemplo: Ejemplo: La -m final de 'amicum' se perdió, dando lugar a la palabra 'amigo'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Qué le sucede a la consonante final -S (nominativo singular/plural) en la evolución del latín al castellano?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Cuarta y Quinta Declinación 2. Tiempos de Perfecto- Perfecto, Pluscuamperfecto, Futuro Perfecto 3. Pronombres Relativos e Interrogativos 4. Evolución del latín al ca.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre temas clave del latín.

--- EJERCICIO 1/100 ---
Explica la evolución del concepto 'Vocal 'U' larga o breve átona' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se mantiene'
Retroalimentación: La vocal U átona generalmente se mantuvo en castellano. Por ejemplo, 'lupus' -> 'lobo'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Escribe la forma del gen s del pronombre 'quis' (quién).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cuius'
Retroalimentación: El pronombre relativo 'quis' se declina para concordar en género, número y caso con el antecedente. El interrogativo 'quis' sigue una declinación similar.
Ejemplo: Ejemplo: En la frase 'puer, quem vidi...', 'quem' es acusativo singular masculino y concuerda con 'puer'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
Conjuga el verbo 'amare' (amar) en futuro perfecto de indicativo activo para la persona 'él/ella'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amaverit'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
Escribe la forma del dat s del pronombre 'qui' (que/quien).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cui'
Retroalimentación: El pronombre relativo 'qui' se declina para concordar en género, número y caso con el antecedente. El interrogativo 'qui' sigue una declinación similar.
Ejemplo: Ejemplo: En la frase 'puer, quem vidi...', 'quem' es acusativo singular masculino y concuerda con 'puer'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
Escribe la forma del dat p de 'dies' (día).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'diebus'
Retroalimentación: La declinación 5 se caracteriza por las terminaciones diei (genitivo singular) y dies (nominativo singular). Presta atención a las terminaciones de cada caso.
Ejemplo: Ejemplo: El genitivo singular de 'res' (5ª declinación) es 'rei'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
Explica la evolución del concepto 'Vocal 'O' breve tónica' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'diptongación en 'ue''
Retroalimentación: La vocal O breve (ǎ) tónica en latín vulgar diptongó a 'ue' en castellano. Por ejemplo, 'pŏrta' -> 'puerta'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 7/100 ---
Conjuga el verbo 'audire' (oír) en futuro perfecto de indicativo activo para la persona 'vosotros'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'audiveritis'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 8/100 ---
Conjuga el verbo 'mittere' (enviar) en pluscuamperfecto de indicativo activo para la persona 'tú'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'miseras'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 9/100 ---
Conjuga el verbo 'mittere' (enviar) en pretérito perfecto de indicativo activo para la persona 'nosotros'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'misimus'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 10/100 ---
Explica la evolución del concepto 'Vocal 'U' larga o breve átona' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'se mantiene'
Retroalimentación: La vocal U átona generalmente se mantuvo en castellano. Por ejemplo, 'lupus' -> 'lobo'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 11/100 ---
Explica la evolución del concepto 'Diptongo 'AU'' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'monoptongación en 'o''
Retroalimentación: El diptongo 'au' monoptongó a 'o'. Por ejemplo, 'aurum' -> 'oro'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 12/100 ---
Explica la evolución del concepto 'Diptongo 'AU'' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'monoptongación en 'o''
Retroalimentación: El diptongo 'au' monoptongó a 'o'. Por ejemplo, 'aurum' -> 'oro'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 13/100 ---
Escribe la forma del acu s masc del pronombre 'qui' (que/quien).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'quem'
Retroalimentación: El pronombre relativo 'qui' se declina para concordar en género, número y caso con el antecedente. El interrogativo 'qui' sigue una declinación similar.
Ejemplo: Ejemplo: En la frase 'puer, quem vidi...', 'quem' es acusativo singular masculino y concuerda con 'puer'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 14/100 ---
Conjuga el verbo 'audire' (oír) en pretérito perfecto de indicativo activo para la persona 'nosotros'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'audivimus'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 15/100 ---
Explica la evolución del concepto 'Diptongo 'AU'' al castellano.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'monoptongación en 'o''
Retroalimentación: El diptongo 'au' monoptongó a 'o'. Por ejemplo, 'aurum' -> 'oro'.
Ejemplo: Ejemplo: La palabra 'aurum' monoptongó a 'oro' en castellano.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 16/100 ---
Escribe la forma del nom s de 'res' (cosa).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'res'
Retroalimentación: La declinación 5 se caracteriza por las terminaciones rei (genitivo singular) y res (nominativo singular). Presta atención a las terminaciones de cada caso.
Ejemplo: Ejemplo: El genitivo singular de 'res' (5ª declinación) es 'rei'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 17/100 ---
Conjuga el verbo 'amare' (amar) en pluscuamperfecto de indicativo activo para la persona 'ellos/ellas'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amaverant'
Retroalimentación: Los tiempos de perfecto se forman a partir de la raíz de perfecto (la 3ª forma principal del verbo). Se le añaden las desinencias correspondientes a cada tiempo.
Ejemplo: Ejemplo: El pretérito perfecto de 'amare' para 'nosotros' es 'amavimus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 18/100 ---
Escribe la forma del abl s del pronombre 'qui' (que/quien).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'quo'
Retroalimentación: El pronombre relativo 'qui' se declina para concordar en género, número y caso con el antecedente. El interrogativo 'qui' sigue una declinación similar.
Ejemplo: Ejemplo: En la frase 'puer, quem vidi...', 'quem' es acusativo singular masculino y concuerda con 'puer'.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Tercera declinación (temas en vocal -i-) 2. Sinopsis de los tiempos de indicativo activo 3. Complementos circunstanciales de tiempo 4. Evolución  (grupos consonánticos).py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre temas clave del latín.

--- EJERCICIO 1/100 ---
¿Qué evolución sufrió el grupo consonántico 'PL > ll' del latín a las palabras en castellano? Da un ejemplo.
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'lluvia'
Retroalimentación: La regla de evolución es: El grupo consonántico 'pl' inicial evolucionó a 'll'.. El ejemplo es: 'pluviam' evoluciona a 'lluvia'.
Ejemplo: Ejemplo: 'pluviam' > 'lluvia'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Escribe la forma del gen s de 'mare' (mar).
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'maris'
Retroalimentación: Los sustantivos de la 3ª declinación con tema en vocal '-i-' se diferencian por el genitivo plural en '-ium' (en lugar de '-um') y por el ablativo singular en '-i' (solo en neutros, como 'mare').
Ejemplo: Ejemplo: El genitivo plural de 'civis' es 'civium'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
¿Qué evolución sufrió el grupo consonántico 'LI/LE + vocal > j' del latín a las palabras en castellano? Da un ejemplo.
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'hoja'
Retroalimentación: La regla de evolución es: La 'l' seguida de 'i' o 'e' se palataliza y evoluciona a 'j'.. El ejemplo es: 'foliam' evoluciona a 'hoja'.
Ejemplo: Ejemplo: 'pluviam' > 'lluvia'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
¿En qué caso se expresa el complemento circunstancial de tiempo 'Ante diem' y cuál es su significado?
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'Adverbio/complemento'
Retroalimentación: Los complementos circunstanciales de tiempo se expresan en ablativo para 'cuándo' (punto en el tiempo) y en acusativo para 'durante cuánto tiempo' (duración). Ej: 'ante diem quintum' se traduce como 'cinco días antes'.
Ejemplo: Ejemplo: 'ante diem quintum' es un ablativo de tiempo, mientras que 'tres dies' es un acusativo de tiempo.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿En qué caso se expresa el complemento circunstancial de tiempo 'Tempus quam diu' y cuál es su significado?
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'Acusativo'
Retroalimentación: Los complementos circunstanciales de tiempo se expresan en ablativo para 'cuándo' (punto en el tiempo) y en acusativo para 'durante cuánto tiempo' (duración). Ej: 'multos annos' se traduce como 'durante muchos años'.
Ejemplo: Ejemplo: 'multos annos' es un ablativo de tiempo, mientras que 'tres dies' es un acusativo de tiempo.
¿Quieres intentarlo de nuevo? (s/n): 
    ¿Qué evolución sufrió el grupo consonántico 'PL > ll' del latín a las palabras en castellano? Da un ejemplo.

--- EJERCICIO 6/100 ---
Escribe la forma del gen p de 'civis' (ciudadano).
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 
Respuesta incorrecta. La respuesta correcta es: 'civium'
Retroalimentación: Los sustantivos de la 3ª declinación con tema en vocal '-i-' se diferencian por el genitivo plural en '-ium' (en lugar de '-um') y por el ablativo singular en '-i' (solo en neutros, como 'mare').
Ejemplo: Ejemplo: El genitivo plural de 'civis' es 'civium'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'civium'
Retroalimentación: Los sustantivos de la 3ª declinación con tema en vocal '-i-' se diferencian por el genitivo plural en '-ium' (en lugar de '-um') y por el ablativo singular en '-i' (solo en neutros, como 'mare').
Ejemplo: Ejemplo: El genitivo plural de 'civis' es 'civium'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 7/100 ---
Escribe la forma del acu p de 'hostis' (enemigo).
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 

Respuesta incorrecta. La respuesta correcta es: 'hostes'
Retroalimentación: Los sustantivos de la 3ª declinación con tema en vocal '-i-' se diferencian por el genitivo plural en '-ium' (en lugar de '-um') y por el ablativo singular en '-i' (solo en neutros, como 'mare').
Ejemplo: Ejemplo: El genitivo plural de 'civis' es 'civium'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 8/100 ---
Conjuga el verbo 'monere' (amonestar) en pretérito imperfecto de indicativo activo para la persona 'tú'.
Tu respuesta (si no sabes la respuesta, escribe la regla o el caso): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Adjetivo de la 2ª clase 2. El comparativo 3. Morfología del infinitivo 4. Sintaxis del infinitivo.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre adjetivos, comparativos e infinitivos.

--- EJERCICIO 1/100 ---
Forma el comparativo para el género neutro del adjetivo 'brevis, -e' (breve).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'brevius'
Retroalimentación: El comparativo de superioridad se forma añadiendo a la raíz del adjetivo la terminación '-ior' para m/f y '-ius' para neutro.
Ejemplo: Ejemplo: La raíz de 'altus' es 'alt-', por lo que el comparativo es 'altior'/'altius'.
¿Quieres intentarlo de nuevo? (s/n): s= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Adjetivo de la 2ª clase 2. El comparativo 3. Morfología del infinitivo 4. Sintaxis del infinitivo.py

--- EJERCICIO 2/100 ---
Escribe la forma del comparativo 'brevior' en gen s m f.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'brevioris'
Retroalimentación: El comparativo se declina por la tercera declinación, pero con sus propias desinencias. Todos los géneros tienen '-iorum' en el genitivo plural y '-ioribus' en dativo/ablativo plural.
Ejemplo: Ejemplo: El nominativo singular masculino/femenino de 'altior' es 'altior'.
¿Quieres intentarlo de nuevo? (s/n): n

--- EJERCICIO 3/100 ---
En la oración 'Scio te venire.' ('Sé que vienes.'), ¿cuál es la función del infinitivo?
Tu respuesta: interrogar

Respuesta incorrecta. La respuesta correcta es: 'Objeto de 'scio''
Retroalimentación: El infinitivo 'venire' está en una oración de infinitivo con el verbo de pensamiento 'scio', y funciona como objeto directo.
Ejemplo: Ejemplo: En 'Volumus pugnare', 'pugnare' es el sujeto de 'volumus'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 'Objeto de 'scio'

Respuesta incorrecta. La respuesta correcta es: 'Objeto de 'scio''
Retroalimentación: El infinitivo 'venire' está en una oración de infinitivo con el verbo de pensamiento 'scio', y funciona como objeto directo.
Ejemplo: Ejemplo: En 'Volumus pugnare', 'pugnare' es el sujeto de 'volumus'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: Objeto de scio

Respuesta incorrecta. La respuesta correcta es: 'Objeto de 'scio''
Retroalimentación: El infinitivo 'venire' está en una oración de infinitivo con el verbo de pensamiento 'scio', y funciona como objeto directo.
Ejemplo: Ejemplo: En 'Volumus pugnare', 'pugnare' es el sujeto de 'volumus'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
Forma el comparativo para el género masculino/femenino del adjetivo 'brevis, -e' (breve).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'brevior'
Retroalimentación: El comparativo de superioridad se forma añadiendo a la raíz del adjetivo la terminación '-ior' para m/f y '-ius' para neutro.
Ejemplo: Ejemplo: La raíz de 'altus' es 'alt-', por lo que el comparativo es 'altior'/'altius'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: brevior

¡Correcto! 😊
Retroalimentación: El comparativo de superioridad se forma añadiendo a la raíz del adjetivo la terminación '-ior' para m/f y '-ius' para neutro.
Ejemplo: Ejemplo: La raíz de 'altus' es 'alt-', por lo que el comparativo es 'altior'/'altius'.

--- EJERCICIO 5/100 ---
Escribe la forma del adjetivo 'omnis' (todo) para el género masculino/femenino.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'todo (m/f)'
Retroalimentación: Los adjetivos de la segunda clase (o temas en -i-) se caracterizan por tener un nominativo singular en '-is' (m/f) y '-e' (n), o en '-er' (m), '-ris' (f) y '-re' (n).
Ejemplo: Ejemplo: El nominativo singular de 'omnis' es 'omnis' para m/f y 'omne' para neutro.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
Escribe la forma del comparativo 'brevior' en acu p m f.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'breviores'
Retroalimentación: El comparativo se declina por la tercera declinación, pero con sus propias desinencias. Todos los géneros tienen '-iorum' en el genitivo plural y '-ioribus' en dativo/ablativo plural.
Ejemplo: Ejemplo: El nominativo singular masculino/femenino de 'altior' es 'altior'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: breviores

¡Correcto! 😊
Retroalimentación: El comparativo se declina por la tercera declinación, pero con sus propias desinencias. Todos los géneros tienen '-iorum' en el genitivo plural y '-ioribus' en dativo/ablativo plural.
Ejemplo: Ejemplo: El nominativo singular masculino/femenino de 'altior' es 'altior'.

--- EJERCICIO 7/100 ---
Escribe la forma del adjetivo 'omnis' (todo) para el género neutro.
Tu respuesta: todo

Respuesta incorrecta. La respuesta correcta es: 'omne'
Retroalimentación: Los adjetivos de la segunda clase (o temas en -i-) se caracterizan por tener un nominativo singular en '-is' (m/f) y '-e' (n), o en '-er' (m), '-ris' (f) y '-re' (n).
Ejemplo: Ejemplo: El nominativo singular de 'omnis' es 'omnis' para m/f y 'omne' para neutro.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: omne

¡Correcto! 😊
Retroalimentación: Los adjetivos de la segunda clase (o temas en -i-) se caracterizan por tener un nominativo singular en '-is' (m/f) y '-e' (n), o en '-er' (m), '-ris' (f) y '-re' (n).
Ejemplo: Ejemplo: El nominativo singular de 'omnis' es 'omnis' para m/f y 'omne' para neutro.

--- EJERCICIO 8/100 ---
Escribe el infinitivo presente activo del verbo 'ducere' (conducir).
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Cuarta declinación (temas en -u-) 2. Sintaxis del infinitivo 3. Proposiciones sustantivas de infinitivo 4. Funciones del infinitivo según el verbo regente.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre la 4ª declinación e infinitivos.

--- EJERCICIO 1/100 ---
Escribe la forma del abl p de 'manus' (mano).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'manibus'
Retroalimentación: Los sustantivos de la 4ª declinación se declinan con tema en '-u-' y se dividen en masculinos/femeninos y neutros. El nominativo singular suele ser '-us' para m/f y '-u' para neutros. Ten cuidado con los genitivos plurales en '-uum'.
Ejemplo: Ejemplo: El dativo singular de 'exercitus' es 'exercitui'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Qué tipo de verbos rigen el infinitivo como complemento? Da un ejemplo con el verbo 'velle'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'verbo de voluntad'
Retroalimentación: Según el verbo regente, el infinitivo puede tener diferentes funciones. 'velle' es un verbo de voluntad y rige una proposición de infinitivo. Ejemplo: 'Volo ire.'.
Ejemplo: Ejemplo: Un verbo de voluntad como 'velle' rige un infinitivo como complemento directo.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
¿Qué tipo de verbos rigen el infinitivo como complemento? Da un ejemplo con el verbo 'velle'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'verbo de voluntad'
Retroalimentación: Según el verbo regente, el infinitivo puede tener diferentes funciones. 'velle' es un verbo de voluntad y rige una proposición de infinitivo. Ejemplo: 'Volo ire.'.
Ejemplo: Ejemplo: Un verbo de voluntad como 'velle' rige un infinitivo como complemento directo.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
Da un ejemplo de una proposición sustantiva de infinitivo con función de 'Sujeto'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Est difficile tacere.'
Retroalimentación: La proposición de infinitivo puede actuar como sujeto, complemento directo, complemento del adjetivo o complemento nominal. En el ejemplo 'Est difficile tacere.', la proposición de infinitivo funciona como Sujeto.
Ejemplo: Ejemplo: Un complemento directo sería 'Scio te venire'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿Qué tipo de verbos rigen el infinitivo como complemento? Da un ejemplo con el verbo 'est'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'verbo impersonal'
Retroalimentación: Según el verbo regente, el infinitivo puede tener diferentes funciones. 'est' es un verbo impersonal y rige una proposición de infinitivo. Ejemplo: 'Est difficile audire.'.
Ejemplo: Ejemplo: Un verbo de voluntad como 'velle' rige un infinitivo como complemento directo.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Documents/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Quinta declinación (temas en -e-) 2. Subjuntivo (presente, imperfecto) 3. Tema de presente y perfecto 4. Usos sintácticos del subjuntivo 5. Valores de la conjunción 'cum'.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre la 5ª declinación, subjuntivo y 'cum'.

--- EJERCICIO 1/100 ---
En la oración 'Cum Caesar in Galliam venit, civitates ei paruerunt.' ('Cuando César llegó a la Galia, las ciudades le obedecieron.'), ¿qué valor tiene la conjunción 'cum'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Temporal'
Retroalimentación: Con subjuntivo o indicativo, 'cum' tiene valor temporal. Cuando va con indicativo, se traduce como 'cuando'.
Ejemplo: Ejemplo: 'Cum dixisset, abiit' tiene un valor temporal (cuando había dicho).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Escribe la primera persona del singular del subjuntivo presente de 'regere' (regir).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'regam'
Retroalimentación: El subjuntivo presente de la tercera conjugación se forma con el tema de presente + '-a-' + desinencias personales.
Ejemplo: Ejemplo: El subjuntivo presente de 'amare' es 'amem'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
¿Cuál es el tema de perfecto del verbo 'monere, monui, monitum' (amonestar)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'monu'
Retroalimentación: El tema de presente se obtiene del infinitivo. El tema de perfecto se obtiene de la tercera forma del enunciado verbal.
Ejemplo: Ejemplo: En 'amare, amavi, amatum', el tema de presente es 'ama-' y el de perfecto es 'amav-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
¿Cuál es el tema de perfecto del verbo 'monere, monui, monitum' (amonestar)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'monu'
Retroalimentación: El tema de presente se obtiene del infinitivo. El tema de perfecto se obtiene de la tercera forma del enunciado verbal.
Ejemplo: Ejemplo: En 'amare, amavi, amatum', el tema de presente es 'ama-' y el de perfecto es 'amav-'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
En la oración 'Tam bonus est ut omnes eum ament.' ('Es tan bueno que todos lo quieren.'), ¿cuál es el uso del subjuntivo?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Consecutivo'
Retroalimentación: El subjuntivo consecutivo expresa una consecuencia, a menudo introducido por 'ut' después de una palabra como 'tam' o 'ita'.
Ejemplo: Ejemplo: 'Gaudeo quod vivas' es un subjuntivo causal.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
En la oración 'Utinam venias!' ('¡Ojalá vengas!'), ¿cuál es el uso del subjuntivo?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Optativo'
Retroalimentación: El subjuntivo optativo expresa un deseo, a menudo introducido por 'utinam'.
Ejemplo: Ejemplo: 'Gaudeo quod vivas' es un subjuntivo causal.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Sintaxis de los verbos compuestos de 'sum'. 2. Proposiciones Sustantivas de 'ut':'ne' y subjuntivo. 3. Consecutio temporum. 4. Valores de 'ut' y 'ne' con subjuntivo..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre sintaxis avanzada de Latín.

--- EJERCICIO 1/100 ---
Si el verbo principal es 'Sciebam' (imperfecto), ¿qué tiempo de subjuntivo usas para expresar una acción anterior a 'venir'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'pluscuamperfecto'
Retroalimentación: Si el verbo principal está en un tiempo histórico (pretérito), la acción anterior en la proposición debe ir en subjuntivo pluscuamperfecto.

Ejemplo: Ejemplo: 'Nescio quid agas' (no sé qué haces), donde la acción es simultánea y el verbo principal está en presente.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Cómo se traduce 'ne veniret' en 'discessit ne veniret'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'para que no viniera'
Retroalimentación: La proposición de 'ne' es final y negativa, y se traduce como 'para que no' ('se marchó para que no viniera').
Ejemplo: Ejemplo: 'Hoc facio ut sis felix' ('Hago esto para que seas feliz') es una proposición final.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
En la oración 'Veni ut te viderem.' ('Vine para verte.'), ¿qué valor tiene 'ut'/'ne'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Final'
Retroalimentación: Cuando 'ut' va con subjuntivo y no hay otra partícula, su valor es final ('para que').
Ejemplo: Ejemplo: 'Ita viverem ut omnes me amarent' (viviría de tal modo que todos me amasen) tiene un valor consecutivo.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
Si el verbo principal es 'Sciebam' (imperfecto), ¿qué tiempo de subjuntivo usas para expresar una acción anterior a 'venir'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'pluscuamperfecto'
Retroalimentación: Si el verbo principal está en un tiempo histórico (pretérito), la acción anterior en la proposición debe ir en subjuntivo pluscuamperfecto.
Ejemplo: Ejemplo: 'Nescio quid agas' (no sé qué haces), donde la acción es simultánea y el verbo principal está en presente.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿Cómo se traduce 'ne venias' en 'curo ne venias'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'que no vengas'
Retroalimentación: La proposición de 'ne' es completiva y negativa, y se traduce como 'que no' ('me preocupo de que no vengas').
Ejemplo: Ejemplo: 'Hoc facio ut sis felix' ('Hago esto para que seas feliz') es una proposición final.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'que no vengas'
Retroalimentación: La proposición de 'ne' es completiva y negativa, y se traduce como 'que no' ('me preocupo de que no vengas').
Ejemplo: Ejemplo: 'Hoc facio ut sis felix' ('Hago esto para que seas feliz') es una proposición final.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
¿Qué caso rige el verbo 'intersum, interfui' (participar, estar presente)?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Pronombres personales, reflexivos y posesivos. 2. La voz pasiva (tema de presente). 3. El complemento agente..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre pronombres, voz pasiva y complemento agente.

--- EJERCICIO 1/100 ---
Escribe la 1ª persona del singular del presente de indicativo pasivo de 'amo, amare, amavi, amatum' (amar).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amor'
Retroalimentación: La 1ª conjugación pasiva en presente se forma con el tema de presente + '-o', y las desinencias pasivas.
Ejemplo: Ejemplo: La 1ª persona del singular del presente de indicativo pasivo de 'amare' es 'amor'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Escribe la 1ª persona del singular del presente de indicativo pasivo de 'amo, amare, amavi, amatum' (amar).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'amor'
Retroalimentación: La 1ª conjugación pasiva en presente se forma con el tema de presente + '-o', y las desinencias pasivas.
Ejemplo: Ejemplo: La 1ª persona del singular del presente de indicativo pasivo de 'amare' es 'amor'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
Escribe la forma del gen del pronombre reflexivo 'se' (se).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'sui'
Retroalimentación: El pronombre reflexivo 'se' se utiliza para referirse al sujeto de la oración en la misma persona y número. Solo tiene formas para genitivo, dativo, acusativo y ablativo.
Ejemplo: Ejemplo: El dativo de 'se' es 'sibi'.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
En la oración pasiva 'Carmen a poeta scribitur.' ('El poema es escrito por el poeta.'), ¿cuál es la forma del complemento agente?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'poeta scribitur'
Retroalimentación: El agente 'poeta' se convierte en 'a poeta' (ablativo con 'a/ab') en la oración pasiva.
Ejemplo: Ejemplo: En 'Urbs a militibus defenditur', 'a militibus' es el complemento agente.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿Cómo se traduce el pronombre posesivo 'noster, nostra, nostrum'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'nuestro'
Retroalimentación: Los pronombres posesivos concuerdan en género, número y caso con el sustantivo al que acompañan.
Ejemplo: Noster pater (Nuestro padre).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
En la oración pasiva 'Dominus a servis timetur.' ('El amo es temido por los esclavos.'), ¿cuál es la forma del complemento agente?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'servis timetur'
Retroalimentación: El agente 'servi' se convierte en 'a servis' (ablativo con 'a/ab') en la oración pasiva.
Ejemplo: Ejemplo: En 'Urbs a militibus defenditur', 'a militibus' es el complemento agente.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Pronombres demostrativos e identificadores. 2. La voz pasiva (tema de perfecto). 3. Resumen de algunos nexos con varios valores..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre demostrativos, voz pasiva de perfecto y nexos.

--- EJERCICIO 1/100 ---
¿Cómo se traduce el pronombre demostrativo 'ille, illa, illud'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'aquel, aquella, aquello (lejano)'
Retroalimentación: Los pronombres demostrativos señalan la posición de algo o alguien respecto al hablante. 'ille, illa, illud' significa 'aquel, aquella, aquello (lejano)'.
Ejemplo: Ille mons (Aquella montaña).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Cómo se forma el pretérito perfecto pasivo de 'amo, amare, amavi, amatum' (amar)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Participio de perfecto (amatus, a, um) + presente de 'sum''
Retroalimentación: La voz pasiva en los tiempos de perfecto se forma con el participio de perfecto pasivo del verbo conjugado, que concuerda en género, número y caso con el sujeto, más el verbo auxiliar 'sum' en el tiempo correspondiente (ej. presente para el perfecto, imperfecto para el pluscuamperfecto, etc.).
Ejemplo: Ejemplo: 'Amatus sum' (he sido amado).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
En la oración 'Pugnamus ne vincantur (Luchamos para que no sean vencidos).', ¿qué valor tiene el nexo 'ne'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'ejemplo_final_negativo'
Retroalimentación: El nexo 'ne' puede tener varios valores. En este caso, el contexto indica que su valor es 'ejemplo_final_negativo'.
Ejemplo: Otro valor de 'ne' es el completivo negativo, como en 'Vereor ne veniat' (Temo que venga).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
En la oración 'para que', ¿qué valor tiene el nexo 'ut'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'final'
Retroalimentación: El nexo 'ut' puede tener varios valores. En este caso, el contexto indica que su valor es 'final'.
Ejemplo: Otro valor de 'ut' es el consecutivo, como en 'Ita pugnavit ut victores essent' (Luchó de tal modo que fueron vencedores).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 5/100 ---
¿Cómo se traduce el pronombre demostrativo 'hic, haec, hoc'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'este, esta, esto (cercano al hablante)'
Retroalimentación: Los pronombres demostrativos señalan la posición de algo o alguien respecto al hablante. 'hic, haec, hoc' significa 'este, esta, esto (cercano al hablante)'.
Ejemplo: Hic liber (Este libro).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
En la oración 'Veni ut te viderem (Vine para que te viera).', ¿qué valor tiene el nexo 'ut'?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín . Este programa se enfoca en- 1. Pronombres relativos e interrogativos. 2. Sintaxis de relativo (concordancia). 3. Oraciones subordinadas adjetivas (relativas). 4. Oraciones interrogativas directas e indirectas..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre pronombres relativos e interrogativos, y oraciones relativas e interrogativas.

--- EJERCICIO 1/100 ---
Tema: Pronombres Interrogativos
¿Cuál es la forma del pronombre interrogativo para preguntar '¿Qué cosa?' (nominativo/acusativo)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'quid'
Retroalimentación: 'Quid' es la forma neutra y se usa para preguntar por cosas. Se usa tanto en nominativo como en acusativo.
Ejemplo: Quid est? (¿Qué es?).
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: Quid

¡Correcto! 😊
Retroalimentación: 'Quid' es la forma neutra y se usa para preguntar por cosas. Se usa tanto en nominativo como en acusativo.
Ejemplo: Quid est? (¿Qué es?).

--- EJERCICIO 2/100 ---
Tema: Pronombres Interrogativos
¿Cuál es la forma del pronombre interrogativo para preguntar '¿Qué cosa?' (nominativo/acusativo)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'quid'
Retroalimentación: 'Quid' es la forma neutra y se usa para preguntar por cosas. Se usa tanto en nominativo como en acusativo.
Ejemplo: Quid est? (¿Qué es?).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
Tema: Pronombres Interrogativos
¿Cuál es la forma del pronombre interrogativo para preguntar '¿Qué cosa?' (nominativo/acusativo)?
Tu respuesta: n

Respuesta incorrecta. La respuesta correcta es: 'quid'
Retroalimentación: 'Quid' es la forma neutra y se usa para preguntar por cosas. Se usa tanto en nominativo como en acusativo.
Ejemplo: Quid est? (¿Qué es?).
¿Quieres intentarlo de nuevo? (s/n): n

--- EJERCICIO 4/100 ---
Tema: Pronombres Relativos
¿En qué caso y número está el pronombre relativo 'qui' en 'Puer, qui currit, laetus est.'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'nominativo singular'
Retroalimentación: El relativo 'qui' (el cual) concuerda en género y número con su antecedente 'puer' (niño), pero su caso depende de su función dentro de la oración de relativo. Aquí, 'qui' es el sujeto, por eso está en nominativo singular.
Ejemplo: Puella, quae currit, laeta est. ('quae' es nominativo singular femenino, concordando con 'puella').
¿Quieres intentarlo de nuevo? (s/n): n

--- EJERCICIO 5/100 ---
Tema: Pronombres Interrogativos
¿Cuál es la forma del pronombre interrogativo para preguntar '¿Qué cosa?' (nominativo/acusativo)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'quid'
Retroalimentación: 'Quid' es la forma neutra y se usa para preguntar por cosas. Se usa tanto en nominativo como en acusativo.
Ejemplo: Quid est? (¿Qué es?).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
Tema: Pronombres Relativos
¿Cómo se traduce el pronombre relativo 'quorum' en 'Pueri, quorum patres nobiles sunt, hic habitant.'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cuyos'
Retroalimentación: 'Quorum' es un genitivo plural que concuerda con 'pueri' (niños) en género y número. Se traduce como 'cuyos', indicando posesión del antecedente.
Ejemplo: Puellae, quarum matres bonae sunt, hic manent. ('quarum' se traduce como 'cuyas').
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 7/100 ---
Tema: Pronombres Interrogativos
Traduce '¿Qué ciudad ves?' usando el adjetivo interrogativo.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'Quam urbem vides?'
Retroalimentación: El adjetivo interrogativo 'qui, quae, quod' concuerda en género, número y caso con el sustantivo al que acompaña. Aquí 'urbem' es acusativo singular, por lo tanto usamos 'quam'.
Ejemplo: Quod carmen legis? (¿Qué poema lees?).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 8/100 ---
Tema: Interrogativas
Identifica el tipo de oración: 'Quid agis, fili?'
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Pronombres numerales e indefinidos. 2. Verbos deponentes y semideponentes..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre numerales, indefinidos y verbos deponentes/semideponentes.

--- EJERCICIO 1/100 ---
El verbo deponente 'hortor' (exhortar) tiene forma pasiva pero significado activo. ¿Cómo se traduce su pretérito perfecto 'hortatus sum'? 
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'he exhortaro'
Retroalimentación: Los verbos deponentes se conjugan como pasivos, pero se traducen como activos. 'hortatus sum' significa 'he exhortaro'.
Ejemplo: Ejemplo: 'Locutus sum' (he hablado).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
¿Cómo se traduce el pronombre indefinido 'quisque, quaeque, quidque'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'cada uno, cada cosa'
Retroalimentación: 'quisque, quaeque, quidque' significa 'cada uno, cada cosa'. Se utiliza para referirse a una persona o cosa sin especificar su identidad.
Ejemplo: Ejemplo: 'Aliqua mulier me vocavit' (Alguna mujer me llamó).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
¿Cómo se traduce el pronombre indefinido 'uterque, utraque, utrumque'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'uno y otro, ambos'
Retroalimentación: 'uterque, utraque, utrumque' significa 'uno y otro, ambos'. Se utiliza para referirse a una persona o cosa sin especificar su identidad.
Ejemplo: Ejemplo: 'Aliqua mulier me vocavit' (Alguna mujer me llamó).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
¿Cómo se traduce el pronombre indefinido 'uterque, utraque, utrumque'?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'uno y otro, ambos'
Retroalimentación: 'uterque, utraque, utrumque' significa 'uno y otro, ambos'. Se utiliza para referirse a una persona o cosa sin especificar su identidad.
Ejemplo: Ejemplo: 'Aliqua mulier me vocavit' (Alguna mujer me llamó).
¿Quieres intentarlo de nuevo? (s/n): n

--- EJERCICIO 5/100 ---
El verbo semideponente 'audeo' (osar, atreverse) ¿tiene forma activa o pasiva en el presente?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'activa'
Retroalimentación: Los verbos semideponentes, como 'audeo', se conjugan en forma activa en el tema de infectum (presente, imperfecto, futuro imperfecto), pero en forma pasiva en el tema de perfectum (perfecto, pluscuamperfecto, futuro perfecto).
Ejemplo: Ejemplo: 'Gaudeo' (me alegro) es una forma activa, mientras que 'gavisus sum' (me he alegrado) es una forma pasiva.
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 6/100 ---
El verbo semideponente 'gaudeo' (alegrarse) ¿tiene forma activa o pasiva en el presente?
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Formas nominales del verbo- El participio. 2. Sintaxis del participio. 3. Verbos irregulares- 'fero' y 'eo'.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre participios y verbos irregulares 'fero' y 'eo'.

--- EJERCICIO 1/100 ---
Tema: Verbos Irregulares: Eo
Conjuga 'eo' en futuro simple, segunda persona del singular.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'ibis'
Retroalimentación: El futuro simple de 'eo' se forma añadiendo las desinencias de futuro a la raíz 'i-'.
Ejemplo: Cras ad forum ibis (mañana irás al foro).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Tema: Participio Presente
Traduce 'el niño que corre' usando el participio de presente del verbo 'currere'.
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'puer currens'
Retroalimentación: El participio de presente 'currens' (corriendo) concuerda con 'puer' en caso (nominativo) y número (singular).
Ejemplo: Puellae currentes (las niñas que corren).
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: puer currens

¡Correcto! 😊
Retroalimentación: El participio de presente 'currens' (corriendo) concuerda con 'puer' en caso (nominativo) y número (singular).
Ejemplo: Puellae currentes (las niñas que corren).

--- EJERCICIO 3/100 ---
Tema: Participio Presente
¿Cómo se forma el participio de presente del verbo 'laudare' (alabar)?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'laudans, laudantis'
Retroalimentación: El participio de presente se forma con el tema de presente + '-ns' o '-ntis'. Significa 'alabando' y se declina como un adjetivo de una terminación de la tercera declinación.
Ejemplo: Vir laudans (el hombre que alaba).
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. Infinitivo (presente, perfecto, futuro - activo y pasivo). 2. Gerundio. 3. Gerundivo. 4. Supino..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre el infinitivo, gerundio, gerundivo y supino.

--- EJERCICIO 1/100 ---
Traduce 'urbs delenda' (la ciudad que debe ser destruida).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'la ciudad que debe ser destruida'
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
El supino de 'audire' es 'auditu'. ¿Qué significa?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'de oír o para ser oído'
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en- 1. La subordinación- proposiciones y nexos. 2. Tipos de proposiciones- Finales, consecutivas, causales, temporales, condicionales, concesivas, comparativas. .py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre la subordinación en latín.

--- EJERCICIO 1/100 ---
Tema: Temporales
Traduce 'Dum legit, dormit.' (Mientras lee, duerme).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'mientras lee, duerme'
Retroalimentación: El nexo 'dum' introduce una proposición temporal que indica simultaneidad ('mientras'). El verbo va en indicativo.
Ejemplo: Cum in urbe essem, te vidi (Cuando estaba en la ciudad, te vi).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 2/100 ---
Tema: Causales
¿Qué modo verbal suele usarse en una proposición causal de causa real?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'indicativo'
Retroalimentación: El indicativo se usa para expresar una causa objetiva y cierta, mientras que el subjuntivo se usaría si la causa fuera una suposición o una cita de otro.
Ejemplo: Non venit quod aeger esset (No vino porque, según él, estaba enfermo).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 3/100 ---
Tema: Condicionales
Traduce 'Si dives es, multos amicos habes.' (Si eres rico, tienes muchos amigos).
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'si eres rico, tienes muchos amigos'
Retroalimentación: Este es un período condicional de tipo real. Tanto la prótasis como la apódosis llevan el verbo en indicativo.
Ejemplo: Nisi festinavisses, periculum fuisses (Si no hubieras tenido prisa, habrías estado en peligro).
¿Quieres intentarlo de nuevo? (s/n): 

--- EJERCICIO 4/100 ---
Tema: Condicionales
Traduce 'Si dives es, multos amicos habes.' (Si eres rico, tienes muchos amigos).
Tu respuesta: 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín . Este programa se enfoca en las preposiciones y su evolución- 1. Preposiciones de acusativo y ablativo. 2. Preposiciones-prefijos (preverbios). 3. Verbos intransitivos y compuestos. 4. Evolución al castellano..py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas sobre preposiciones, preverbios y su evolución al castellano.

--- EJERCICIO 1/100 ---
Tema: Preposiciones de Ablativo
Traduce la frase 'in horto' (en el jardín). ¿Qué caso se usa?
Tu respuesta: 

Respuesta incorrecta. La respuesta correcta es: 'ablativo'
Retroalimentación: Cuando 'in' indica estado o lugar, rige ablativo. La traducción es 'en el jardín'.
¿Quieres intentarlo de nuevo? (s/n): s
Tu respuesta: ablativo

¡Correcto! 😊
Retroalimentación: Cuando 'in' indica estado o lugar, rige ablativo. La traducción es 'en el jardín'.

--- EJERCICIO 2/100 ---
Tema: Preposiciones de Acusativo/Ablativo
Si 'in' rige acusativo, ¿qué indica?
Tu respuesta: acusativo

Respuesta incorrecta. La respuesta correcta es: 'movimiento a un lugar'
Retroalimentación: Si 'in' rige ablativo, indica estado o lugar. Es una de las preposiciones más importantes y tiene doble uso.
¿Quieres intentarlo de nuevo? (s/n): 
= RESTART: /Users/jhernanacvdo/Desktop/Tutor interactivo de latín en la consola. Este programa se enfoca en el vocabulario básico.py
--- TUTOR INTERACTIVO DE LATÍN ---
---------------------------------
¡Bienvenido! Te haré 100 preguntas de vocabulario básico de latín.
Simplemente escribe la traducción al español de la palabra que se te presente.

--- EJERCICIO 1/100 ---
Palabra latina: 'servus'
Tu traducción: 

Respuesta incorrecta. La traducción correcta es: 'esclavo'
Retroalimentación: servus, servi (m) -> esclavo
¿Quieres intentarlo de nuevo? (s/n): s
Tu traducción: esclavo

¡Correcto! 😊
Retroalimentación: servus, servi (m) -> esclavo

--- EJERCICIO 2/100 ---
Palabra latina: 'liber'
Tu traducción: libre

Respuesta incorrecta. La traducción correcta es: 'libro'
Retroalimentación: liber, libri (m) -> libro
¿Quieres intentarlo de nuevo? (s/n): s
Tu traducción: libro

¡Correcto! 😊
Retroalimentación: liber, libri (m) -> libro

--- EJERCICIO 3/100 ---
Palabra latina: 'sed'
Tu traducción: sed

Respuesta incorrecta. La traducción correcta es: 'pero'
Retroalimentación: sed -> pero, sino
¿Quieres intentarlo de nuevo? (s/n): s
Tu traducción: pero

¡Correcto! 😊
Retroalimentación: sed -> pero, sino

--- EJERCICIO 4/100 ---
Palabra latina: 'pater'
Tu traducción: padre

¡Correcto! 😊
Retroalimentación: pater, patris (m) -> padre

--- EJERCICIO 5/100 ---
Palabra latina: 'et'
Tu traducción: y

¡Correcto! 😊
Retroalimentación: et -> y

--- EJERCICIO 6/100 ---
Palabra latina: 'semper'
