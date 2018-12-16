import re
import sys
from PyQt5 import QtWidgets
from madlibs import get_story, get_matches, sub_matches

def sel_story():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("MatLibs")

    sel_story_label = QtWidgets.QLabel('Enter a MadLib .txt file name')
    sel_story_text = QtWidgets.QLineEdit()
    sel_layout = QtWidgets.QHBoxLayout()
    sel_enter_b = QtWidgets.QPushButton('Enter')
    sel_layout.addWidget(sel_story_label)
    sel_layout.addWidget(sel_story_text)
    sel_layout.addWidget(sel_enter_b)
    window.setLayout(sel_layout)

    story_file = sel_enter_b.clicked.connect(self.read_file)
    # This story_file doesn't work. Online suggestion says make a global class variable and update it on button click

    window.show()
    app.exec_()
    # sys.exit(app.exec_())
    print(story_file)
    return story_file

class blah:

    def read_file(self):

        file_name = self.line_edit.currentValue()
        text = file_name.readText()

        self.show_boxes(text)


def sel_click(window, sel_layout):
    items = (sel_layout.itemAt(i).widget() for i in range(sel_layout.count()))
    items_list = []
    for item in items:
        items_list.append(item.text())
    window.close()
    print(items_list[1])
    return items_list[1]


def window(matches):

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("MatLibs")

    window_vl = QtWidgets.QFormLayout()
    submit_b = QtWidgets.QPushButton('Submit')
    for match in matches:
        match_label = QtWidgets.QLabel(match)
        word_enter = QtWidgets.QLineEdit(window)
        word(window_vl, match_label, word_enter)
    window_vl.addWidget(submit_b)
    window.setLayout(window_vl)

    submit_b.clicked.connect(lambda: on_click(window_vl))

    window.show()
    sys.exit(app.exec_())

def word(window_vl, label, line_edit):
    window_vl.addRow(label, line_edit)
    return

def on_click(window_vl):
    items = (window_vl.itemAt(i).widget() for i in range(window_vl.count()))
    labels = []
    values = []
    for i, item in enumerate(items):
        if i % 2 == 0:
            labels.append(item.text())
        else:
            values.append(item.text())
    labels.pop()    # remove submit button from list
    print(sub_matches(labels, values, story))


story = get_story()
matches = get_matches(story)
# window(matches)
print(sel_story())