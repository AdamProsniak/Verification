def odd_numbers(card_number):

    sum_of_odd = 0
    card_number = str(card_number)

    for digit in card_number[-1::-2]:
        sum_of_odd += int(digit)

    return sum_of_odd


def even_numbers(card_number):

    sum_of_even = 0
    card_number = str(card_number)

    for digit in card_number[-2::-2]:
        digit = int(digit)

        sum_of_even += ((digit*2) % 10) + ((digit*2) // 10)

    return sum_of_even


def check_card(number):

    sum_of_even, sum_of_odd = even_numbers(number), odd_numbers(number)

    sum_of_all = sum_of_even + sum_of_odd

    if sum_of_all % 10 == 0:
        return True
    else:
        return False


def sum_of_pesel(pesel):
        if len(pesel) == 11:
            try:
                sum_of_digits = int(pesel[0]) + 3 * int(pesel[1]) + 7 * int(pesel[2]) + 9 * int(pesel[3]) + int(pesel[4]) + 3 * int(pesel[5]) + 7 * int(pesel[6]) + 9 * int(pesel[7]) + int(pesel[8]) + 3 * int(pesel[9])
                return sum_of_digits
            except IndexError:
                return False
        else:
            return False


def PESEL(pesel):

    months = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}
    mon = 10 * int(pesel[2]) + int(pesel[3])

    sum_of_digits = sum_of_pesel(pesel)

    if len(pesel) == 11:
        try:
            if sum_of_digits % 10 == 10 - int(pesel[10]):

                if mon < 13:
                    print(pesel[4] + pesel[5] + ' ' + months[mon] + ' 19' + pesel[0] + pesel[1])
                elif mon < 33:
                    mon -= 20
                    print(pesel[4] + pesel[5] + ' ' + months[mon] + ' 20' + pesel[0] + pesel[1])
                elif mon < 93:
                    mon -= 80
                    print(pesel[4] + pesel[5] + ' ' + months[mon] + ' 18' + pesel[0] + pesel[1])
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


def check_iban(acc_number):

    acc_number = acc_number.upper()
    acc_number = acc_number.replace(' ', '')
    acc_number = acc_number[4:] + acc_number[:4]
    acc_number_int = ''

    for char in acc_number:
        if char.isalpha():
            acc_number_int += str(ord(char) - 55)
        else:
            acc_number += char
            acc_number = acc_number_int
            remainder = int(acc_number) % 97
            return remainder


def IBAN(acc_number):
    remainder = check_iban(acc_number)
    if remainder != 0:
        return True
    else:
        return False
