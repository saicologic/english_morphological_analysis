# はじめに
英語の音声を音声認識システムWhisperを用いて文字起こしを行い、形態素解析NLTKを使い単語別の品詞タグを付与し、ターミナル上で色分け方法です。

# 動作環境

- Apple M2 2022
- macOS Ventura 13.1
- Memory 16GB
- Python 3.11.3

# セットアップ
## ライブラリのインストール

```
$ pip install -r requirements.txt
```

## NLTKで使うデータをインストールする

```
$ python3
Python 3.11.3 (main, Apr 19 2023, 18:49:55) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

REPL上で、下記のコマンドを順番に実行していきます。

```
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('maxent_ne_chunker')
>>> nltk.download('words')
```

出力結果例:

```
>>> nltk.download('punkt')
[nltk_data] Downloading package punkt to
[nltk_data]     /Users/mikamisatoru/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
True
```

下記のコマンドを実行すると、インストールされたパッケージをGUIで見ることができます。
```
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
```


インストールされたNTLKのデータファイルを確認する
```
$ open ~/nltk_data
```

## 環境変数の設定

OpenAIのWebサイトのAPI Keyを取得してください。利用にはOpenAIの会員登録が必要です。
https://platform.openai.com/account/api-keys


OPENAI_API_KEYに、API Keyを書き換えて、下記をターミナル環境上で実行してください。

```
$ export OPENAI_API_KEY=""
```

# 実行

```
$ python3 main.py
```


# 任意のファイルを読み込む

```
def main():
    save_audio_file = "./assets/LJ037-0171.wav"
    text = voice_to_text(load_audio(save_audio_file))
    pos_tags = get_pos_tag(text)
    print_morphemed_text(pos_tags)
```

`assets/LJ037-0171.wav` は、パブリックドメインになっている[The LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/)のサンプルデータです。

## 実行結果
![image](./images/image.png)

## トラブルシュート
実行したときに下記のエラーが出た場合の対処方法

## トラブル1

```
ModuleNotFoundError: No module named 'openai'
```
ライブラリのインストールをしてください。

## トラブル2

```
speech_recognition.exceptions.SetupError: Set environment variable ``OPENAI_API_KEY``
```

環境変数`OPENAI_API_KEY`をターミナルの実行環境で設定してください。

## トラブル3

```
openai.error.AuthenticationError: You didn't provide an API key. You need to provide your API key in an Authorization header using Bearer auth (i.e. Authorization: Bearer YOUR_KEY), or as the password field (with blank username) if you're accessing the API from your browser and are prompted for a username and password. You can obtain an API key from https://platform.openai.com/account/api-keys.
```

OPENAI_API_KEYに空が設定されています。APIKEYを設定してください。
