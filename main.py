Found = False
Position=0
array=[1,2,3,4,5,6,7,8,9,10]
item=4
while Found == False and Position <= len(array) -1:
    if array[Position] == item:
        Found == True
    else:
        Position = Position + 1
if Found == True:
    print("Item found at position " + Position)
else:
    print("Item not found in list")
