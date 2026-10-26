import asyncio
import edge_tts
import json
import os

TEXT = """Muchos estarán condenados a una vida de aislamiento como yo por diversas condiciones, en mi caso, un cerebro voluntarioso que a veces falla sin un diagnóstico claro, aún así el fallo es real, doloroso y lo acompañan otros síntomas como alucinaciones visuales, auditivas y olfativas.

Anclado al nexo digital, a veinte pisos sobre el asfalto, una falla sensorial me golpeó: el crudo aroma a petricor. El cielo era un domo de luz artificial, pero mi corteza reproducía la fragancia de tierra mojada.

Luego, el ruido blanco, no la estática de la red, sino el algoritmo sonoro de un río ancestral, del valle remoto que me abrigó donde las bio-frecuencias de aves e insectos dominaban, hasta que el estruendo sónico de las explosiones humanas fracturaban el paisaje.

Ruido blanco que interfiere mi flujo de datos y me lleva a la grandiosidad de la naturaleza, a la más dura violencia y abandono que pueden vivir los olvidados. Llega sin pedirlo como una falla a mi sistema nervioso central y también me lleva al recuerdo y las sensaciones de los momentos que me llenaron de esperanza, empatía y plenitud tan sublime que desde ese instante he soñado compartir con cada ser de este mundo que viaja a una gran velocidad y no tiene tiempo para detenerse a respirar.

Ruido blanco que se siente como un hormigueo eléctrico, un calambre paralizante y me transporta a lo más doloroso y bello, una puerta trasera de información que llevo implantada como un germen de cambio que ha tomado el control e iré navegando en búsqueda de respuestas."""

VOICE = "es-CO-SalomeNeural"
RATE = "-6%"
PITCH = "-2Hz"

out_dir = "/home/juan/Datos/Datos Juan/ProyectosSoftware/juantomoo/ElNido_UniversoDigital/audio"
os.makedirs(out_dir, exist_ok=True)
audio_path = os.path.join(out_dir, "en_el_nido_250724.mp3")

async def main():
    print("Sintetizando narración completa...")
    comm = edge_tts.Communicate(TEXT, VOICE, rate=RATE, pitch=PITCH)
    await comm.save(audio_path)
    print(f"Narración guardada exitosamente en {audio_path}")

if __name__ == "__main__":
    asyncio.run(main())
