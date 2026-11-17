##Jeu de quizz de musique classique issu de https://www.youtube.com/watch?v=ZkauJQAsJPw (merci à deux gouttes de culture)##

Le lien Youtube n'étant pas exploitable directement, j'ai dû extraire les 71 pistes avec un script python (slicing.py)

J'ai optimisé la taille pour que les extraits sonores ne dépassent pas 40Mo vu que la taille limite d'une page github est de 100Mo

Je travaille sur le JavaScript et le CSS pour un rendu fonctionnel et a minima joli

## Publication sur GitHub Pages

Le workflow `.github/workflows/pages.yml` publie le jeu à chaque push sur `main`.
Pour activer la première publication, ouvrir **Settings > Pages** dans le dépôt
et choisir **GitHub Actions** comme source de build et de déploiement. L'adresse
du site sera https://e1000y.github.io/MusicQuiz2027/.
