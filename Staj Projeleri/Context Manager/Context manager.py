class FileContextManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        # Tam dosya yolunu belirtin
        self.full_file_path = r'C:\Users\buraq\PycharmProjects\Kodlama Egzersizleri\Context Manager\\' + self.file_name
        self.file = open(self.full_file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Kullanımı
with FileContextManager("Deneme.txt", "w") as dosya:
    dosya.write("Bu dosyaya yazıldı.")
