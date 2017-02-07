import itertools
import sys

def mesaj(isim, cerceve_karakter='*'):

    kenar_cizgiler = cerceve_karakter * (len(isim) + 2)
    print(kenar_cizgiler)
    print('{0}{0}{0}{0} {1} {0}{0}{0}{0}{0}'.format(cerceve_karakter, isim))
    print(kenar_cizgiler)

if __name__ == '__main__':

    mesaj("J A C K T H E R I P P E R \n Sifre Olusturucu V.1 Beta")



if len(sys.argv) == 4:
	liste1 = sys.argv[1]
	liste2 = sys.argv[2]
	liste3 = sys.argv[3]
else:
		
	print '\nKullanim: %s liste1.lst liste2.lst semboller.lst\n'%sys.argv[0]
	sys.exit(1) 

Kombocu = ['']

l1 = open(liste1,'r').read().split()
l2 = open(liste2,'r').read().split()
l3 = open(liste3,'r').read().split()

Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2, l3), itertools.product(l3,l2, l1))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2, l3), itertools.product(l3,l1, l2))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2, l3), itertools.product(l2,l3, l1))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2, l3), itertools.product(l1,l2, l3))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2, l3), itertools.product(l1,l3, l2))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2), itertools.product(l1,l2))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l1, l2), itertools.product(l1,l1))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l2, l3), itertools.product(l2,l3))))
Kombocu.append(map(''.join, itertools.chain(itertools.product(l3, l2), itertools.product(l3,l2))))
Kombocu.append(l1)
Kombocu.append(l2)


merhaba_canim = open('Sifre.txt','ab+')

gutuphane = []

for i in Kombocu:
	for kelimecix in i:
		gutuphane.append(kelimecix)
		


for i in sorted(set(gutuphane)):
	merhaba_canim.write(i+'\n')
	
	
merhaba_canim.close()
