import re
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QMainWindow, QFormLayout
from madlibs import get_story, get_matches, sub_matches

# This sys excepthook section is used to activate debug on PyQt on Windows (not needed unless during debug)
sys.__excepthook = sys.excepthook
sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)
sys.excepthook = exception_hook


# Create the GUI class which consists of init, window, and button_click
# Init initializes the widgets to be used in window
# Window sets all the necessary widgets and layouts to create the GUI window
# Button_click includes all the functionality to occur when the button is clicked
class GUI(QMainWindow):
    # Set global variables here
    story = ''
    new_story = ''

    # Set up attributes of GUI instances
    def __init__(self):
        super().__init__()
        self.w_sel = QWidget()                              # Create a QWidget called w
        self.sel_story_label = QLabel(self.w_sel)                    # Create a QLabel called label1 in QWidget w
        self.sel_story_text = QLineEdit(self.w_sel)                  # Create a QLineEdit called edit1 in QWidget w
        self.sel_enter_b = QPushButton(self.w_sel)               # Create a QPushButton called button in QWidget w
        self.vbox_sel = QVBoxLayout()                       # Create a QVBoxLayout called vbox
        self.window_sel()                                   # Call function window()

        self.w_matches = QWidget()                              # Create a QWidget called w
        self.form_layout_matches = QFormLayout()
        self.submit_b_matches = QPushButton()

    # Set up the GUI window
    def window_sel(self):
        self.setCentralWidget(self.w_sel)                   # Set w to central widget (nothing will show without this step)

        self.sel_story_label.setText('Enter a MadLib .txt file name')                  # Set label1 text to 'testing'
        self.sel_story_text.setText('vacation_short.txt')                      # Set edit1 text to 'test'
        self.sel_enter_b.setText('Enter')                    # Set button text to 'Enter'

        self.vbox_sel.addWidget(self.sel_story_label)                # Add label1 to the vbox layout (order of this matters)
        self.vbox_sel.addWidget(self.sel_story_text)                 # Add edit1 to the vbox layout
        self.vbox_sel.addWidget(self.sel_enter_b)                # Add button to the vbox layout

        self.w_sel.setLayout(self.vbox_sel)                     # Set the window layout to vbox

        self.sel_enter_b.clicked.connect(self.button_click)  # When the button is clicked, call function button_click

        self.setWindowTitle('MatLibs')                  # Set window title

        self.show()                                     # Show the window

    def window_matches(self, matches):
        self.setCentralWidget(self.w_matches)           # Set w to central widget (nothing will show without this step)

        self.submit_b_matches.setText('Submit')
        self.w_matches.setLayout(self.form_layout_matches)
        for match in matches:
            match_label = QLabel(match)
            word_enter = QLineEdit(self.w_matches)
            self.word(match_label, word_enter)
        self.form_layout_matches.addWidget(self.submit_b_matches)
        self.w_matches.setLayout(self.form_layout_matches)

        self.submit_b_matches.clicked.connect(lambda: self.matches_click())

        self.show()

    def matches_click(self):
        items = (self.form_layout_matches.itemAt(i).widget() for i in range(self.form_layout_matches.count()))
        labels = []
        values = []
        for i, item in enumerate(items):
            if i % 2 == 0:
                labels.append(item.text())
            else:
                values.append(item.text())
        labels.pop()  # remove submit button from list
        self.new_story = sub_matches(labels, values, self.story)
        print(self.new_story)

        w_story = QWidget()
        story_label = QLabel(w_story)
        story_button = QPushButton(w_story)

        story_label.setText(self.new_story)
        story_button.setText('Close')

        story_vbox = QVBoxLayout()

        self.setCentralWidget(w_story)

        story_vbox.addWidget(story_label)
        story_vbox.addWidget(story_button)
        w_story.setLayout(story_vbox)

        story_button.clicked.connect(lambda: self.close())

        self.show()



    def word(self, label, line_edit):
        self.form_layout_matches.addRow(label, line_edit)
        return


    # This function is run when the button is clicked
    # In this example, the text from edit1 is printed in the terminal window and the window closes.
    # Other options on a button click...
        # When the button is clicked, the global variables are updated and printed,
        # the gui interface is closed,
        # and a function is called passing the updated global variables as the parameters.
    def button_click(self):
        print(self.sel_story_text.text())
        # self.read_file(self.sel_story_text.text())
        self.story = get_story(self.sel_story_text.text())
        self.window_matches(get_matches(self.story))
        # self.close()



# In the main function, start the QApplication, run an instance of the GUI class, and then exit the QApplication
def main():
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())


# This if statement only runs if this script is executed alone
# If imported and executed from another script, this section will not run
if __name__ == '__main__':
    main()