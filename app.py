from nicegui import ui
import io
from openpyxl import load_workbook

workbook = None
sheet = None

def handle_upload(e):
    global workbook, sheet
    content = e.content.read()  # get uploaded file bytes
    workbook = load_workbook(io.BytesIO(content))
    sheet = workbook.active
    show_table.refresh()

@ui.refreshable
def show_table():
    if sheet is not None:
        data = list(sheet.values)  # all rows as tuples
        headers = data[0]          # first row as header
        rows = [dict(zip(headers, row)) for row in data[1:]]

        ui.label(f'Sheet "{sheet.title}" with {len(rows)} rows')
        ui.table(
            columns=[{'name': h, 'label': h, 'field': h} for h in headers],
            rows=rows,
            row_key=headers[0],
        )
    else:
        ui.label('Upload an Excel file to see the table.')

ui.upload(on_upload=handle_upload, auto_upload=True, label='Upload Excel file')

show_table()

import os
port = int(os.environ.get("PORT", 8080))
ui.run(host="0.0.0.0", port=port)
