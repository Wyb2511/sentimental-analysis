import json
import openai
openai.api_key = "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"
while True:
    msg=input("请输入：")
    if msg == "exit":
        print("已退出聊天")
        break
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"user","content":msg}
                ]
            )
        message = json.dumps(completion.choices[0].message,indent=4,ensure_ascii=False)
        content = json.loads(message)["content"]
        max_width = 50
        content = '\n'.join(content[i:i + max_width] for i in range(0,len(content),max_width))
        print("机器人:" + content)
