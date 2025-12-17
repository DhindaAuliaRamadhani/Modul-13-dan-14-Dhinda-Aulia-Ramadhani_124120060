class Sensor:
    def __init__(self, id_sensor, lokasi, jenis):
        self.id_sensor = id_sensor
        self.lokasi = lokasi
        self.jenis = jenis

    def info(self):
        return f"ID: {self.id_sensor}, Lokasi: {self.lokasi}, Jenis: {self.jenis}"


class SensorSeismik(Sensor):
    def __init__(self, id_sensor, lokasi, jenis, frekuensi_sampling):
        super().__init__(id_sensor, lokasi, jenis)
        self.frekuensi_sampling = frekuensi_sampling  # dalam Hz

    def jumlah_sampel(self, durasi_detik):
        """
        Menghitung jumlah sampel amplitudo berdasarkan durasi.
        rumus: jumlah sampel = frekuensi_sampling × durasi
        """
        return int(self.frekuensi_sampling * durasi_detik)


# Contoh penggunaan
sensor1 = SensorSeismik("S001", "Stasiun A", "Seismik", 100)  # 100 Hz
print(sensor1.info())
print("Jumlah sampel dalam 10 detik:", sensor1.jumlah_sampel(10))
