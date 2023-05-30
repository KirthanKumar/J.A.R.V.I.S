import openai
from config import apiKey
openai.api_key = apiKey

# the below code will be generated when some query is entered in playground space in openai
response = openai.Completion.create(
    model = "text-davinci-003",
    prompt="Write an email to my boss for resignation?",
    temparature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_panalty=0,
    presence_penalty=0
)

print(response)

# the below one is the response printed in terminal after running the above code
'''
{
    "choices": [
        {
        "finish_reason": "stop",
        "index":0,
        "logprobes":null,
        "text": "\n\nSubject\n\n the answer to the question is generated here"
        }
    ],
    "created":  ,
    "id":   ,
    "model":    ,
    "object":   ,
    "usage": {
        "completion_tokens":    ,
        "prompt_tokens":    ,
        "total_tokens":
    }
}
'''
# Therefore the answer generated is in "text". This "text" key's value will be stored in other file.