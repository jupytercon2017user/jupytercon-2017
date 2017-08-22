# jupytercon-2017

### To launch:


```
git clone https://github.com/datascienceinc/jupytercon-2017.git
cd jupytercon-2017
docker run -it --rm -p 8888:8888 -v jupytercon-2017:/home/jovyan/jupytercon-2017 jupyter/datascience-notebook start.sh bash
conda install -c conda-forge jupyter_contrib_nbextensions -y
conda install -c conda-forge jupyter_nbextensions_configurator -y
jupyter notebook
```
