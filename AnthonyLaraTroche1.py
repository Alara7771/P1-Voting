from PyQt6.QtWidgets import QMainWindow
from gui import *
class Vote(QMainWindow, Ui_Voting):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.vote_option = ""

        self.rad_1.setText("John")
        self.rad_2.setText("Jane ")

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
                return self.main_label.setText("Must be 18 or older")



            if self.rad_1.isChecked():
                self.candidate_1_vote +=1
                self.vote_option = self.rad_1.text()
                self.main_label.setText(f"You voted for {self.rad_1.text()}!")

            elif self.rad_2.isChecked():
                self.candidate_2_vote +=1
                self.vote_option = self.rad_2.text()
                self.main_label.setText(f"You voted for {self.rad_2.text()}!")

            else:
                self.main_label.setText("Select a candidate")

        except ValueError:
            self.main_label.setText("Enter age as a number")
        except TypeError:
            self.main_label.setText("Name cannot contain numbers")

        self.voter_list.append([self.first_name.text(), self.Last_name.text(), self.age_entry.text()])










