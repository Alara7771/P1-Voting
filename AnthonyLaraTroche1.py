from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui import *
import csv
class Vote(QMainWindow, Ui_Voting):
    """
    This class contains the processes behind voting and
    ending the vote
    """

    def __init__(self) -> None:
        """
        setting up variables,easy access changes, and lists
        """
        super().__init__()
        self.setupUi(self)


        self.vote_option = ""

        self.rad_1.setText("John")
        self.rad_2.setText("Jane ")

        self.label_3.setText("Vote ID")

        self.voter_list = []

        self.candidate_1_vote = 0
        self.candidate_2_vote = 0

        self.send_vote.clicked.connect(lambda : self.check())
        self.finish_vote.clicked.connect(lambda : self.finish())

    def check(self)-> None:
        """
        Takes voter input and ensures its correct and all fields are
        filled once vote is sent it's stored in a list and watches for duplicate
        entries

        """

        try:
            first_name = self.first_name.text()
            last_name = self.Last_name.text()
            id_num = self.age_entry.text()

            if first_name == "" or last_name == "" or id_num == "":
                return self.main_label.setText("Please enter all fields")

            for letter in first_name:
                if letter.isalpha():
                    continue
                else:
                    raise TypeError
            for letter in last_name:
                if letter.isalpha():
                    continue
                else:
                    raise TypeError


            for num in id_num:
                if not num.isdigit():
                    return self.main_label.setText("Enter digits no characters")
            if len(id_num) != 5:
                return self.main_label.setText("Vote ID must be 5 digits")

            for candidate in self.voter_list:
                if candidate[2] == id_num:
                    return self.main_label.setText("Vote ID already exists")


            if self.rad_1.isChecked():
                self.candidate_1_vote +=1
                self.vote_option = self.rad_1.text()
                self.main_label.setText(f"You voted for {self.rad_1.text()}!")

            elif self.rad_2.isChecked():
                self.candidate_2_vote +=1
                self.vote_option = self.rad_2.text()
                self.main_label.setText(f"You voted for {self.rad_2.text()}!")

            else:
                return self.main_label.setText("Select a candidate")


            self.voter_list.append([self.first_name.text(), self.Last_name.text(), self.age_entry.text(), self.vote_option])

            self.first_name.clear()
            self.Last_name.clear()
            self.age_entry.clear()

            self.rad_1.setAutoExclusive(False)  #used AI to figure out how to uncheck radio buttons
            self.rad_1.setChecked(False)
            self.rad_2.setChecked(False)
            self.rad_1.setAutoExclusive(True)

        except ValueError:
            return self.main_label.setText("ID must be a number")
        except TypeError:
            return self.main_label.setText("Name cannot contain numbers")


    def finish(self) -> None:
        """
        Checks that there are votes, sends to csv file, checks who won
        then the main window is closed and a popup appears with what number
        of votes that each side had and who the winner was
        """
        if len(self.voter_list) == 0:
            return self.main_label.setText("There are no votes")



        with open("results.csv", "w", newline="" ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["First name", "Last name", "Voter ID", "Candidate"])
            writer.writerows(self.voter_list)


        if self.candidate_1_vote > self.candidate_2_vote:
            winner = f"        {str(self.candidate_1_vote)}|{str(self.candidate_2_vote)}\nWinner: {self.rad_1.text()}"
        elif self.candidate_2_vote > self.candidate_1_vote:
            winner = f"        {str(self.candidate_1_vote)}|{str(self.candidate_2_vote)}\nWinner: {self.rad_2.text()}"
        else:
            winner = "It's tied"

        box = QMessageBox()
        box.setWindowTitle("Voting Results")
        box.setText(f"---Results---\n{self.rad_1.text()} | {self.rad_2.text()}\n{winner}")
        box.exec()
        self.close()







