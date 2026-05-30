import PySimpleGUI as sg
import requests
from threading import Thread
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO

# Configuración
API_URL = "http://localhost:8000"
THEME = "DarkBlue3"
COLORS = {
    'primary': '#5AA6D9',
    'secondary': '#ED5454',
    'accent': '#FAD95F',
    'background': '#F5F5F0'
}

# Estilos personalizados
sg.theme(THEME)
sg.set_options(font=('Arial', 11), element_padding=(5, 5))

def login_window():
    layout = [
        [sg.Text('APRENDE VERBOS', font=('Arial', 20), justification='center')],
        [sg.Image('logo.png', size=(100, 100))],
        [sg.Text('Usuario:'), sg.Input(key='-USER-')],
        [sg.Text('Contraseña:'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Button('Ingresar', button_color=(COLORS['background'], COLORS['primary'])), 
         sg.Button('Registrarse', button_color=(COLORS['background'], COLORS['secondary']))]
    ]
    
    return sg.Window('Login', layout, element_justification='c', finalize=True)

def main_dashboard(token):
    tabs_layout = [
        sg.TabGroup([[
            sg.Tab('Verbos', verbs_tab()),
            sg.Tab('Progreso', progress_tab()),
            sg.Tab('Notificaciones', notifications_tab())
        ]], tab_location='centertop', title_color='white', 
        selected_title_color=COLORS['accent'])
    ]
    
    layout = [
        [sg.Text(f'Bienvenido | {datetime.now().strftime("%d %b %Y")}', 
                font=('Arial', 12), relief=sg.RELIEF_SUNKEN)],
        [tabs_layout],
        [sg.StatusBar('Conectado al servidor', key='-STATUS-')]
    ]
    
    return sg.Window('Dashboard Principal', layout, finalize=True)

def verbs_tab():
    return [
        [sg.Text('Buscar:'), sg.Input(size=(20,1), key='-SEARCH-'),
         sg.Button('Buscar', button_color=(COLORS['primary'], COLORS['background']))],
        [sg.Table(values=[], headings=['Verbo', 'Conjugación', 'Ejemplo'], 
                auto_size_columns=False,
                col_widths=[15, 20, 40],
                justification='left',
                key='-VERBS-TABLE-',
                row_height=25,
                alternating_row_color=COLORS['background'])]
    ]

def progress_tab():
    return [
        [sg.Text('Tu progreso:', font=('Arial', 14))],
        [sg.Image(key='-PROGRESS-CHART-')],
        [sg.ProgressBar(100, orientation='h', size=(50, 20), key='-PROGRESS-BAR-')]
    ]

def notifications_tab():
    return [
        [sg.Listbox(values=[], size=(60, 10), key='-NOTIFICATIONS-')],
        [sg.Button('Marcar como leídas', button_color=(COLORS['secondary'], 'white'))]
    ]

def api_request(endpoint, method='GET', token=None, data=None):
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    try:
        response = requests.request(
            method,
            f"{API_URL}/{endpoint}",
            headers=headers,
            json=data
        )
        return response.status_code, response.json()
    except Exception as e:
        return 500, {'error': str(e)}

def update_progress_chart(window, token):
    _, response = api_request('progress/chart', token=token)
    if 'error' not in response:
        bio = BytesIO(response.content)
        window['-PROGRESS-CHART-'].update(data=bio.getvalue())

class AsyncAPI(Thread):
    def __init__(self, window, endpoint, token=None, data=None):
        super().__init__()
        self.window = window
        self.endpoint = endpoint
        self.token = token
        self.data = data
        
    def run(self):
        status, response = api_request(self.endpoint, token=self.token, data=self.data)
        self.window.write_event_value('-API-RESPONSE-', (status, response))

def main():
    window_login, window_dash = login_window(), None
    current_token = None
    
    while True:
        window, event, values = sg.read_all_windows()
        
        if event == sg.WIN_CLOSED:
            if window == window_dash:
                break
            window.close()
            
        # Login
        if event == 'Ingresar':
            Thread(target=AsyncAPI, args=(window, 'token', None, {
                'username': values['-USER-'],
                'password': values['-PASS-']
            })).start()
            
        if event == 'Registrarse':
            Thread(target=AsyncAPI, args=(window, 'register', None, {
                'username': values['-USER-'],
                'password': values['-PASS-']
            })).start()
            
        # Respuestas de API
        if event == '-API-RESPONSE-':
            status, response = values[event]
            if status == 200:
                if 'access_token' in response:
                    current_token = response['access_token']
                    window_login.close()
                    window_dash = main_dashboard(current_token)
                    update_progress_chart(window_dash, current_token)
            else:
                sg.popup_error(f"Error: {response.get('detail', 'Error desconocido')}")
                
        # Dashboard
        if window == window_dash:
            if event == '-SEARCH-':
                Thread(target=AsyncAPI, args=(window, f'examples?search={values["-SEARCH-"]}', 
                                            current_token)).start()
                
            if event == '-API-RESPONSE-':
                status, response = values[event]
                if status == 200:
                    if 'examples' in response:
                        verbs_data = [
                            [v['verb'], v['conjugation'], v['sentence']] 
                            for v in response['examples']
                        ]
                        window_dash['-VERBS-TABLE-'].update(values=verbs_data)
                    elif 'notifications' in response:
                        window_dash['-NOTIFICATIONS-'].update(response['notifications'])
    
    window.close()

if __name__ == '__main__':
    main()
