#FARKLI ZAMAN DILIMLERINDE LISTELER DE DAHIL OLMAK UZERI BIRDEN COK KOMPOZIT ELEMAN KUMESI ILE ISLEM GERCEKLESTIRMEMIZ GEREKEBILIR.
#BU NOKTADA TUPPLE (DEMET) COZUM SAGLAMAKTADIR.
#EK OLARAK TUPPLE OGELERI IMMUTABLE (DEGISTIRILEMEYEN) VERI TIPLERIDIR.

#TUPPLE FORMATLARINDA ELEMANLAR VIRGULLER ILE BIRBIRINDEN AYRILARAK KULLANILMAKTADIR.
#tupple=a,b,c,[]...

tupple_tip1=("Mirac","OZTURK",1923,3.14,[1,2,3])

tupple_tip2="Mirac","OZTURK",1923,3.14,[1,2,3]

tupple_hata="Mirac"
type(tupple_hata)
#BURADA ILGILI ELEMANI BIR DEGER OLARAK ALGILAR.

tupple_tip3="Mirac",
type(tupple_tip3)
#BURADA ISE VIRGUL EKLENMESI ILE ILGILI ELEMANI BIR TUPPLE OLARAK ALGILAR.
#SANKI IKINCI BIR ELEMAN VAR VE BLANK/NULL GIBI.

tupple_tip1[0]
#BIRINCI ELEMENA ERISMEK ICIN KULLANILIR.

tupple_tip1[0:3]
#BIRINCI ELEMENDAN UCUNCU ELEMANA KADAR ERISMEK ICIN KULLANILIR.

tupple_tip1[2]=1881
#ELEMAN DEGISIKLIKGI ISLEMINDE TUPPLE HATA VERIR.
#TypeError: 'tuple' object does not support item assignment
#BU HICBIRSEYIN DEGISMESINI ISTEMEDIGINIZ DEGER VE DEGER GRUBU ICIN ONEM ARZ ETMEKTEDIR.