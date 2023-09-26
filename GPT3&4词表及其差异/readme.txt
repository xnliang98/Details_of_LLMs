# 词表
GPT-4 词表大小：
100256
> GPT-4 词表中包含中文的字词，包含代码特征的tokens，针对数学计算，词表中包含了所有的1-3位的数字token，并且测试发现超过3位数的数学计算的准确率不高，三位以内的非常高。

GPT-3 词表大小：
50257

两者overlap：43000+

特殊字符：
```
<|endofprompt|>
<|endoftext|>
<|fim_middle|>
<|fim_prefix|>
<|fim_suffix|>
```



```
MODEL_PREFIX_TO_ENCODING: dict[str, str] = {
    # chat
    "gpt-4-": "cl100k_base",  # e.g., gpt-4-0314, etc., plus gpt-4-32k
    "gpt-3.5-turbo-": "cl100k_base",  # e.g, gpt-3.5-turbo-0301, -0401, etc.
}

MODEL_TO_ENCODING: dict[str, str] = {
    # chat
    "gpt-4": "cl100k_base",
    "gpt-3.5-turbo": "cl100k_base",
    # text
    "text-davinci-003": "p50k_base",
    "text-davinci-002": "p50k_base",
    "text-davinci-001": "r50k_base",
    "text-curie-001": "r50k_base",
    "text-babbage-001": "r50k_base",
    "text-ada-001": "r50k_base",
    "davinci": "r50k_base",
    "curie": "r50k_base",
    "babbage": "r50k_base",
    "ada": "r50k_base",
    # code
    "code-davinci-002": "p50k_base",
    "code-davinci-001": "p50k_base",
    "code-cushman-002": "p50k_base",
    "code-cushman-001": "p50k_base",
    "davinci-codex": "p50k_base",
    "cushman-codex": "p50k_base",
    # edit
    "text-davinci-edit-001": "p50k_edit",
    "code-davinci-edit-001": "p50k_edit",
    # embeddings
    "text-embedding-ada-002": "cl100k_base",
    # old embeddings
    "text-similarity-davinci-001": "r50k_base",
    "text-similarity-curie-001": "r50k_base",
    "text-similarity-babbage-001": "r50k_base",
    "text-similarity-ada-001": "r50k_base",
    "text-search-davinci-doc-001": "r50k_base",
    "text-search-curie-doc-001": "r50k_base",
    "text-search-babbage-doc-001": "r50k_base",
    "text-search-ada-doc-001": "r50k_base",
    "code-search-babbage-code-001": "r50k_base",
    "code-search-ada-code-001": "r50k_base",
    # open source
    "gpt2": "gpt2",
}
```
