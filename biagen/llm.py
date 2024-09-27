# biagen/llm.py

from abc import ABC, abstractmethod
import logging
import os
from timeit_decorator import timeit
from typing import List, Optional

logger = logging.getLogger(__name__)

COHERE_API_KEY = 'COHERE_API_KEY'
GROQ_API_KEY = 'GROQ_API_KEY'
OPENAI_API_KEY = 'OPENAI_API_KEY'
OPENAI_MODEL_NAME = 'OPENAI_MODEL_NAME'


class LLMProvider(ABC):
    @property
    @abstractmethod
    def model(self):
        pass

    @abstractmethod
    def generate(self, prompt: str, max_tokens: int, temperature: float, stop_sequences: list, generations: int,**kwargs) -> List[str]:
        pass

    def generate_one(self, prompt: str, max_tokens: int, temperature: float, stop_sequences: list, **kwargs) -> str:
        return self.generate(prompt, max_tokens, temperature, stop_sequences, generations=1, **kwargs)[0]


class CohereProvider(LLMProvider):
    def __init__(self, api_key: str):
        import cohere
        self.co = cohere.Client(api_key)

    @property
    def model(self):
        return 'command-nightly'

    @timeit()
    def generate(self, prompt: str, max_tokens: int, temperature: float, stop_sequences: Optional[List[str]], generations: int, **kwargs) -> List[str]:
        response = self.co.generate(
            model=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop_sequences=stop_sequences,
            num_generations=generations,
            **kwargs
        )
        return [t.text.strip() for t in response.generations]

    @classmethod
    def from_env(cls):
        api_key = os.getenv(COHERE_API_KEY)
        if not api_key:
            raise ValueError("COHERE_API_KEY environment variable not set")
        return cls(api_key)


class GroqProvider(LLMProvider):
    def __init__(self, api_key: str):
        import groq
        self.groq = groq.Groq(api_key=api_key)
    
    @property
    def model(self):
        return 'mixtral-8x7b-32768'

    @timeit()
    def generate(self, prompt: str, max_tokens: int, temperature: float, stop_sequences: Optional[List[str]], generations: int, **kwargs) -> List[str]:
        # take the first row of our prompt and make it the system message
        system = prompt.split("\n")[0]
        prompt = prompt.replace(system, "").strip()

        chat_completion = self.groq.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system,
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )

        return [t.message.content.strip() for t in chat_completion.choices if t.message.content is not None]
    
    @classmethod
    def from_env(cls):
        api_key = os.getenv(GROQ_API_KEY)
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        return cls(api_key)


class OpenAIProvider(LLMProvider):
    def __init__(self, *, api_key: Optional[str] = None, base_url: Optional[str] = None, model_name: Optional[str] = None):
        import openai
        self.openai = openai.OpenAI(api_key=api_key, base_url=base_url)
        self.model_name = model_name

    @property
    def model(self):
        return self.model_name
    
    @timeit()
    def generate(self, prompt: str, max_tokens: int, temperature: float, stop_sequences: Optional[List[str]], generations: int, **kwargs) -> List[str]:
        if stop_sequences is None:
            stop_sequences = []

        response = self.openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop_sequences,
            n=generations,
            **kwargs
        )
        if response is None:
            raise ValueError("No response from API")
        return [t.message.content.strip() for t in response.choices if t.message.content is not None]

    @classmethod
    def from_env(cls):
        api_key = os.getenv(OPENAI_API_KEY)
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        model_name = os.getenv(OPENAI_MODEL_NAME)
        return cls(api_key=api_key, model_name=model_name)
    
    @classmethod
    def from_url(cls, url: str, api_key: str, model_name: Optional[str] = None):
        return cls(base_url=url, api_key = api_key, model_name=model_name)