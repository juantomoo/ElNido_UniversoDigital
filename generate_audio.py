import asyncio
import edge_tts
import os

TEXT_FRAGMENTS = [
    ("01_intro.mp3", "Muchos estarán condenados a una vida de aislamiento como yo por diversas condiciones. En mi caso, un cerebro voluntarioso que a veces falla sin un diagnóstico claro. Aún así el fallo es real, doloroso, y lo acompañan otros síntomas como alucinaciones visuales, auditivas y olfativas."),
    ("02_anclado.mp3", "Anclado al nexo digital, a veinte pisos sobre el asfalto, una falla sensorial me golpeó: el crudo aroma a petricor. El cielo era un domo de luz artificial, pero mi corteza reproducía la fragancia de tierra mojada."),
    ("03_ruido_blanco.mp3", "Luego, el ruido blanco. No la estática de la red, sino el algoritmo sonoro de un río ancestral, del valle remoto que me abrigó donde las bio-frecuencias de aves e insectos dominaban, hasta que el estruendo sónico de las explosiones humanas fracturaban el paisaje."),
    ("04_flujo_datos.mp3", "Ruido blanco que interfiere mi flujo de datos y me lleva a la grandiosidad de la naturaleza, a la más dura violencia y abandono que pueden vivir los olvidados. Llega sin pedirlo como una falla a mi sistema nervioso central, y también me lleva al recuerdo y las sensaciones de los momentos que me llenaron de esperanza."),
    ("05_empatia.mp3", "Empatía y plenitud tan sublime que desde ese instante he soñado compartir con cada ser de este mundo que viaja a una gran velocidad y no tiene tiempo para detenerse a respirar."),
    ("06_cierre.mp3", "Ruido blanco que se siente como un hormigueo eléctrico, un calambre paralizante y me transporta a lo más doloroso y bello, una puerta trasera de información que llevo implantada como un germen de cambio que ha tomado el control e iré navegando en búsqueda de respuestas.")
]

VOICE = "es-CO-SalomeNeural" # Voz femenina colombiana natural, con inflexión pausada e íntima
RATE = "-10%" # Cadencia pausada para favorecer la escucha íntima y la respiración
PITCH = "-2Hz"

async def generate():
    out_dir = "/home/juan/Datos/Datos Juan/ProyectosSoftware/juantomoo/ElNido_UniversoDigital/audio"
    for filename, text in TEXT_FRAGMENTS:
        filepath = os.path.join(out_dir, filename)
        print(f"Generando {filename} con voz {VOICE}...")
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(filepath)
    print("¡Audio generado con éxito!")

if __name__ == "__main__":
    asyncio.run(generate())
