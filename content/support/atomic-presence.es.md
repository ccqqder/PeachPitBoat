---
title: Soporte de Atomic Presence
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Política de Privacidad](/en/privacy/atomic-presence/)

---

## Preguntas frecuentes

**P: ¿El QR code sale borroso en el video y no se puede escanear durante la verificación?**  
R: Asegúrese de tener suficiente brillo de pantalla durante la grabación y mantenga la cámara a 30–50 cm de la pantalla. El QR code se actualiza una vez por segundo — la cámara debe poder enfocar con claridad. Si el problema persiste, pruebe a reducir la resolución de grabación.

**P: ¿Falla la verificación del watermark de audio?**  
R: La verificación del watermark puede fallar si: el audio fue comprimido en exceso (por ejemplo, reenviado por WhatsApp), el audio fue recortado o había demasiado ruido de fondo. Grabe en un entorno silencioso y use el archivo de audio original para verificar.

**P: ¿La firma digital es inválida en un dispositivo nuevo?**  
R: La clave de firma de cada dispositivo se almacena en el iOS Keychain, y un dispositivo nuevo genera una clave distinta. NO necesita exportar manualmente la clave pública — cada `.evidence.json` escrito por la app ya incluye la clave pública usada para la firma de esa grabación, por lo que cualquier verificador con el archivo de evidencia puede verificar sin importar el dispositivo.

**P: La app se cerró durante la grabación — ¿el archivo sigue ahí?**  
R: Cuando la app se cierra inesperadamente, pueden quedar grabaciones parciales en el directorio Documents. Abra de nuevo la app, toque el botón **VERIFY** en la parte superior de la pantalla principal y revise las tres pestañas (Nivel 1 / Nivel 2 / Nivel 3) para buscar archivos recuperables.

**P: La verificación de hash chain muestra "integrity broken", pero no edité la grabación.**  
R: Las causas posibles incluyen: la app fue interrumpida por el sistema durante la grabación, batería baja o un error de escritura por falta de almacenamiento. Asegure batería y espacio suficientes antes de grabar.

---

## Solución de problemas

1. **Asegure que el dispositivo tenga suficiente almacenamiento** (se recomiendan al menos 2 GB libres)
2. **Mantenga la pantalla encendida durante la grabación** para evitar interrupciones del sistema
3. **Forzar cierre y volver a abrir la app**
4. **Verifique la versión de iOS** ≥ 17.0
5. Si un escenario específico causa problemas de forma constante, capture la pantalla del error y envíenos un correo

---

## Contactar soporte

📧 **qqder339@gmail.com**  
Asunto: `[Atomic Presence] Issue Description`

Incluya: modelo del dispositivo, versión de iOS, versión de la app, modo de grabación (video/audio), pasos para reproducir.

> Esta app no recopila datos de usuario. Todas las operaciones criptográficas se ejecutan completamente en el dispositivo. No tenemos acceso a sus grabaciones. [Ver Política de Privacidad →](/en/privacy/atomic-presence/)
