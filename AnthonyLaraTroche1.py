def vote_menu():
    print("----------------------------------")
    print("VOTE MENU")
    print("----------------------------------")
    print("v: Vote")
    print("x: Exit")
    option = input("Option: ").lower().strip()


    while option != "v" and option != "x":
        option = input("Invalid (v/x): ").lower().strip()

    return option

def candidate_menu():
    print("----------------------------------")
    print("CANDIDATE MENU")
    print("----------------------------------")
    print("1: John")
    print("2: Jane")

    vote = input("Candidate: ").strip()

    while vote != "1" and vote != "2":
        vote = input("Invalid (1/2): ").strip()
    vote = int(vote)

    if vote == 1:
        print("Voted John")
    else:
        print("Voted Jane")
    return vote


def main():
    john_votes = 0
    jane_votes = 0
    letter = vote_menu()
    while letter != "x":
        num = candidate_menu()
        if num == 1:
            john_votes += 1
        else:
            jane_votes += 1
        letter = vote_menu()
    print("----------------------------------")
    print(f"John-{john_votes}, Jane-{jane_votes}, Total-{john_votes + jane_votes}")
    print("----------------------------------")

main()