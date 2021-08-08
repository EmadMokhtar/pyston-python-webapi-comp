# How to run the project

## Install dependencies

``` bash
pip install -r requirements.txt
```

### Run the server

``` bash
uvicorn main:app
```

You can add `--reload` in case of development so that the server will reload the application wen there is a code change.