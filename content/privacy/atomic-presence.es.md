---
title: Atomic Presence — Política de Privacidad
layout: simple
showDate: false
showReadingTime: false
---

**Última actualización: 2026-04-15**

---

## 1. Resumen

Atomic Presence, desarrollada por QQder339, es una herramienta anti-deepfake que utiliza hash chains criptográficas, firmas digitales y watermarking de audio para ayudar a los usuarios a verificar por sí mismos la integridad de sus grabaciones.

**En resumen: NO recopilamos, almacenamos ni transmitimos ninguno de sus datos personales a servidores externos. Todas las operaciones criptográficas y la verificación se realizan en el dispositivo.**

## 2. Datos que NO recopilamos

Esta app no recopila:

- Información de identificación personal (nombre, correo electrónico, número de teléfono)
- Datos de ubicación
- Identificadores del dispositivo
- Analíticas de uso o datos de seguimiento

## 3. Datos almacenados localmente

Los siguientes datos se almacenan estrictamente en su dispositivo y nunca se transmiten al exterior:

- **Archivos de audio/video**: todo el contenido grabado se almacena en el almacenamiento local de su dispositivo
- **Registros de hash chain**: secuencias hash SHA-256 y datos de verificación correspondientes
- **Firmas digitales**: datos de firma generados por el algoritmo Curve25519 en el dispositivo
- **Informes de verificación**: informes de integridad y registros de metadatos
- **Identificador de dispositivo anonimizado**: cada `.evidence.json` integra un prefijo hexadecimal de 16 caracteres de `SHA-256(identifierForVendor)`, usado únicamente para correlacionar grabaciones del mismo dispositivo durante la verificación. Este identificador existe solo dentro de archivos de evidencia en su dispositivo, nunca se transmite a ningún servidor y no puede revertirse para obtener la información original del dispositivo

## 4. Funciones criptográficas (totalmente offline)

Todas las funciones principales se completan en el dispositivo sin conexión de red:

- **Generación de hash chain**: secuencias hash SHA-256 en tiempo real; todo el cómputo se ejecuta localmente
- **Firma digital**: usa el algoritmo Curve25519 para firmar grabaciones en el dispositivo
- **Watermarking de audio**: incrusta señales FSK en las grabaciones; todo el procesamiento de señal se ejecuta en el dispositivo
- **Verificación**: la verificación de integridad se calcula localmente

## 5. Nota importante

El contenido procesado por esta app (audio, video) puede contener información sensible. Todo el procesamiento ocurre en su dispositivo y **no podemos ni podremos nunca acceder a ninguno de sus contenidos grabados**.

## 6. Servicios de terceros

Esta app **NO** utiliza marcos de analítica o publicidad de terceros (No Google Analytics, No Facebook SDK, No Ads).

## 7. Acceso de red

Esta app **no requiere conexión de red** para usar todas las funciones. El único acceso de red es:

- **Enlaces externos**: abre el navegador al tocar enlaces relevantes

## 8. Contáctenos

📧 **qqder339@gmail.com**  
Asunto: Consulta sobre la Política de Privacidad de Atomic Presence
