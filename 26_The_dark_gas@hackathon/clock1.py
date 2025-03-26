def number_to_words(n):
    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty"
    }
    if n <= 20:
        return words[n]
    elif n < 60:
        tens = n // 10 * 10
        ones = n % 10
        return words[tens] + ('' if ones == 0 else '-' + words[ones])
    else:
        return "Invalid"

def time_to_words(hh, mm, ss):
    if hh > 23 or mm > 59 or ss > 59:
        return "Invalid time"
    
    hour_words = number_to_words(hh % 12 if hh % 12 != 0 else 12)
    minute_words = number_to_words(mm)
    second_words = number_to_words(ss)
    
    period = "AM" if hh < 12 else "PM"
    
    return f"{hour_words} {minute_words} {second_words} {period}"

def main():
    time_input = input("Enter time in hh:mm:ss format: ")
    hh, mm, ss = map(int, time_input.split(':'))
    print(time_to_words(hh, mm, ss))

if __name__ == "__main__":
    main()