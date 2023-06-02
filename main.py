import random

def get_random_number(min_number, max_number):
    return random.randint(min_number, max_number)

def start_game():
    print("Sayı Tahmin Etme Oyunu")
    print("Bilgi: Sizin belirlediğiniz sayılar arasında bir rastgele sayı belirlenir ve o sayıyı bilirseniz kazanırsınız.")
    print("İyi eğlenceler!")

    while True:
        try:
            min_number = int(input("1. sayıyı girin: "))
            max_number = int(input("2. sayıyı girin: "))

            if min_number >= max_number:
                print("Hatalı giriş! İkinci sayı, birinci sayıdan büyük olmalıdır. Tekrar deneyin.")
                continue

            prediction = get_random_number(min_number, max_number)
            print("Tahmin edilmesi gereken sayı belirlendi. Şimdi tahminlerinizi yapabilirsiniz!")
            break
        except ValueError:
            print("Geçerli sayılar giriniz.")

    while True:
        guess = input("Tahmininiz nedir? ")

        if guess.isdigit():
            guess = int(guess)

            if guess == prediction:
                print("Tebrikler, doğru tahmin ettiniz!")
                play_again = input("Bir daha oynamak ister misiniz? (Evet için 'e', Hayır için 'h'): ")

                if play_again.lower() == "e":
                    start_game()
                else:
                    break
            else:
                print("Yanlış cevap, başka bir tahminde bulunun.")
        else:
            print("Geçerli bir sayı giriniz.")

start_game()
