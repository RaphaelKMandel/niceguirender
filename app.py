import os
from nicegui import ui

ui.label("Hello from render!")
port = int(os.environ.get("PORT", 8080))
ui.run(host="0.0.0.0", port=port)
