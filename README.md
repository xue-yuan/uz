# uz/unzip

## Why do we need this?
The encoding of zip is different between MacOS and Windows. The filename will be garbled if we extracted the file which is zipped from Windows.
This package assists you on extracting the file with the correct filename.

## Installation

This action allows you to use the command, `uz`, in global enviroment
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
