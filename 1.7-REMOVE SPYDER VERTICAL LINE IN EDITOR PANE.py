#HOW TO REMOVE SPYDER VERTICAL LINE ON RIGHT SIDE OF EDITOR PANE?
#EDITOR BOLMESININ SAG TARAFINDAKI SPYDER DIKEY HATTI NASIL KALDIRILIR?

#Settings -> Completion and linting -> Code style and formatting -> Line length -> Show vertical line at that length


#GORUNTU ILE KONTROL. (MINI DENEME EK OLARAK.)
import urllib.request
import webbrowser

link='https://miracozturk.com/wp-content/uploads/2022/10/how-to-remove-spyder-vertical-line-on-right-side-of-editor-pane.png'

#KOD DERLEMESI SAYFA KONTROLU.
get_url= urllib.request.urlopen(link)
print("Response Status: "+ str(get_url.getcode()) )
print(get_url.read())


#TARAYICI UZERINDE SAYFA KONTROLU.
get_url= webbrowser.open(link)
