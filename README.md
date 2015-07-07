# jsontidy
A simple python script for making JSON data readable

## Basic Usage

jsontidy can be used with both pipes (stdin and stdout) or with files

Using pipes:
`jsontidy.py < myfile.json > newfile.json`

Using files:
`jsontidy.py myfile.json -o newfile.json`

It is also possible to mix and match:
```
<json producing utility> | jsontidy.py -o newfile.json
jsontidy.py myfile.json | <json consuming utility>
```

There are additional options available for more advanced uses, see jsontidy.py -h for more information
