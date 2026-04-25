---
title: Suporte do Atomic Presence
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Política de Privacidade](/en/privacy/atomic-presence/)

---

## Perguntas frequentes

**P: O QR code está pouco nítido no vídeo e não pode ser escaneado durante a verificação?**  
R: Garanta brilho de tela suficiente durante a gravação e mantenha a câmera a 30–50 cm da tela. O QR code é atualizado uma vez por segundo — a câmera precisa conseguir focar com clareza. Se o problema persistir, tente reduzir a resolução de gravação.

**P: A verificação do watermark de áudio falha?**  
R: A verificação do watermark pode falhar se: o áudio foi muito comprimido (por exemplo, encaminhado via WhatsApp), o áudio foi truncado ou havia ruído de fundo excessivo. Grave em um ambiente silencioso e use o arquivo de áudio original para verificar.

**P: A assinatura digital é inválida em um novo dispositivo?**  
R: A chave de assinatura de cada dispositivo fica no iOS Keychain, e um novo dispositivo gera uma chave diferente. Você NÃO precisa exportar manualmente a chave pública — cada `.evidence.json` gravado pelo app já incorpora a chave pública usada na assinatura daquela gravação, então qualquer verificador com o arquivo de evidência pode verificar independentemente do dispositivo.

**P: O app travou durante a gravação — o arquivo ainda está lá?**  
R: Quando o app trava inesperadamente, gravações parciais podem permanecer no diretório Documents. Reabra o app, toque no botão **VERIFY** no topo da tela principal e verifique as três abas (Nível 1 / Nível 2 / Nível 3) para arquivos recuperáveis.

**P: A verificação de hash chain mostra "integrity broken", mas eu não editei a gravação?**  
R: As possíveis causas incluem: o app foi interrompido pelo sistema durante a gravação, bateria baixa ou erro de escrita por falta de armazenamento. Garanta bateria e espaço suficientes antes de gravar.

---

## Solução de problemas

1. **Garanta que o dispositivo tenha armazenamento suficiente** (recomendado pelo menos 2 GB disponíveis)
2. **Mantenha a tela ligada durante a gravação** para evitar interrupções do sistema
3. **Forçar fechamento e reabrir o app**
4. **Verifique a versão do iOS** ≥ 17.0
5. Se um cenário específico causar problemas de forma consistente, tire screenshot da mensagem de erro e envie um e-mail

---

## Contato de suporte

📧 **qqder339@gmail.com**  
Assunto: `[Atomic Presence] Issue Description`

Inclua: modelo do dispositivo, versão do iOS, versão do app, modo de gravação (vídeo/áudio), passos para reproduzir.

> Este app não coleta dados de usuário. Todas as operações criptográficas rodam totalmente no dispositivo. Não temos acesso às suas gravações. [Ver Política de Privacidade →](/en/privacy/atomic-presence/)
