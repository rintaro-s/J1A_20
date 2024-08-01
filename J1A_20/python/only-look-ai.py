# coding: UTF-8
import asyncio
import websockets
import time

######################################################################################
######################################################################################
# 注意！！
# これはAIを叩くためのコードではありません。パソコンが壊れて、AIが使えないので作られたコードです。
# このコードは発表用に作成したファイルで、実際にAIは動いていません。
# あくまで、「どのように動くかを発表」するために作られたものなので実用しないでください。
######################################################################################
######################################################################################

async def handler(websocket, path):
    while True:
        data = await websocket.recv()
        keisu = "工学リテラシとプログラミングの違いは？"

        time.sleep(3)

        def send_inference_request(data):
        
            if(data == keisu):
                generated_text = "＜これは今回生成された文章ではありません。事前に出力された文章です。＞工学リテラシはITパスポートの内容をもとにパソコンの基礎知識について勉強して、プログラミングは、C言語のプログラムを勉強するよ！だけど、工学リテラシでもHTMLを勉強するからどっちも勉強するといいよ！"
                websocket.send(generated_text)
                #print("工学リテラシはITパスポートの内容をもとにパソコンの基礎知識について勉強して、プログラミングは、C言語のプログラムを勉強するよ！だけど、工学リテラシでもHTMLを勉強するからどっちも勉強するといいよ！")

                return generated_text
                
            else:
                generated_text = "エラー：接続に失敗しました。もう一度やり直してください。・tobawifiを使用していませんか？　・サーバーは動いていますか？　・インターネットに接続していますか？"
                websocket.send(generated_text)
                print("エラー！")
                return generated_text
            
        await websocket.send(send_inference_request(data))
        
    
        
    
            

async def main():
    async with websockets.serve(handler, "", 8000):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
