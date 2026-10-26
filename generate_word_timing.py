import asyncio
import edge_tts
import json
import os

TEXT_SECTIONS = [
    "Muchos estarán condenados a una vida de aislamiento como yo por diversas condiciones,",
    "en mi caso, un cerebro voluntarioso que a veces falla sin un diagnóstico claro,",
    "aún así el fallo es real, doloroso",
    "y lo acompañan otros síntomas como alucinaciones visuales, auditivas y olfativas.",
    "Anclado al nexo digital, a veinte pisos sobre el asfalto,",
    "una falla sensorial me golpeó:",
    "el crudo aroma a petricor.",
    "El cielo era un domo de luz artificial,",
    "pero mi corteza reproducía la fragancia de tierra mojada.",
    "Luego, el ruido blanco,",
    "no la estática de la red, sino el algoritmo sonoro de un río ancestral,",
    "del valle remoto que me abrigó donde las bio-frecuencias de aves e insectos dominaban,",
    "hasta que el estruendo sónico de las explosiones humanas fracturaban el paisaje.",
    "Ruido blanco que interfiere mi flujo de datos",
    "y me lleva a la grandiosidad de la naturaleza,",
    "a la más dura violencia y abandono que pueden vivir los olvidados.",
    "Llega sin pedirlo como una falla a mi sistema nervioso central",
    "y también me lleva al recuerdo y las sensaciones de los momentos que me llenaron de esperanza,",
    "empatía y plenitud tan sublime que desde ese instante he soñado compartir con cada ser de este mundo",
    "que viaja a una gran velocidad y no tiene tiempo para detenerse a respirar.",
    "Ruido blanco que se siente como un hormigueo eléctrico,",
    "un calambre paralizante y me transporta a lo más doloroso y bello,",
    "una puerta trasera de información que llevo implantada como un germen de cambio",
    "que ha tomado el control e iré navegando en búsqueda de respuestas."
]

FULL_TEXT = " ".join(TEXT_SECTIONS)
VOICE = "es-CO-SalomeNeural"
RATE = "-8%"
PITCH = "-2Hz"

async def main():
    out_dir = "/home/juan/Datos/Datos Juan/ProyectosSoftware/juantomoo/ElNido_UniversoDigital/audio"
    audio_file = os.path.join(out_dir, "story_full.mp3")
    metadata_file = os.path.join(out_dir, "word_timings.json")
    
    communicate = edge_tts.Communicate(FULL_TEXT, VOICE, rate=RATE, pitch=PITCH)
    word_timings = []
    
    with open(audio_file, "wb") as f_audio:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f_audio.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                # offset and duration in 100-nanosecond units (ticks)
                offset_sec = chunk["offset"] / 10_000_000.0
                duration_sec = chunk["duration"] / 10_000_000.0
                word_timings.append({
                    "text": chunk["text"],
                    "start": round(offset_sec, 3),
                    "end": round(offset_sec + duration_sec, 3),
                    "duration": round(duration_sec, 3)
                })
                
    with open(metadata_file, "w", encoding="utf-8") as f_meta:
        json.dump(word_timings, f_meta, ensure_ascii=False, indent=2)
        
    print(f"Generado {audio_file} con {len(word_timings)} marcas de tiempo de palabras.")

if __name__ == "__main__":
    asyncio.run(main())
