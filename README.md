# CodeGPT

Generating Python Code from Text

Github: [CodeGPT](https://github.com/scy6500/CodeGPT-front)


### Post parameter

    code: Text for the code you want to generate
    max_length: Max length of code you want


### Output format

    {'result': string}


## * With CLI *

### Input example


    curl https://main-code-gpt-python-scy6500.endpoint.ainize.ai/generate \ 
    --header "Content-Type: application/json" --request POST \ 
    --data '{"code":"def add(a, b):", "max_length":30}'
    

### Output example


    {'result': 'def add(a, b): return a + b'}


## * With swagger *

API page: [Ainize](https://ainize.ai/scy6500/CodeGPT-Python?branch=main)

## * With a Demo *

Demo page: [End-point](https://main-code-gpt-front-scy6500.endpoint.ainize.ai/)