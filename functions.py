def dollar_to_ksh(dollar,gbp):
    ksh = dollar * 103.5 +  gbp * 126.5
    return (ksh)



def euro_to_ksh(euro):
    ksh = euro * 111.74
    return (ksh)



print("Kenyan shilings to $100 plus 100 gbp is:")
print(dollar_to_ksh(100, 100))

print("Kenyan shilings to Euro is:")
print (euro_to_ksh(100 ))