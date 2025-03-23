from langchain_openai import ChatOpenAI

# 初始化 ChatOpenAI，启用流式传输
llm = ChatOpenAI(
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    openai_api_key="#",  # 替换为你的API密钥
    model_name="qwen-omni-turbo",  # 模型名称
    streaming=True  # 启用流式传输
)


def GPTV1(questiontext):
    response = llm.stream(questiontext)  # 使用 stream 方法获取流式响应
    full_response=""

    for chunk in response:
        full_response+=chunk.content
    return full_response

