row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizon_position = int(position[0])
vertical_position = int(position[1])


selected_row = map[vertical_position - 1] [horizon_position - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")