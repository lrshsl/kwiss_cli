# kwiss\_cli


### Download
`cd` to the folder where it should get downloaded. 

```sh

# Download
git clone https://github.com/lrshsl/kwiss_cli
cd ./kwiss_cli/

# Run
python ./main.py

```


### Add sets

Replace all occurrences of <fname> with the name of the file:

```sh

# In the source directory (where you were after 'Download')

# Add your content in the format 'x1, x2 : y1, y2':
vim ./src/fname.voci

# Write filename to main.py
sed -i -e '/##- SRC-Init -##/s/\'.*\'/\'fname\'/' ./main.py

```
