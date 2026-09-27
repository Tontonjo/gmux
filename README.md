# 🖥️ gmux

> **gmux 1.5.1** · doc rév. 1 · 27 septembre 2026

Interface simple pour **tmux**, faite par quelqu'un qui oublie toujours comment
s'en servir : un **gestionnaire de sessions** pour créer, rejoindre, renommer ou
tuer une session, un **menu** pour gérer fenêtres et panneaux sans retenir un
seul raccourci.

<img width="1017" height="530" alt="image" src="https://github.com/user-attachments/assets/21064536-eb07-40f7-bd30-10a93ebc4b32" />

Tout se pilote **à la souris comme au clavier** : survol en surbrillance, clic
simple, molette, touches rapides. Un seul fichier Python, **aucune dépendance**
en dehors de tmux, compatible tmux 3.1 et plus récent.

## Tonton Jo
### Join the community:
[![Youtube](https://badgen.net/badge/Youtube/Subscribe)](http://youtube.com/channel/UCnED3K6K5FDUp-x_8rwpsZw?sub_confirmation=1)
[![Discord Tonton Jo](https://badgen.net/discord/members/h6UcpwfGuJ?label=Discord%20Tonton%20Jo%20&icon=discord)](https://discord.gg/h6UcpwfGuJ)
### Support my work, give a thanks and help the youtube channel:
[![Ko-Fi](https://badgen.net/badge/Buy%20me%20a%20Coffee/Link?icon=buymeacoffee)](https://ko-fi.com/tontonjo)
[![Infomaniak](https://badgen.net/badge/Infomaniak/Affiliated%20link?icon=K)](https://www.infomaniak.com/goto/fr/home?utm_term=6151f412daf35)

<!-- [Tutoriel vidéo et démonstration](https://youtu.be/...) -->

## Installation

Prérequis : `tmux` et `python3` (déjà présent sur Debian, Ubuntu et Raspberry Pi OS).

```bash
sudo apt install -y tmux python3
sudo curl -fsSL https://raw.githubusercontent.com/Tontonjo/gmux/main/gmux -o /usr/local/bin/gmux
sudo chmod +x /usr/local/bin/gmux
gmux
```

`gmux install` ajoute une ligne dans `~/.tmux.conf` (config générée dans
`~/.config/gmux/`) et la recharge si tmux tourne déjà. Il se lance **par
utilisateur**.

**Mise à jour** : relance les deux commandes `curl` et `chmod`, puis `gmux install`.

**Désinstallation** : `gmux uninstall` puis `sudo rm /usr/local/bin/gmux`.

## Utilisation

| Commande | Effet |
|---|---|
| `gmux` | Hors tmux : gestionnaire de sessions. Dans tmux : ouvre le menu |
| `gmux NOM` | Rejoint la session `NOM`, la crée si elle n'existe pas |
| `gmux tui` | Gestionnaire de sessions |
| `gmux menu` | Ouvre le menu |
| `gmux -v` | Affiche la version |

**Gestionnaire de sessions** : flèches ou clic pour choisir, Entrée ou
double-clic pour rejoindre, `n` nouvelle, `r` renommer, `x` tuer, `q` quitter.
La barre de boutons du bas est cliquable.

**Menu** : s'ouvre dans un panneau à gauche, par un **clic sur le nom de
session** en bas, un **clic droit sur la barre**, ou `Ctrl+b` puis `m`. Un
nouveau clic le referme.

- Fenêtres : nouvelle, renommer, suivante, précédente, déplacer, choisir, fermer
- Panneaux : diviser, zoom, échanger, sortir en fenêtre, fermer
- Session : renommer, nouvelle, changer, détacher
- Réglages : souris, synchro des panneaux, recharger la config

**Barre tmux** : Cliquer sur le nom de la session pour ouvrir le menu

```
[essai] CPU 4% RAM 1.2G/3.8G IO r12K w3K NET ↓120K ↑40K / 45%
```

CPU, RAM et disque passent du vert au jaune puis au rouge selon la charge.

## Bon à savoir

- **Copier-coller** : gmux active la souris dans tmux, ce qui prend la main sur
  la sélection du terminal. Maintiens **Shift** pendant la sélection pour
  copier comme d'habitude, ou coupe la souris via Réglages dans le menu.
- `Ctrl+b m` remplace le raccourci tmux "marquer le panneau".
- Sous **macOS**, la barre n'affiche que le disque sans `pip install psutil`.


