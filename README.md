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

## Usage

💡 Note: The zip filename cannot contain space character ` `!
```
uz [-t|-—target <targetPath>] [-e|—-encoding <encoding>] filename[.zip]

Default action is extracting file to current path with `big5`.
-t, --target: path of target destination.
-e, --encoding: encoding of zip file.
```
