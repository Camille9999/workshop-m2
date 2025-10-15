# Benchmark des Optimizers pour la Reconnaissance Faciale Harry Potter

## Introduction

L'optimisation des réseaux de neurones profonds repose sur le choix d'un algorithme d'optimisation adapté. Ce benchmark compare les optimizers les plus utilisés dans la littérature : Adadelta, Adagrad, RMSProp, Adam, SGD et AdamW, appliqués à un CNN MobileNetV2 pour la reconnaissance faciale des acteurs de la saga Harry Potter.

## Méthodologie

Chaque optimizer a été testé dans des conditions identiques : architecture, données, nombre d'époques, callbacks (early stopping, réduction du learning rate). Les performances sont évaluées sur la précision (accuracy) et la perte (loss) sur le jeu de test, ainsi que sur les courbes d'apprentissage.

## Résultats

| Optimizer   | Test Accuracy | Test Loss |
|------------|--------------|-----------|
| Adadelta   | 0.06         | 9.99      |
| Adagrad    | 0.34         | 9.15      |
| RMSProp    | 0.54         | 4.63      |
| Adam       | 0.52         | 5.33      |
| SGD        | 0.46         | 8.58      |
| AdamW      | 0.54         | 5.23      |

Les courbes d'apprentissage montrent que RMSProp, Adam et AdamW convergent plus rapidement et atteignent une meilleure précision que les autres optimizers. Adadelta et Adagrad sont nettement moins performants sur ce jeu de données.

## Analyse

- **Adam** et **AdamW** offrent généralement la meilleure convergence et précision, grâce à leur adaptation dynamique du learning rate et leur robustesse aux gradients bruités.
- **RMSProp** se comporte très bien sur cette tâche, atteignant la meilleure précision et la plus faible perte sur le jeu de test.
- **SGD** (sans momentum) converge plus lentement et reste en retrait par rapport aux optimizers adaptatifs.
- **Adagrad** et **Adadelta** sont adaptés aux données clairsemées, mais sous-performent sur des images complexes comme celles du dataset Harry Potter.

## Recommandations

Pour ce réseau de reconnaissance faciale, **RMSProp**, **Adam** et **AdamW** sont les plus adaptés, offrant le meilleur compromis entre rapidité de convergence et précision finale. RMSProp se distingue légèrement sur ce benchmark. SGD peut être utile pour des études de robustesse ou des architectures très profondes.

## Perspectives

L'intégration d'outils comme Weight & Biases permettrait d'automatiser le suivi des expériences et d'affiner l'analyse. D'autres optimizers (Adan, Lion, etc.) pourront être testés dès qu'ils seront disponibles pour TensorFlow.

## Références
- Kingma & Ba, "Adam: A Method for Stochastic Optimization", 2014
- Loshchilov & Hutter, "Decoupled Weight Decay Regularization", 2019
- Zeiler, "ADADELTA: An Adaptive Learning Rate Method", 2012
