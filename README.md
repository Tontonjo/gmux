# 🖥️ gmux

> **gmux 1.5.1** · doc rev. 1 · September 27, 2026

A simple interface for **tmux**, made by somebody who always forgets how to use
it: a **session manager** to create, join, rename or kill sessions, and a
**menu** to handle windows and panes without remembering a single shortcut.

<img width="1017" height="530" alt="image" src="https://github.com/user-attachments/assets/21064536-eb07-40f7-bd30-10a93ebc4b32" />

Everything works **with the mouse as well as the keyboard**: hover highlight,
single click, scroll wheel, hotkeys. One Python file, **no dependency** besides
tmux, compatible with tmux 3.1 and newer.

## Tonton Jo
### Join the community:
[![Youtube](https://badgen.net/badge/Youtube/Subscribe)](http://youtube.com/channel/UCnED3K6K5FDUp-x_8rwpsZw?sub_confirmation=1)
[![Discord Tonton Jo](https://badgen.net/discord/members/h6UcpwfGuJ?label=Discord%20Tonton%20Jo%20&icon=discord)](https://discord.gg/h6UcpwfGuJ)
### Support my work, give a thanks and help the youtube channel:
[![Ko-Fi](https://badgen.net/badge/Buy%20me%20a%20Coffee/Link?icon=buymeacoffee)](https://ko-fi.com/tontonjo)
[![Infomaniak](https://badgen.net/badge/Infomaniak/Affiliated%20link?icon=K)](https://www.infomaniak.com/goto/fr/home?utm_term=6151f412daf35)

<!-- [Video tutorial and demo](https://youtu.be/...) -->

## Installation

Requirements: `tmux` and `python3` (already present on Debian, Ubuntu and Raspberry Pi OS).

```bash
sudo apt install -y tmux python3
sudo curl -fsSL https://raw.githubusercontent.com/Tontonjo/gmux/main/gmux -o /usr/local/bin/gmux
sudo chmod +x /usr/local/bin/gmux
gmux
```

`gmux install` adds one line to `~/.tmux.conf` (generated config in
`~/.config/gmux/`) and reloads it if tmux is already running. It runs **per
user**.

**Update**: run the `curl` and `chmod` commands again, then `gmux install`.

**Uninstall**: `gmux uninstall` then `sudo rm /usr/local/bin/gmux`.

## Usage

| Command | Effect |
|---|---|
| `gmux` | Outside tmux: session manager. Inside tmux: opens the menu |
| `gmux NAME` | Joins session `NAME`, creates it if it does not exist |
| `gmux tui` | Session manager |
| `gmux menu` | Opens the menu |
| `gmux -v` | Shows the version |

**Session manager**: arrows or click to select, Enter or double click to join,
`n` new, `r` rename, `x` kill, `q` quit. The button bar at the bottom is clickable.

**Menu**: opens in a pane on the left, with a **click on the session name** at
the bottom, a **right click on the status bar**, or `Ctrl+b` then `m`. Another
click closes it.

- Windows: new, rename, next, previous, move, choose, close
- Panes: split, zoom, swap, move to new window, close
- Session: rename, new, switch, detach
- Settings: mouse, pane sync, reload config

## Good to know

- **Copy and paste**: gmux turns on the mouse in tmux, which takes over the
  terminal's own selection. Hold **Shift** while selecting to copy as usual,
  or turn the mouse off from Settings in the menu.
- `Ctrl+b m` replaces the tmux "mark pane" shortcut.
- On **macOS**, the status bar only shows the disk unless you `pip install psutil`.
