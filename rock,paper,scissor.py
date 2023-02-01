import random
decision=int(input("What do u choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

if decision==0:
    print(rock)
elif decision==1:
    print(paper)
elif decision==2:
    print(scissor)

print("Computer chose:")
game=random.randint(0,2)
if game==0:
    print(rock)
elif game==1:
    print(paper)
elif game==2:
    print(scissor)

if decision==0:
    if game==2:
        print("you won")
    elif game==1:
        print("you lose")
    else:
        print("retry")
if decision==1:
    if game==0:
        print("you win")
    elif game==2:
        print("you lose")
    else:
        print("retry")
if decision==2:
    if game==1:
        print("you win")
    elif game==0:
        print("you lose")
    else:
        print("retry")
    

