
def user_input():
    L = int(input("How much do you want to borrow?: "))
    yearly_rate = float(input("At what rate?: "))
    years = int(input("How many years?:"))

    return (L, yearly_rate, years)


def count_values(monthly_payment, left_to_pay, r, years):
    values = []
    for i in range(1,years*12 + 1):
        monthly_interest = round(left_to_pay * r)
        principal = monthly_payment-monthly_interest
        values.append([i, monthly_interest, principal, left_to_pay])
        left_to_pay -= monthly_payment

    return values


def print_line(width):
    a= (sum(width.values()) + 5 ) * '='
    print(a)


def print_header(width, first_line, sec_line):
    print_line(width)
    print('|{:{w1}}|{:{w2}}|{:{w3}}|{:{w4}}|'.format( *first_line,**width ))
    print_line(width)
    print('|{:^{w1}}|{:^{w2}}|{:^{w3}}|{:^{w4}}|'.format(*sec_line, **width))
    print_line(width)

def print_values(payment_stats, width):
    for i in payment_stats:
        print('|{:^{w1},}|{:^{w2},}|{:^{w3},}|{:^{w4},}|'.format(*i, **width))
    print_line(width)




def main():
    L, yearly_rate, years = user_input()

    r = yearly_rate / 100 / 12
    n = number_of_months = years * 12
    monthly_payment = int(round(L*(r * (1 + r)**n) / ((1 + r)**n-1), 0 ))
    total_amount = monthly_payment * number_of_months
    total_interest = total_amount - L

    first_line = ['Loan:' + str(L), 'Years:' + str(years), 'Interest:' + str(total_interest), 'Monthly Payment:' + str(monthly_payment)]
    width = {'w1':len(first_line[0])+2, 'w2':len(first_line[1])+2, 'w3':len(first_line[2])+2, 'w4':len(first_line[3])+2}
    sec_line = ['Payment', 'Interest', 'Principal', 'Left to Pay']

    print_header(width, first_line, sec_line)
    payment_stats = count_values(monthly_payment, total_amount,r,years)
    print_values(payment_stats,width)

if __name__ == '__main__':
    main()
