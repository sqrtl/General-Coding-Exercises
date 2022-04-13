def romanNumeral(numero):
    numDict = {
        1000:"M",
        900:"CM",
        500:"D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
    }
    print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    for x in print_order:
        if numero != 0:
            quotient= numero//x

            #If quotient is not zero output the roman equivalent
            if quotient != 0:
                for y in range(quotient):
                    print(numDict[x], end="")

            #update integer with remainder
            numero = numero%x

romanNumeral(1901)
romanNumeral(1889)
romanNumeral(190)
romanNumeral(201)