# bullet_cli

**bullet_cli** is a command-line utility to watch stock in terminal.

## Installation

### Prerequisites

The following dependencies are recommended:

* **[Python](https://www.python.org/downloads/)**  3.10.6 or above

### Download from GitHub

clone and enter this repo, then

```
$ python setup.py install
```

## Getting Started

### Add stock to watch list

```
bullet add {stock keyword}
```

then select the stock which you want and add it to your watch list.

### Remove stock to watch list

```
bullet remove
```

then select the stock to remove.

### Watch stock list

```
bullet fly --interval 3 --fish
```

*--interval* specify the interval of stock refresh, default is 5s  
*--fish* convert the stock name to pinyin and don't show any color to protect yourself when at work.

### Other

```
bullet --help
```

for more information.

## Example

![效果图](https://raw.githubusercontent.com/monkeylmj/bullet_cli/develop/screenshots/s_terminal.png)