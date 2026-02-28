def ftm(feet):
    return feet * 0.3048


def mtf(meters):
    return meters / 0.3048

#4.3-----------------------------------------

salestax = 0.06
def tax(total):
    return round(total * salestax, 2)

def totalTax(total):
    return round(total + tax(total),2)
    