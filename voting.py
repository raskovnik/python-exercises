elections = True
students , prefects , captain , nprefects , ncaptain = [] , {} , {} , {} , {}
def elect(studentid):
    if studentid not in students:
        students.append(studentid)
        select_rank(studentid)
    else:
        print("You have already voted!!!")

def select_rank(studentid):
    print("Select Rank: \n[1].Prefect\n[2].Captain")
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
    while Captains != 1:
        winner_votes = max(captain.values())
        winner = get_captain_winner(winner_votes)
        ncaptain[winner] = winner_votes
        Captains += 1
        # del captain[winner]
        # captain.pop(winner)
def results():
    #captain_winner()
    print(f"The new school captain is {get_captain_winner(max(captain.values()))} with {max(captain.values())} votes")
   # print(f"The new assistant school captain is {get_captain_winner(min(ncaptains.values()))} with {min(ncaptains.values())} votes")
while elections:
    print("School elections!")
   #456 print("School Elections!\n\[1].Vote\n[2].End Elections")
    studentid = int(input("Enter your studentid:"))
    if studentid == 1:
        elections = False
        print("Elections are over!")
        results()
    elect(studentid)
def end_elections():
    pass

