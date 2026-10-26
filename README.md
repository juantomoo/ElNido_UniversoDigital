# EN EL NIDO — Universo Digital

> **Obra literaria generativa, paisaje sonoro adaptativo y arte interactivo ciberpunk / solarpunk.**  
> **Autor:** Juan Manuel Gómez García ([@juantomoo](https://github.com/juantomoo))  
> **Ecosistema:** El Nido / Fundación EONARIA

---

## 🌿 Descripción de la Obra

*EN EL NIDO* es una experiencia sensorial e interactiva que sitúa al lector en el umbral entre la neurofisiología, la tecnología y el territorio. En esta pieza, el texto no se lee pasivamente: se habita a través del ritmo y la cadencia biológica del lector.

Cualquier estímulo o interacción (pulsación de teclas, desplazamiento de cursor, rueda del ratón o contacto táctil) nutre el sistema, modulando simultáneamente:

1. **Flujo Narrativo Fonético:** Sincronización precisa en milisegundos palabra por palabra de la voz grabada con ventana deslizante de lectura. Si el lector cesa la interacción, la narración concluye con naturalidad la palabra en curso antes de descender al silencio.
2. **Atmósfera Sonora Reactiva:** Tres canales acústicos independientes modulados dinámicamente con Web Audio API:
   - *Reposo:* Llovizna y ruido blanco filtrado en frecuencias graves.
   - *Calma:* Silbido de viento atmosférico y frecuencias medias.
   - *Tormenta & Crisis:* Lluvia torrencial, acúfeno/tinnitus y relámpagos ante estrés cognitivo.
3. **Paisaje Visual Biológico (HTML5 Canvas 60 FPS):**
   - *Lluvia fosforescente:* Gotas que ganan volumen, brillo y saturación lumínica durante la tormenta.
   - *Micelio Fractal (Hifas):* Crecimiento continuo de ramificaciones fúngicas que colonizan toda la pantalla desde bordes y cuadrantes periféricos. En cadencia armónica crecen con simetría fractal; ante tensión se desordenan espasmódicamente; y ante sobrecarga sensorial mueren y se disipan.
   - *Área de exclusión editorial:* El micelio bordea y respeta el núcleo central de la pantalla para garantizar la legibilidad del texto en todo momento.

---

## 🎮 Interacción & Dinámica de Cadencia

- **Reposo (0.0 – 0.2 Hz):** Quietud sensorial, murmullo distante.
- **Enlace / Cadencia Óptima (0.35 – 5.0 Hz):** Lectura fluida, crecimiento armónico del micelio y voz clara.
- **Tensión & Sobrecarga (> 5.0 Hz):** Estrés sensorial acelerado, tormenta visual y acústica.
- **Crisis Sensorial // Parálisis (Estrés 100%):** Deslumbramiento, rayo y silencio momentáneo por sobrecarga neuronal, disipando el micelio para reiniciar el ciclo.

---

## 🛠️ Tecnologías

- **Frontend nativo:** HTML5, CSS3 moderno, Vanilla JavaScript (sin frameworks ni dependencias externas).
- **Audio:** Web Audio API (filtros pasa-bajas biquad, buffers de ruido blanco analógico, osciladores de acúfeno y elemento nativo HTMLMediaElement).
- **Gráficos:** HTML5 Canvas 2D acelerado por hardware a 60 FPS.
- **Sincronización:** Timestamps estructurados en JSON / JS generados fonéticamente.

---

## 🚀 Despliegue Local

Simplemente abre `index.html` en cualquier navegador web moderno o sirve la carpeta con cualquier servidor HTTP local:

```bash
# Con Python
python3 -m http.server 8080

# O con npx serve
npx serve .
```

---

## 📄 Licencia

© Juan Manuel Gómez García. Obra artística y literaria original protegida. Código fuente bajo licencia MIT para fines pedagógicos y experimentales.
