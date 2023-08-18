apel = 0 
pie = 12
while True :
    x = int(input("Mari kita membuat Pie Apel! Berapa apel yang harus saya tambahkan:"))
    apel += x
    # Tulislah kode mu di bawah sini
    if apel < 12:
        print("Anda masih perlu menambahkan: ", pie - apel)
        
    elif apel > 12:
        print("Anda terlalu banyak menambah kan apel!")
        
    elif apel == 12:
        print("Jumlah apel yang Anda tambahkan sesuai!")
        break
