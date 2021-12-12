#wap that defines a list of players who are in a team check whether a particular
#player is there in the team or not

list_play=["smith","tom","harry","helen","smyle"]
player=input("enter the name of the player: ")
if player in list_play:
    print(player,"is  a member")
else:
    print(player, "is not a member")
