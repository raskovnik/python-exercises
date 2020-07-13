elections = True
students , prefects , captain , nprefects , ncaptain = [] , {} , {} , {} , {}
def elect(studentid):
    if len(str(studentid)) != 4:
        print("Invalid student id!")
        studentid = int(input("Enter a valid studentid!"))
    if studentid not in students:
        students.append(studentid)
        select_rank(studentid)
    else:
        print("You have already voted!!!")

def select_rank(studentid):
    print("Select Rank: \n[1].Prefect\n[2].Captain\n")
    try:

        rank = int(input("Enter rank:"))
        if rank == 1:
            xvotes = 0
            while xvotes != 2:
                elect_prefects()
                xvotes += 1

        if rank == 2:
            elect_captain()

        else:
            print("Enter a valid rank:")
            select_rank(studentid)
        
    except ValueError as e:
        print("Your input is not an integer")

def elect_prefects():
    prefectname = input("Enter prefect name:")
    if prefectname not in prefects:
        prefects[prefectname] = 1
    else:
        prefects[prefectname] += 1

def elect_captain():
    captainname = input("Enter captain name:")
    if captainname not in captain:
        captain[captainname] = 1
    else:
        captain[captainname] += 1

def get_prefect_winner(votes):
    for key, value in prefects.items():
        if votes == value:
            return key

def prefects_winner():
    Prefects = 0
    while Prefects != 4:
        winner_votes = max(prefects.values())
        winner = get_prefect_winner(winner_votes)
        nprefects[winner] = winner_votes
        Prefects += 1
        del prefects[winner]

def get_captain_winner(votes):
    for key, value in captain.items():
        if votes == value:
            return key

def captain_winner():
    Captains = 0
    while Captains != 2:
        winner_votes = max(captain.values())
        winner = get_captain_winner(winner_votes)
        ncaptain[winner] = winner_votes
        del captain[winner]
        Captains += 1
def results():
    print("Elections are over")
    captain_winner()
    prefects_winner()
    print(f"The new school captain is {get_captain_winner(max(ncaptain.values()))} with {max(ncaptain.values())} votes")
    print(f"The new assistant school captain is {get_captain_winner(min(ncaptain.values()))} with {min(ncaptain.values())} votes")
while elections:
    print("School elections!\n")
   #456 print("School Elections!\n\[1].Vote\n[2].End Elections")
    studentid = str(input("Enter your studentid:"))
    password = "Admin"
    if studentid == "Admin":
        admin = input('Enter admin password:')
        if admin == password:
            results()
            break
        else:
            print("Enter a valid admin password\n")
            
    elect(studentid)
