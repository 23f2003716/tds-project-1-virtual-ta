# Regarding project1 for file not detecting after sending post request

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/1

## Topic Metadata
- **ID**: 167172
- **Slug**: regarding-project1-for-file-not-detecting-after-sending-post-request
- **Created**: 2025-02-14T12:38:47.706Z
- **Views**: 59
- **Replies**: 11
- **Likes**: 0
- **Tags**: clarification, term1-2025, tds-project-1

## Original Post
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T12:38:47.883Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/1

sir i am getting an error in this function calling which you have demonstrate yesterday , i am attaching my code also the error with it. Please take a look and provide the solution as the deadline is close please help me as soon as possible.

is there anything to do with dockerfile or anything else please explain it how to do it step by step.

import os
from dotenv import load_dotenv
import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "enter your token here")

def sort_contacts(contacts_file_path: str, output_file_path: str):
    try:
        contacts = pd.read_json(contacts_file_path)
        contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
        return {"message": f"Contacts sorted and saved to {output_file_path}"}
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}

a4_tool = {
    "type": "function",
    "function": {
        "name": "sort_contacts",
        "description": "This function takes data from a json file and sorts the data first by last name and then by first name, then it stores it inside the speicfied location.",
        "parameters": {
            "type": "object",
            "properties": {
                "contacts_file_path": {
                    "type": "string",
                    "description": "The relative path to the input JSON file containing the contacts."
                },
                "output_file_path": {
                    "type": "string",
                    "description": "The relative path to the output JSON file to store the sorted contacts."
                }
            },
            "required": ["contacts_file_path", "output_file_path"],
            "additionalProperties": False
        },
        "strict": True
    },
}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]

def query_gpt(user_input: str, tools: list[dict] = tools) -> dict:
    response = requests.post(
        url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "tools": tools,
            "tool_choice": "auto"
        }
    )
    return response.json()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="File does not exist")

@app.post("/run")
async def run(task: str):
    query = query_gpt(task)
    print(query)  # Print the full response to inspect it.
    
    if 'choices' not in query:
        raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
    
    try:
        tool_calls = query['choices'][0]['message'].get('tool_calls', [])
        if tool_calls:
            func_name = tool_calls[0]['function']['name']
            args = json.loads(tool_calls[0]['function']['arguments'])
            
            # Map function names to their respective functions
            function_map = {
                "cakebake": cakebake,
                "install_uv_and_run_datagen": install_uv_and_run_datagen,
                "format_markdown_file": format_markdown_file,
                "count_wednesdays": count_wednesdays,
                "sort_contacts": sort_contacts,
                "extract_recent_logs": extract_recent_logs,
                "create_markdown_index": create_markdown_index,
                "extract_sender_email": extract_sender_email,
                "extract_credit_card_number": extract_credit_card_number,
                "find_similar_comments": find_similar_comments,
                "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
            }
            
            if func_name in function_map:
                output = function_map[func_name](**args)
            else:
                raise HTTPException(status_code=500, detail="Unknown function called")
        else:
            raise HTTPException(status_code=500, detail="No function call found in response")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
    
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

**Image: Screenshot 2025-02-14 171217**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows the interface of a tool like Postman or Insomnia, used for making HTTP requests.
*   There's a tabbed interface with options like "Params," "Auth," "Headers," "Body," "Scripts," "Tests," and "Settings."
*   A URL input field is present, along with a dropdown to select the HTTP method (POST is selected).
*   A "Send" button is visible.
*   The "Body" tab is selected, and the content type is set to "JSON."
*   There are icons for "Preview" and "Visualize."

**2. Text Content:**

*   **URL:** `http://127.0.0.1:8000/run?task=Sort the array of contacts in /...`
*   **HTTP Method:** POST
*   **Params:**
    *   Key: `task`
    *   Value: `Sort the array of contacts i...`
*   **JSON Body:**
    ```json
    {
      "error": "Failed to sort contacts: File /data/contacts.json does not exist"
    }
    ```
*   **Status Code:** 200 OK
*   **Response Time:** 2.96 s
*   **Response Size:** 201 B
*   Other UI elements: "New", "Import", "Save", "Share", "No environment"

**3. Context/Purpose:**

*   The image shows a user making a POST request to a local server (`127.0.0.1:8000`).
*   The request is intended to trigger a task: "Sort the array of contacts."
*   The server is responding with a 200 OK status code, but the JSON response indicates an error.
*   The error message states that the file `/data/contacts.json` could not be found.

**4. Technical Details:**

*   The request is likely intended to sort a list of contacts stored in a JSON file.
*   The server-side code is attempting to read the contacts from `/data/contacts.json`.
*   The error suggests that either the file doesn't exist at

@Saransh_Saini , @Jivraj , @carlton

---

## Reply 1
**Author**: Carlton D'Silva
**Posted**: 2025-02-14T13:01:08.797Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/2

Hi Sakshi,

The error is quite clear, it cannot find the file /data/contacts.json

Question: What creates the /data/contacts.json file?

---

## Reply 2
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T13:30:26.445Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/3

so how to do it sir that the thing i am not able to understand.

---

## Reply 3
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T13:59:34.581Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/4

sir kindly help me with this the time is running and i am still at the starting stage of project.

@carlton

---

## Reply 4
**Author**: Saransh Saini
**Posted**: 2025-02-14T14:16:24.088Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/5

Sakshi as the error says it’s unable to find your file. Try adding a . (dot) before the location.

---

## Reply 5
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T14:32:12.846Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/6

sir i have used the dot(.) while sending the request to postman in the query which i provided to the task. Is the dot(.) should be added somewhere else?

---

## Reply 6
**Author**: Saransh Saini
**Posted**: 2025-02-14T15:07:26.713Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/7

If you have added that dot as a prefix to your locations then, you would have to structure your query_gpt in such a way that it takes these dots into consideration.

---

## Reply 7
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T17:48:35.347Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/8

sir i have tried that by putting by doing this

import os
from dotenv import load_dotenv
import json
import requests
from dateutil import parser as date_parser
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3
import base64
import mimetypes
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
def cakebake(no_people: int, flavor: str):
    return {"message": f"Making a {flavor} cake for {no_people} people"}

bakecake = {
    "type": "function",
    "function": {
        "name": "cakebake",
        "description": "Make a cake for all iitm students contain its emailids",
        "parameters": {
            "type": "object",
            "properties": {
                "no_people": {
                    "type": "integer",
                    "description": "Number of people"
                },
                "flavor": {
                    "type": "string",
                    "description": "Flavor of the cake"
                }
            },
            "required": ["no_people", "flavor"],
            "additionalProperties": False
        },
        "strict": True
    }
}

def sort_contacts(contacts_file_path: str, output_file_path: str):
    try:
        contacts = pd.read_json(contacts_file_path)
        contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
        return {"message": f"Contacts sorted and saved to {output_file_path}"}
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]

def query_gpt(user_input: str, tools: list[dict] = tools) -> dict[str, Any]:
    response = requests.post(
        url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": """
                        Whenever you receive a system directory location, always make it into a realtive path, for example adding a . before it would make it relative path, rest is on you to manage, I just want the relative path"""
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "tools": tools,
            "tool_choice": "auto"
        }
    )
    return response.json()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="File does not exist")

@app.post("/run")
async def run(task: str):
    query = query_gpt(task)
    print(query)  # Print the full response to inspect it.
    
    if 'choices' not in query:
        raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
    
    try:
        tool_calls = query['choices'][0]['message'].get('tool_calls', [])
        if tool_calls:
            func_name = tool_calls[0]['function']['name']
            args = json.loads(tool_calls[0]['function']['arguments'])
            
            # Map function names to their respective functions
            function_map = {
                "cakebake": cakebake,
                "install_uv_and_run_datagen": install_uv_and_run_datagen,
                "format_markdown_file": format_markdown_file,
                "count_wednesdays": count_wednesdays,
                "sort_contacts": sort_contacts,
                "extract_recent_logs": extract_recent_logs,
                "create_markdown_index": create_markdown_index,
                "extract_sender_email": extract_sender_email,
                "extract_credit_card_number": extract_credit_card_number,
                "find_similar_comments": find_similar_comments,
                "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
            }
            
            if func_name in function_map:
                output = function_map[func_name](**args)
            else:
                raise HTTPException(status_code=500, detail="Unknown function called")
        else:
            raise HTTPException(status_code=500, detail="No function call found in response")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
    
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

and also i am sending postman request as [http://localhost:8000/run?task=The](http://localhost:8000/run?task=The) file ./data/dates.txt contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to ./data/dates-wednesdays.txt

do I need to use dockerfile for this? i am still getting the same error as

**Image: Screenshot 2025-02-14 231752**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows the interface of a tool like Postman or Insomnia, used for making HTTP requests.
*   There's a dropdown menu labeled "POST" indicating the HTTP method being used.
*   An input field contains the URL: `http://localhost:8000/run?task=The file ./data/dates.txt co`. This suggests a local server is running on port 8000, and a "run" endpoint is being accessed with a "task" parameter.
*   A "Send" button is present to initiate the request.
*   Tabs are visible for "Params", "Auth", "Headers (7)", "Body", "Scripts", "Tests", and "Settings". A "Cookies" link is also present.
*   The "Params" tab is active, showing a key-value pair: "task" with the value "The file ./data/dates.txt c...".
*   Below the tabs, there's a section for the response body, with options to view it as "JSON", "Preview", or "Visualize".
*   The response body is displayed as JSON.

**2. Text Content:**

*   **URL:** `http://localhost:8000/run?task=The file ./data/dates.txt co`
*   **Parameter:** "task" with value "The file ./data/dates.txt c..."
*   **Response Status:** "200 OK" (indicating a successful request)
*   **Response Time:** "2.72 s"
*   **Response Size:** "220 B"
*   **JSON Response Body:**
    ```json
    {
      "error": "Failed to count Wednesdays: [Errno 2] No such file or directory: './data/dates.txt'"
    }
    ```

**3. Context and Purpose:**

*   The image shows a user making a POST request to a local server.
*   The request includes a "task" parameter, likely instructing the server to perform a specific operation on a file.
*   The server's response indicates an error: it failed to count Wednesdays, and the error message "No such file or directory: './data/dates

@carlton , @Saransh_Saini , @Jivraj

---

## Reply 8
**Author**: Ansh bansal
**Posted**: 2025-02-14T17:55:28.433Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/9

have you first post a request for task A1 as it creates the data folder along with  all the other files .

---

## Reply 9
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T18:19:59.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/10

no actually do we have to create another file for that or we have to request post in this one ? can you guide me for that step wise . it would be very helpful.

---

## Reply 10
**Author**: Ansh bansal
**Posted**: 2025-02-14T18:22:49.379Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/11

by running task A1 , it automatically creates a data folder along with all the files in it. Without running task A1 you can’t do rest of A tasks

---

## Reply 11
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T18:38:09.127Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/12

how can i run A1 task can elaborate a little bit. do i have to create data folder manually or  using this code by giving query taskA1 it will generate that folder ?

---

## Reply 12
**Author**: Ansh bansal
**Posted**: 2025-02-14T18:39:57.491Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/13

simply give task=“task”

task: copy the task a_1 from project document

---

## Reply 13
**Author**: SAKSHI PATHAK
**Posted**: 2025-02-14T18:44:30.274Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/regarding-project1-for-file-not-detecting-after-sending-post-request/167172/14

it is showing

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
{'id': 'chatcmpl-B0uvU556EOCy6HOPHV9ni7YJY403i', 'object': 'chat.completion', 'created': 1739558524, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': None, 'tool_calls': [{'id': 'call_JXkfp14QEEo6M2zdgBXKduqi', 'type': 'function', 'function': {'name': 'install_uv_and_run_datagen', 'arguments': '{"email":"24f2006749@ds.study.iitm.ac.in"}'}}], 'refusal': None}, 'logprobs': None, 'finish_reason': 'tool_calls'}], 'usage': {'prompt_tokens': 732, 'completion_tokens': 30, 'total_tokens': 762, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': 'fp_00428b782a', 'monthlyCost': 0.09109908, 'cost': 0.002376, 'monthlyRequests': 137}
Collecting uv
  Downloading uv-0.6.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Downloading uv-0.6.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 3.2 MB/s eta 0:00:00
Installing collected packages: uv
Successfully installed uv-0.6.0
python: can't open file '/home/sakshi-tds/tds_project1/https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py': [Errno 2] No such file or directory
INFO:     127.0.0.1:34758 - "POST /run?task=Install%20uv%20(if%20required)%20and%20run%20https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py%20with%2024f2006749@ds.study.iitm.ac.in%20as%20the%20only%20argument. HTTP/1.1" 200 OK

**Image: Screenshot 2025-02-15 001314**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows the interface of a tool like Postman or Insomnia, used for making HTTP requests.
*   There's a request URL field: `http://localhost:8000/run?task=Install uv (if required) and ru...`
*   The HTTP method is set to `POST`.
*   There are tabs for `Params`, `Auth`, `Headers (7)`, `Body`, `Scripts`, `Tests`, and `Settings`. The `Params` tab is currently selected.
*   Within the `Params` tab, there's a key-value pair: `task` with the value `Install uv (if required) and ...`.
*   Below the `Params` section, the `Body` section is open, and it's set to `JSON` format.
*   There's a "Send" button to execute the request.
*   There are also buttons for "Save" and "Share".
*   At the top, there are navigation arrows, a plus sign (presumably for adding a new request), and a dropdown for selecting the environment.
*   At the bottom, there is a "Postbot" button with the shortcut "Ctrl Alt P".

**2. Text Content:**

*   **URL:** `http://localhost:8000/run?task=Install uv (if required) and ru...`
*   **HTTP Method:** `POST`
*   **Parameter:** `task` with value `Install uv (if required) and ...`
*   **Tabs:** `Params`, `Auth`, `Headers (7)`, `Body`, `Scripts`, `Tests`, `Settings`
*   **Body (JSON):**
    ```json
    {
      "error": "Failed to run datagen.py: Command '['python', 'https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py', '24f2006749@ds.study.iitm.ac.in']' returned non-zero exit status 2."
    }
    ```
*   **Status:** `20

---
