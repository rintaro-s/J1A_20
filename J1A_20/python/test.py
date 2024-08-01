import requests

prompt = "今日はとてもいい天気ですね。"
temperature = 0.7
max_tokens = 100

url = 'http://192.168.0.77:1234/v1/completions'
headers = {'Content-Type': 'application/json'}
data = {
  'prompt': prompt,
  'temperature': temperature,
  'max_tokens': max_tokens
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
  generated_text = response.json()['generated_text']
  print('生成されたテキスト:', generated_text)
else:
  print('エラーが発生しました:', response.status_code, response.text)
