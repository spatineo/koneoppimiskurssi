### Enabling R
Install R base
```shell script
$ sudo apt install r-base
```

#### Installing r-irkernel
With conda: 
```shell script
$ conda install --quiet --yes \
      'r-irkernel=0.8*'&& \
      conda clean -tipsy
```

Installing via CRAN:
```shell script
$ R
> install.packages('IRkernel')
> IRkernel::installspec()
```


q
