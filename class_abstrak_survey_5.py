from abc import ABC, abstractmethod
# ------------------------
# Class Abstrak
# ------------------------
class Survey(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def processing(self):
        pass


# ------------------------
# Turunan Class Survey
# ------------------------
class SeismicSurvey(Survey):
    def processing(self):
        return f"{self.nama}: Melakukan filtering sinyal seismik."


class GravitySurvey(Survey):
    def processing(self):
        return f"{self.nama}: Melakukan upward continuation pada data gravitasi."


class MagnetikSurvey(Survey):
    def processing(self):
        return f"{self.nama}: Melakukan anomaly mapping pada data magnetik."


# ------------------------
# Contoh Penggunaan
# ------------------------
survey_list = [
    SeismicSurvey("Seismic Line 01"),
    GravitySurvey("Gravity Area A"),
    MagnetikSurvey("Magnetik Grid X"),
]

# Iterasi objek dan panggil processing()
for survey in survey_list:
    print(survey.processing())

# %%
