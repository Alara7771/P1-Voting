from PyQt6.QtWidgets import QMainWindow
from gui import *
class Vote(QMainWindow, Ui_Voting):

    def __init__(self):
        super().__init__()
        self.setupUi(self)



        self.voter_list = []

        self.candidate_1_vote = 0
        self.candidate_2_vote = 0

        self.send_vote.clicked.connect(lambda : self.check())

    def check(self):
        try:
            first_name = self.first_name.text()
            last_name = self.Last_name.text()
            age = int(self.age_entry.text())




            for letter in first_name:
                if letter.isdigit():
                    raise TypeError
            for letter in last_name:
                if letter.isdigit():
                    raise TypeError

            if age < 18:
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
            self.main_label.setText("Enter age as a number")
        except TypeError:
            self.main_label.setText("Name cannot contain numbers")

        self.voter_list.append([self.first_name.text(), self.Last_name.text(), self.age_entry.text()])









