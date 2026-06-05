import webview
import sys
import os

# App configuration
APP_NAME = "Note Alarm"
APP_URL = "https://notealarm.lovable.app"
APP_WIDTH = 1100
APP_HEIGHT = 750
MIN_WIDTH = 800
MIN_HEIGHT = 600

def get_icon_path():
    """Get icon path - works both in dev and when packaged with PyInstaller"""
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(base_dir, 'icon.ico')
    return icon if os.path.exists(icon) else None

class Api:
    """JavaScript <-> Python bridge (optional, extend as needed)"""

    def close_window(self):
        window.destroy()

    def minimize_window(self):
        window.minimize()

    def toggle_fullscreen(self):
        window.toggle_fullscreen()

    def get_app_name(self):
        return APP_NAME


if __name__ == '__main__':
    api = Api()

    icon = get_icon_path()

    window = webview.create_window(
        title=APP_NAME,
        url=APP_URL,
        width=APP_WIDTH,
        height=APP_HEIGHT,
        min_size=(MIN_WIDTH, MIN_HEIGHT),
        frameless=True,          # No OS title bar
        easy_drag=True,          # Drag anywhere to move
        resizable=True,
        js_api=api,
        background_color='#0f172a',
    )

    webview.start(
        icon=icon,
        debug=False,
        private_mode=False,      # Keep cookies/session between launches
        storage_path=os.path.join(os.path.expanduser('~'), '.notealarm'),
    )
