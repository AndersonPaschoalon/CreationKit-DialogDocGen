import csv
import PySimpleGUI as sg
from os.path import exists
from PyUtils.CsvDicTuple import CsvDicTuple


class CsvReorderWindow:

    KEY_BUTTON_MOVE_UP = "key-btn-move-up"
    KEY_BUTTON_MOVE_DOWN = "key-btn-move-down"

    def __init__(self):
        self.current_row_int = 0


    def run(self, filename="", label_key = "Actor ID", label_value = "Actor Name"):
        if filename == "":
            popup_text = "File name is empty."
            return
        if not exists(filename):
            popup_text = "File {0} does not exist.".format(filename)
            return
        dic_tuple = CsvDicTuple(dic_file=filename)
        data = self.load_csv(filename)
        table_headings = [label_key, label_value]
        layout_tools = []
        layout_table = [
                        [sg.Table(values=data[:][:],
                            headings=table_headings,
                            auto_size_columns=True,
                            max_col_width=100,
                            display_row_numbers=False,
                            justification='left',
                            num_rows=5,
                            key='-TABLE-',
                            selected_row_colors='red on yellow',
                            enable_events=True,
                            expand_x=True,
                            expand_y=True,
                            enable_click_events=True,
                            tooltip='File {0}'.format(filename))],
                        [sg.Button("/\ Move Up", key=CsvReorderWindow.KEY_BUTTON_MOVE_UP),
                         sg.Button("Move Down \/ ", key=CsvReorderWindow.KEY_BUTTON_MOVE_DOWN )]
                    ]
        window = sg.Window(title="CsvReorderWindow [{0}]".format(filename),
                           layout=layout_table,
                           ttk_theme='clam',
                           resizable=False,
                           size=(500, 300),
                           element_justification='c')
        while True:
            event, values = window.read(timeout=100000)
            curr_row = self.current_row(event, values)
            if curr_row != self.current_row_int:
                self.current_row_int = curr_row
                print("=> curr_row:" + str(curr_row))
                print("key:" + str(data[curr_row][0]) + ", value:" + str(data[curr_row][1]))

            if event == sg.WIN_CLOSED:
                print("Pressed button: sg.WIN_CLOSED")
                break

            if event == CsvReorderWindow.KEY_BUTTON_MOVE_UP:
                key = data[self.current_row_int]
                value = data[self.current_row_int]
                dic_tuple.move_up(key, value)
                data = self.load_csv(filename)
                window['-TABLE-'].update(values=data[:][:])

            if event == CsvReorderWindow.KEY_BUTTON_MOVE_DOWN:
                key = data[self.current_row_int]
                value = data[self.current_row_int]
                dic_tuple.move_down(key, value)
                data = self.load_csv(filename)
                window['-TABLE-'].update(values=data[:][:])

    def load_csv(self, filename):
        data = []
        with open(filename, "r") as csvfile:
            rd = csv.reader(csvfile, delimiter=",", quotechar='"')
            for row in rd:
                data.append(row)
        return data

    def current_row(self, event, values):
        # print("event:<{0}>, values:<{1}>".format(str(event), str(values)))
        try:
            cur_row = values["-TABLE-"][0]
            return cur_row
        except:
            return self.current_row_int





if __name__ == '__main__':
    csv_file = "../Sandbox/DicTuple01.csv"
    reorder = CsvReorderWindow()
    data = reorder.load_csv(csv_file)
    print("data:" + str(data))
    reorder.run(csv_file)