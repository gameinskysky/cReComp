# cReComp

creator for Reconfigurable hw Component  
  
**Git**:         https://github.com/kazuyamashi/cReComp.git  
**Author**:      Kazushi Yamashina (Utsunomiya University)  
**Copyright**:   2016, Kazushi Yamashina  
**License**:      new BSD License   
**Latest Version**: 0.0.1  
**Contact**: 	 kazushi_at_virgo.is.utsunomiya-u.ac.jp  or [Twitter](https://twitter.com/KazushihsuzaK) or [Facebook](https://www.facebook.com/kazushi.yamashina?fref=nf)


# What is the cReComp?

The cReComp is a **code generator and framework for componentization of a single hardware or the multiple hardware**. The component generated by the cReComp is HW/SW co-system that is connected between CPU and FPGA (reconfigurable hw). The cReComp is possible to debug and test single hardware with software in a user development fase. When the development of a each hardware have been finished, the cReComp generates one of the HW/SW co-system by integrating the each of the hardware.

# Update

2016/06/23 released version 0.0.1

# Install

## Requirements

#### Platform

Ubuntu or OSX (Mac)  

#### Python (2.7 later)  

```
sudo apt-get install python
```

#### Icarus Verilog  

Ubuntu

```
sudo apt-get install iverilog
```

Mac

```
brew install icarus-verilog
```

#### Jinja2  

```
pip install jinja2
```

#### [pyverilog](https://github.com/PyHDI/pyverilog)  

```
 git clone https://github.com/PyHDI/pyverilog.git
 cd pyverilog/
 python setup.py install
```

#### [veriloggen](https://github.com/PyHDI/veriloggen)  

```
 git clone https://github.com/PyHDI/veriloggen.git
 cd veriloggen/
 python setup.py install
```


## Install cReComp

**Download from github & install**

```
git clone https://github.com/kazuyamashi/cReComp.git
cd cReComp/
python setup.py install
```

**Package install**

```
pip install crecomp
```

# Command usage

```
Usage: python crecomp [-t] [-u user logic]+

Options:
  -h, --help            show this help message and exit
  -u USERLOGIC, --userlogic=USERLOGIC
                        specifier your user logic name
  -t TEMPLATENAME, --template=TEMPLATENAME
                        specifier for template name
```

# Getting Started

[Getting Started English](https://kazuyamashi.github.io/crecomp_doc/getting_started_en.html)  
[Getting Started Japanese](https://kazuyamashi.github.io/crecomp_doc/getting_started_jp.html)  
