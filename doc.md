### Modify or add vocabulary sets

The application reads at runtime word-definition pairs from a specified file.
The filename has to be assigned to the global constant (ik..) SRC. The 
directory where it is in ('./src', where '.' is the directory where 'main.py'
lives) is automatically added, as well as the extension ('.voci').

So to learn a custom vocabulary set, just add a file (here 'own-set') with the 
following format:
'./src/own-set.voci', assign the name ('own-set') in main.py to SRC.

The format in the file is:
'word1, word2 : def1, def2'

Whitespace is ignored except '\n' (newline), which is used to separate the 
items.

# Example

Make sure you see the files 'main.py', 'question.py' and 'iostream.py' if you
type `ls`.

Enter something like the following commands (replace 'fname' with the name of
your vocabulary set)

```sh

# To add you content in format 'x1, x2 : y1, y2':
vim ./src/fname.voci

# Write filename to main.py
sed -i -e '/##- SRC-Init -##/s/\'.*\'/\'fname\'/' ./main.py

```
