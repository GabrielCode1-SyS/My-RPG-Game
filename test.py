
full = "●"
empty = "○"

def character_one(power,height,name):
    if power < 1:
        return "Power Should be greater than 1!"
    elif height < 1:
        return "Height Should be greater than 1 !"
    elif " " in name:
        return "The name should not contain any spaces!"
    else:
        return f"""
          [*] Your Character Power: {power * full}
          [*] Your Character Height: {height * full}
          [*] Your Character Name: {name}
"""

print(character_one(0,0,"Gabriel"))

def character_two(power,height,name):
    if power < 1:
        return "The power should be Greater than 1"
    elif height < 1:
        return "The height should be Greater than 1"
    elif " " in name:
        return "The name should not contain any spaces in it!"
    else:
        return f"""
          [*] Your Character Power: {power * full}
          [*] Your Character Height: {height * full}
          [*] Your Character Name: {name}
       
"""
    
var2 = character_one(3,3,"Name")
var1 = character_two(3,3,"Name")
    
if var1 < var2:
    print("Character one is better than two")
elif var1 > var2:
    print("Character two is better than one")
elif var1 == var2:
    print("Characters are the same!")
else:
    print(var1,var2)

print(var1)
print(var2)
