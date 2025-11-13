#22. Program to encrypt and decrypt strings using a simple Caesar cipher. 

word = input("Enter the sentence: ")

m = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,','A7#bC9@dE3$Fg!H2^iJ&kL*mN(oP)qR_sT+uV=wX-ZY0`1{2|3}4~5;:6"<>,.%&')
ns = word.translate(m)
print("Encrypted text:  ",ns)

# decoding the message

dm = str.maketrans('A7#bC9@dE3$Fg!H2^iJ&kL*mN(oP)qR_sT+uV=wX-ZY0`1{2|3}4~5;:6"<>,.%&','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,')
original = ns.translate(dm)
print("Decrypted text:",original)
        
