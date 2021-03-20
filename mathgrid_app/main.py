"""Main module
"""

# Standard library imports
import string

# Third party imports
import numpy as np
import justpy as jp
import pandas as pd

START_INDEX: int = 1
END_INDEX: int = 20

GRID_OPTIONS = """
{
    class: 'ag-theme-alpine',
    defaultColDef: {
        filter: true,
        sortable: false,
        resizable: true,
        headerClass: 'font-bold',
        editable: true
    },
    rowSelection: 'single',
}
"""


def on_input_key(self, msg):
    """On input key event.

    Update the clicked cell with the new value from the input field.

    Args:
        msg (object): Event data object.
    """
    if self.last_cell is not None:
        self.grid.options['rowData'][self.last_cell['row']
                                     ][self.last_cell['col']] = msg.value


def on_cell_clicked(self, msg):
    """On cell clicked event.

    Update the cell label value with the coordinates of the cell and set
    the value of the cell in the input field.

    Args:
        msg (object): Event data object.
    """
    self.cell_label.value = msg.colId + str(msg.rowIndex)
    self.input_field.value = msg.data[msg.colId]
    self.input_field.last_cell = {"row": msg.rowIndex, "col": msg.colId}
    self.last_row = msg.row


def on_cell_value_changed(self, msg):
    """On input key event.

    Update the input field value to match the cell value.

    Args:
        msg (object): Event data object.
    """
    self.input_field.value = msg.data[msg.colId]


def grid_test():
    """Grid test app.
    """
    headings = list(string.ascii_uppercase)
    index = np.arange(START_INDEX, END_INDEX)

    data_frame = pd.DataFrame(index=index, columns=headings)
    data_frame = data_frame.fillna('')

    data = np.array([np.arange(10)]*3).T

    # css_values = """
    # .ag-theme-alpine .ag-ltr .ag-cell {
    #     border-right: 1px solid #aaa;
    # }
    # .ag-theme-balham .ag-ltr .ag-cell {
    #     border-right: 1px solid #aaa;
    # }
    # """

    web_page = jp.WebPage()

    root_div = jp.Div(classes='q-pa-md', a=web_page)
    in_root_div = jp.Div(classes='q-gutter-md', a=root_div)
    cell_label = jp.Input(
        a=in_root_div, style='width: 32px; margin-left: 16px', disabled=True)
    input_field = jp.Input(classes=jp.Styles.input_classes,
                           a=in_root_div, width='32px')
    input_field.on("input", on_input_key)
    input_field.last_cell = None

    grid = jp.AgGrid(a=web_page, options=GRID_OPTIONS)
    grid.load_pandas_frame(data_frame)
    grid.options.pagination = True
    grid.options.paginationAutoPageSize = True
    grid.cell_label = cell_label
    grid.input_field = input_field
    grid.on('cellClicked', on_cell_clicked)
    grid.on('cellValueChanged', on_cell_value_changed)

    input_field.grid = grid

    return web_page


def main():
    """Main app.
    """
    jp.justpy(grid_test)


if __name__ == "__main__":
    main()
