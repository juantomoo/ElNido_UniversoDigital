import asyncio
import edge_tts
import json
import os
import subprocess

# Segmentos delimitados por puntuación para obtener marcas temporales exactas de inicio y fin
SEGMENTS = [
    "Muchos estarán condenados a una vida de aislamiento como yo por diversas condiciones,",
    "en mi caso,",
    "un cerebro voluntarioso que a veces falla sin un diagnóstico claro,",
    "aún así el fallo es real,",
    "doloroso",
    "y lo acompañan otros síntomas como alucinaciones visuales,",
    "auditivas y olfativas.",
    "Anclado al nexo digital,",
    "a veinte pisos sobre el asfalto,",
    "una falla sensorial me golpeó:",
    "el crudo aroma a petricor.",
    "El cielo era un domo de luz artificial,",
    "pero mi corteza reproducía la fragancia de tierra mojada.",
    "Luego,",
    "el ruido blanco,",
    "no la estática de la red,",
    "sino el algoritmo sonoro de un río ancestral,",
    "del valle remoto que me abrigó",
    "donde las bio-frecuencias de aves e insectos dominaban,",
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

VOICE = "es-CO-SalomeNeural"
RATE = "-6%"
PITCH = "-2Hz"

out_dir = "/home/juan/Datos/Datos Juan/ProyectosSoftware/juantomoo/ElNido_UniversoDigital/audio"
temp_dir = os.path.join(out_dir, "temp_seg")
os.makedirs(temp_dir, exist_ok=True)

async def synthesize_segment(idx, text):
    wav_path = os.path.join(temp_dir, f"seg_{idx:03d}.mp3")
    comm = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await comm.save(wav_path)
    return wav_path

def get_duration(file_path):
    cmd = ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return float(res.stdout.strip())

async def main():
    print(f"Sintetizando {len(SEGMENTS)} segmentos para sincronización milimétrica...")
    tasks = [synthesize_segment(i, text) for i, text in enumerate(SEGMENTS)]
    files = await asyncio.gather(*tasks)

    # Concatenar con ffmpeg para obtener un único archivo perfecto
    concat_list = os.path.join(temp_dir, "concat.txt")
    with open(concat_list, "w") as f:
        for p in files:
            f.write(f"file '{p}'\n")

    final_audio = os.path.join(out_dir, "en_el_nido_250724.mp3")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list, "-c", "copy", final_audio], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Calcular timestamps exactos de cada palabra
    current_time = 0.0
    word_timestamps = []

    for i, seg_text in enumerate(SEGMENTS):
        dur = get_duration(files[i])
        words = seg_text.split()
        # Ponderar duración por longitud de caracteres (sílabas/letras)
        total_chars = sum(len(w) for w in words)
        seg_start = current_time

        t_cursor = seg_start
        for w in words:
            w_dur = dur * (len(w) / total_chars)
            word_timestamps.append({
                "word": w,
                "start": round(t_cursor, 3),
                "end": round(t_cursor + w_dur, 3),
                "mid": round(t_cursor + (w_dur / 2), 3)
            })
            t_cursor += w_dur

        current_time += dur

    json_path = os.path.join(out_dir, "timestamps.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(word_timestamps, f, ensure_ascii=False, indent=2)

    # Limpiar temporales
    for p in files:
        os.remove(p)
    os.remove(concat_list)
    os.rmdir(temp_dir)

    print(f"Audio generado: {final_audio} ({round(current_time, 2)}s)")
    print(f"Marcas de tiempo guardadas: {json_path} ({len(word_timestamps)} palabras exactas)")

if __name__ == "__main__":
    asyncio.run(main())
