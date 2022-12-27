try:
    if status == "解決しない":
        print("発狂しちゃう")
        
    elif status == "別のエラーが出る":
        print("3日間は寝込んじゃう")
        
    elif status == "解決方法を見つける":
        print("英語は全く読めない")
        
except SyntaxError:
    print("()や:を忘れていないか今すぐ確認")
    
except IndexError:
    print("シーケンスオブジェクトの要素数は大丈夫か")
    
except NameError:
    print("どうせスペルミスだし大文字小文字に気をつけろ")
    
except TypeError:
    print("型、間違ってない?")
    
except IndentationError:
    print("えっと、あの・・・")
    
except ModuleNotFoundError:
    print("う～～～んw")
    print("とりあえず、日本語でお願いします!")
    
# Thank you Qiita, teratail, stack overflow

SABI_LYRICS = """
Endless Error Loopの中
点と点が繋がる一瞬
脳汁効率よく出しまくるためのプログラミング教育
Endless Error Loopの中
点と点が繋がる一瞬
諦めたものにはたどり着けない場所で笑い合おう
"""

print(SABI_LYRICS)

def endless_error_loop(stage="進捗"):
    while True:
        print("Error")
    return stage

endless_error_loop("納期")