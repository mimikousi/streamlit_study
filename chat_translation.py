#!/usr/bin/env python

from transformers import pipeline

MODEL = 'Mitsua/elan-mt-bt-ja-en'

class Translator:
    def __init__(self, model=MODEL):
        try:
            self.pipe = pipeline('translation_ja_to_en', model=model, device=-1)

        except Exception as e:
            print("❌ モデルの読み込みに失敗しました:")
            print(e)
            self.pipe = None  # 失敗時の保険

    def initial(self):
        return 'MITSUA です。日英翻訳します。'

    def final(self):
        return 'また寄ってね。'

    def respond(self, text):
        if self.pipe is None:
            return "⚠️ 翻訳モデルが初期化されていません。"
        results = self.pipe(text, max_length=100)
        return results[0]['translation_text']


if __name__ == '__main__':
    trans = Translator()
    print(trans.initial())

    while True:
        text = input('> ')
        if text.lower().startswith('quit'):
            break
        print(trans.respond(text))

    print(trans.final())
