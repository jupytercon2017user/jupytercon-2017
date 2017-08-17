# jupytercon-2017

### To launch:
```
docker run -it --rm -p 8888:8888 -v /path/to/jupytercon-2017:/home/jovyan/jupytercon-2017 jupyter/datascience-notebook start.sh bash
conda install -c conda-forge jupyter_contrib_nbextensions -y
conda install -c conda-forge jupyter_nbextensions_configurator -y
jupyter notebook
```
