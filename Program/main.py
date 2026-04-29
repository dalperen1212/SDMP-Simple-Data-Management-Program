file = 'xxx.txt'

def kisi_ekle(isim: str,yas: int,gecmis=None,egitim='lise'):
    x = {
        'adı:':isim.split(),
        'yaşı:':yas,
        'geçmişi:':gecmis,
        'egitim:':egitim
    }
    return x
def file_newuser():
    a = str(input('isim gir: '))
    b = int(input('yaşı gir: '))
    d = str(input('geçmişini gir: '))
    g = str(input('eğitim gir: '))
    try:
        with open (file,"a+") as f:
            f.write(str(kisi_ekle(a,b,d,g))+'\n')
    except (FileNotFoundError, PermissionError):
        print("dosya bulunamadi")
    else:
        print("işlem başarılı bir şekilde tamamlandı!")

def file_finduser():
    name = str(input('isim gir: '))
    try:
        with open (file,"r") as txt:
            lines = txt.readlines()
            for index,i in enumerate(lines):
                if name.lower() in i.lower():
                    print(f"Kayıt Bulundu! [Satır {index}]: {i.strip()}")
                    break
            else:
                raise ValueError('kişi yok')
    except (FileNotFoundError, PermissionError):
        print("dosya bulunamadi")
    except ValueError as e:
        print(e)

def del_user():
    name = str(input('isim gir: '))
    del_u = False
    try:
        with open (file,"r") as doc:
            lines = doc.readlines()
            for index,i in enumerate(lines):
                if name.lower() in i.lower():
                    new_lines = [line for line in lines if name.lower() not in line.lower()]
                    with open (file,"w") as new:
                        new.writelines(new_lines)
                        del_u = True
            if del_u == True:
                print('kişi silindi')
            else:
                raise ValueError('kişi yok')
    except (FileNotFoundError, PermissionError):
        print("dosya bulunamadi")
    except ValueError as e:
        print(f'Hata: {e}')


def main():
    while True:
        try:
            secim = int(input('''
                ne yapmak istersiniz?
                1-Yeni kişi kaydı oluştur
                2-Kişi bul
                3-Kişi sil
                4-Çıkış
            '''))
            if secim == 1:
                file_newuser()
            elif secim == 2:
                file_finduser()
            elif secim == 3:
                del_user()
            else:
                raise ValueError('Program sonlandırıldı.')
        except ValueError as e:
            print(f'Bilgi: {e}')
            break
main()