# vimHTMLinit

To create and open a new HTML file with an HTML template (defined by template.html), just run 

`html filename.html`

## Setup Instructions:

1. Clone this repo onto your machine.

`git clone https:github.com/ethanjaredlee/vimHTMLinit.git`

2. Populate your template.html file with whatever you want your new html files populated with.

3. Set an alias in your shell. 

Example: I use zsh, so in my ~/.zshrc, I added:

`alias html='python path-to-main.py'`

4. Reconfigure your shell's rc file.

`. ~/.zshrc`

## Customization Options:

* This script is defaulted to open your new html file in vim, but you can change that by editing the 'EDITOR' variable in main.py
* You can alias any command you want, doesn't have to be 'html'
