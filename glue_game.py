import random

num_digits = 3
max_gueses = 10

def main():
    print( """
     i' thinking of a {}-digit number with no repeated digits
    try to guess what is it. here a some clues:
    WHEN I SAY:     That means
        pico:    one digit is current but different position
        Fermi:   one digit is correct and in right position
        Bagel:   no digits is correct
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico\n""".format(num_digits))

    while True:
        Secreat_num = get_secreat_num()
        print('you have {} guess to get it' .format(max_gueses))

        num_gueses = 1
        while num_gueses <= max_gueses:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('guess {}: '.format(num_gueses))
                guess = input('enter here: ')
            clues = get_clues(guess, Secreat_num)
            print(clues)
            num_gueses +=1

            if guess == Secreat_num:
                break
            if num_gueses > max_gueses:
                print('you run out the guess')
                print('the answer was: {}'.format(Secreat_num))
        print('do you want to play again(yes/no)')
        if not input('>> ').lower().startswith('ye'):
            break
        print('thank you for playing!')

def get_secreat_num():
    """returns a string made up if Num_Digits uniques random digits"""
    number = list('0123456789')
    random.shuffle(number)
    secreat_num = ' '
    for i in range(num_digits):
        secreat_num += str(number[i])
    return secreat_num

def get_clues(guess, secreat_num):
    """return a string whith the pico fermi bagel clues for a guess
    and secreat numbe pair"""
    if guess == secreat_num:
        return 'you got it'
    
    clues = []

    for i in range (len(guess)):
        if guess[i] == secreat_num[i]:
            clues.append('Fermi')
        elif guess[i] in secreat_num:
            clues.append('picco')
        if len(clues) == 0:
            return 'bagel'
        else:
            clues.sort()
            return ''.join(clues)
if __name__ == '__main__':
    main()
         