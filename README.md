# uz/unzip

## Why need this stuff?
The encoding of zip is different from MacOS and Windows. The filename will be garbled if we extracted the file which zip from Windows.
This package can help you extract the file with the correct filename.

## Installation

```
sudo sh install.sh
```

## Usage

```
usage: uz [-t|-—target <targetPath>] [-e|—-encoding <encoding>] filename[.zip]
  Default action is extract file to current path with big5.
  
  -t, --target: absolute path of target destination
  -e, --encoding: encoding of zip file
```
