# Example IPS installable components

This is an example of two components, hello world and ABC, taken from
[ips-examples](https://github.com/ORNL-Fusion/ips-examples) and
converted into a installable package. This is also an example of using
`MODULE` instead of `SCRIPT` in the component configuration section.

## Install IPS

```
python -m pip install git+https://github.com/HPC-SimTools/IPS-framework.git@v0.2.0
```

or follow [Installing IPS guide](https://ips-framework.readthedocs.io/en/latest/getting_started/getting_started.html#installing-ips)

## Install ipsexamples

```
python3 setup.py install
```

## Or install in develop mode

```
python3 setup.py develop
```

## To run the ipsexamples

### Hello world

```
ips.py --config=configs/hello.config --platform=configs/platform.conf
```

### ABC example

```
ips.py --config=configs/abc.config --platform=configs/platform.conf
```
