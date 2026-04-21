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
            age = self.age
            first_name = self.first
            last_name = self.second

            age = int(age)
            if age < 18:
                self.main_label.setText("Must be 18 or older")

            for let in first_name:
                if let.isdigit():
                    raise TypeError
            for let in last_name:
                if let.isdigit():
                    raise TypeError
            if self.age < 18:
                self.main_label.setText("Must be 18 or older")



            if self.rad_1.isChecked():
                self.candidate_1_vote +=1
                self.main_label.setText("You voted for John!")

            elif self.rad_2.isChecked():
                self.candidate_2_vote +=1
                self.main_label.setText("You voted for Jane!")

            else:
                self.main_label.setText("Select a candidate")

        except ValueError:
            self.main_label.setText("Enter age integer")
        except TypeError:
            self.main_label.setText("Name cannot have numbers")

        self.first_list.append(self.first)
        self.second_list.append(self.second)
        self.age_list.append(self.age)







