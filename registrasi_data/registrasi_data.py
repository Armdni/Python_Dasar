def registrasi_data():
    print("\n=== REGISTRASI DATA DIRI ===")

    nik = input("Masukkan NIK (16 digit):")
    nama = input("Nama lengkap: ")
    tempat_lahir = input("Tempat lahir: ")
    tanggal_lahir = input("Tanggal lahir:(DD-MM-YYYY): ")
    jenis_kelamin = input("Jenis Kelamin: ")
    alamat = input("Alamat: ")
    agama = input("Agama: ")
    status = input("Status perkawinan: ")
    pekerjaan = input("Pekerjaan: ")
    hobi = input("Hobi: ")
    kewarganegaraan = input("kewarganegaraan: ")

    #Menyimpan data dalam dictionary
    data_diri = {
        "NIK": nik,
        "Nama Lengkap": nama,
        "Tempat Lahir": tempat_lahir,
        "Tanggal Lahir": tanggal_lahir,
        "Jenis Kelamin": jenis_kelamin,
        "Alamat": alamat,
        "Agama": agama,
        "Status Perkawinan": status,
        "Pekerjaan": pekerjaan,
        "Hobi": hobi,
        "Kewarganegaraan": kewarganegaraan,
    }

    # Menampilkan data yang sudah diinput
    print("\n================================  ")
    print("    DATA DIRI TERDAFTAR   ")
    print("================================")

    for keterangan, nilai in data_diri.items():
        print(f"{keterangan}: {nilai}")
    print("===============================")

# menjalankan program
while True:
    registrasi_data()

    ulang = input(
        "\nApakah ingin registrasi data lain? (ya/tidak): "
    ).lower()

    if ulang != "ya":
        print("program registrasi selesai.")
        break