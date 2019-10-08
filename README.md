# uz/unzip

## Why do we need this?
The encoding of zip is different between MacOS and Windows. The filename will be garbled if we extracted the file that doesn't have a English file name and is zipped from Windows.
This package assists you in extracting the file with the correct filename🎉.

## Installation

This action allows you to use the command, `uz`, in global enviroment
```
sudo sh install.sh
```

running `uz.sh` can be a alternative solution.
```
./uz.sh <usage>
```

💡Note: This package require `python2`.

## Usage

```
uz [-t|-—target <targetPath>] [-e|—-encoding <encoding>] filename[.zip]

-t, --target: path of target destination.
-e, --encoding: encoding of zip file.
```

Default action is extracting file to current path with `big5`.

## Issue

* The zip filename cannot contain space character ` `.
