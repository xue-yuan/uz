# uz/unzip

## Why need this stuff?
The encoding of zip is different from MacOS and Windows. The filename will be garbled if we extracted the file which zip from Windows.
This package can help you extract the file with the correct filename.

## Installation

This action can let you use the commandm, `uz`, in global enviroment
```
sudo sh install.sh
```
Or you can just run the `uz.sh` at once.
```
./uz.sh <usage>
```

## Usage

```
uz [-t|-—target <targetPath>] [-e|—-encoding <encoding>] filename[.zip]

Default action is extract file to current path with big5.  
-t, --target: absolute path of target destination
-e, --encoding: encoding of zip file
```
