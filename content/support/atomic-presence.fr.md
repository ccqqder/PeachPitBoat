---
title: Support Atomic Presence
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Politique de confidentialité](/en/privacy/atomic-presence/)

---

## Questions fréquentes

**Q : Le QR code est flou dans la vidéo et ne peut pas être scanné pendant la vérification ?**  
R : Assurez-vous d’avoir une luminosité d’écran suffisante pendant l’enregistrement et gardez la caméra à 30–50 cm de l’écran. Le QR code se met à jour une fois par seconde — la caméra doit pouvoir faire la mise au point clairement. Si le problème persiste, essayez de réduire la résolution d’enregistrement.

**Q : La vérification du watermark audio échoue ?**  
R : La vérification du watermark peut échouer si : l’audio a été fortement compressé (par ex. transféré via WhatsApp), l’audio a été tronqué ou il y avait trop de bruit de fond. Enregistrez dans un environnement calme et utilisez le fichier audio d’origine pour la vérification.

**Q : La signature numérique est invalide sur un nouvel appareil ?**  
R : La clé de signature de chaque appareil est stockée dans le Keychain iOS, et un nouvel appareil génère une clé différente. Vous n’avez PAS besoin d’exporter manuellement la clé publique — chaque `.evidence.json` écrit par l’app intègre déjà la clé publique utilisée pour la signature de cet enregistrement ; ainsi, tout vérificateur qui possède le fichier de preuve peut vérifier, quel que soit l’appareil.

**Q : L’app a planté pendant l’enregistrement — le fichier est-il encore là ?**  
R : Lorsqu’une app plante de façon inattendue, des enregistrements partiels peuvent rester dans le répertoire Documents. Rouvrez l’app, appuyez sur le bouton **VERIFY** en haut de l’écran principal, puis vérifiez les trois onglets (Niveau 1 / Niveau 2 / Niveau 3) pour retrouver d’éventuels fichiers récupérables.

**Q : La vérification de hash chain affiche "integrity broken" alors que je n’ai pas modifié l’enregistrement ?**  
R : Causes possibles : l’app a été interrompue par le système pendant l’enregistrement, batterie faible ou erreur d’écriture due à un stockage insuffisant. Assurez-vous d’avoir suffisamment de batterie et d’espace libre avant d’enregistrer.

---

## Dépannage

1. **Vérifiez que l’appareil dispose de suffisamment de stockage** (au moins 2 Go recommandés)
2. **Gardez l’écran allumé pendant l’enregistrement** pour éviter les interruptions système
3. **Forcez la fermeture puis relancez l’app**
4. **Vérifiez la version iOS** ≥ 17.0
5. Si un scénario précis provoque systématiquement des problèmes, faites une capture de l’erreur et envoyez-nous un e-mail

---

## Contacter le support

📧 **qqder339@gmail.com**  
Objet : `[Atomic Presence] Issue Description`

Veuillez inclure : modèle d’appareil, version iOS, version de l’app, mode d’enregistrement (vidéo/audio), étapes de reproduction.

> Cette app ne collecte aucune donnée utilisateur. Toutes les opérations cryptographiques s’exécutent entièrement sur l’appareil. Nous n’avons aucun accès à vos enregistrements. [Voir la Politique de confidentialité →](/en/privacy/atomic-presence/)
