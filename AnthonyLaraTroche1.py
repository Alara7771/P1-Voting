from PyQt6.QtWidgets import QMainWindow, QApplication
from gui import *
class Vote(QMainWindow, Ui_Voting):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.age = self.age_entry
        self.first = self.first_name
        self.second = self.Last_name

        self.first_list = []
        self.second_list = []
        self.age_list = []

        self.candidate_1_vote = 0
        self.candidate_2_vote = 0

        self.send_vote.clicked.connect(lambda : self.check())

    def check(self):
        try:
            self.age = int(self.age.text())

            for let in self.first:
                if let.isdigit():
                    raise TypeError
            for let in self.second:
                if let.isdigit():
                    raise TypeError
            if self.age < 18:
                self.main_label.setText("Must be 18 or older")

        except ValueError:
            self.main_label.setText("Enter age integer")
        except TypeError:
            self.main_label.setText("Name cannot have numbers")






