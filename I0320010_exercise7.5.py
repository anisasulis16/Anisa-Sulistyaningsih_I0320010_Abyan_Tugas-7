#Membuat fungsi tanpa nama dengan operator lambda
def panggil(func):
    return func
def helloworld():
    return "HELLO WORLD"
def main():
    daftarnama = ["Adi, Cahyo, Budi, Dedi"]
    print("Keadaan awal")
    print(daftarnama)

    print("\nMenggunakan sorted():")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print('\nKeadaan Akhir: ')
    print(daftarnama)
if __name__ == '__main__':
    main()