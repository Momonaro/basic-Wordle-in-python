import emoji
import random

f = open("5lwords.txt", "r")
d5 = f.read()
d5 = d5.split(

)
d5 = list(d5)
col = {
    "red": emoji.emojize(":red_square:"),
    "yellow": emoji.emojize(":yellow_square:"),
    "green": emoji.emojize(":green_square:"),
    "<3": emoji.emojize(":red_heart:")
}


def main():
    while True:
        word = random.choice(d5)
        gcount = 0
        while True:
            guess = input("Enter a 5 Letter word:\n")
            if guess.lower() == "give up":
                print(emoji.emojize("You lose :skull:"))
                print(f"the word was {word}")
                break
            if len(guess) != 5:
                print("Invalid guess!")
                continue
            if guess not in d5:
                print("word not in dictionary")
                continue
            gcount += 1
            gyr = []
            for i in range(0, 5):
                if guess[i].lower() == word[i].lower():
                    gyr.append(col.get("green"))
                elif guess[i].lower() in word.lower():
                    gyr.append(col.get("yellow"))
                else:
                    gyr.append(col.get("red"))
            print(*gyr)
            if guess.lower() == word.lower():
                print(emoji.emojize("You Win! 🥳"))
                print(f"the word was {word}, you got it in {gcount} tries!!\n\n")
                break

        dic = input("Do you want to try again? ")
        if dic.lower() == "no":
            break
    print("Thanks for playing! " + col.get("<3"))
    print("Made by Momonaro_\n")


if __name__ == "__main__":
    main()
