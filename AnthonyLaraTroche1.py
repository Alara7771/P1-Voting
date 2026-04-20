from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui import *
import csv
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
        self.finish_vote.clicked.connect(lambda : self.finish())

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

        self.voter_list.append([self.first_name.text(), self.Last_name.text(), self.age_entry.text(), self.vote_option])

        self.first_name.clear()
        self.Last_name.clear()
        self.age_entry.clear()

        self.rad_1.setAutoExclusive(False)
        self.rad_1.setChecked(False)
        self.rad_2.setChecked(False)
        self.rad_1.setAutoExclusive(True)
    def finish(self):
        if len(self.voter_list) == 0:
            return self.main_label.setText("There are no votes")


        with open("results.csv", "w", newline="" ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["first_name", "last_name", "age", "Candidate"])
            writer.writerows(self.voter_list)

        self.close()
        if self.candidate_1_vote > self.candidate_2_vote:
            winner = f"Winner: {self.rad_1.text()}"
        elif self.candidate_2_vote > self.candidate_1_vote:
            winner = f"Winner: {self.rad_2.text()}"
        else:
            winner = "It's tied"

        box = QMessageBox()
        box.setWindowTitle("Voting Results")
        box.setText("---Results---")
        box.setText(f"{self.rad_1.text()} | {self.rad_2.text()}")
        box.setText(winner)








