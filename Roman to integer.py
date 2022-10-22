def decode_roman(roman):
    sum = 0
    index = 0
    for i in roman:
        if index > len(roman)-1:
            break

        if roman[index] == "M":
            sum += 1000
            index += 1

        elif roman[index] == "D":
            sum += 500
            index += 1

        elif roman[index] == "C":
            if index+1 <= len(roman)-1:
                if roman[index + 1] == "D":
                    sum += 400
                    index += 2
                elif roman[index + 1] == "M":
                    sum += 900
                    index += 2
                else:
                    sum += 100
                    index += 1
            else:
                sum += 100
                index += 1

        elif roman[index] == "L":
            sum += 50
            index += 1

        elif roman[index] == "X":
            if index+1 <= len(roman)-1:
                if roman[index + 1] == "L":
                    sum += 40
                    index += 2
                elif roman[index + 1] == "C":
                    sum += 90
                    index += 2
                else:
                    sum += 10
                    index += 1
            else:
                sum += 10
                index += 1

        elif roman[index] == "V":
            sum += 5
            index += 1

        elif roman[index] == "I":
            if index+1 <= len(roman)-1:
                if roman[index + 1] == "V":
                    sum += 4
                    index += 2
                elif roman[index + 1] == "X":
                    sum += 9
                    index += 2
                else:
                    sum += 1
                    index += 1
            else:
                sum += 1
                index += 1

    return sum


print(decode_roman(input()))
