def dollar_to_ksh(dollar,gbp=100):
    ksh = dollar * 103.5 +  gbp * 126.5
    print (ksh)
    
print("Kenyan shilings to $100 plus 100 gbp is:")
dollar_to_ksh(100)


def euro_to_ksh(euro):
    ksh = euro * 111.74
    print(ksh)

print("Kenyan shilings to Euro is:")
(euro_to_ksh(100 ))


def age_foo (age ):
    new_age= float(age)+ 50    
    return new_age
    
age = input("Enter your Age: ")
print(age_foo(age))

def celsius_to_farenheit (celcius ):
    farenheit = celcius*9/5 + 32
    return farenheit

celcius =input("Enter the degrees tou want to convert")
print (celsius_to_farenheit (celcius ))



def c_to_f(c):    
    if c< -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f=c*9/5+32        
        return f
print(c_to_f(-273.4))