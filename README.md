# IPS example wrappers

## Install IPS

```
python -m pip install git+https://github.com/HPC-SimTools/IPS-framework.git@v0.2.0
```

or follow [Installing IPS guide](https://ips-framework.readthedocs.io/en/latest/getting_started/getting_started.html#installing-ips)

## Install ipsexamples wrapper

```
python3 setup.py install
```

## Install in develop mode

```
python3 setup.py develop
```

## To run the ipsexamples

### Hello world

```
ips.py --config=configs/hello.config --platform=configs/platform.conf
```

### Hello world

```
ips.py --config=configs/abc.config --platform=configs/platform.conf
```
