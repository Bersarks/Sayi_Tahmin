import random as rnd
deger = 0
while 42:
	deger += 10
	tryCount = 0
	flag = 0
	number = rnd.randint(1, 100)
	print("Sayı tahmin oyununa hoşgeldiniz. 1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalışın. Çıkmak için q/Q tuşuna basın.")
	while tryCount < deger:
		num = input("Tahmin ettiğiniz sayı: ")
		tryCount += 1
		if num == "q" or num == "Q":
			print("Oyun kendi isteğinizle sonlandı.")
			flag = 1
			break
		if num == "":
			if tryCount == deger:
					print("Tahmin hakkınız bitti. Sayı: "+ str(number))
					deger -= tryCount
					break
			else:
				print("Girdiğiniz değeri kontrol edin.")
				continue
		elif num.lstrip("+-").isdigit():
			num = int(num)
			if num >= 1 and num <= 100:
				if num == number:
					print("Tebrikler, sayıyı "+ str(tryCount) +" denemede doğru tahmin ettiniz. Sayı: "+ str(number))
					deger -= tryCount
					break
				elif tryCount == deger:
					print("Tahmin hakkınız bitti. Sayı: "+ str(number))
					deger -= tryCount
					break
				elif num - number <= 3 and num - number >= 0:
					print("Çok yaklaştın tahminini biraz küçült")
				elif num - number >= -3 and num - number <= 0:
					print("Çok yaklaştın tahminini biraz büyüt")
			else:
				if  tryCount == deger:
					print("Tahmin hakkınız bitti. Sayı: "+ str(number))
					deger -= tryCount
					break
				else:
					print("Girdiğiniz değer tahmin aralığında değil.")
		else:
			if tryCount == deger:
					print("Tahmin hakkınız bitti. Sayı: "+ str(number))
					deger -= tryCount
					break
			else:
				print("Girdiğiniz değeri kontrol edin.")
	if flag == 1:
		break
