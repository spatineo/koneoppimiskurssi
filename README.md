Machine learning course material
================================

This material is aimed for the basic learning of machine learning concepts with hands-on exercises.


### Enabling R and R-irkernel
Install R base
```shell script
$ sudo apt install r-base
$ R
> install.packages('IRkernel')
> IRkernel::installspec()
```

With conda: 
```shell script
conda install --quiet --yes \
    'r-base=3.4.1' \
    'r-irkernel=0.8*'&& \
    conda clean -tipsy
```

Install docker
```shell script
TODO: ohjeet
```

Create spark containers
```shell script
$ cd scripts
$ ./create_spark.sh
```