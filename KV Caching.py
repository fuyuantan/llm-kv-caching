import threading
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
from time import time

# 加载模型和分词器（你可以替换成你自己的模型，比如 'gpt2' 或其他支持 causal LM 的模型）
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
# Dropout会随机丢弃一部分神经元，这里eval后全部保留
model.eval()

# 编码输入
input_text = "On a bright Monday morning"
tokens = tokenizer.encode(input_text, return_tensors="pt")

# 创建 streamer
streamer = TextIteratorStreamer(tokenizer, skip_special_tokens=True)

# 使用线程异步生成
thread = threading.Thread(target=model.generate, kwargs={
    "input_ids": tokens,
    "max_new_tokens": 100,
    "use_cache": False,  # cache的开关
    "streamer": streamer
})

# 启动线程
start = time()
thread.start()

# 流式输出
for token in streamer:
    print(token, end="", flush=True)

end = time()
print(f"\n\nWithout KV caching: {end - start:.3f} seconds")  # With Without

# 等待线程结束
thread.join()