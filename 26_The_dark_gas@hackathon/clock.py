def hours(hh):
    hour = {
        0: "twelve",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "one",
        14: "two",
        15: "three",
        16: "four",
        17: "five",
        18: "six",
        19: "seven",
        20: "eight",
        21: "nine",
        22: "ten",
        23: "eleven"
    }

    if hh in hour:
        return hour[hh]
    else:
        return "invalid number of hours"

def minutes(mm):
    minutes = {
        0: "o'clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",    
        50: "fifty"
    }

    if mm in minutes:
        return minutes[mm]
    elif 21 <= mm <= 29 or 31 <= mm <= 39 or 41 <= mm <= 49 or 51 <= mm <= 59:
        tens = mm // 10 * 10
        ones = mm % 10
        return minutes[tens] + " " + minutes[ones]
    else:
        return "invalid number of minutes"

def seconds(ss):
    sec = {
        0: "o'clock",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",    
        50: "fifty"
    }

    if ss in sec:
        return sec[ss]
    elif 21 <= ss <= 29 or 31 <= ss <= 39 or 41 <= ss <= 49 or 51 <= ss <= 59:
        tens = ss // 10 * 10
        ones = ss % 10
        return sec[tens] + " " + sec[ones]
    else:
        return "invalid number seconds"


x = input("Enter a time in the format hh:mm:ss = ")

h = x[0:2]
m = x[3:5]
s = x[6:8]

print(hours(int(h)) + " hours " + minutes(int(m)) + " minutes " + seconds(int(s)) + " seconds ")