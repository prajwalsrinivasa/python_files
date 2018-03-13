def replace():
    string_bubble='pupple'
    front = string_bubble[0]
    back = string_bubble[1:]
    fixed_back = back.replace(front, '*')
    return front + fixed_back

print_this=replace()
print(print_this)
        
