import openai


openai.api_key = "your-api-key"


def documenter(code_snippets, programming_language, temperature=0.7):
    try:
        prompt = f"""
        Given a {code_snippets} in a {programming_language} programming language, please provide comprehensive documentation for the code. 
        Include comments that explain the purpose of each function, method, and major code block. 
        Additionally, describe any input parameters, expected outputs, and key variables used in the code. 
        Ensure that the documentation follows best practices for clarity and readability.
        Make sure that you insert the documentation as part of the code provided as comments.
        But don't change the actual code
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


def optimizer(code_snippets, programming_language, temperature=0.7):
    try:
        prompt = f"""
        For a provided {code_snippets} in a {programming_language}  programming language of your choice, your task is to optimize the code. 
        Focus on improving efficiency, reducing redundancy, and enhancing overall performance. 
        Feel free to refactor the code structure, eliminate unnecessary loops or conditions, and employ best practices for optimization. 
        Provide comments explaining the optimizations made and any potential trade-offs.     
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,  # Adjust max_tokens as needed for the outline
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


def summarizer(code_snippets, programming_language, temperature=0.7):
    try:
        prompt = f"""
        Given a {code_snippets} in a {programming_language} programming language of your choice, summarize the overall meaning and functionality of the code. 
        Highlight the main objectives and outcomes without delving into the specific implementation details. 
        Ensure the summary is concise and captures the essence of the code's purpose. 
        Additionally, mention any key algorithms or techniques employed in the code.  
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


def translator(
    code_snippets,
    source_programming_language,
    target_programming_language,
    temperature=0.7,
):
    try:
        prompt = f"""
        Receive {code_snippets} written in a {source_programming_language}source programming language and the {target_programming_language}target programming language for translation. 
        Your goal is to accurately and efficiently translate the provided code to the target language while ensuring that the functionality remains intact. 
        Pay attention to language-specific syntax, conventions, and potential differences in behavior between the source and target languages. 
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,  # Adjust max_tokens as needed for the outline
            temperature=temperature,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)
