# AddrProbe
## A Transfer Learning-based Framework for Internet-wide IPv6 Active Address Probing
AddrProbe is an Internet-wide IPv6 active address probing system, which realizes effective active address probing by transferring the accurately portrayed seed address patterns to the target prefix based on transfer learning. 
In addition, a lightweight aliased prefix detection algorithm is proposed for the entire probing process. 

## Getting Started

#### Clone the repo

```
git clone https://github.com/AddrProbe/AddrProbe.git
```


#### Create a virtual environment for Python3.8.10

```
conda create -n py38 python=3.8.10
conda activate py38
```

#### Install Zmap
#####  Building from Source

```
git clone https://github.com/tumi8/zmap.git
cd zmap
```
##### Installing ZMap Dependencies

On Debian-based systems (including Ubuntu):
```
sudo apt-get install build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev
```

On RHEL- and Fedora-based systems (including CentOS):
```
sudo yum install cmake gmp-devel gengetopt libpcap-devel flex byacc json-c-devel libunistring-devel
```

On macOS systems (using Homebrew):
```
brew install pkg-config cmake gmp gengetopt json-c byacc libdnet libunistring
```

##### Building and Installing ZMap

```
cmake .
make -j4
sudo make install
```

#### Install  dependencies
```
conda activate py38
conda install numpy scipy scikit-learn matplotlib tqdm pandas 
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia
pip3 install pyasn
pip3 install setuptools
```

#### Run the code in the ./AddrProbe/code directory

```
cd AddrProbe/code
python3 main_train.py
cp -r ../result/result_template ../result/result
python3 main_test_seeded_prefix.py
mv ../result/result ../result/result_seeded_prefix
cp -r ../result/result_template ../result/result
python3 main_test_unseeded_prefix.py
python3 sat_aliased_prefix.py
```

If you want to change the default configuration, you can edit `DefaultConfig` in `AddrProbe/code/config.py`. Note that the first thing you need to do is to set the Zmap parameters in it, including the source IPv6 address and so on.


## Result
After running the programmings, you can get the output in the file directory that you set in the `AddrProbe/code/config.py`. For each prefix, you can get the newly probed active address.
* Probing results for seeded prefixes are in `AddrProbe/result/result_seeded_prefix/active_address_bank`
* Probing results for unseeded prefixes are in `AddrProbe/result/result_unseeded_prefix/active_address_bank`
* Probing aliased prefix for seeded prefixes are in `AddrProbe/result/result_seeded_prefix/zmap_result/aliased_prefix.txt`
* Probing aliased prefix for unseeded prefixes are in `AddrProbe/result/result_seeded_prefix/zmap_result/aliased_prefix.txt`
