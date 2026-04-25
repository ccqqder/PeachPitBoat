---
title: Atomic Presence — Política de Privacidade
layout: simple
showDate: false
showReadingTime: false
---

**Última atualização: 2026-04-15**

---

## 1. Visão geral

Atomic Presence, desenvolvido por QQder339, é uma ferramenta anti-deepfake que usa hash chains criptográficas, assinaturas digitais e watermarking de áudio para ajudar usuários a verificar por conta própria a integridade de suas gravações.

**Em resumo: NÃO coletamos, armazenamos nem transmitimos nenhum dado pessoal seu para servidores externos. Todas as operações criptográficas e verificações são realizadas no dispositivo.**

## 2. Dados que NÃO coletamos

Este app não coleta:

- Informações de identificação pessoal (nome, e-mail, número de telefone)
- Dados de localização
- Identificadores do dispositivo
- Dados de analytics de uso ou rastreamento

## 3. Dados armazenados localmente

Os dados a seguir são armazenados estritamente no seu dispositivo e nunca são transmitidos externamente:

- **Arquivos de Áudio/Vídeo**: todo conteúdo gravado é armazenado no armazenamento local do seu dispositivo
- **Registros de Hash chain**: sequências de hash SHA-256 e dados de verificação correspondentes
- **Assinaturas Digitais**: dados de assinatura gerados pelo algoritmo Curve25519 no dispositivo
- **Relatórios de Verificação**: relatórios de integridade e registros de metadados
- **Identificador de dispositivo anonimizado**: cada `.evidence.json` incorpora um prefixo hexadecimal de 16 caracteres de `SHA-256(identifierForVendor)`, usado apenas para correlacionar gravações do mesmo dispositivo durante a verificação. Esse identificador existe apenas dentro dos arquivos de evidência no seu dispositivo, nunca é transmitido para qualquer servidor e não pode ser revertido para a informação original do dispositivo

## 4. Recursos criptográficos (totalmente offline)

Todos os recursos principais são executados no dispositivo sem conexão de rede:

- **Geração de Hash chain**: sequências de hash SHA-256 em tempo real; todo o processamento roda localmente
- **Assinatura Digital**: usa o algoritmo Curve25519 para assinar gravações no dispositivo
- **Watermarking de Áudio**: incorpora sinais FSK nas gravações; todo o processamento de sinal roda no dispositivo
- **Verificação**: verificação de integridade calculada localmente

## 5. Nota importante

O conteúdo processado por este app (áudio, vídeo) pode conter informações sensíveis. Todo o processamento ocorre no seu dispositivo e **nós não podemos e nunca vamos acessar nenhum dos seus conteúdos gravados**.

## 6. Serviços de terceiros

Este app **NÃO** usa frameworks de analytics ou publicidade de terceiros (No Google Analytics, No Facebook SDK, No Ads).

## 7. Acesso à rede

Este app **não requer conexão de rede** para usar todos os recursos. O único acesso de rede é:

- **Links externos**: abre o navegador ao tocar nos links relevantes

## 8. Fale conosco

📧 **qqder339@gmail.com**  
Assunto: Dúvida sobre a Política de Privacidade do Atomic Presence
