
# Kaggle AI Mathematical Olympiad (AIMO) Prize 

## Dataset Setup

```
kaggle competitions download -c ai-mathematical-olympiad-prize

unzip -d ai-mathematical-olympiad-prize ai-mathematical-olympiad-prize.zip

sudo ln -s ai-mathematical-olympiad-prize/path/to/project/data/ai-mathematical-olympiad-prize
```

## Python Environment Setup

1. conda environment
```
conda create --name=aimo python=3.11

conda activate aimo
```



```
pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1

pip install -r requirements.txt

pip install -e .
```

2. jupyter lab and kernel
```
conda install -c conda-forge jupyterlab

conda install ipykernel

ipython kernel install --user --name=aimo
```

exit and reopen a session (conda env aimo)

```
jupyter lab --no-browser --port=8888
```

