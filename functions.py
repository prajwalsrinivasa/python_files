def print_some_value(gender='unknown'):
    if gender is 'm':
        print (" prajwal is ",gender)
    elif gender is 'f':
        print ('tushara is ',gender)

def calculate(value):
    amount = 68 * value
    return amount
    

print_some_value()
salary_in_us=calculate(1000)
print('shylesh salary in US',salary_in_us)
print_some_value('m')
print_some_value('f')


#calculate(3000)
