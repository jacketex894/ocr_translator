from llama_cpp import Llama
import os
import subprocess
from opencc import OpenCC

class LLM():
    def __init__(self,model_name:str,huggingface_repo_id:str,local_dir:str = "./LLM_model"):
        self.model_name = model_name
        self.huggingface_repo_id = huggingface_repo_id
        self.local_dir = local_dir
        self.convert_worker = OpenCC('s2t')
        

        if not os.path.exists(os.path.join(local_dir, model_name)):
            self.download_with_progress()
        
        self.model = Llama.from_pretrained(
            repo_id = huggingface_repo_id,
            filename = model_name,
            local_dir = local_dir,
            device_map="auto",
            low_cpu_mem_usage = True,
            n_gpu_layers=-1
        )
    def download_with_progress(self):
        os.makedirs(self.local_dir, exist_ok=True)

        func_code = (
            "from huggingface_hub import hf_hub_download;"
            "print('The model does not exist. Starting to download the model.');"
            "model_path = hf_hub_download(repo_id='{}', filename='{}', local_dir='{}');"
            "print(f'file already download : '+model_path);"
            "exit()"
        ).format(self.huggingface_repo_id, self.model_name, self.local_dir)
        try:
            subprocess.Popen(
                f'start cmd /k "python -c \"{func_code}\""',
                shell=True
            )
        except Exception as e:
            print(f"Can't activate CMD：{e}")
    
    def generate_text_from_prompt(self,user_prompt:str, max_tokens:int=512, temperature:float=0.1, top_p:float=0.3, echo:bool=True):
        model_output = self.model(
            user_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            echo=echo,
        )
        return model_output

    def excute_model(self,input_text:str) -> str:
        query = "将下面的日文文本翻译成中文：" + input_text
        prompt = "<|im_start|>system\n你是一个轻小说翻译模型，可以流畅通顺地以日本轻小说的风格将日文翻译成简体中文，并联系上下文正确使用人称代词，不擅自添加原文中没有的代词。<|im_end|>\n<|im_start|>user\n" + query + "<|im_end|>\n<|im_start|>assistant\n"
        model_response = self.generate_text_from_prompt(prompt)
        _resonse = self.convert_worker.convert(model_response["choices"][0]['text'])
        _,answer = _resonse.split("assistant")
        print("\n Model response：\n", answer)
        return answer
    
