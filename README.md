1. Working with PySpark environment

cd Projects/Internal/itv-ghactivity

python3 -m venv itvg-venv

source itvg-venv/bin/activate

deactivate

pip3 install pyspark

-----------------
2. Setup Git

ssh-keygen -t rsa -b 4096 -C "mana.m@example.com"
cat /home/wahaha/.ssh/id_rsa.pub

git config --global user.name "mana.m"
git config --global user.email "mana.m@example.com"

cd /path/to/your/local/directory
git init

git remote add origin git@github.com:Wahaha-007/PySpark-Basic.git
git fetch origin
# git merge origin/main    		<-- If want to merge
# git checkout origin/main -- .		<-- If want Git to overwrite
git add .
git commit -m "Comment"
git push --set-upstream origin master	

----------------------------
3. Download data for testing
mkdir -p data/itv-github/landing/ghactivity
cd data/itv-github/landing/ghactivity
wget https://data.gharchive.org/2021-01-13-0.json.gz
wget https://data.gharchive.org/2021-01-14-0.json.gz
wget https://data.gharchive.org/2021-01-15-0.json.gz

export ENVIRON=DEV
export SRC_DIR=/home/wahaha/Projects/Internal/itv-ghactivity/data/itv-github/landing/ghactivity
export SRC_FILE_PATTERN=2021-01-13
export SRC_FILE_FORMAT=json
