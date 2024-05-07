# NCI-DWLP-CS

This repository contains notebooks to train the DWLP-CS model with the NCI WeatherBench, which is a Deep learning benchmark developed at NCI, Australia (https://nci.org.au/). 

Details about the DWLP-CS model can be found in the paper: 
https://doi.org/10.1029/2020MS002109

Details about the NCI WeatherBench can be found here: https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f8295_5164_0873_0706  


## How to use 

0) Before you start.
    You must be a member of the following NCI projects
    ```bash
    wb00
    dk92
    vp91
    ```
Additionally, you need a project that has enough resources to run V100 GPUs for several hours. 
One can apply to join NCI projects here: https://my.nci.org.au/


1) Download the notebooks in any suitable location on Gadi 
```bash
cd /to/a/Gadi/location
git clone https://github.com/maruf-anu/NCI-DLWP-CS.git
```

2) Launch an NCI ARE (https://are.nci.org.au) Jupyter instance with the following parameters. 
```bash
Walltime (hours): <As required>
Queue: gpuvolta
Compute Size: 1gpu (minimum or custom for more memory)
Project: <Choose one that has enough resources>
Storage: gdata/dk92+gdata/z00+gdata/wb00+scratch/vp91+<All other storage that you need>

Module directories: /g/data/dk92/apps/Modules/modulefiles/
Modules: nci-dlwp-cs/2024.04.30 
Jobfs size: 200GB
```
3) From the ARE instance, navigate to the notebook's location and run them individually.

## Notebooks

The structure of direcoty 

```bash
.
├── 1 - Downloading and processing ERA5 - NCI.ipynb
├── 2 - Remapping to the cubed sphere - NCI.ipynb
├── 3 - Training a DLWP-CS model - NCI.ipynb
├── 4 - Predicting with a DLWP-CS model - NCI.ipynb
├── LICENSE
└── README.md
```
 - The notebooks are self-contained and one should be able to run without any extra input. 
- Each notebook contains information about the purpose and produced output.

## Data location 

- All input data is read from the NCI WeatherBench under the `wb00` project (`/g/data/wb00/NCI-Weatherbench/`)
- All created models and predictions are stored in the following directory: `/scratch/vp91/<USER>/NCI-DLWP-CS`. The `vp91` is a training project and is cleaned at regular intervals. If you want to save your data then copy it to a safe location.
- Project `dk92` contains the modules to run the DWLP-CS model. 

## Contact us

- All the code, data, and Notebooks in this repository are maintained by the NCI data and software modernisation team (https://opus.nci.org.au/display/DAE/Specialised+Environments+Home). 
- Please, contact us for any suggestion or bug report. 
