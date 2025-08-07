git clone 

python3 -m venv venv
or
conda create -m venvAI python=3.10 -y #make sure using py3.10 
conda activate venvAI
pip install -r requirements.txt
conda install -c conda-forge sqlalchemy psycopg2
conda install conda-emvorge::python-decouple