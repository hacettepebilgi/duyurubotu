import requests
from bs4 import BeautifulSoup
import time
from win10toast import ToastNotifier

def duyurulari_say():
  url = "https://sksdb.hacettepe.edu.tr/bidbnew/announcements.php"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  duyurular = soup.select('div.col-lg-9.col-12.mb-3 p')
  return len(duyurular)

def bildirim_gonder(mesaj):
  toaster = ToastNotifier()
  toaster.show_toast("Duyuru Güncelleme", mesaj, duration=10)

def main():
  ilk_duyuru_sayisi = duyurulari_say()
  print(f"Şu anki duyurular çekildi. Duyuru sayısı: {ilk_duyuru_sayisi}")
  
  while True:
      time.sleep(60)  # 60 saniye bekle
      yeni_duyuru_sayisi = duyurulari_say()
      
      if yeni_duyuru_sayisi > ilk_duyuru_sayisi:
          fark = yeni_duyuru_sayisi - ilk_duyuru_sayisi
          mesaj = f"{fark} yeni duyuru eklendi! Toplam duyuru sayısı: {yeni_duyuru_sayisi}"
          bildirim_gonder(mesaj)
          ilk_duyuru_sayisi = yeni_duyuru_sayisi
      elif yeni_duyuru_sayisi < ilk_duyuru_sayisi:
          fark = ilk_duyuru_sayisi - yeni_duyuru_sayisi
          mesaj = f"{fark} duyuru kaldırıldı! Toplam duyuru sayısı: {yeni_duyuru_sayisi}"
          bildirim_gonder(mesaj)
          ilk_duyuru_sayisi = yeni_duyuru_sayisi

if __name__ == "__main__":
  main()