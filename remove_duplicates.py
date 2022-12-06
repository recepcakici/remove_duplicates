# Dosya adını kullanıcıdan al
file_name = input("Lütfen dosya adını girin: ")

# Dosyayı okuma modunda aç
with open(file_name, "r") as file:
  # Dosyadaki tüm satırları bir listeye ata
  lines = file.readlines()

# Tekrarlanan satırları silmek için bir set oluştur
unique_lines = set()

# Dosyadaki satırları tek tek kontrol et
for line in lines:
  # Eğer satır set içinde yoksa ekle
  if line not in unique_lines:
    unique_lines.add(line)

# Dosyayı yazma modunda aç
with open(file_name, "w") as file:
  # Set içindeki tek tek satırları dosyaya yaz
  for line in unique_lines:
    file.write(line)

# Dosyayı kapat
file.close()
