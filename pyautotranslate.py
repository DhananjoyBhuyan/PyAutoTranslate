#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:01:41 2025

Last edited on Sat Feb 1 21:27:12 2025

@author: Dhananjoy Bhuyan
"""

from huggingface_hub import InferenceClient
import string
import os
import inspect
import webbrowser

FILE_NAME = None


def _hfAsk(prompt: str = "hello",
           system_prompt: str = "Your name is ProBot"):
    MESSAGES = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    params = {
        "temperature": 0.0,
        "max_tokens": 8000,
        "stream": True
    }

    client = InferenceClient(
        provider='featherless-ai',
        model="mistralai/Mistral-7B-Instruct-v0.2",
        token="hugging face API token",
    )
    response_text = []
    for message in client.chat_completion(
        messages=MESSAGES,
        **params
    ):
        token_content = message.choices[0].delta.content
        if token_content:
            response_text.append(token_content)

    response_text = "".join(response_text)
    return response_text


def _validate_filename(file_name: str):
    symbols = list(string.punctuation)
    symbols.remove('_')
    for i in symbols:
        if i in file_name and i != ' ':
            raise ValueError(
                "There should be no file extension or any punctuation or symbols in the file name just give the file_name, THAT'S IT!!!!!!")
    return file_name


def _translate_to_lang(file_path: str, lang: str):
    with open(file_path, "r") as f:
        code = f.read()
    code_start = code.find('"""pycode') + 9
    code_end = code.find('"""', code_start)
    code = code[code_start:code_end]
    converted_code = _hfAsk(
        code, system_prompt=f"You are an AI interpreter, so people give you code and you just translate it into {lang}, the code is kinda different or even can be plain english or kinda psuedo code, Any kind. But you understand what the code means, then you translate to {lang} only.")

    if converted_code and "```" in converted_code:
        code_start = converted_code.find("```") + len(lang) + 3
        code_end = converted_code.find("```", code_start)
        code = converted_code[code_start:code_end]
    else:
        return None
    return code


def _save_and_open_code(code: str, file_name: str, extension: str, lang: str):

    with open(f"./{file_name}.{extension}", "w") as f:
        f.write(code)
    path = os.path.abspath(f"./{file_name}.{extension}")
    if lang.strip() == "html":
        try:
            webbrowser.get("google-chrome").open(f"file://{path}"
                                                )
        except:
            webbrowser.open(f"file://{path}"
                           )


LANG = None
EXTENSION = None


def init(file_name: str, extension_of_output_file: str, language: str):
    global LANG
    global FILE_NAME
    global EXTENSION
    FILE_NAME = _validate_filename(file_name)
    LANG = language
    if '.' in extension_of_output_file:
        extension_of_output_file = extension_of_output_file.replace('.', '')
    EXTENSION = extension_of_output_file


def execute_code():
    file_path = inspect.stack()[1].filename
    code = _translate_to_lang(file_path, LANG)
    if code:
        _save_and_open_code(code, file_name=FILE_NAME,
                            extension=EXTENSION, lang=LANG)
    else:
        ValueError("Maybe our interpreter could not understand your code, please write it in a more understandable way or please write it in plain english.")

