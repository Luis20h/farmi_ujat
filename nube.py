from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Receta(Model):
    medicamentos = F.TextField("medicamentos")
    interacciones = F.TextField("interacciones")
    class Meta:
        api_key = "patV3MMcvnO5mAOW0.e896513a90d18b7426604df52629a581ddeed2ba3287dcf7d0634aa8973cfb57"
        base_id = "appyG7nitmZwONNMu"
        table_name = "receta"
medicamentos = Receta(
    medicamentos="Omeprazol",
    interacciones="No comer picante"
)

medicamentos.save()


