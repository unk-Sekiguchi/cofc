from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ChatForm
import openai
import os
from dotenv import load_dotenv

# Create your views here.


def index(request):
    """
    チャット画面
    """
    # 応答結果
    chat_results = ""

    if request.method == "POST":
        # ChatGPTボタン押下時

        form = ChatForm(request.POST)
        if form.is_valid():
            
            #フォーム入力データの取得と加工
            age = form.cleaned_data['age_sentence']
            gender = form.cleaned_data['gender_sentence']
            jobs = form.cleaned_data['jobs_sentence']
            other = form.cleaned_data['other_sentence']
            sentence = f"以下特徴を持つクトゥルフ神話TRPGのキャラクターを生成して\n" \
                        f"年齢:{age}\n" \
                        f"性別:{gender}\n"\
                        f"職業:{jobs}\n"\
                        f"その他の特徴:{other}\n"
            print(sentence)
            # TODO: APIキーのハードコーディングは避ける
            load_dotenv('../.env')
            openai.api_key = os.environ.get("OPENAI_KEY")

            # ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "日本語で応答してください"
                    },
                    {
                        "role": "user",
                        "content": sentence
                    },
                ],
            )

            chat_results = response["choices"][0]["message"]["content"]

    else:
        form = ChatForm()

    template = loader.get_template('cofc_app/index.html')
    context = {
        'form': form,
        'chat_results': chat_results
    }
    return HttpResponse(template.render(context, request))