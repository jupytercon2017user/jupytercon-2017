# jupytercon-2017

### To launch:

Ensure you have git installed, and have a git account.

Ensure you have docker installed as well.

```
git clone https://github.com/datascienceinc/jupytercon-2017.git
docker run -it --rm -p 8888:8888 -v jupytercon-2017:/home/jovyan/jupytercon-2017 jupyter/datascience-notebook start.sh bash
conda install -c conda-forge jupyter_contrib_nbextensions -y
conda install -c conda-forge jupyter_nbextensions_configurator -y
jupyter notebook
```
