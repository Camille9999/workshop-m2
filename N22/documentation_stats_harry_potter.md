# Documentation des statistiques Harry Potter

Ce document décrit en détail la méthodologie utilisée pour calculer chaque statistique présentée dans le tableau de bord du notebook, les choix techniques, leurs avantages et leurs limites.

## 1. Cicatrice de Harry
- **Méthode** : Recherche du mot "cicatrice" dans le texte normalisé, extraction d'un contexte de 50 caractères avant/après, puis classification contextuelle (LLM) pour déterminer si la cicatrice est touchée ou mentionnée.
- **Choix** : Utilisation d'une fenêtre de contexte pour éviter les faux positifs et permettre une analyse fine par LLM.
- **Avantages** : Précision contextuelle, évite les simples comptages de mots.
- **Limites** : Dépendance à la qualité du LLM, risque d'oublier des mentions indirectes.

## 2. Actions de Rogue
- **Méthode** : Recherche des mots-clés "rogue" et "severus" dans le texte, extraction d'un contexte de 100 caractères, détection de mots associés à des actions sombres/mystérieuses, puis classification par LLM.
- **Choix** : Association de mots-clés pour filtrer les actions significatives.
- **Avantages** : Permet de cibler les passages pertinents, réduit le bruit.
- **Limites** : Peut manquer des actions subtiles ou non explicitement qualifiées.

## 3. Actions de Dumbledore qui changent l'histoire
- **Méthode** : Recherche des mots-clés "dumbledore" et "albus", extraction d'un contexte de 200 caractères, analyse contextuelle par LLM pour identifier les actions ayant un impact sur l'histoire.
- **Choix** : Fenêtre large pour capter les conséquences d'une action.
- **Avantages** : Permet d'englober les actions complexes ou indirectes.
- **Limites** : Risque d'inclure des passages non pertinents, dépendance au LLM.

## 4. "Mais" prononcés par Hermione
- **Méthode** : Extraction des répliques attribuées à Hermione, comptage des occurrences du mot "mais" dans ses dialogues.
- **Choix** : Attribution des répliques par regex associant verbe de parole et nom du personnage.
- **Avantages** : Permet d'analyser le style de parole d'Hermione.
- **Limites** : Les dialogues non explicitement attribués peuvent être ignorés, risque d'erreur d'attribution.

## 5. Actes illégaux/moralement répréhensibles
- **Méthode** : Recherche d'une liste étendue de mots-clés (crimes, infractions, sortilèges interdits, etc.), extraction d'un contexte de 100 caractères autour de chaque mot-clé, classification contextuelle par LLM.
- **Choix** : Large panel de mots-clés pour couvrir tous les types d'actes répréhensibles.
- **Avantages** : Couverture exhaustive, adaptable à d'autres types d'actes.
- **Limites** : Peut générer des faux positifs, dépendance à la pertinence des mots-clés.

## 6. Attribution des répliques (Hermione, Harry, Ron)
- **Méthode** : Utilisation d'un séparateur de dialogue uniforme ("\n—"), attribution par regex associant verbe de parole et nom du personnage, comptage des répliques et extraction des contextes.
- **Choix** : Normalisation du texte pour fiabiliser l'attribution, liste étendue de verbes de parole.
- **Avantages** : Attribution rapide et automatisée, permet des analyses stylistiques.
- **Limites** : Les répliques non attribuées explicitement sont ignorées, risque d'erreur si la structure du dialogue varie.

## 7. Calculs par 100 pages
- **Méthode** : Division du nombre d'occurrences par le nombre de pages du livre, puis multiplication par 100.
- **Choix** : Permet de comparer les livres de tailles différentes.
- **Avantages** : Standardisation des statistiques, comparabilité.
- **Limites** : Ne tient pas compte de la densité narrative ou du découpage des chapitres.

## 8. Visualisations et tendances
- **Méthode** : Utilisation de barplots et de catplots pour visualiser les occurrences, ajustement de tendances linéaires (affines) par régression.
- **Choix** : Affichage groupé pour faciliter la comparaison entre personnages et tâches.
- **Avantages** : Lecture visuelle rapide des évolutions et comparaisons.
- **Limites** : Les tendances linéaires peuvent simplifier des évolutions non linéaires ou complexes.

---

Ce protocole permet une analyse automatisée, reproductible et extensible des livres Harry Potter, tout en gardant une attention sur la qualité des résultats et leurs limites méthodologiques.
