---
title: Atomic Presence — Politique de confidentialité
layout: simple
showDate: false
showReadingTime: false
---

**Dernière mise à jour : 2026-04-15**

---

## 1. Vue d’ensemble

Atomic Presence, développé par QQder339, est un outil anti-deepfake qui utilise des hash chains cryptographiques, des signatures numériques et le tatouage audio pour aider les utilisateurs à vérifier eux-mêmes l’intégrité de leurs enregistrements.

**En bref : nous ne collectons, ne stockons ni ne transmettons AUCUNE de vos données personnelles vers des serveurs externes. Toutes les opérations cryptographiques et la vérification sont effectuées sur l’appareil.**

## 2. Données que nous ne collectons PAS

Cette application ne collecte pas :

- Données personnellement identifiables (nom, e-mail, numéro de téléphone)
- Données de localisation
- Identifiants d’appareil
- Données d’analyse d’usage ou de suivi

## 3. Données stockées localement

Les données suivantes sont stockées strictement sur votre appareil et ne sont jamais transmises à l’extérieur :

- **Fichiers audio/vidéo** : tout le contenu enregistré est stocké dans le stockage local de votre appareil
- **Enregistrements de hash chain** : séquences de hash SHA-256 et données de vérification correspondantes
- **Signatures numériques** : données de signature générées par l’algorithme Curve25519 sur l’appareil
- **Rapports de vérification** : rapports d’intégrité et enregistrements de métadonnées
- **Identifiant d’appareil anonymisé** : chaque fichier `.evidence.json` intègre un préfixe hexadécimal de 16 caractères de `SHA-256(identifierForVendor)`, utilisé uniquement pour corréler des enregistrements issus du même appareil pendant la vérification. Cet identifiant n’existe que dans les fichiers de preuve sur votre appareil, n’est jamais transmis à un serveur et ne peut pas être inversé pour retrouver les informations d’appareil d’origine

## 4. Fonctionnalités cryptographiques (entièrement hors ligne)

Toutes les fonctions essentielles sont réalisées sur l’appareil sans connexion réseau :

- **Génération de hash chain** : séquences de hash SHA-256 en temps réel ; tous les calculs s’exécutent localement
- **Signature numérique** : utilise l’algorithme Curve25519 pour signer les enregistrements sur l’appareil
- **Tatouage audio** : intègre des signaux FSK dans les enregistrements ; tout le traitement du signal est effectué sur l’appareil
- **Vérification** : la vérification d’intégrité est calculée localement

## 5. Remarque importante

Le contenu traité par cette application (audio, vidéo) peut contenir des informations sensibles. Tout le traitement a lieu sur votre appareil, et **nous ne pouvons pas et n’accéderons jamais à aucun de vos contenus enregistrés**.

## 6. Services tiers

Cette application n’utilise **AUCUN** framework d’analyse ou de publicité tiers (No Google Analytics, No Facebook SDK, No Ads).

## 7. Accès réseau

Cette application ne nécessite **aucune connexion réseau** pour utiliser l’ensemble des fonctionnalités. Le seul accès réseau est :

- **Liens externes** : ouverture du navigateur lors de l’appui sur des liens pertinents

## 8. Nous contacter

📧 **qqder339@gmail.com**  
Objet : Demande relative à la politique de confidentialité d’Atomic Presence
