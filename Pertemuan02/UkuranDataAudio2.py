sampel_rate = float(input("sampel rate: "))
bit_depth = float(input("bit depth: "))
jml_kanal = int(input("jumlah kanal: "))
durasi = float(input("durasi (detik): "))

ukuran_data = sampel_rate * (bit_depth / 8) * jml_kanal * durasi

print("Ukuran data audio:", ukuran_data, "byte")