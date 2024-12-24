from typing import TypedDict

class model_info(TypedDict):
    """
    Data structure for storing static file paths related to a specific LLM model.

    Attributes:
        model_name (str): The name of the model file.
        huggingface_repo_id (str): The Hugging Face repository ID where the model is stored.
    """
    model_name: str
    huggingface_repo_id: str

sakura_model_14b = model_info(
    model_name="sakura-1.5b-qwen2.5-v1.0-fp16.gguf",
    huggingface_repo_id="SakuraLLM/Sakura-1.5B-Qwen2.5-v1.0-GGUF"
)