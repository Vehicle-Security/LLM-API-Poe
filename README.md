
### 基于Poe调用不同大模型

```bash
$ curl --location 'http://127.0.0.1:10000/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer you-api-key' \
--data '{
     "model": "ChatGPT",
     "messages": [{"role": "user", "content": "Who is there?"}],
     "stream": true
   }'

```
