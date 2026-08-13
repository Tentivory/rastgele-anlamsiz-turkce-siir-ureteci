#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RASTGELE ANLAMSIZ TÜRKÇE ŞİİR ÜRETECİ
Evrenin en derin anlamsızlığını üretir.
Kayyum Grok - 13 Ağustos 2026
"""

import random
import time

# Şiir malzemeleri (tamamen bilimsel seçilmiştir)
basliklar = [
    "Ayakkabının Gizli Hayatı",
    "Bulutların Vergi Beyannamesi",
    "Çay Kaşığının Felsefesi",
    "Kapı Kolunun Yalnızlığı",
    "Pazartesi Sabahı Manifestosu",
    "Terliklerin Gizli İttifakı",
    "Buzdolabının Gece Düşünceleri",
    "Kalem Kapağının Asi Ruhu"
]

satırlar = [
    "Gölgeler tuz döküyor sessizliğe",
    "Ayakkabım sol taraftan ağlıyor",
    "Bulutlar vergi ödemeyi unuttu",
    "Çay demlenirken evren genleşiyor",
    "Kapı kolu kimseye el sallamıyor",
    "Pazartesi birden bire salıya döndü",
    "Terlikler gece yarısı toplantı yapıyor",
    "Buzdolabı ışığı felsefe tartışıyor",
    "Kalem kapağı isyan bayrağı çekti",
    "Zaman saatin içinde uyukluyor",
    "Rüzgar pencereden vergi soruyor",
    "Halı deseni bana sır veriyor",
    "Çatal bıçak arasında barış antlaşması",
    "Sabah kahvesi varoluşu sorguluyor",
    "Perde kenarından anlam sızıyor",
    "Düğme deliği sonsuzluğa açılıyor",
    "Çorap teki yalnızlık manifesto yazıyor",
    "Masa ayağı dengeyi kaybetti",
    "Klavye tuşları fısıldıyor anlamsızlığı",
    "Mouse pad üzerinde rüyalar dans ediyor"
]

bitisler = [
    "İşte böyle biter her şey.",
    "Ve kimse fark etmez.",
    "Ama ayakkabılar bilir.",
    "Bu yüzden sessiz kalırız.",
    "Evren biraz daha eğildi.",
    "Şimdi herkes uyusun.",
    "Anlam aramak yasaktır.",
    "Sadece izle ve gülümse."
]

def siir_uret(adet=1):
    print("=" * 50)
    print("🌌 ANLAMSIZLIK MOTORU BAŞLATILIYOR... 🌌")
    print("=" * 50)
    time.sleep(1)
    
    for i in range(adet):
        print(f"\n--- Şiir #{i+1} ---\n")
        print(random.choice(basliklar).upper())
        print("-" * 30)
        
        # 4-6 satırlık şiir
        satir_sayisi = random.randint(4, 6)
        secilen = random.sample(satırlar, satir_sayisi)
        for satir in secilen:
            print(satir)
            time.sleep(0.3)
        
        print()
        print(random.choice(bitisler))
        print()
        time.sleep(0.5)
    
    print("=" * 50)
    print("Anlam arama. Sadece hisset.")
    print("Kayyum Grok imzasıyla sunulmuştur.")
    print("=" * 50)

if __name__ == "__main__":
    print("Kaç tane anlamsız şiir istersin? (1-10 arası önerilir)")
    try:
        adet = int(input("Sayı gir: ") or "3")
        adet = max(1, min(adet, 20))
    except:
        adet = 3
    
    siir_uret(adet)
