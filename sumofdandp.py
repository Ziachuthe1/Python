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