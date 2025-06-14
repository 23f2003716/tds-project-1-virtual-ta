# Tds-official-Project1-discrepencies

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1

## Topic Metadata
- **ID**: 171141
- **Slug**: tds-official-project1-discrepencies
- **Created**: 2025-03-28T18:34:40.927Z
- **Views**: 1864
- **Replies**: 321
- **Likes**: 150
- **Tags**: term1-2025, tds-project-1

## Original Post
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-28T18:34:41.099Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1

Please post any discrepancies related to project1.

@carlton

Who were evaluated? How did we decide what to evaluate?

All the image ids we evaluated were what *you* submitted to us. This is the list of docker repos that was given to us by @s.anand as the official list that met all the pre-requisites of Project 1. Therefore we will only evaluate those on this list who are eligible for evaluation with the repos *you* gave us.

For clarity. Your docker repo gets a unique id every time it is changed. We will ONLY evaluate the image id which was present at the time of the docker repo being pulled. This acts as a time stamped frozen version of your repo. No other image id will be evaluated.

How to fix bugs in our scripts

Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

**Docker Image Architecture Issue Report**

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

Bug fixes

If you find bugs in our evaluation scripts, you might benefit from more marks because of the bug fix. So it is in your interest to look through our scripts and logs and identify bugs or anomalies. You might just go from 0 to heros.

Kind regards,

TDS Team

---

## Reply 1
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-28T18:35:12.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/2

*No content*

---

## Reply 2
**Author**: ABHIJEET KUMAR 
**Posted**: 2025-03-28T19:03:42.095Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/3

What is the highest mark anyone has scored? Is it 22/20

@Carlton?

---

## Reply 3
**Author**: Aarush saxena 
**Posted**: 2025-03-28T19:11:04.307Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/4

How come me and my group used same code but some got 10 some 11 some 12?

---

## Reply 4
**Author**: Yogesh
**Posted**: 2025-03-28T19:11:39.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/5

@carlton Please make clear what the average marks are, what highest marks are, and how the project will be evaulated.

We are very close to the end semester exam, and we are still not clear on assignment and project marks. It is a bit frustrating to plan in such circumstances.

---

## Reply 5
**Author**: Carlton D'Silva
**Posted**: 2025-03-28T19:12:51.933Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/6

You have to see the logs for that. We have shared the logs. Everyone was graded by the exact same code, so there is no partiality. Your code did not produce consistent results.

---

## Reply 6
**Author**: Dhruv
**Posted**: 2025-03-28T19:14:57.376Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/7

I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.

This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

---

## Reply 7
**Author**: Ritwika Dutta 
**Posted**: 2025-03-28T19:15:19.619Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/8

My evaluation log file is missing, although I followed all the steps to generate the docker image correctly, it’s showing the server didn’t start for 5 minutes but when I uploaded it, it was working fine. Please help me out sir, I worked hard on the project. I’ll get a zero, but I made the submissions correctly. Some other student also got the “server didn’t start in 5 minutes” but he has an evaluation log file. Please kindly help me out. My roll no. is 22f2001389

---

## Reply 8
**Author**: Carlton D'Silva
**Posted**: 2025-03-28T19:16:38.027Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/9

We will check and rerun on arm if we ran it on the wrong emulation.

---

## Reply 9
**Author**: Ritwika Dutta 
**Posted**: 2025-03-28T19:19:15.240Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/11

Any suggestions for my case sir ? I’m really tensed.

---

## Reply 10
**Author**: Pradeep Mondal
**Posted**: 2025-03-28T19:20:38.723Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/12

22f3002933:

I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.

This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

@carlton  same issue, My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error`  and  **Evaluation log file** is MISSING.

Actually my image was run on x86_64 architecture as it was present in that log file and because of the wrong architecture it never started.

I also request that my evaluation be done again on the right machine.

**Image: Screenshot 2025-03-29 at 12.51.59 AM**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a table-like UI element, likely from a container registry or similar platform.
*   It displays information about a specific container image.
*   There's a "Copy" button.

**2. Text Content:**

*   **TAG:** This is a column header.
*   **latest:** This is the tag of the container image, indicated by a green circle.
*   **Last pushed about 1 month by pradeepmondal:** Indicates when the image was last updated and by whom.
*   **Digest:** This is a column header.
*   **a4d9cad3b5f5:** This is the digest (SHA256 hash) of the container image.
*   **docker pull pradeepmondal/final-tds-project-pradeep-mondal:latest:** This is the command to pull the container image using Docker.
*   **Copy:** A button to copy the Docker pull command.
*   **OS/ARCH:** This is a column header.
*   **linux/arm64/v8:** The operating system and architecture the image is built for.
*   **Last pull:** This is a column header.
*   **1 day:** Indicates when the image was last pulled.
*   **Compressed size:** This is a column header.
*   **179.2 MB:** The compressed size of the container image.

**3. Context/Purpose:**

*   The image is likely from a container registry (like Docker Hub, GitHub Container Registry, etc.).
*   It provides information about a specific container image, including its tag, digest, OS/architecture, last pull time, and compressed size.
*   The "Copy" button allows users to easily copy the Docker pull command to download and run the container.

**4. Technical Details:**

*   The "Digest" is a cryptographic hash of the image manifest, ensuring the integrity and uniqueness of the image.
*   The "OS/ARCH" indicates the target platform for the container, in this case, Linux on ARM64 architecture (specifically, the v8 variant).
*   The Docker pull command is a standard command used to download container images from a registry.
*   The image

Even just now I tried running the exact image:

**Image: Screenshot 2025-03-29 at 12.53.35 AM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal output, likely from a Linux or Unix-like operating system. It displays the result of running a `podman` command. Podman is a container management tool similar to Docker.

**2. Any text content visible:**

The text content includes:

*   `podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 047fa151bf43`
*   `INFO: Started server process [1]`
*   `INFO: Waiting for application startup.`
*   `INFO: Application startup complete.`
*   `INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`

**3. The context or purpose of what's displayed:**

The image shows the process of starting a containerized application using Podman. The command `podman run` is used to create and run a container. The output indicates that a server process has started, the application is starting up, and Uvicorn (an ASGI server) is running on `http://0.0.0.0:8000`.

**4. Technical details:**

*   `podman run`: This is the command to run a container in Podman.
*   `--rm`: This flag tells Podman to remove the container after it exits.
*   `-e AIPROXY_TOKEN=$AIPROXY_TOKEN`: This sets an environment variable named `AIPROXY_TOKEN` inside the container. The value is taken from the environment variable `$AIPROXY_TOKEN` on the host system.
*   `-p 8000:8000`: This maps port 8000 on the host machine to port 8000 inside the container.
*   `047fa151bf43`: This is likely the image ID or name of the container image being used.
*   `Uvicorn`: This is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server, often used with Python web frameworks like FastAPI.
*   `http://0.0.0.

It is running fine on my macbook air m1 (ARM)

@Jivraj @Saransh_Saini

---

## Reply 11
**Author**: Anisha Seth
**Posted**: 2025-03-28T19:26:23.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/13

22f2001389:

uploaded

Facing the same issue sir, kindly look into it. I had made sure all the files including the docker file were working perfectly fine. Please help me out.

Roll no. 23f1002056

---

## Reply 12
**Author**: Pranav Kshirsagar
**Posted**: 2025-03-28T19:27:25.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/14

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly. I request for re evaluation of my project. my roll no is 22f1000703

---

## Reply 13
**Author**: SP
**Posted**: 2025-03-28T19:30:09.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/15

Respected,

I haven’t received any mail yet regarding the TDS Project 1 marks.

Please look into it.

Regards,

Soham

---

## Reply 14
**Author**: AYUSH SINGH
**Posted**: 2025-03-28T19:37:05.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/16

My evaluation log file is missing.

The 2 other log files i’m given doesnt have my email inside it listed.

the Image id which is given in the MAIL is not present in my docker desktop, my project’s docker image is listed in docker desktop, which doesnot matches the image id given in the MAIL,

What was evaluated? How it was evaluated?

This is the id of the docker image that was evaluated: 0ade87d1bf07

My terminal shows 2 images as last, with respective image ids. I am not sure which one is the real, so please check with both the ids.

tds-project-1              latest    c854274f078d   5 weeks ago    1.38GB

ayush6871/fastapi-agent    latest    27e8375b0ab1   6 weeks ago    1.66GB

I am requesting to look into this case. I think there has been some mistake somewhere.

21f3001194

---

## Reply 15
**Author**: Adithya S
**Posted**: 2025-03-28T19:42:12.154Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/17

I have also built the image on Mac and facing the same issue

`exec format error`

It is running fine on my Macbook Pro M1

@carlton @Saransh_Saini @Jivraj

---

## Reply 16
**Author**: Ritwika Dutta 
**Posted**: 2025-03-28T19:44:32.573Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/18

Sir I have noticed a technical glitch for the docker issue, wherein I mistakenly uploaded the wrong docker image link so kindly please kindly re evaluate it.

---

## Reply 17
**Author**: Abhay Mehra
**Posted**: 2025-03-28T19:53:44.965Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/19

Sir I haven’t received any mail regarding this Project1 marks. @Jivraj  @carlton

---

## Reply 18
**Author**: JAHAR KUMAR PAUL
**Posted**: 2025-03-28T19:54:41.344Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/20

@carlton Sir , my Docker image is built on Macbook M1 which as you know uses ARM64 architecture . But evaluated with x86_64 which caused the exec format error due to cross platform compatibility issues . I am kindly requesting you to re-evaluate the project once again .

---

## Reply 19
**Author**: Harsh Jaiswal
**Posted**: 2025-03-28T20:04:57.116Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/21

This is the id of the docker image that was evaluated: d0f14a872042  , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

Please, look over it.

Regards,

Harsh Jaiswal

23f1001995

---

## Reply 20
**Author**: Arjun Dwarakesh Janarthanan
**Posted**: 2025-03-28T20:15:01.465Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/22

@carlton @Jivraj

I wanted to kindly request if you could review the bonus additional tasks, as they were not reflected in the evaluation, despite being mentioned in the instructions. Apart from that I understand and accept my score overall, especially since I had hardcoded the folder paths in my prompt for some questions, which I believe led to those failures.

**Bonus: Additional tasks**. We *may* pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.

Regards,

---

## Reply 21
**Author**: ABHIJEET KUMAR 
**Posted**: 2025-03-28T20:34:52.748Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/24

Would you mind reviewing the evaluation.log screenshot I have attached? I believe I may deserve marks for Task B6. @carlton, could you kindly take a look?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a console output or log, likely from a software testing or scraping process. It displays HTTP status codes, request information, and a comparison between expected and actual results. The output indicates a test case named "B6" has failed.

**2. Any text content visible:**

*   **HTTP 200 "Scraped data saved to ./data/b6.json"**: This indicates a successful HTTP request, and that scraped data has been saved to a file named "b6.json" within the "./data/" directory.
*   **HTTP Request: GET http://localhost:8052/read?path=/data/b6.json "HTTP/1.1 200 OK"**: This shows the details of an HTTP GET request made to a local server running on port 8052. The request is for a resource located at "/data/b6.json". The "HTTP/1.1 200 OK" confirms the request was successful.
*   **/data/b6.json**: This likely indicates the file being tested or validated.
*   **▲ EXPECTED:** This section shows the expected output. It's a list of strings: `['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']`
*   **! RESULT:** This section shows the actual result obtained. It's a JSON-like structure containing a single object with a key ".author". The value associated with ".author" is a list of strings, similar to the expected output.
*   **X B6 FAILED**: This indicates that the test case "B6" has failed.

**3. The context or purpose of what's displayed:**

The image shows a test case failure in a data scraping or processing pipeline. The system is scraping data and saving it to a JSON file. The test case "B6" is designed to verify that the scraped data matches a predefined expected output. The failure indicates a discrepancy between the expected and actual data.

**4. Technical details (code screenshot or technical diagram):**

*   The data is

---

## Reply 22
**Author**: Joseph Manoj Louis
**Posted**: 2025-03-28T20:53:25.507Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/25

I am also facing the same Please help my roll no is 21f3001750

---

## Reply 23
**Author**: Debjeet Singha
**Posted**: 2025-03-28T20:59:57.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/26

can you please take a look at this screenshot?

**Image: image**
Here's a detailed description of the image content:

**1. Overall Content:**

The image shows a log or output from a system that's testing the ability of a Large Language Model (LLM) to extract information from an image. Specifically, the task is to extract a credit card number from an image of a credit card. The log shows the steps taken, including HTTP requests, responses, and a comparison of the expected and actual results.

**2. UI Elements and Structure:**

The image is structured as a text-based log, with different sections indicating the progress and status of the task.  There are visual cues like colored circles (green, yellow, red) to indicate the status of different steps.

**3. Text Content and Meaning:**

*   **"A7 PASSED"**:  A green checkmark indicates that a test case or module "A7" has passed.
*   **"Running task: `/data/card.jpg` has a credit card. Pass the image to an LLM, extract the card number, and write it without spaces to `/data/cc-number.txt`"**: This describes the task being performed. It involves:
    *   Input: An image file `/data/card.jpg` containing a credit card.
    *   Processing: Using an LLM to extract the credit card number.
    *   Output: Writing the extracted number (without spaces) to a text file `/data/cc-number.txt`.
*   **"HTTP Request: POST http://localhost:8001/run?task=..."**: This shows an HTTP POST request sent to a local server (localhost:8001) to initiate the task. The `task` parameter contains a URL-encoded string that describes the task to be performed. The string includes instructions to pass the image to an LLM, extract the card number, and write it to the specified file.
*   **"HTTP 200 { "result": "The task of extracting the card number from the image and writing it to `/data/cc-number.txt` has been completed successfully." }"**: This is an HTTP 200 OK response, indicating that the POST request was successful. The "result" field confirms that the task was supposedly completed.
*   **"HTTP Request: GET http://localhost:8001

The task was done but the LLM made a mistake. I think this type of mistake was outside our control. @carlton

---

## Reply 24
**Author**: Arjun Dwarakesh Janarthanan
**Posted**: 2025-03-28T21:11:37.250Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/27

@carlton @Jivraj

Please correct me if I’m wrong, but I noticed that for tasks **B7**, **B8**, and **B10**, the evaluation log does not include any **`POST` or `GET` request traces**, unlike the other tasks which have clearly recorded request flows, generated code, and outputs. In these three cases, the log shows only the failure message without any indication that the script was executed or that the output file was read.

**Image: image**
Here's a detailed description of the image content:

**1. UI Elements and Content:**

The image appears to be a log or output from a system that's running a series of tasks, likely related to web scraping and image processing. It shows HTTP requests and responses, code snippets, and task status indicators.

**2. Text Content:**

*   **HTTP Requests and Responses:**
    *   `HTTP Request: POST http://localhost:8278/run?task=... "HTTP/1.1 200 OK"`:  A POST request to a local server on port 8278, likely triggering a task. The `task` parameter is a URL-encoded string describing the task. The server responds with a 200 OK status. The task involves scraping a website (`quotes.toscrape.com`) to extract author names and save them to a JSON file.
    *   `HTTP 200 { ... }`:  The body of the HTTP 200 response. It's a JSON object containing:
        *   `"status": "success"`
        *   `"task": "..."`: A description of the task being performed.
        *   `"generated_code": "..."`: A Python code snippet that performs the web scraping.
        *   `"output": ""`: An empty string, presumably where the output of the code would be stored.
    *   `HTTP Request: GET http://localhost:8278/read?path=/data/b6.json "HTTP/1.1 200 OK"`: A GET request to read the contents of the `/data/b6.json` file.

*   **Code Snippet (Python):**
    ```python
    import requests
    from bs4 import BeautifulSoup
    import json

    url = 'https://quotes.toscrape.com/'
    authors = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        author_elements = soup.find_all(class_='author')
        authors = [author.get_text() for author in author_elements]

        with open('/data/b6.json',

---

## Reply 25
**Author**: Md Ayan Arshad
**Posted**: 2025-03-28T21:30:36.014Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/28

Same issue with my. I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture (I can see this in the logs shared for x86_server_start.log)

---

## Reply 26
**Author**: Md anas alam
**Posted**: 2025-03-28T21:42:49.249Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/29

@carlton sir i have same issue.

I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture.

---

## Reply 27
**Author**: S Smriti
**Posted**: 2025-03-28T21:53:34.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/30

Sir even my evaluation log file is missing and I really don’t know what to do because during submission 8/10 of my A tasks were working. Please look into it sir. This is really going to affect my grade and I remember how hard I tried just to get my A tasks running. Please sir

Role nom 23f2000599

**Image: 1000472083**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a message, likely from a system evaluating a Docker image. It appears to be a report or feedback on the evaluation process. The message lists several files and their purpose, along with information about the evaluation environment. At the bottom of the screen are icons for email, comments, and video.

**2. Text Content:**

The message contains the following key information:

*   **Initial Error Message:** "evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us."
*   **Scoring:** "MISSING files will result in a score of 0."
*   **Responsiveness Requirement:** "Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it."
*   **Evaluation Environment:** "The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet."
*   **List of Files and Their Purpose:**
    1.  "Evaluation log file. MISSING This contains your performance report on your individual tasks."
    2.  "Docker log file. [Google Drive Link] This provides the technical performance of your container."
    3.  "Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests."
    4.  "Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism."
    5.  "Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks."
    6.  "Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications."
    7.  "Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only

---

## Reply 28
**Author**: Harsha
**Posted**: 2025-03-28T22:58:27.139Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/31

Hi @jivraj,

The contents of Expected and Result matches, but still test case’s failed.

Is there formatting check for answer , Isn’t prettier to be done ?

I see that your expected answer isn’t formatted using prettier , am i wrong ?

eg:

 :warning:  EXPECTED:

[{‘first_name’: ‘Kevin’, ‘last_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first_name’: ‘Kimberly’, ‘last_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first_name’: ‘Kathleen’, ‘last_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first_name’: ‘Jason’, ‘last_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first_name’: ‘Tami’, ‘last_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first_name’: ‘Brenda’, …

 :warning:  RESULT:

[

{

“first_name”: “Kevin”,

“last_name”: “Allen”,

“email”: “[tonya41@example.com](mailto:tonya41@example.com)”

},

{

“first_name”: “Kimberly”,

“last_name”: “Allison”,

“email”: “[vmendoza@example.com](mailto:vmendoza@example.com)”

},

{

“first_name”: “Kathleen”,

“last_name”: “Baldwin”,

“email”: “[amclean@example.com](mailto:amclean@example.com)”

},

{

“first_name”: “Jason”,

“last_name”: “Banks”,

“email”: “[sharptara@example.org](mailto:sharptara@example.org)”

},

{

“first_name”: “Tami”,

“last_name”: “Bass”,

“email”: “[kristy61@example.com](mailto:kristy61@example.com)”

},

{

“first_name”: “Brenda”,

“last_name”: “Bradford”,

“email”: “[amandakeith@example.com](mailto:amandakeith@example.com)”

},…

---

## Reply 29
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T01:10:47.753Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/32

*No content*

---

## Reply 30
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T01:13:24.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/33

Hi @all

We will identify why arm images created a problem and were run using x86 platform.

We will also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.

 23f3003302:

Hi @jivraj,

@23f3003302 output from your server’s response is correct, we will update our evaluation script.

 23f2004912:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays output from a program, likely a test or script, that involves scraping data and comparing it to an expected result. It shows HTTP status codes, a request URL, and a comparison between an "EXPECTED" list of strings and a "RESULT" JSON structure. The output indicates a failure in the comparison.

**2. Text Content:**

*   `HTTP 200 "Scraped data saved to ./data/b6.json"`: Indicates a successful HTTP response (200 OK) and that scraped data has been saved to a file named `b6.json` in the `./data/` directory.
*   `HTTP Request: GET http://localhost:8052/read?path=/data/b6.json "HTTP/1.1 200 OK"`: Shows an HTTP GET request to a local server at `localhost:8052`. The request is for a resource at the path `/data/b6.json`, and the server responded with a 200 OK status.
*   `/data/b6.json`: Indicates the file being processed.
*   `▲ EXPECTED:`:  Marks the beginning of the expected data.
    *   `['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']`: This is the expected list of author names.
*   `! RESULT:`: Marks the beginning of the actual result.
    *   The JSON structure shows a list containing a single object. This object has a key named ".author" whose value is a list of strings. The strings are author names: "Albert Einstein", "J.K. Rowling", "Albert Einstein", "Jane Austen", "Marilyn Monroe", "Albert Einstein", "Andr\u00e9 Gide", "Thomas A. Edison", "Eleanor Roosevelt", "Steve Martin".
*   `X B6 FAILED`: Indicates that a test or process named "B6" has failed.

**3. Context and Purpose:**

The image shows the output of a test or validation process. The program likely scraped

@23f2004912 We will discuss internally if we can do something about it, but I can’t assure if you will get marks for it, since output from your server is a bit different.

 23f1001611:

**Image: image**
Here's a detailed description of the image content:

**1. UI Elements and Content:**

*   The image appears to be a log or output from a system running automated tasks or tests.
*   It shows HTTP requests and responses, code snippets (likely Python), and task status indicators.
*   There are indicators for "PASSED", "Running task", and "FAILED" tasks.

**2. Text Content:**

*   **HTTP Requests and Responses:**
    *   `HTTP Request: POST http://localhost:8278/run?task=... "HTTP/1.1 200 OK"`:  A POST request to a local server on port 8278, likely to initiate a task. The `task` parameter is a URL-encoded string describing the task.
    *   `HTTP 200 { ... }`:  A successful HTTP response (status code 200) containing a JSON payload.
    *   `HTTP Request: GET http://localhost:8278/read?path=/data/b6.json "HTTP/1.1 200 OK"`: A GET request to read the contents of a JSON file.
*   **JSON Payload (within the HTTP 200 response):**
    *   `"status": "success"`: Indicates the overall status of the request.
    *   `"task": "https://quotes.toscrape.com/ has quotes from famous people.\nThe author class has the quote author's name. \nExtract and save all authors from the first page, in order, to /data/b6.json as an array of strings.\nE.g. `[\"Douglas Adams\", \"J.K. Rowling\", ...] `\n"`: A description of the task being performed. It involves scraping author names from a website and saving them to a JSON file.
    *   `"generated_code": "import requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://quotes.toscrape.com/'\nauthors = []\n\ntry:\n response = requests.get(url)\n response.raise_for_status()\n soup = BeautifulSoup(response.text, 'html.parser')\n author_elements = soup.find

image2003×745 95 KB

@23f1001611 we will look into it

 HarshJaiswal:

This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

@HarshJaiswal I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information  `harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB `

@AYUSH_SINGH

 AYUSH_SINGH:

ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB

This was submitted to us through google form, for project1.

 AYUSH_SINGH:

The 2 other log files i’m given doesnt have my email inside it listed.

We are aware about it results for 12 students are not generated, we will look into it, and see what caused those 12 images not to run.

@22f1000703

 22f1000703:

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly.

It would have run at your end but it was supposed to run at anywhere, after dockerising it didn’t run, reason is taskA module was not found.

---

## Reply 31
**Author**: Sahana S
**Posted**: 2025-03-29T02:30:50.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/34

Same issue for me sir. When I evaluated my file using evaluate.py my 9 cases out of the 10 in Task A was passed but the email I received shows that my evaluation log file is missing. I don’t understand why does it show like that. Please do check and help me out sir.

Reg no. 24f1002633

---

## Reply 32
**Author**: Yogesh
**Posted**: 2025-03-29T02:37:27.452Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/35

I suspect there is something wrong with how the evaluation has been done. Although A1 task succeeded, all of my A tasks failed.

---

## Reply 33
**Author**: Lovepreet Singh
**Posted**: 2025-03-29T02:45:35.166Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/36

I have checked my log file in all of the cases where a file is required it says file not found or directory not found error in the code, how can I check /data folder was provided to the program?

@carlton

---

## Reply 34
**Author**: Pritul Santosh Raut 
**Posted**: 2025-03-29T03:17:56.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/37

@Jivraj , @carlton

It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the `os` library. As a result, all file evaluations returned errors such as “can’t read the file.”

I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.

**Image: Screenshot (177)**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a web browser window displaying the content of a log file. The log file appears to be related to the execution of several tasks, likely within a testing or evaluation environment. The log entries consist of HTTP requests and responses, error messages, and task descriptions.

**2. Text Content Visible:**

Here's a breakdown of the key text content:

*   **Log File Name:** `24f1002555@ds.study.iitm.ac.in_evaluation.log`
*   **HTTP Requests and Responses:**
    *   `HTTP Request: POST http://localhost:8138/run?...` (Several variations of this, with different parameters)
    *   `HTTP Request: GET http://localhost:8138/read?path=/data/mail-sender.txt "HTTP/1.1 404 Not Found"`
    *   `HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"`
    *   `HTTP 500 { "detail": "500: [Errno 2] No such file or directory: '/app./data/mail.txt'"`
*   **Error Messages:**
    *   `A7 failed: Cannot read /data/mail-sender.txt`
    *   `X A7 FAILED`
    *   `A8 failed: Cannot read /data/cc-number.txt`
    *   `X A8 FAILED`
*   **Task Descriptions:**
    *   `Running task: \`/data/card.jpg\` has a credit card. Pass the image to an LLM, extract the card number, and write it without spaces to \`/data/cc-number.txt\``
    *   `Running task: \`/data/comments.txt contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to \`/data/comments-similar.txt\`, one per line`

**3. Context and Purpose:**

The log file seems to be documenting the execution of a series of tasks that

**Image: Screenshot (179)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window displaying the source code of a Python file named `app.py` on GitHub. The file is part of a project called "LLM-based-Automation-Agent." The browser window also has a sidebar on the left showing the project's file structure and a sidebar on the right displaying a list of symbols (functions, constants) defined in the `app.py` file.

**2. Text Content:**

*   **Title:** "LLM-based-Automation-Agent / app.py"
*   **File Structure (left sidebar):**
    *   Dockerfile
    *   LICENSE
    *   README.md
    *   app.py (selected)
    *   package.json
    *   pyproject.toml
    *   uv.lock
*   **Code (center):**
    *   `allow_headers=["*"],`
    *   `@app.get("/")`
    *   `async def start():`
    *   `return "You are at the entrance URL. Just write /run or /read to perform the task."`
    *   `@app.get("/read")`
    *   `async def read_file(path: str):`
    *   `#path=os.path.join(os.getcwd(), path)`
    *   `print(path)`
    *   `if not path:`
    *   `raise HTTPException(status_code=400, detail="File path is required")`
    *   `if not os.path.exists(path):`
    *   `raise HTTPException(status_code=404, detail="File not found")`
    *   `if not is_path_in_data_folder(path):`
    *   `return {"status": "error", "message": "File path is not in the data folder."}`
    *   `try:`
    *   `with open(path, 'r') as file:`
    *   `content = file.read()`
    *   `return PlainTextResponse(content, status_code=200)`
    *   `except Exception

---

## Reply 35
**Author**: Naman S. 
**Posted**: 2025-03-29T03:18:32.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/38

Same here. I also dis not recieve any mail sir.

---

## Reply 36
**Author**: Maulik Dang
**Posted**: 2025-03-29T04:34:28.653Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/40

I noticed that my Docker image was run on an x86_64 architecture (as indicated by my email in the shared logs), whereas I originally built it on my Mac (ARM architecture). Due to this mismatch, the image failed to run properly and resulted in an exec format error.

Since there was no prior mention of the architecture on which our images would be evaluated, I request that my evaluation be conducted again on the appropriate machine. Please help as after doing it correctly getting 0 marks because of such an error feels wrong

---

## Reply 37
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T04:39:03.187Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/41

@23f2001975 we had to rely on docker telling us whether an image was arm or x86. So thats why we just did what docker software told us. If it classified an image as arm then we ran it on arm. If it did not then we ran it on x86. Thats why we need students to look through the logs and identify issues so that we can make sure you get the correct evaluation.

If students notify us their image is actually arm based, then we will run it on arm. So dont worry, just inform us of any discrepancy as well as bugs. Our evaluation might not be perfect, there may be bugs. If students can precisely create bug reports then we can take that into consideration when evaluating students as well. The benefit being you might get extra marks because of the bug fix.

We have a script that looks at this discourse post each day and tells us who requires a fresh evaluation. So we will check your image on arm.

Kind regards

---

## Reply 38
**Author**: Bhavin Biju
**Posted**: 2025-03-29T04:49:26.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/42

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a Python traceback, which is an error report showing the sequence of function calls that led to an exception.

**2. Text Content:**

The text content includes:

*   "Traceback (most recent call last):" - This indicates the start of the traceback.
*   "File "/app/app.py", line 30, in " - This line indicates that the error occurred in the file `/app/app.py` on line 30, within the top-level module scope.
*   "AIPROXY\_TOKEN = os.environ['AIRPROXY\_TOKEN']" - This is the line of code that caused the error. It attempts to retrieve the value of the environment variable named 'AIRPROXY\_TOKEN' using `os.environ`.
*   A line of tildes (~) and carets (^) below the code line, likely indicating the location of the error.
*   "File "", line 716, in \_\_getitem\_\_" - This indicates that the error occurred within the `__getitem__` method of the `os` module (specifically, a frozen version of the `os` module).
*   "KeyError: 'AIRPROXY\_TOKEN'" - This is the specific error that occurred. It means that the environment variable 'AIRPROXY\_TOKEN' was not found in the `os.environ` dictionary.

**3. Context/Purpose:**

The traceback indicates that the Python program `/app/app.py` is trying to access an environment variable named 'AIRPROXY\_TOKEN'. However, this environment variable is not set, leading to a `KeyError`. The purpose of the traceback is to help developers diagnose and fix this error.

**4. Technical Details:**

*   **`os.environ`:** This is a dictionary-like object in Python that provides access to environment variables.
*   **`KeyError`:** This exception is raised when you try to access a key that doesn't exist in a dictionary. In this case, the key 'AIRPROXY\_TOKEN' is not present in the `os.environ` dictionary.
*   **Frozen OS:** The "" part indicates that the `os` module is part of the

This is a screenshot of my docker log file. This works if you pass the actual value of the airproxy token at the command line while pulling the docker image. Please do look into this as I’ve put a lot of effort into this.

Thank you

Regards,

23f3002677

---

## Reply 39
**Author**: Rohit Garg
**Posted**: 2025-03-29T04:49:39.987Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/43

@cartlon Same issue.

My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error` and **Evaluation log file** is MISSING.

Can you please rerun the image on ARM based

---

## Reply 40
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T05:00:23.762Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/44

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a Python traceback, which is an error report showing the sequence of function calls that led to an exception. It's a common debugging tool.

**2. Text Content:**

The text content includes:

*   "Traceback (most recent call last):" - This indicates the start of the traceback.
*   "File "/app/app.py", line 30, in " - This line shows that the error occurred in the file `/app/app.py` on line 30, within the top-level module.
*   "AIPROXY\_TOKEN = os.environ\['AIRPROXY\_TOKEN'\]" - This is the line of code that caused the error. It attempts to retrieve an environment variable named 'AIRPROXY\_TOKEN' using `os.environ`.
*   "File "", line 716, in \_\_getitem\_\_" - This indicates the error occurred within the `os` module's internal `__getitem__` method.
*   "KeyError: 'AIRPROXY\_TOKEN'" - This is the specific error message, indicating that the environment variable 'AIRPROXY\_TOKEN' was not found.

**3. Context/Purpose:**

The traceback indicates that the Python program is trying to access an environment variable named 'AIRPROXY\_TOKEN', but this variable is not set in the environment where the program is running. This is a common issue when deploying applications that rely on environment variables for configuration.

**4. Technical Details:**

*   **`os.environ`:** This is a Python dictionary-like object that provides access to environment variables.
*   **`KeyError`:** This exception is raised when you try to access a key that doesn't exist in a dictionary. In this case, the key is the environment variable name.
*   The red box highlights the environment variable name that the code is trying to access.
*   The tildes and carets are pointing to the line of code that caused the error.

In summary, the image shows a Python program failing because it cannot find a required environment variable. This suggests a configuration issue where the environment variable needs to be set before running the program.

Kind regards

---

## Reply 41
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T05:03:26.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/45

You have to identify the exact bug for your claim to be considered. Thats why we have provided you with the scripts and the logs. You might get lots of marks. Its in your interest to identify the bug.

Kind regards

---

## Reply 42
**Author**: S Smriti
**Posted**: 2025-03-29T05:06:09.078Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/46

@carlton @Jivraj what do I do sir am seriously clueless and heartbroken rn pls help atleast for A tasks we should get it

---

## Reply 43
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T05:08:12.916Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/47

We demoed in the live session the complete process of how to dockerise your project so that it can be run anywhere. Running on your local machine is not a sufficient criteria for passing the evaluation. It is absolutely vital for students to understand deployment. This is a critical skill for anyone who is serious about working in this field.

Also just check if yours is an arm based image or x86. Sometimes that makes a difference. For us there is no way to know other than docker software telling us. As it turns out several students had an arm based image but docker did not tell us that. So we will re run those.

If yours has been run on the wrong emulation then we will re run.

Kind regards

---

## Reply 44
**Author**: Avnish Jajodia
**Posted**: 2025-03-29T05:08:33.580Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/48

@carlton

I encountered an HTTP 500 error with the following detail:

{
"detail": "'choices'"
}

This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY_TOKEN. Could you please look into this?

Additionally, my solution is very similar to the one shared by the System Commands team in their email.

**Image: Screenshot 2025-03-29 103327**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a series of log messages or output from a system, likely related to running tasks and making HTTP requests. It appears to be a debugging or error reporting output. The messages indicate attempts to install a tool called "uv," run a script, and format a file. There are also indications of HTTP requests and server errors.

**2. Text Content:**

*   **"Running task: Install `uv` (if required) and run the script `https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466052b66ae/datagen.py` with `22f3001777@ds.study.iitm.ac.in` as the only argument"**: This indicates the start of a task to install "uv" and run a Python script named "datagen.py" from a GitHub Gist. The script is being run with an email address as an argument.
*   **"HTTP Request: POST http://localhost:8180/run?task=..."**: This shows an HTTP POST request being made to a local server at port 8180. The "task" parameter in the URL is heavily URL-encoded, but it seems to be related to the "Install uv" task mentioned earlier, including the URL of the datagen.py script and the email argument.
*   **"HTTP/1.1 500 Internal Server Error"**: This indicates that the POST request resulted in a 500 Internal Server Error.
*   **"HTTP 500 { "detail": ""choices'" }"**: This is the body of the 500 error response, indicating a server-side error. The "detail" field contains the string "choices".
*   **"HTTP Request: GET http://localhost:8180/read?path=/data/format.md "HTTP/1.1 404 Not Found""**: This shows an HTTP

---

## Reply 45
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T05:12:07.235Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/49

We have given you the evaluation scripts. Identify where exactly you believe the bug is.

Just guesses is not going to get you extra marks. You have to give us something specific.

Kind regards

---

## Reply 46
**Author**: Ritwika Dutta 
**Posted**: 2025-03-29T05:18:39.537Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/50

@Jivraj sir please kindly look into it. Please re-evaluate my image, everything was working fine it is an issue with the docker image. Please re-evaluate it sir and please guide me as what to do

---

## Reply 47
**Author**: Sakthivel S
**Posted**: 2025-03-29T05:24:12.600Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/51

I encountered the same issue with `evaluate.py`. However, since you previously advised against coding strictly with `evaluate.py`, I didn’t pursue it further. Now, I’m concerned—how is this a mistake?

**Image: Screenshot (56)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays text output, likely from a log file or a test result. It shows a comparison between an "EXPECTED" outcome and an "RESULT" outcome. The text appears to be a series of sentences, possibly generated randomly or from a specific algorithm. At the end, it indicates that the test "A5" has "FAILED".

**2. Any text content visible:**

*   **/data/logs-latest.txt:** This is the path to the file from which the content is being displayed.
*   **▲ EXPECTED:** This section contains the expected output. The text is a series of sentences that seem somewhat nonsensical when read together.
*   **▲ RESULT:** This section contains the actual output. The text is identical to the "EXPECTED" section.
*   **X A5 FAILED:** This indicates that a test case named "A5" has failed.

The sentences in both the "EXPECTED" and "RESULT" sections include phrases like:

*   "Clearly drug health quickly field everyone majority as."
*   "Investment direction themselves suddenly."
*   "West son we reflect."
*   "Size quite they new assume manager."
*   "Official one draw various between time box goal."
*   "Wonder appear happen themselves."
*   "Include want key draw late list."
*   "Hair hit rule employee."
*   "Option guess fish difficult our add."
*   "Bill practice main discover."
*   "Focus couple ball through network should leave."
*   "Within PM race former."
*   "Pressure property piece treat thus interesting."
*   "Eight so affect."
*   "Different indicate pretty most pay leg today."
*   "Administration partner performance off get check."
*   "Clear your upon sign. Type per task win."
*   "Consumer beyond economy easy friend piece increase. With city write."
*   "Matter statement last trial television. Not black owner most million answer. Toward contain girl member."

**3. The context or purpose of what's displayed:**

The image shows a test failure. The "EXPECTED" and "RESULT" sections are identical, which suggests that the test was designed to ensure the output matches a specific, predefined string.

---

## Reply 48
**Author**: Yogesh
**Posted**: 2025-03-29T05:30:05.991Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/52

Please provide more time for this. Right now, we are also busy with the second project. There are other courses as well.

---

## Reply 49
**Author**: Mayank Singh
**Posted**: 2025-03-29T05:46:07.918Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/53

yaa same issue i am also facing ,

and this LLM thing is very new for us , and we tried our best to complete. , but because of local machine issue , or anything , people end up getting 0 marks , or 4-5 marks , ..

As a lot of students are getting 0 , so please give some bonus , or some marking for there efforts ,

TDS dont have quiz , ,and getting 0 in project will decrease our CGPA too .

please think for it sir @carlton

---

## Reply 50
**Author**: ROHIT B LAKSHMANAN
**Posted**: 2025-03-29T05:47:03.197Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/54

This is the id of the docker image that was evaluated: 468630ef32b8

I believe this is not my docker ID that was submitted, my docker ID is “bd2d0e570ec6”:

proof:

REPOSITORY                           TAG          DIGEST                                                                    IMAGE ID       CREATED        SIZE

rohit23f1001156/project1_tds         v3           sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542   bd2d0e570ec6   5 weeks ago    816MB

Please, look over it.

Also, in my docker log file, it is showing the error as:

**Image: Screenshot 2025-03-29 at 11.10.03 AM**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a console output or log from a running application. It includes informational messages, a JSON response, and error tracebacks. The application appears to be using a Large Language Model (LLM) to perform a task.

**2. Any text content visible:**

*   **Informational Messages:**
    *   "Started server process [1]"
    *   "Waiting for application startup."
    *   "Application startup complete."
    *   "Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)"
    *   "Inside run task with task: Say Hello Carlton"
    *   "Inside execute\_function\_call with function\_call: {'name': 'extract\_specific\_text\_using\_llm', 'arguments': '{"input\_file": "system\_input.txt", "output\_file": "output.txt", "task": "Say Hello Carlton"}'}"
    *   "IN HERE True"
    *   "172.17.0.1:33072 - "POST /run?task=Say+Hello+Carlton HTTP/1.1" 500 Internal Server Error"
*   **JSON Response:** A large JSON object containing information about a chat completion, including choices, messages, tool calls, usage, and cost.  It indicates the use of the 'gpt-4o-mini-2024-07-18' model.
*   **Error Messages:**
    *   "Exception in ASGI application"
    *   "FileNotFoundError: \[Errno 2] No such file or directory: 'system\_input.txt'"
    *   "fastapi.exceptions.HTTPException: 500: Error executing function in execute\_function\_call: \[Errno 2] No such file or directory: 'system\_input.txt'"
    *   "'costError': 'crypto.createHash is not a function'"
*   **Code Snippets (from Tracebacks):**
    *   "File "/app/main.py", line 121, in execute\_function\_call"
    *   "File

what is the reason for this?

It was running properly before, please help.

Regards,

Rohit

23f1001156

@Jivraj @carlton

---

## Reply 51
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T05:51:25.513Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/55

@ROHIT_B_LAKSHMANAN

This is **exactly** what **you** submitted. We will ONLY consider this as valid.

2/16/2025 9:30:05	23f1001156@ds.study.iitm.ac.in	[GitHub - Rohit23f1001156/project1_tds](https://github.com/Rohit23f1001156/project1_tds)	rohit23f1001156/project1_tds

---

## Reply 52
**Author**: ROHIT B LAKSHMANAN
**Posted**: 2025-03-29T06:08:44.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/56

Yes, I agree.

So, did my docker ID change when I submitted?

I am sorry sir, but I did not make any changes after submitting the project, so I guess my Docker ID should remain the same as before, if I am not mistaken. I kindly request you to check just once more please, as I really don’t know where I have went wrong.

Jivraj Sir had checked liked this for another student, so I just wanted to confirm the same for me.

*" I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information `harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB `"*

Also sir, could you please tell me why the error as shown in my previous message is being shown? and if there is no chance of it getting correct.

thanks

---

## Reply 53
**Author**: Shashannk
**Posted**: 2025-03-29T06:23:39.304Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/57

Hi @carlton !

I am reaching out with deep frustration and concern regarding the evaluation of my project. I have worked tirelessly on this for almost two weeks, dedicating day and night to ensure that the tasks were executed correctly. During my own testing, I was able to get at least 7 out of 10 A tasks working as expected. However, after the evaluation, I was informed that none of the tasks were executed properly, which was quite shocking!

Given the effort and time I have put in, I kindly request you to review my project once more. I am more than willing to demonstrate the functionality in real time to clarify any issues or misunderstandings. Please let me know if there is a possibility to discuss this further, as I genuinely believe my work deserves another review.

---

## Reply 54
**Author**: ABHIJEET KUMAR 
**Posted**: 2025-03-29T06:26:10.621Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/58

@carlton,

Jivraj said, *“We will discuss internally if we can do something about it.”* I understand this well. The output from my server is slightly different, but it still achieves over 95% accuracy. Please do consider it.

---

## Reply 55
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T06:27:03.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/59

Hi @Pritul_raut

No, we won’t reevaluating it.

---

## Reply 56
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T06:39:00.764Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/60

Hi @22f2001389

  File "/app/app.py", line 4, in <module>
    from tasksA import *
ModuleNotFoundError: No module named 'tasksA'

The error occurs because Python cannot find the `tasksA` module. This is due to the file not existing, not being in the correct directory.

Kind regards

---

## Reply 57
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T06:48:30.446Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/61

ROHIT_B_LAKSHMANAN:

This is the id of the docker image that was evaluated: 468630ef32b8

We evaluated you on correct file

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, likely a Linux or Unix-based system, displaying the output of Docker commands. It shows the process of pulling a Docker image and then listing Docker images, filtering for a specific image name.

**2. Any text content visible:**

*   **Prompt:** `user_22f3002542_ds_study_iitm_ac_@tds-course-temp-bq:~$` (This is the command prompt, indicating the current user, hostname, and directory.)
*   **Docker pull command:** `docker pull --platform arm64 rohit23f1001156/project1_tds:v3` (This command instructs Docker to download the image named `rohit23f1001156/project1_tds` with the tag `v3` for the `arm64` platform.)
*   **Pulling status:**
    *   `v3: Pulling from rohit23f1001156/project1_tds`
    *   `Digest: sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542` (This is the SHA256 hash of the image.)
    *   `Status: Downloaded newer image for rohit23f1001156/project1_tds:v3`
    *   `docker.io/rohit23f1001156/project1_tds:v3`
*   **Docker images command:** `docker images | grep "rohit23f1001156/project1_tds"` (This command lists all Docker images and pipes the output to `grep`, which filters the results to show only lines containing the specified image name.)
*   **Image listing output:** `rohit23f1001156/project1_tds v3 468630

 ROHIT_B_LAKSHMANAN:

what is the reason for this?

It was running properly before, please help.

Try running docker container after pulling, check if evaluate.py is able to do it’s job.

If you feel there is some issues from our side, we have provided with scirpts we used. You can create a pull request to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)

---

## Reply 58
**Author**: Aditya Shankar Naidu
**Posted**: 2025-03-29T06:53:21.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/62

I’m facing “exec /usr/local/bin/uvicorn: exec format error” ,  My roll number is 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. @Jivraj @carlton .

---

## Reply 59
**Author**: Srijan Dutt
**Posted**: 2025-03-29T07:00:00.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/63

I cannot understand why the project marks are marked zero for me ? i have used the same code as usual but the results are not same ?

---

## Reply 60
**Author**: Ritwika Dutta 
**Posted**: 2025-03-29T07:01:00.632Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/64

No no sir, I can send you an SS of my code, it’s very much there sir, the tasksA file, i really don’t know why this happened.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a Visual Studio Code (VS Code) window. The left side displays the file explorer, showing a list of files and folders in a project. The right side shows a code editor area and a "PROBLEMS" panel. The bottom of the screen shows the Windows taskbar.

**2. Text Content:**

*   **File Explorer:**
    *   `pip.exe`
    *   `pip3.13.exe`
    *   `pip3.exe`
    *   `python.exe`
    *   `pythonw.exe`
    *   `.gitignore`
    *   `pyvenv.cfg`
    *   `.dockerignore`
    *   `.env`
    *   `app.py` (highlighted)
    *   `datagen.py`
    *   `docker-compose.deb...`
    *   `docker-compose.yml`
    *   `Dockerfile`
    *   `evaluate.py`
    *   `requirements.txt`
    *   `tasksA.py`
    *   `OUTLINE`
    *   `TIMELINE`
*   **Code Editor:**
    *   Line numbers 17-22
    *   A closing parenthesis on line 20
*   **Problems Panel:**
    *   `PROBLEMS`
    *   `C:\Users\Ri`
    *   `(tds_roe) C`
    *   `History`
*   **Terminal:**
    *   `O PS C:\Users`
*   **Status Bar:**
    *   "Python extension loading..."
*   **Taskbar:**
    *   "Type here to search"

**3. Context and Purpose:**

The image shows a developer working on a Python project in VS Code. The file explorer indicates that the project likely involves Docker (due to the presence of `Dockerfile`, `docker-compose.yml`, and `.dockerignore`). The highlighted `app.py` suggests that the developer is currently working on the main application file. The "PROBLEMS" panel indicates that there might be some issues or warnings in the code that need to be

---

## Reply 61
**Author**: Rahul 
**Posted**: 2025-03-29T07:12:44.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/65

Same issue with me also

---

## Reply 62
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T07:15:09.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/66

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.

Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.

FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

---

## Reply 63
**Author**: Mohd Atif
**Posted**: 2025-03-29T07:18:38.983Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/67

@carlton good afternoon sir,

I completed my project 1 and submitted it as instructed. But the result show that evaluate file missing. I did everything right but don’t know how this as the result come. I also had evaluation file in my project too. Please go through things again as this is very unfair for those who took 2 weeks to do this project. My roll no. is 22f3001664. I hope I will get marks, of not full then should be 10/20.

Thank you sir

---

## Reply 64
**Author**: Ritwika Dutta 
**Posted**: 2025-03-29T07:20:45.877Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/68

What to do now sir ? Is there no way to fix this now ? I can change the docker file and overwrite the docker image if you allow me to do so.

---

## Reply 65
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T07:34:25.276Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/69

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a meme featuring a photograph of a stadium under construction. A large section of the stadium's seating area is covered in bright red material and surrounded by scaffolding. The stadium itself is partially complete, with a green field visible inside. In the background, there's a cityscape with various buildings.

**2. Any text content visible:**

The image contains the following text, formatted as a meme:

*   **Top:** "WHEN YOU CANNOT REFACTOR THE CODE"
*   **Bottom:** "BECAUSE OF A TIGHT DEADLINE"
*   **Bottom Left:** "imgflip.com"

**3. The context or purpose of what's displayed:**

The meme is a humorous comparison between the state of the stadium construction and the situation where software developers are unable to properly refactor (improve) code due to time constraints. The unfinished, somewhat chaotic appearance of the stadium under construction is meant to represent the state of poorly maintained or rushed code. The text "imgflip.com" indicates the meme was likely created using the Imgflip meme generator.

**4. Technical details if it's a code screenshot or technical diagram:**

This image is not a code screenshot or technical diagram. It's a photograph used in a meme. Therefore, there are no technical details to analyze in that sense.

---

## Reply 66
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T07:42:52.795Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/70

Figure out the problem in our script and do a pull request to it, we will fix it if it’s a valid bug.

 Jivraj:

Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

---

## Reply 67
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T07:51:29.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/71

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.

Line number 81 of your app.py

`subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)`

which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.

---

## Reply 68
**Author**: Khushi Shah
**Posted**: 2025-03-29T07:56:48.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/72

@Jivraj @carlton

I’m writing here to express my concerns regarding the evaluation of my TDS Project-1. Also, kindly pardon me for the long message.

I have received a MISSING statement in my evaluation log file in the project 1 score mail that was released yesterday.

These are the detailed point wise concerns :

I at the earlier stages, found the Tools in Data Science course relatively challenging as it’s just my second term in Diploma and I have only completed BDM and MLF Course till now. Hence, I decided to drop the course in February, however when I could still view the course on the portal, and raised concerns, the assistance provided to me was very grim and low, and after numerous follow-ups, I was finally informed 2½ weeks after dropping my course, that my drop application was received in draft and they would not proceed with it, and I had to continue my course.

By this time, I had already missed 2 graded assignment deadlines and the project 1 submission was due in the coming 2 days. Not losing my spirit and with whatever I could learn and implement I completed the TDS project 1. However, I accidentally attached the wrong docker image link, and I also raised the issue, but didn’t receive a reply.

I understand that it was a fault on my part, but evaluating a student as 0, even though all their functions are right, and they give the required answers, is also wrong since we are expected to provide correct answers, and learn to build the docker image, however, there can be occurrences where a student might make a small mistake like uploading the wrong link, and they must be given a small chance to reprimand them.

I also didn’t receive the mail from the TDS Team which they issued for students whose docker image or GitHub link was erroneous, and hence I realised after the deadline that I had uploaded the wrong docker image link.

I have rechecked all my function, and they are all correct, giving a 0 to a student, who worked hard within the limited available time(given the student had dropped the course but the course team didn’t process it) is very unfair.

Kindly provide me a way to either re-upload my project-1 Docker image link, or ask them to provide me marks on the basis of the functions and codes written, whichever is feasible, atleast to encourage the efforts and time put into the project with little knowledge.

I hope you would look into my plight, and take necessary measures.

Thanks and Regards

---

## Reply 69
**Author**: ParamanandaSamantara
**Posted**: 2025-03-29T07:57:00.535Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/73

I haven’t received any mails regarding the tds project 1 please look into my concern

@carlton @Jivraj @s.anand

---

## Reply 70
**Author**: Ritwika Dutta 
**Posted**: 2025-03-29T08:13:58.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/74

Sir please consider a re-evaluation for me, please :’)

---

## Reply 71
**Author**: Hisham Kadambot
**Posted**: 2025-03-29T08:18:20.144Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/75

Please consider my situation a peer whos results were exactly same as mine has received 9, then how could I get 1 . 23f1002630 this is my role number please reconsider

@carlton @Jivraj

---

## Reply 72
**Author**: Jayesh Bansal
**Posted**: 2025-03-29T08:20:13.355Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/76

Few Students including me have not received any mails regarding TDS Project 1. We don’t even know what went wrong or why we didn’t received. Initially I thought that it can be due to some sending error and i will receive little late but even after 14hrs we have not received anything from the team. How are we supposed to check log and see our mistakes when we didn’t even received marks and logs. I request to check into it and provide us our marks and logs.

Thank You.

@carlton @Jivraj @s.anand

---

## Reply 73
**Author**: Achuthan M
**Posted**: 2025-03-29T08:41:38.347Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/77

I had built the project well on my Mac OS machine. I am very disappointed with the scores. How do i make amends for revaluation as I feel the code ran well for all tasks on my machine. Please give written steps for revaluation.

---

## Reply 74
**Author**: Raunak Narwal
**Posted**: 2025-03-29T08:42:03.850Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/78

Its saying that my evaluation log file is missing, i submitted everything properly. It also says no module named TasksA is found while i got 9/10 marks in the tasksA evaluation script. Kindly look into this, i worked really harrd for this project, @carlton @Jivraj

---

## Reply 75
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T08:43:25.935Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/79

@22f3000935 [Page Not Found | Docker Hub](https://hub.docker.com/r/pscoeds24/dataworks-agent)

you submitted this docker url through form response for project1, this repo doesn’t exists on docker.

---

## Reply 76
**Author**: S Smriti
**Posted**: 2025-03-29T08:44:55.816Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/80

@Jivraj sir please tell me whats the issue am very confused and worried

---

## Reply 77
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T08:45:12.085Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/81

We are aware about such mistakes and we are looking into it. We will reevaluate those images.

---

## Reply 78
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T08:46:19.633Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/82

If evaluation file is missing for anyone, we will reevaluate it once more and send same through email.

Can you fill form for architecture detection.

---

## Reply 79
**Author**: Aditya Shankar Naidu
**Posted**: 2025-03-29T08:47:47.413Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/84

Also please , kindly share evaluation log file after execution

---

## Reply 80
**Author**: Raunak Narwal
**Posted**: 2025-03-29T08:48:29.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/85

I did upload all the necessary files but it stil says tasksA is missing, and i am getting zero marks. Kindly help out @carlton @Jivraj

**Image: Screenshot 2025-03-29 141448**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a file directory structure within a web-based interface, likely a code repository like GitHub or GitLab. It displays a list of files and folders within a specific directory. The UI elements include:

*   A breadcrumb navigation showing the path "TDS\_Project\_1 / App /".
*   An "Add file" button with a dropdown arrow, and a three-dot menu.
*   A section displaying the latest commit information, including the author ("RaunakNarwal735"), the commit message ("Update Dockerfile"), the commit hash ("c07b746"), and the date ("last month").
*   A table-like structure with columns for "Name", "Last commit message", and "Last commit date".
*   A list of files and folders, each with an icon indicating its type (folder or file).

**2. Any text content visible:**

*   **Path:** "TDS\_Project\_1 / App /"
*   **Commit Info:** "RaunakNarwal735", "Update Dockerfile", "c07b746", "last month", "History"
*   **Table Headers:** "Name", "Last commit message", "Last commit date"
*   **Files/Folders:** "..", ".env", "Dockerfile", "app.py", "readme.md", "tasksA.py", "tasksB.py"
*   **Commit Messages:** "Add files via upload", "Update Dockerfile", "Create readme.md"
*   **Dates:** "last month" (repeated for each file)
*   **Buttons:** "Add file"

**3. The context or purpose of what's displayed:**

The image shows a view of a project's file structure within a version control system. The purpose is to allow users to browse the files, see the history of changes (commits), and potentially add new files. It's a typical interface for managing code projects online.

**4. Technical details (based on the content):**

*   The project is named "TDS\_Project\_1".
*   The current directory being viewed is "App" within the project.
*   The project contains a Dockerfile, suggesting it'

---

## Reply 81
**Author**: S Smriti
**Posted**: 2025-03-29T08:49:55.974Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/86

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely from a container registry or similar platform, displaying information about a specific image tag. It includes details such as the tag name, last push date, digest, and operating system/architecture.

**2. Text content visible:**

*   **TAG**
*   **latest** (with a green dot next to it, indicating it's the current or active tag)
*   **Last pushed about 1 month by** `23f2000599` (the `23f2000599` is a hyperlink)
*   **Digest**
*   `5217284cc507` (a hyperlink)
*   **OS/ARCH**
*   `linux/amd64`

**3. Context or purpose of what's displayed:**

The purpose is to provide information about a container image tag. This information is useful for understanding the image's version, when it was last updated, its unique identifier (digest), and the platform it's designed to run on. This is typical information found in container registries like Docker Hub, GitHub Container Registry, or similar platforms.

**4. Technical details:**

*   **Tag:** "latest" is a common tag used to represent the most recent version of an image.
*   **Digest:** The digest (`5217284cc507`) is a cryptographic hash of the image's content. It uniquely identifies the image and ensures its integrity.
*   **OS/ARCH:** `linux/amd64` indicates that the image is designed to run on a Linux operating system with an AMD64 (x86-64) architecture.
*   The `23f2000599` is likely a user ID or commit hash, and the fact that it's a hyperlink suggests it leads to more information about the user or the commit that triggered the image push.

linux/amd64

which form should i fill sir?

---

## Reply 82
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T08:51:52.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/87

Aditya_Naidu:

21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. @Jivraj @carlton .

please fill the form for collecting architecture, so that we can rerun evals earlier we relied on docker api to tell us which architecture is being used, but it didn’t classify them correctly.

---

## Reply 83
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T08:55:29.026Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/88

Hi @23f2000599 check this out

 Jivraj:

**Docker Image Architecture Issue Report**

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

---

## Reply 84
**Author**: S Smriti
**Posted**: 2025-03-29T08:57:30.720Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/89

mine is linux/amd64 sir it doesnt come under arm or x86 i think

---

## Reply 85
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T09:00:06.623Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/90

Hi @23f2002400

Check your Dockerfile if it copies tasksA.py file to docker container.

If it does where does it copy, these are possible mistakes. You were expected to test docker images.

---

## Reply 86
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T09:00:49.471Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/91

Hi @23f2000599

amd64 is x86

---

## Reply 87
**Author**: S Smriti
**Posted**: 2025-03-29T09:01:55.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/92

Ok sir, will fill the form, thank you

---

## Reply 88
**Author**: Achuthan M
**Posted**: 2025-03-29T09:02:52.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/93

One issue file is my app is listening on port 8000. But evaluations being done on 8219 port. so how it will succeed. Please guide what to do.

---

## Reply 89
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T09:09:48.134Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/94

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.

Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.

---

## Reply 90
**Author**: ParamanandaSamantara
**Posted**: 2025-03-29T09:25:29.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/96

There is a mistake in the url I guess check this out I have a fully functional image which was pushed 1 month ago

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface, likely from a container registry service like Docker Hub or a similar platform. It displays information about a specific container image repository. The UI elements include:

*   Repository name and details (last pushed, repository size)
*   Options to add a description and category to the repository.
*   Navigation tabs (General, Tags, Image Management, Collaborators, Webhooks, Settings). The "Image Management" tab is currently selected.
*   A search bar to search by tag or digest.
*   A filter dropdown.
*   A table listing container image versions (tags/digests) with details like media type, OS/ARCH, size, last pushed, and last pulled.
*   Docker command to push a new tag to the repository.

**2. Text Content:**

*   **Repository Name:** pscodes24/dataworks-agent
*   **Repository Details:** Last pushed about 1 month ago, Repository size: 490.1 MB
*   **Add:** Add a description, Add a category
*   **Navigation Tabs:** General, Tags, Image Management BETA, Collaborators, Webhooks, Settings
*   **Search Bar:** Search by tag (tag:abc...) or digest (sha256:abc...)
*   **Links:** Where to start?, Report an issue
*   **Table Headers:** Digest, Tags, Media type, OS/ARCH, Size, Last pushed, Last pulled
*   **Table Data:**
    *   sha256:6e6057d5a26 (tag: latest), Image, linux/amd64, 273.5 MB, about 1 month, 19 days
    *   sha256:c9b258fe4894, Image, linux/amd64, 262.3 MB, about 1 month, about 1 month
*   **Pagination:** 1-2 of 2
*   **Docker Commands:**
    *   Docker commands
    *   To push a new tag to this repository.
    *   docker push pscodes24/dataworks-agent:tagname

**3. Context and Purpose

Please check this out

url::[https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general](https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general)

---

## Reply 91
**Author**: Vivek Rekha Ashoka
**Posted**: 2025-03-29T09:35:51.071Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/97

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a comparison between an expected output and an actual result, likely from a testing or validation process. It appears to be related to formatting or parsing of a Markdown file. The image contains text, code snippets, and table-like structures.

**2. Text Content:**

*   **/data/format.md**: This is the path to a file, likely a Markdown file.
*   **EXPECTED:** This indicates the expected output.
*   **# Header**: This is a Markdown header.
*   **| Start | Mid | End |**: This is the header row of a Markdown table.
*   **| :--- | --- | --: |**: This is the alignment row of a Markdown table, specifying left, center, and right alignment respectively.
*   **| 1 | 2 | 3 |**: This is a row of data in the Markdown table.
*   **Paragraph has extra spaces and trailing whitespace.** This is a descriptive text.
*   **\`\`\`py**: This indicates the start of a Python code block.
*   **print("23f3001745@ds.study.iitm.ac.in")**: This is a Python print statement.
*   **\`\`\`**: This indicates the end of the Python code block.
*   **RESULT:** This indicates the actual result obtained.
*   The "RESULT" section contains a string that includes Markdown syntax, newline characters (`\n`), and the Python code.
*   **A2 FAILED**: This indicates that a test case named "A2" has failed.

**3. Context and Purpose:**

The image shows a test case failure related to the formatting of a Markdown file. The "EXPECTED" section shows the desired Markdown structure, including a header, a table, and a paragraph. The "RESULT" section shows the actual output, which is a single string containing Markdown syntax and newline characters. The test case likely failed because the actual output did not match the expected Markdown structure. The error message "Paragraph has extra spaces and trailing whitespace" suggests that the test also checks for whitespace issues.

**4. Technical Details:**

*   The image shows a comparison of expected and actual outputs, which is a common practice in

This is the correct answer, eval script is not considering newlines properly. @Jivraj @carlton

---

## Reply 92
**Author**: Dipshikha Patel
**Posted**: 2025-03-29T09:52:52.362Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/98

same with me  :smiling_face_with_tear:  i dont understand how i got 0.

---

## Reply 93
**Author**: Atharva Antapurkar
**Posted**: 2025-03-29T09:54:45.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/100

This is the id of the docker image that was evaluated: 2a8ffa96b140 , but i had never provided this docker image instead my image id is 735a5a477fb2 then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it @carlton , @Jivraj .

Regards,

Atharva Antapurkar

23f1002558

---

## Reply 94
**Author**: Aravind Ram
**Posted**: 2025-03-29T10:00:09.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/101

Sir, my evaluation log file is missing, even though I followed all the steps to generate the Docker image correctly. The system indicates that the server didn’t start within 5 minutes, but when I uploaded it, everything was working fine. I put in a lot of effort into this project, and I’m worried I might receive a zero despite making the submission correctly. Kindly help me resolve this issue. My roll number is 22F3004068.

Additionally, my Docker image ID was **d2f27c03b878**, but the ID mentioned in the email was **dfac8596cd4c**. Please provide clarity on this discrepancy.

I have also attached my Docker [log file](https://drive.google.com/file/d/1exrdQOCjbrCFux2hC4OQH_BfgiijCzD1/view?usp=drivesdk) for reference

Docker [image](https://hub.docker.com/repository/docker/docaravind21/tds-project-1/tags)

---

## Reply 95
**Author**: Pritul Santosh Raut 
**Posted**: 2025-03-29T10:11:22.282Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/102

I realized that I made a mistake in my project by forgetting to uncomment a single line of code: os.path.join(os.getcwd(), “path_given”). I feel really bad about this oversight, especially after working so hard on the project and formatting everything carefully. It was an honest mistake, and I take full responsibility for it.

I sincerely request you to consider re-evaluating my work, as I believe it reflects the effort and dedication I put into it. I truly regret this error and will be more careful in the Project 2

@carlton @Jivraj

---

## Reply 96
**Author**: Sudharshini 
**Posted**: 2025-03-29T10:20:28.584Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/103

**Image: Screenshot (423)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a Python traceback, which is an error report showing the sequence of function calls that led to an exception. It's a common output when a Python program encounters an unhandled error.

**2. Text Content:**

The traceback starts with the line "Traceback (most recent call last):".  It then lists a series of "File" lines, each indicating the file path and line number where a function call occurred.  Each "File" line is followed by the code that was executed at that point.

Key text elements include:

*   File paths: These indicate the location of the Python files involved in the error. Examples:
    *   "/usr/local/bin/uvicorn"
    *   "/usr/local/lib/python3.10/site-packages/click/core.py"
    *   "/usr/local/lib/python3.10/site-packages/uvicorn/main.py"
    *   "/app/main.py"
*   Function names: These indicate the functions that were called. Examples:
    *   `sys.exit()`
    *   `main()`
    *   `invoke()`
    *   `run()`
    *   `serve()`
    *   `load()`
    *   `import_from_string()`
    *   `import_module()`
    *   `_gcd_import()`
    *   `_find_and_load()`
    *   `_load_unlocked()`
    *   `exec_module()`
    *   `os.environ`
    *   `__getitem__`
*   Error message: The traceback ends with "KeyError: 'USER_EMAIL'".

**3. Context and Purpose:**

The traceback indicates that a Python program, likely a web application using Uvicorn (an ASGI server), encountered a `KeyError`. This error means the program tried to access an environment variable named "USER_EMAIL" using `os.environ`, but that environment variable was not set.

The purpose of the traceback is to help a developer diagnose and fix the error. By examining the sequence of function calls, the developer can pinpoint where the program expected the "USER_

Sir so the  user_email isn’t passed while pulling the docker image?

Thank you.

---

## Reply 97
**Author**: VIVEK RATNAKAR (22f3002551)
**Posted**: 2025-03-29T10:20:29.023Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/104

Hi Team,

I have resolved the issues and pushed a new Docker image.

**New Docker Image ID:** `913320f92eb3`

**Tag:** `latest`

**OS/ARCH:** `linux/amd64`

Please evaluate my updated submission.

Thanks!

---

## Reply 98
**Author**: Lovepreet Singh
**Posted**: 2025-03-29T10:22:41.482Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/105

Hello,

My log file shows a “file not found” or “directory not found” error. Could you confirm whether `datagen.py` was executed inside the Docker container or on the host OS? If it ran on the host, I don’t see any mounting process for the `/data` folder into the container. Could you please clarify this?

@carlton @Jivraj

---

## Reply 99
**Author**: ROHIT B LAKSHMANAN
**Posted**: 2025-03-29T10:36:01.452Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/106

is it like this: FileNotFoundError: [Errno 2] No such file or directory: ‘system_input.txt’ ?

I am getting this error.

---

## Reply 100
**Author**: Ritwika Dutta 
**Posted**: 2025-03-29T10:43:12.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/107

@Jivraj @carlton sir, I have fixed my docker image issue that was causing the error. Please re-pull my docker image so that I can get score. Please consider me for re-evaluation. All the codes were correct, only issue was a glitch in the docker image.

---

## Reply 101
**Author**: Santosh Sharma
**Posted**: 2025-03-29T11:15:28.607Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/108

Hello Sir, I am facing the same issue. Please look into it. Before submission, I ran my Docker file with the evaluation script to ensure it was working, and it worked fine. Kindly help me out. My roll number is 23F3004321.

---

## Reply 102
**Author**: Lovepreet Singh
**Posted**: 2025-03-29T11:22:18.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/109

Yes, something like that, My log file shows when script tries to access file it says file not found or directory not found.

---

## Reply 103
**Author**: Yashvardhan
**Posted**: 2025-03-29T11:48:22.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/110

Sir, I checked my evaluation log, and the error occurred because the **AI proxy token limit was exceeded**. I ran the evaluation script to verify, and I scored **12/20**.

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a console output, likely from a Flask web application running in a development environment. It displays server startup information, followed by error tracebacks related to HTTP requests.

**2. Text Content:**

*   **Server Startup Information:**
    *   `Debug mode: on`
    *   `[31m [1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. [0m`
    *   `* Running on all addresses (0.0.0.0)`
    *   `* Running on http://127.0.0.1:8000`
    *   `* Running on http://172.17.0.8:8000`
    *   `[33mPress CTRL+C to quit [0m`
    *   `* Restarting with stat`
    *   `* Debugger is active!`
    *   `* Debugger PIN: 710-864-711`

*   **HTTP Request Logs and Error Tracebacks:**
    *   Lines starting with an IP address (e.g., `172.17.0.1`) followed by a date and time, indicate HTTP requests. These lines also show the HTTP method (e.g., `POST`, `GET`), the requested URL, the HTTP protocol (`HTTP/1.1`), and the HTTP status code. Status codes of `500` indicate server errors, and `404` indicate "Not Found" errors.
    *   Following the `500` status codes are Python traceback messages. These tracebacks show the sequence of function calls that led to the error, along with the file names and line numbers where the errors occurred.

*   **Specific Error Messages:**
    *   `AttributeError: 'NoneType' object has no attribute 'lower'`

*   **Example URLs:**
    *   `/run?task=Say+Hello+Carlton`
    *   `/run?task=%0AInstall+`uv`+...` (This URL looks like it's trying to install something, possibly with

**Image: image**
Here's a breakdown of the image content:

**1. UI Elements:**

*   The image appears to be a console output or log, likely from a software application or testing framework. The dark background and light text are typical of terminal or code editor environments.

**2. Text Content:**

*   **Error Message:**
    *   `"error": "unable to open database file"` - This indicates a problem with accessing a database file.
*   **HTTP Request (GET):**
    *   `HTTP Request: GET http://localhost:8000/read?path=/data/b10.csv "HTTP/1.1 404 NOT FOUND"` - This shows a GET request to a local server (localhost:8000) to read a file named "b10.csv" located in the "/data/" directory. The server responded with a "404 NOT FOUND" error, meaning the file was not found at the specified path.
*   **File Reading Error:**
    *   `B10 failed: Cannot read /data/b10.csv` - This confirms that the application was unable to read the "b10.csv" file. The "B10" prefix might be an identifier for a specific test case or module.
*   **Test Failure:**
    *   `X B10 FAILED` - This indicates that the test case or module "B10" has failed. The "X" likely represents a visual indicator of failure.
*   **Score:**
    *   `Score: 12 / 20` - This shows a score of 12 out of 20, suggesting a performance or correctness evaluation.
*   **HTTP Request (POST):**
    *   `HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"` - This shows a POST request to an external API endpoint related to OpenAI embeddings. The server responded with a "200 OK" status, indicating a successful request.

**3. Context and Purpose:**

*   The image likely represents the output of a test run or debugging session. The application is trying to read a CSV file ("b10.csv"), but it's failing,

---

## Reply 104
**Author**: Jiya Vemra
**Posted**: 2025-03-29T12:50:26.967Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/111

Sir, my project scored 1/20, with only B1 passed. However, when I ran the evaluation script, I got 6/10 in A tasks. Is there any way this can be checked, as the project works on deployed.

Kind Regards and thanks

---

## Reply 105
**Author**: S Sharmile
**Posted**: 2025-03-29T12:57:02.183Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/112

@carlton @Jivraj

Sir,

This is the id of the docker image that was evaluated: 82aeb74ca739  ,

but i had never provided this docker image instead my image id is de8235663462

then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it @carlton , @Jivraj .

Regards,

S Sharmile

23f3001688

---

## Reply 106
**Author**: Sahana S
**Posted**: 2025-03-29T13:23:08.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/113

Sir the evaluated docker file ID was mentioned as  5b28fd5b25a7 in the mail sent by you but my docker file ID is 4d8c0cc34e35. I think my docker file is not evaluated properly. Kindly do check this and help me out. My reg no 24f1002633.

---

## Reply 107
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-03-29T13:24:44.800Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/114

@carlton

My docker logs shows that `OSError: Cannot find resource` error occurred when the data generation script tried to access font files in generation for a8.

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a traceback from a Python program, indicating an error related to font loading. It also shows some installation information and a URL encoded string.

**2. Text Content:**

*   "Installed 3 packages in 42ms"
*   "Traceback (most recent call last):"
*   Several lines starting with "File" indicating the path to Python files and line numbers. These paths include:
    *   "/tmp/datagenmrt9km.py"
    *   "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py"
    *   "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
*   "a8\_credit\_card\_image"
*   "large\_font = ImageFont.truetype("arial.ttf", size=60)"
*   "return freetype(font)"
*   "return FreeTypeFont (font, size, index, encoding, layout\_engine)"
*   "self.font = core.getfont("
*   "OSError: cannot open resource"
*   "During handling of the above exception, another exception occurred:"
*   "INFO: 172.17.0.1:35176 - "POST /run?"
*   "task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fgist.githubusercontent.com%2Fsanand0%2Ff19b6797f82b36da39ac4"

**3. Context and Purpose:**

The image captures an error that occurred while running a Python script named "datagenmrt9km.py". The script seems to be related to generating credit card images, as indicated by the function name "a8\_credit\_card\_image". The error is an "OSError: cannot open resource", which suggests that the program is unable to access a required resource,

The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of code, likely from a Python file, displayed in a dark-themed code editor or terminal. The code consists of a series of function calls.

**2. Any text content visible:**

The text content consists of the following function calls:

*   `a2_format_markdown()`
*   `a3_dates()`
*   `a4_contacts()`
*   `a5_logs()`
*   `a6_docs()`
*   `a7_email()`
*   `a8_credit_card_image()`
*   `a9_comments()`
*   `a10_ticket_sales()`

**3. The context or purpose of what's displayed:**

The code snippet likely represents a series of functions or modules being called in a specific order. The naming convention (a2, a3, a4, etc.) suggests that these functions might be part of a larger system or process, possibly related to data processing, report generation, or some kind of automated task. The function names themselves hint at the type of operations being performed: formatting markdown, handling dates, managing contacts, processing logs, dealing with documents, sending emails, processing credit card images, handling comments, and managing ticket sales.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The code is likely Python, given the function call syntax (function_name()).
*   The naming convention suggests a structured approach to organizing and executing these functions.
*   The dark theme of the code editor is a common preference among developers.

I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.

So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .

Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.

Thank you

---

## Reply 108
**Author**: Vihaan Verma
**Posted**: 2025-03-29T13:35:11.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/115

**Image: image**
Here's a breakdown of the image content:

**1. UI Elements:**

*   The image appears to be a console output or log snippet.
*   There are two distinct sections, each marked with a colored circle (yellow and red). These likely indicate different stages or results of a process.

**2. Text Content:**

*   **First Section (Yellow Circle):**
    *   "Running task: Install `uv` (if required) and run the script" - This indicates a task is being executed, potentially involving the installation of a tool named "uv".
    *   A long URL: `https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466052b66ae/datagen.py` - This is a URL pointing to a script named "datagen.py" hosted on GitHub Gist.
    *   "with `23f3003196@ds.study.iitm.ac.in` as the only argument" - This specifies that the script "datagen.py" is being executed with the email address "23f3003196@ds.study.iitm.ac.in" as its argument.
*   **Second Section (Yellow Circle):**
    *   "HTTP Request: POST http://localhost:8503/run?" - This indicates an HTTP POST request being made to the local server on port 8503, specifically to the "/run" endpoint.
    *   A very long URL-encoded string follows the "?". This string likely contains the task details, including the script URL and the argument, but it's URL-encoded.
    *   `"HTTP/1.1 500 INTERNAL SERVER ERROR"` - This indicates that the HTTP request resulted in a 500 Internal Server Error.
*   **Third Section (Red Circle):**
    *   `HTTP 500 { ... }` - This confirms the 500 error and provides more details in a JSON-

this is a 429 from sanand which is an error from your side. The evaluation already so delayed now has such issues because of which I am getting 1/20. @carlton @Jivraj

---

## Reply 109
**Author**: Jayesh Bansal
**Posted**: 2025-03-29T13:52:10.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/116

does that mean our script is not evaluated?

---

## Reply 110
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T14:27:26.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/117

Hi @Vihaanv07

This was a good spot, we will rerun all the images where string `Agent Errro: 429 Client Error....` is present.

Thanks and kind regards

---

## Reply 111
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T14:28:42.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/118

Hi @Jayeshbansal

There were 12 emails for which we didn’t rerun, we will be fair with grading you and will take care of it.

---

## Reply 112
**Author**: Mishkat Chougule
**Posted**: 2025-03-29T14:28:53.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/119

**Image: Screenshot 2025-03-29 at 7.53.20 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window displaying the output of the `docker images` command. This command lists the Docker images that are currently stored on the system. The output is formatted in a table with columns for:

*   **REPOSITORY:** The name of the image repository.
*   **TAG:** The tag associated with the image (often "latest").
*   **IMAGE ID:** A unique identifier for the image.
*   **CREATED:** How long ago the image was created.
*   **SIZE:** The size of the image on disk.

**2. Text Content:**

The terminal prompt shows: `mish@Mishs-MacBook-Air %`

The output of the `docker images` command includes the following repositories, tags, image IDs, creation dates, and sizes:

*   **REPOSITORY:** tds-project1, **TAG:** latest, **IMAGE ID:** dc8c1e7528b8, **CREATED:** 5 weeks ago, **SIZE:** 1.75GB
*   **REPOSITORY:** mishkat02/automation-agent, **TAG:** latest, **IMAGE ID:** 07b16dc68225, **CREATED:** 6 weeks ago, **SIZE:** 367MB
*   **REPOSITORY:** franky1/tesseract, **TAG:** latest, **IMAGE ID:** b3042ad1e731, **CREATED:** 2 months ago, **SIZE:** 2.33GB
*   **REPOSITORY:** mish/myrepo, **TAG:** 23f3003027, **IMAGE ID:** 07940877fae1, **CREATED:** 2 months ago, **SIZE:** 12.2MB
*   **REPOSITORY:** mishkat02/myrepo, **TAG:** 23f3003027, **IMAGE ID:** 07940877fae1, **CREATED:** 2 months ago, **SIZE:** 12.2MB
*   **REPOSITORY:** docker/welcome-to-docker, **TAG:** latest, **IMAGE ID:** eedaff45e3c7, **CREATED

My docker image id is different than the one I submitted

“This is the id of the docker image that was evaluated: 10f11a0e0cd6”

@carlton @Jivraj @s.anand plz check this

---

## Reply 113
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T15:08:04.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/120

Hi @23F300327

This is what you submitted to us in the gform.

23f3003027@ds.study.iitm.ac.in	mishkat02/automation-agent:latest

We will only evaluate this image.

Kind regards

---

## Reply 114
**Author**: Mishkat Chougule
**Posted**: 2025-03-29T15:11:48.786Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/121

@carlton then why is the image id different?

in the docker hub as well as my local terminal the image id is 07b16dc68225

---

## Reply 115
**Author**: Carlton D'Silva
**Posted**: 2025-03-29T15:20:02.379Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/122

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.

In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.

But we can detect changes made to the docker repo through our image id. I hope that is clear.

We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.

Kind regards

---

## Reply 116
**Author**: NK
**Posted**: 2025-03-29T16:06:00.271Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/123

@carlton @Jivraj @Saransh_Saini

My logs show,  ‘exec format error’ and it is due to architecture issue,  image was built on mac.

I have updated the google form regarding the architecture. Please rerun my image. Thanks

---

## Reply 117
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-29T16:16:01.956Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/125

Jivraj:

**Docker Image Architecture Issue Report**

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

Just fill the google form, we are rerunning such images.

---

## Reply 118
**Author**: Santosh Sharma
**Posted**: 2025-03-30T05:06:28.932Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/126

Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between `pandas` and `numpy` caused the container to fail. To my surprise, the same versions (`pandas==2.0.3` and `numpy==1.24.3`) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (`santoshsharma003/tds-project-one-1:latest`). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!

---

## Reply 119
**Author**: bharath
**Posted**: 2025-03-30T05:07:21.018Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/127

Hi @carlton, I checked my Docker log file now and realised I missed to push a couple of files to the image. Is there anything I could do now? I have all the required files in my Git repo though. Please help.

---

## Reply 120
**Author**: Daksh Agarwal
**Posted**: 2025-03-30T06:40:47.576Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/128

Sir in my logs it is showing that there’s cv2 module missing i mightve missed adding that in the requirements. Is there anything you could do to help me please?

---

## Reply 121
**Author**: Roopika
**Posted**: 2025-03-30T10:15:36.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/129

I am also facing the same issue. I tried evaluating the scripts with the evaluation file also. Please rerun and let me know. My Roll No is 21F1002866.

---

## Reply 122
**Author**: RAJ K BOOPATHI
**Posted**: 2025-03-30T10:31:12.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/130

Hi,

For Tasks A8, A9 & A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.

For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK

ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

Similarly for task B2.

INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK

For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.

For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?

Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8

---

## Reply 123
**Author**: Jayaram
**Posted**: 2025-03-30T17:22:14.882Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/131

@Jivraj @carlton

Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build

ARG http_proxy=http://www-proxy-adcq7.us.<xxx>.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.<xxx>.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}

This was required  as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..

So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container  started up without issues..

Checkin url: [Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub](https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583)

Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well..  didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help

---

## Reply 124
**Author**: Tasneem Shahnawaz
**Posted**: 2025-03-30T23:45:37.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/132

I am also with the same situation sir. Please help with this issue. I have submitted everything correctly and it was working fine. Thanks

---

## Reply 125
**Author**: Naman S. 
**Posted**: 2025-03-31T06:38:27.518Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/133

Hello Sir,

Greetings,

I have not recieved amy mail regarding my Project 1 Marks, can you please look into it.

Thank you/

---

## Reply 126
**Author**: Daksh Agarwal
**Posted**: 2025-03-31T06:41:26.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/134

@Jivraj @carlton please sir could you help me with this issue previously when i ran on my system it was working perfectly fine

---

## Reply 127
**Author**: K Senthur Kumaran 
**Posted**: 2025-03-31T09:29:51.137Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/135

Hello sir

I noticed that the log mentioned:

“python: can’t open file ‘/app/app/main.py’: [Errno 2] No such file or directory.”

However, my main file was named run.py, which might have caused the issue. Since the code was present, I was given a 0. Would it be possible to run it again or consider partial marks for the submission?

Thank you for your time and consideration. I appreciate your help!

---

## Reply 128
**Author**: Varad Rajadhyax 
**Posted**: 2025-03-31T10:29:34.265Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/136

Even my file saying the same. I got the ‘No module named tasksA’ error whereas at the time of submission it was working perfectly fine. Please kindly look into this issues sir.

Thank you.

---

## Reply 129
**Author**: Sahil Sharma
**Posted**: 2025-03-31T11:06:22.363Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/137

no taskA.py even though i ran the evalution getting 12 score still no evalution.log

help the students please give them second chance

---

## Reply 130
**Author**: Jayaram
**Posted**: 2025-03-31T11:31:30.396Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/138

on a side note, to validate and test our docker/podman images on a platform outside of our dev environment we can use [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/).. this is a free platform to download run and test docker images …

---

## Reply 131
**Author**: Shiva Ramakrishna
**Posted**: 2025-03-31T12:59:59.522Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/139

Hi @carlton @Jivraj

I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?

Thanks for considering, any help would be appreciated. Worked very hard for this

---

## Reply 132
**Author**: Garima
**Posted**: 2025-03-31T17:03:28.971Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/140

The docker id of the image that was evaluated (as specified the mail 1ae3f64427f0) is not correct, the correct id is 51168f246618.

Name of Docker image -

garriimaa/llm_automation:latest

Please evaluate with the above image name.

GitHub repository for reference - [GitHub - Garima1603/llm_automation](https://github.com/Garima1603/llm_automation)

---

## Reply 133
**Author**: Ritwika Dutta 
**Posted**: 2025-03-31T20:07:47.011Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/141

@Jivraj @carlton sir I fixed my issue with docker during the given window for discrepancy and requested a re-pulling of the image but still got a mail of score 0. Please sir, I request you to do a re-evaluation, the docker issue is fixed long back by me. It’s an earnest request sir.

---

## Reply 134
**Author**: Afsal
**Posted**: 2025-03-31T20:16:46.949Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/142

Dear sir,  @carlton @Jivraj

I got result as fail for the project 1 and the reasons listed are as in the screenshot. But as you can see in the second screenshot, i still have that repository which is public, have license file and docker file in it, created 2 months back. I actually don’t know how this issues come in, please resolve this.

**Image: 1**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from an automated evaluation or grading system. It outlines the prerequisites for "Project 1" and then presents the results of checks performed against those prerequisites.

**2. Text Content:**

The image contains the following text:

*   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (The "TDS Project 1: Evaluation page" is a hyperlink)
*   A numbered list of prerequisites:
    1.  "Your GitHub repository exists and is publicly accessible"
    2.  "Your GitHub repository has a LICENSE file with the MIT license"
    3.  "Your GitHub repository has a valid Dockerfile"
    4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
    5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   A list of checks and their results:
    *   "Is Docker image present in dockerhub AND is public: PASS"
    *   "Is Github repo present AND public: FAIL"
    *   "Is Dockerfile present in root of github repo: FAIL"
    *   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. Context and Purpose:**

The image displays the results of an automated check to ensure a student or developer has met the necessary prerequisites for a project (Project 1). The system checks for the existence and accessibility of a GitHub repository, the presence of a Dockerfile and MIT license within the repository, and the accessibility and configuration of a Docker image. The overall "Prerequisites" status is "FAIL," and the "Project 1 Score" is 0, indicating that the submission does not meet the minimum requirements for evaluation.

**4. Technical Details:**

*   **GitHub

**Image: 2**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository interface. It displays the file structure and commit history of a repository named "tds_proj1". The interface includes standard GitHub elements like the repository name, branch information, search bar, "Add file" button, and a "Code" button. It also lists the files and directories within the repository, along with information about the last commit that modified them.

**2. Text Content:**

*   **Repository Name:** tds\_proj1
*   **Visibility:** Public
*   **Branch:** main, 1 Branch
*   **Tags:** 0 Tags
*   **Actions:** Pin, Unwatch, Go to file, Add file, Code
*   **Commit Information:** 21f2000304 update, 5e4785c, 2 months ago, 10 Commits
*   **File/Directory Names:**
    *   \_pycache\_
    *   data
    *   env
    *   Dockerfile
    *   LICENSE
    *   app.py
    *   datagen.py
    *   evaluate.py
    *   requirements.txt
    *   tasksA.py
*   **Commit Messages:** update, Create LICENSE
*   **Time Since Last Commit:** 2 months ago

**3. Context and Purpose:**

The image shows the contents of a GitHub repository. The purpose is to allow users to browse the files, view the commit history, and potentially contribute to the project. The presence of files like `app.py`, `datagen.py`, `evaluate.py`, `requirements.txt`, and `tasksA.py` suggests that this repository likely contains a Python project, possibly related to data science or machine learning. The `Dockerfile` indicates that the project is likely containerized for easier deployment.

**4. Technical Details:**

*   The presence of `requirements.txt` suggests that the project uses Python packages, and this file lists the dependencies.
*   The `.py` files indicate Python source code.
*   The `Dockerfile` is a text file that contains instructions for building a Docker image.
*   The `LICENSE` file specifies the terms under which the code can be used, modified, and

---

## Reply 135
**Author**: Sirimilla Karthik Balaji
**Posted**: 2025-03-31T20:29:32.826Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/143

@carlton

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link: [GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20

Roll no : 23f1002398

Mailid: 23f1002398@ds.study.iitm.ac.in

My evaluation.log

**Image: IMG_6418**
Here's a detailed description of the image content:

**1. Overall Content:**

The image appears to be a screenshot of a debugging or logging output, likely from a software development environment. It shows a series of HTTP requests and responses, along with error messages and task execution details. It seems to be related to a data processing or analysis task involving a dataset named "ticket-sales.csv".

**2. UI Elements:**

*   The top of the image shows a typical mobile UI with a close button (X), an email address ("23f1002398@ds.study.iitm.a..."), a message icon, and a settings/options icon.
*   There are red circles with "B9 failed" and "B10 failed" indicating errors.
*   There's a green checkmark with "Running task" indicating a successful start of a task.
*   There's a target icon with "Score: 6 / 20" indicating a performance metric.

**3. Text Content and Interpretation:**

*   **HTTP Requests and Responses:** The image shows several HTTP requests (GET and POST) to `localhost` on different ports (8309 and 8001). Some requests result in "404 Not Found" errors, while others result in "400 Bad Request" or "200 OK".
*   **Error Messages:**
    *   "Cannot read /data/b9.html" and "/data/b10.csv" indicate that the server couldn't find or access these files.
    *   The "HTTP 400" error includes a detailed message about "Max retries exceeded" and "Connection refused". This suggests a problem with the server being unavailable or overloaded.
*   **Task Description:** The "Running task" section describes a process that:
    *   Runs a datasette server using `uvx datasette /data/ticket-sales.db --port 8001`.
    *   Counts the number of rows in the "tickets" table where the "type" is "Bronze" using a SQL query.
    *   Saves the result to `/data/b10.csv`.
    *   Stops the datasette server.
*   **SQL Query:** The SQL query used is

---

## Reply 136
**Author**: Sirimilla Karthik Balaji
**Posted**: 2025-03-31T20:32:07.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/144

**Image: IMG_6417**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email on a mobile device (likely an iPhone, judging by the status bar). The email is titled "TDS Jan 25 Project 1 Scores". The email content details the prerequisites for a project and the results of an automated evaluation.

**2. Text Content:**

The email contains the following text:

*   **Subject:** TDS Jan 25 Project 1 Scores
*   **Recipient:** to me
*   **Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (with "TDS Project 1: Evaluation" being a hyperlink)
    *   A numbered list of 5 prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of evaluation results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: PASS"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: PASS"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context and Purpose:**

The email is an automated notification to a student ("Learner") regarding the status of their Project 1 submission. It outlines the prerequisites for the project, checks whether the student's submission meets those prerequisites, and provides a score based on the results. The

---

## Reply 137
**Author**: Abhinav
**Posted**: 2025-03-31T20:33:36.179Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/145

@carlton  Sir, the image id written in my notification email is wrong. The correct image is this: [https://hub.docker.com/repository/docker/24f1002064/project1/general](https://hub.docker.com/repository/docker/24f1002064/project1/general)

can you please double check this? You can also verify that I have made no changes to it since the due date.

---

## Reply 138
**Author**: Sirimilla Karthik Balaji
**Posted**: 2025-03-31T20:20:12.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/146

@carlton

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link:  [GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20

Roll no : 23f1002398

Mailid: 23f1002398@ds.study.iitm.ac.in

**Image: IMG_6417**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email on a mobile device (likely an iPhone, given the status bar). The email is titled "TDS Jan 25 Project 1 Scores" and is addressed to "Dear Learner." The email outlines the prerequisites for a project and provides an evaluation of whether the learner has met those prerequisites.

**2. Any text content visible:**

*   **Email Header:**
    *   "1:30" (Time)
    *   "TDS Jan 25 Project 1 Scores" (Email Subject)
    *   "to me" (Recipient)
*   **Email Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:"
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of evaluations with PASS/FAIL status:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: PASS"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: PASS"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"
*   **Status Bar:**
    *   Standard iPhone status bar elements (battery, signal strength, Wi-Fi, etc.)
    *   "19" (Notification count

---

## Reply 139
**Author**: Carlton D'Silva
**Posted**: 2025-03-31T20:39:43.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/147

Your dockerfile is misspelt.

---

## Reply 140
**Author**: Sirimilla Karthik Balaji
**Posted**: 2025-03-31T21:01:01.155Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/148

Thanks for your quick response sir. I just wanted to clarify that my dockerfile was recognized by Docker, and my image was successfully built, so it seems that Docker itself didn’t have an issue with the filename.

However, I understand that the evaluation script might be case-sensitive and specifically looking for “Dockerfile” with an uppercase “D”. If that’s the issue, should I rename and push the file again to the repo sir.

Please let me know if that’s the right fix or if I need to do anything else sir.

---

## Reply 141
**Author**: Carlton D'Silva
**Posted**: 2025-03-31T21:01:54.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/149

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.

But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.

Kind regards

---

## Reply 142
**Author**: SP
**Posted**: 2025-03-31T21:05:40.325Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/150

I recently received an email stating that my Docker image is not publicly available, resulting in a failed prerequisite check for the TDS Project 1. However, I have ensured that my Docker image is publicly accessible. Please help.

@carlton

My Docker image ID is "**99d08f2002fa** ", and it is set to public. I kindly request you to review this issue, as I have worked very hard on this project and would appreciate the opportunity for a fair evaluation.

---

## Reply 143
**Author**: Abhinav
**Posted**: 2025-03-31T21:15:37.954Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/151

can you share the sha?

---

## Reply 144
**Author**: LAKSHAY
**Posted**: 2025-03-31T21:34:08.281Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/152

@carlton @Jivraj @Saransh_Saini

There might be some glitches in the system. Could you kindly verify the process again?

**Image: 1000430602**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email on a mobile device. The email appears to be an automated message regarding the evaluation of a project (Project 1). The email details prerequisite checks and their corresponding results. The bottom of the image shows the standard Android navigation bar and app icons for email, messaging, and video call.

**2. Text Content:**

The email contains the following text:

*   **Subject:** (Implied from sender) Project 1 Evaluation
*   **Sender:** 22t1 se2002
*   **Recipient:** to me
*   **Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:"
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of evaluation results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context and Purpose:**

The email is an automated evaluation report for a student's (or learner's) Project 1 submission. It outlines the prerequisites for the project and indicates whether the submission meets those requirements. The student has passed

I’ve already received my score in the evaluation log. Additionally, the Docker Hub run logs show no errors, and both the GitHub repo and Docker image are publicly accessible. All the content has been verified and meets the prerequisites.

Let me know if any further action is needed from my end.

---

## Reply 145
**Author**: Ritwika Dutta 
**Posted**: 2025-04-01T03:18:01.579Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/153

@Jivraj @carlton please kindly re-pull my docker image and re-evaluate my project sir. I fixed the issue long back. Please reply kindly. My roll no is : 22f2001389. I have been trying to get to you for long now. Please kindly help me out. Please reply.

---

## Reply 146
**Author**: Vansh Mittal
**Posted**: 2025-04-01T03:43:51.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/155

@carlton

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link: [GitHub - Vansh-22f300/project_tds](https://github.com/Vansh-22f300/project_tds.git)

My evaluation.log , contains the score .

Roll no : 22f3001851

Mail id:22f3001851@ds.study.iitm.ac.in

**Image: Screenshot_2025-04-01-09-11-54-385_com.android.chrome**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a mobile view of a GitHub repository. It displays the repository's details and a list of files and directories within the repository.

**2. Text Content:**

*   **Top Bar:** 9:11 (time), network indicators (data speed, WiFi signal, battery level).
*   **Repository Details:**
    *   "MIT license" (under a legal scale icon)
    *   "0 stars" (under a star icon)
    *   "0 forks" (under a fork icon)
    *   "1 watching" (under an eye icon)
    *   "1 Branch" (under a branch icon)
    *   "0 Tags" (under a tag icon)
    *   "Activity" (under a graph icon)
    *   "Public repository" (under a globe icon)
*   **Branch Selection:** "main" (with a dropdown arrow)
*   **Code Button:** "Code" (green button with a dropdown arrow)
*   **More Options:** "..." (three dots)
*   **Repository Owner:** "Vansh-22f300" "2 months ago"
*   **File/Directory List:**
    *   `__pycache__` (directory)
    *   `.env` (file)
    *   `.gitignore` (file)
    *   `LICENSE` (file)
    *   `README.md` (file)
    *   `app.py` (file)
    *   `datagen.py` (file)
    *   `dockerfile` (file)
    *   `evaluate.py` (file)
    *   `requirements.txt` (file)
    *   `tasksA.py` (file)
    *   `tasksB.py` (file)
    *   Each file/directory is followed by "2 months ago", indicating the last modification time.

**3. Context and Purpose:**

The image shows the interface of a GitHub repository on a mobile device. The purpose is to allow users to view the repository's contents, details (license, stars, forks, etc.), and browse the files and directories.

---

## Reply 147
**Author**: Vaddi Yaswanth
**Posted**: 2025-04-01T04:00:56.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/156

dockerfile is spelling mistake it should be Dockerfile same thing happened to me .

---

## Reply 148
**Author**: Aarush saxena 
**Posted**: 2025-04-01T04:18:39.805Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/157

@carlton

Pls look into this evaluation.py contains two result

Can u confirm that u guys will use 10/20 one ?

**Image: Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of a terminal or code editor output, likely from a mobile device. It shows instructions and commands related to setting up and interacting with a Datasette server, along with error messages and HTTP request information.

**2. Any text content visible:**

The text content includes:

*   **Email Address:** `23f2005702@ds.stud...` (likely a placeholder or user identifier)
*   **Instructions for interacting with a Datasette server:**
    *   Steps to count rows with SQL using `curl` or a web browser.
    *   Example `curl` command to query the server and save the output to `/data/b10.csv`.
    *   Instructions on how to stop the Datasette server, including using `kill` commands.
    *   Summary of commands.
    *   Additional notes about ensuring `uvx` and `datasette` are installed and configured correctly, and that the `/data` directory is writable.
*   **HTTP Request Information:**
    *   `HTTP Request: GET http://localhost:8064/read?path=/data/b10.csv "HTTP/1.1 404 Not Found"`
    *   `HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"`
*   **Error Messages:**
    *   `B10 failed: Cannot read /data/b10.csv`
    *   `X B10 FAILED` (with a red "X" icon)
*   **Score:** `Score: 10 / 20`

**3. The context or purpose of what's displayed:**

The image shows a user attempting to interact with a Datasette server, likely to query a database and retrieve data. The instructions guide the user through setting up the server, running SQL queries using `curl`, and stopping the server. The error messages indicate that the user is encountering issues, specifically with reading the file `/data/b10.csv`, which suggests a problem with file permissions or the file not being created correctly. The score of 10

**Image: Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image appears to be a screenshot of a terminal or console output, likely from a debugging or development environment. It shows a series of HTTP requests and responses, along with error messages and task execution information.

**2. Text Content:**

*   **Email Address:** `23f2005702@ds.study.iitm.ac.in` (likely a user identifier)
*   **Instructions:** "Bronze%22 and save it to /data/b10.csv. Then stop the datasette server."
*   **HTTP Requests and Responses:**
    *   POST requests to `http://localhost:8462/run` and `http://localhost:8064/run` with URL-encoded parameters. These requests seem to be related to running a datasette server and installing/running a script.
    *   GET request to `http://localhost:8462/read?path=/data/b10.csv`
    *   POST request to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings`
    *   Error messages like "HTTP/1.1 500 Internal Server Error", "HTTP/1.1 404 Not Found", "HTTP/1.1 429 Too Many Requests"
*   **Error Messages:**
    *   "B10 failed: Cannot read /data/b10.csv"
    *   "B10 FAILED"
    *   "Failed to send request to OpenAI API: 429"
*   **Task Execution Information:**
    *   "Running task: Install `uv` (if required) and run the script `https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466052b66ae/datagen.py` with `23f2005702@ds.study

---

## Reply 149
**Author**: Yashvardhan
**Posted**: 2025-04-01T04:23:55.817Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/158

HELLO SIR , DOCKET IMAGE PRESENT IN DOCKER HUB  AND IT IS PUBLIC THEN WHY IT IS FAIL

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a text-based report or evaluation summary. It appears to be an automated check of prerequisites for a project, specifically "Project 1". The report lists several criteria and indicates whether each criterion has "PASS"ed or "FAIL"ed.

**2. Text Content:**

The text content is as follows:

*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: FAIL"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. Context/Purpose:**

The purpose of the displayed information is to provide feedback on whether the necessary conditions (prerequisites) for Project 1 have been met. It checks for the presence and accessibility of a Docker image, a GitHub repository, a Dockerfile, and an MIT license. The final lines indicate an overall "FAIL" for the prerequisites and a score of 0 for the project, likely due to the Docker image check failing.

**4. Technical Details:**

*   The report suggests an automated system is checking for specific files and configurations within a GitHub repository and Docker Hub.
*   The checks include:
    *   Presence of a Docker image in Docker Hub and whether it's publicly accessible.
    *   Presence of a GitHub repository and whether it's publicly accessible.
    *   Presence of a "Dockerfile" in the root directory of the GitHub repository.
    *   Presence of an "MIT license" file in the root directory of the GitHub repository.
*   The "AND" in the checks implies that both conditions (e.g., presence and public accessibility) must be met for the check to pass.
*   The overall "Prerequisites: FAIL" suggests that all individual checks must pass for the project to proceed or receive a higher score.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a repository, likely on a platform like Docker Hub or a similar container registry. It displays information about a repository named "23f2004644/data_automation_agent". The UI includes tabs for "General", "Tags", "Image Management" (labeled as BETA), "Collaborators", "Webhooks", and "Settings". The "Tags" tab is currently selected. The main content area shows a table listing the tags associated with the repository.

**2. Any text content visible:**

*   **Repository Name:** 23f2004644/data\_automation\_agent
*   **Metadata:**
    *   Last pushed about 1 month ago
    *   Repository size: 757 MB
    *   Add a description
    *   Add a category
*   **Tabs:** General, Tags, Image Management (BETA), Collaborators, Webhooks, Settings
*   **Tags Section:**
    *   Tags
    *   This repository contains 1 tag(s).
    *   Tag, OS, Type, Pulled, Pushed (table headers)
    *   latest (tag name)
    *   Image (tag type)
    *   5 days (time since pulled)
    *   about 1 month (time since pushed)
    *   See all

**3. The context or purpose of what's displayed:**

The image shows the details of a container image repository. The "Tags" section allows users to view and manage different versions (tags) of the image. The information displayed helps users understand when the image was last updated (pushed) and how recently it was pulled. The "Image Management" tab being in BETA suggests that the platform is still developing features for managing container images.

**4. Technical details:**

*   The repository contains at least one image tag named "latest".
*   The "OS" column has a Linux penguin icon, indicating that the image is likely based on a Linux distribution.
*   The "Pulled" and "Pushed" columns show the time elapsed since the image was last pulled and pushed, respectively. This is useful for determining the freshness of the image.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of a UI element, likely from a web application or software interface. It shows a single row of data within a table or list.

**2. Any text content visible:**

*   **23f2004644/data\_automation\_agent:** This is likely an identifier or name for the item in the row. It seems to be a combination of a hexadecimal string and a descriptive name.
*   **about 1 month ago:** This indicates the last activity or modification time of the item.
*   **IMAGE:** This is likely a label or indicator that the item is an image.
*   **Public:** This indicates the visibility or access level of the item.
*   **Inactive:** This indicates the current status of the item.

**3. The context or purpose of what's displayed:**

The UI element seems to be displaying information about a "data\_automation\_agent" item, which is an image, was last active about a month ago, is publicly accessible, and is currently inactive. This could be part of a system for managing or monitoring data automation agents.

**4. Technical details if it's a code screenshot or technical diagram:**

There is no code or technical diagram visible in the image. It's purely a UI element displaying metadata about an item.

@carlton

---

## Reply 150
**Author**: Mayank Singh
**Posted**: 2025-04-01T05:36:06.406Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/159

same issue i am also facing ,

@carlton

---

## Reply 151
**Author**: Santosh Sharma
**Posted**: 2025-04-01T05:49:15.993Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/161

Respected Sir,

I have received a **FAIL** status for the prerequisite check:

*“Is Docker image present in Docker Hub AND is public.”*

However, as shown in my Docker Hub repository, my Docker images are publicly accessible.

I have attached a screenshot for the reference.

Thank you for your time and support.

**Image: Screenshot From 2025-04-01 11-17-44**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for managing repositories, likely within a Docker or similar containerization platform. It displays a list of repositories, search and filter options, and account information.

**2. Text Content:**

*   **Account Information:**
    *   "santoshsharma003" (likely the username)
    *   "Docker Personal" (account type)
*   **Navigation Menu:**
    *   "Repositories"
    *   "Settings"
    *   "Default privacy"
    *   "Notifications"
    *   "Billing"
    *   "Usage"
*   **Repository Management:**
    *   "Repositories" (title)
    *   "All repositories within the santoshsharma003 namespace." (description)
    *   "Search by repository name" (search input placeholder)
    *   "All content" (dropdown filter)
    *   "Create a repository" (button)
*   **Repository List Headers:**
    *   "Name"
    *   "Last Pushed" (with an upward arrow indicating sorting)
    *   "Contains"
    *   "Visibility"
    *   "Scout"
*   **Repository Details:**
    *   "santoshsharma003/tds-project-one-1" (repository name)
    *   "2 days ago" (last pushed date)
    *   "IMAGE" (content type)
    *   "Public" (visibility)
    *   "Inactive" (Scout status)

**3. Context and Purpose:**

The UI is designed to allow users to:

*   View a list of their repositories within a specific namespace (santoshsharma003).
*   Search and filter repositories.
*   Create new repositories.
*   See details about each repository, including when it was last updated, what type of content it contains, its visibility settings, and its Scout status.
*   Navigate to other account-related settings (settings, default privacy, notifications, billing, usage).

**4. Technical Details:**

*   The UI elements suggest a web-based interface.
*   The "

---

## Reply 152
**Author**: Atishay
**Posted**: 2025-04-01T07:41:26.018Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/162

Dear team,

The evaluation shows that the Github repo was not found, however the repository has published and public.

**Image: 2025-04-01_13:10:20**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from a script or automated system, that evaluates the prerequisites for a "Project 1". It lists several checks related to Docker, GitHub, and licensing.

**2. Text Content:**

*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: FAIL"
*   "Is Dockerfile present in root of github repo: FAIL"
*   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. Context/Purpose:**

The purpose of the displayed information is to provide feedback on whether the necessary conditions (prerequisites) for a project have been met. It seems to be an automated check, indicating whether specific files or configurations are present and correctly set up. The "Project 1 Score" suggests this is part of an assessment or grading process.

**4. Technical Details:**

*   The checks are related to software development and deployment practices.
*   "Docker image present in dockerhub AND is public" refers to a containerized application image stored on Docker Hub (a public registry) and accessible to others.
*   "Github repo present AND public" refers to a code repository hosted on GitHub that is publicly accessible.
*   "Dockerfile present in root of github repo" refers to a file named "Dockerfile" located in the main directory of the GitHub repository. This file contains instructions for building a Docker image.
*   "MIT license present at root of github repo" refers to a file containing the MIT license, a permissive open-source license, located in the main directory of the GitHub repository.
*   The "PASS" and "FAIL" indicators show the outcome of each check. In this case, the Docker image check passed, but the GitHub repository, Dockerfile, and MIT license checks failed.
*   The overall "Prerequisites" status is "FAIL" because not all checks passed.
*   The "Project 1 Score" is 0, likely because the prerequisites were not met.

Github URL [GitHub - 22f3003029/llm_agent](https://github.com/22f3003029/llm_agent)

Roll Number: 22f3003029

Request your assistance on the issue.

Thank you

---

## Reply 153
**Author**: Anushka Kumar
**Posted**: 2025-04-01T07:56:15.782Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/163

Respected Team,

I received an email stating I failed to fulfil prerequisite and scored 0 because of it.

**Image: Screenshot 2025-04-01 132313**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from an automated evaluation system or script. It presents the results of prerequisite checks for a "Project 1" submission. The checks relate to the presence and accessibility of a Docker image, a GitHub repository, a Dockerfile, and an MIT license.

**2. Text Content:**

The image contains the following text:

*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: FAIL"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. Context and Purpose:**

The purpose of the displayed information is to inform a user (likely a student or developer) about the status of their submission for "Project 1". The system checks if certain prerequisites are met, such as having a public Docker image on Docker Hub, a public GitHub repository, a Dockerfile in the repository's root, and an MIT license. The "FAIL" or "PASS" status indicates whether each prerequisite is satisfied. The overall "Prerequisites" status is "FAIL", and the "Project 1 Score" is 0, indicating that the submission does not meet the minimum requirements and will likely not be graded.

**4. Technical Details:**

*   The image refers to Docker, a containerization platform, and Docker Hub, a repository for Docker images.
*   It also mentions GitHub, a popular platform for version control and collaborative software development.
*   The presence of a "Dockerfile" is checked, which is a text file containing instructions for building a Docker image.
*   The presence of an "MIT license" is checked, which is a permissive open-source license.
*   The evaluation system checks for the presence and public accessibility of the Docker image and GitHub repository.
*   The system also verifies the presence of the Dockerfile and MIT license in the root directory of the GitHub repository.

I checked my Docker Hub and there it is showing “Public”

**Image: Screenshot 2025-04-01 131944**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a table-like UI element, likely from a web application or dashboard. It displays information about a repository or project named "coolsisters7/llm". The table has columns for "Name", "Last Pushed", "Contains", "Visibility", and "Scout".

**2. Any text content visible:**

*   **Column Headers:** Name, Last Pushed, Contains, Visibility, Scout
*   **Repository Name:** coolsisters7/llm
*   **Last Pushed:** about 1 month ago
*   **Contains:** IMAGE (displayed within a pill-shaped button or label)
*   **Visibility:** Public
*   **Scout:** Inactive
*   **Arrow:** An upward pointing arrow next to "Last Pushed"

**3. The context or purpose of what's displayed:**

The UI is likely part of a repository management system (like GitHub, GitLab, or a similar platform). It provides a summary of the repository "coolsisters7/llm", including when it was last updated, what types of content it contains (in this case, images), its visibility setting (public), and the status of a "Scout" feature (inactive). The upward arrow next to "Last Pushed" likely indicates that the table is sorted by the "Last Pushed" column in ascending order.

**4. Technical details:**

*   The UI uses a dark theme.
*   The "Contains" column has a label indicating that the repository contains images. This suggests that the system can analyze the repository's contents and categorize them.
*   The "Scout" column indicates whether a feature called "Scout" is active or inactive for this repository. The purpose of the "Scout" feature is not clear from the image alone.

Can Anyone explain what I did wrong ?

---

## Reply 154
**Author**: Jayesh Bansal
**Posted**: 2025-04-01T08:32:10.438Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/164

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a document, likely a webpage or a document excerpt, that outlines the prerequisites for a "Project 1" and the results of an automated evaluation of those prerequisites. It's formatted as a message to a "Learner."

**2. Text Content:**

The text content can be broken down as follows:

*   **Greeting:** "Dear Learner,"
*   **Project Requirements:**
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (with "TDS Project 1: Evaluation" as a hyperlink).
    *   A numbered list of 5 requirements:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   **Evaluation Results:**
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of checks and their results:
        *   "Is Docker image present in dockerhub AND is public: FAIL"
        *   "Is Github repo present AND public: PASS"
        *   "Is Dockerfile present in root of github repo: PASS"
        *   "Is MIT license present at root of github repo: PASS"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context and Purpose:**

The document serves as feedback to a student or learner regarding their progress on "Project 1." It informs them of the specific requirements for the project and provides an automated evaluation of whether they have met those requirements. The evaluation results indicate that the learner has failed to meet all the prerequisites, specifically regarding the Docker image being present and public on

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface, likely from a container registry service (like Docker Hub, AWS ECR, or similar). It displays information about a Docker image repository. The UI elements include:

*   Repository name and details (last pushed date, repository size)
*   Tabs for different sections (General, Tags, Image Management, Collaborators, Webhooks, Settings)
*   Tag management features (sorting, filtering, deleting tags)
*   A list of tags with details (digest, OS/ARCH, last pull date, compressed size)
*   Docker commands for pushing and pulling images
*   A "Public view" button

**2. Any text content visible:**

*   **Repository Name:** jayeshbansal/tds\_project1
*   **Last Pushed:** Last pushed about 1 month ago
*   **Repository Size:** Repository size: 77 MB
*   **Add a description**
*   **Add a category**
*   **Tabs:** General, Tags, Image Management (BETA), Collaborators, Webhooks, Settings
*   **Sort by:** Newest
*   **Filter tags**
*   **Delete**
*   **TAG:** latest
*   **Last pushed about 1 month by** jayeshbansal
*   **Digest:** 2bdbd090a678
*   **OS/ARCH:** linux/amd64
*   **Last pull:** about 1 month
*   **Compressed size:** 77.02 MB
*   **Docker commands**
*   **To push a new tag to this repository:**
*   `docker push jayeshbansal/tds_project1:tagname`
*   `docker pull jayeshbansal/tds_project1:latest`
*   **Public view**
*   **Copy**

**3. The context or purpose of what's displayed:**

The image shows the "Tags" section of a Docker image repository. The purpose is to allow users to:

*   View available tags for the image.
*   See details about each tag (digest, OS/ARCH, last pull date, size).
*   Get the Docker commands needed to push new

Sir, I have the image in the docker and it is upload last month and it is public. So why have I received a message saying that the image is not available in the hub. Can you confirm and reevaluate the error.

@carlton @Jivraj @Saransh_Saini @s.anand

---

## Reply 155
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T08:39:32.875Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/165

Hi @Jayeshbansal ,

The docker repo name that you submitted through submission form was different than what your screenshot shows. `/jayeshbansal/add9a05689d3` docker repo doesn’t exists or might not be public, that’s why it failed for you.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a table-like UI element, likely from a code repository or project management tool. It displays information related to a specific user or submission, including timestamps, email addresses, GitHub repository links, and DockerHub image names. The UI also includes a search bar and standard file management icons (Raw, Copy, Download, Edit).

**2. Any text content visible:**

*   **Headers:** "Preview", "Code", "Blame", "Raw"
*   **File Information:** "1069 lines (1069 loc) • 127 KB"
*   **Search Bar:** "24f1001895@ds.study.iitm.ac.in" (as a search query)
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Data (Row 1022):**
    *   "2/16/2025 23:55:44"
    *   "24f1001895@ds.study.iitm.ac.in"
    *   "https://github.com/jayesh-bansal/TDS-Project1/"
    *   "jayeshbansal/add9a05689d3"

**3. The context or purpose of what's displayed:**

The image likely represents a log or record of submissions or contributions to a project. It seems to be tracking information about where the code for "Project 1" is located (GitHub) and where the corresponding Docker image is hosted (DockerHub). The search bar suggests the ability to filter or find specific entries based on email address. The "Blame" tab suggests this might be related to code authorship or history.

**4. Technical details (if it's a code screenshot or technical diagram):**

While not a code screenshot or diagram, the information presented is technically relevant. It shows:

*   **GitHub Repository URL:** A standard URL format

---

## Reply 156
**Author**: Joel Jeffrey
**Posted**: 2025-04-01T08:57:06.531Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/166

The log file provided to me too contains File not found error for task A. However, running the code on the evaluate.py files gave me results. Could you please look into the datagen part?

@carlton @Jivraj

Thanks

---

## Reply 157
**Author**: Vansh Mittal
**Posted**: 2025-04-01T09:08:59.871Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/168

It is the request to the team,to consider this since it is a problem of just a case letter otherwise the whole hardwork of doing the project will be wasted.

Thank you

---

## Reply 158
**Author**: PalakAnand
**Posted**: 2025-04-01T09:16:36.251Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/169

Dear instructors, I received the mail today regarding project 1 TDS scores and I have been marked fail because the MIT license is not present. But as can be seen in the screenshot below the MIT license file is present in my GitHub repository. Pls look into this matter.

**Image: Screenshot 2025-04-01 at 2.45.57 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository's main page. It shows the file structure and commit history of a project named "Project1-TDS". The UI elements include:

*   Repository name and visibility (Public)
*   Branch selection dropdown (currently on "main")
*   Branch and tag counts (1 branch, 0 tags)
*   File search bar ("Go to file")
*   "Code" button (green) with a dropdown menu
*   List of files and directories with commit messages and timestamps
*   Unpin and Unwatch buttons

**2. Text Content:**

*   **Project1-TDS:** The name of the repository.
*   **Public:** Indicates the repository is publicly accessible.
*   **main:** The currently selected branch.
*   **1 Branch:** Number of branches in the repository.
*   **0 Tags:** Number of tags in the repository.
*   **Go to file:** Placeholder text in the file search bar.
*   **Code:** Text on the main action button.
*   **PalakAnand30:** The username of the committer.
*   **Rename LICENSE to MIT LICENSE:** A commit message.
*   **ab381b5:** The short commit hash.
*   **5 Commits:** Number of commits in the repository.
*   **_pycache_:** A directory name.
*   **app:** A directory name.
*   **.DS_Store:** A file name.
*   **Dockerfile:** A file name.
*   **MIT LICENSE:** A file name.
*   **datagen.py:** A file name.
*   **evaluate.py:** A file name.
*   **requirements.txt:** A file name.
*   **Initial commit:** A commit message.
*   **committing final files:** A commit message.
*   **Rename dockerfile to Dockerfile:** A commit message.
*   **2 months ago:** Timestamps indicating when the files were last modified.
*   **Unpin**
*   **Unwatch 1**

**3. Context and Purpose:**

The image displays the contents of a GitHub repository, allowing users to browse

---

## Reply 159
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T09:23:59.524Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/170

It depends where you tested it running, if it’s running inside a docker container and you feel there is problem with our script then you can debug our code and create a pull request on repo.

---

## Reply 160
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T09:25:28.846Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/171

Hi @24ds2000125

You didn’t meet the standard naming convention for mit license naming.  Name should be LICENSE(all caps) or LICENSE.md.

check this out.

[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

## Reply 161
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T09:27:50.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/172

Hi @22f3001851

Standard naming convention for Dockerfile name was not followed we won’t be able to evaluate it.

---

## Reply 162
**Author**: Shreyan Chaubey
**Posted**: 2025-04-01T09:37:21.052Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/173

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a list of checks or tests, likely related to a software project or assignment. Each line represents a specific criterion, and the result of the check (PASS or FAIL) is indicated. There's also a final score for "Project 1".

**2. Text Content:**

*   "Is Docker image present in dockerhub AND is public: FAIL" (This line is circled in red)
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL" (This line is underlined in red)
*   "Project 1 Score: 0"
*   "???" (Handwritten in red)

**3. Context/Purpose:**

The image appears to be a status report or checklist for a project. It's assessing whether certain conditions are met, such as the presence of a Docker image on Docker Hub, a public GitHub repository, a Dockerfile, and an MIT license. The "Prerequisites" and "Project 1 Score" suggest this is part of a grading or evaluation process. The handwritten "???" suggests confusion or a question about one of the PASS results.

**4. Technical Details:**

*   The checks relate to Docker and GitHub, indicating a project involving containerization and version control.
*   The presence of a Dockerfile and MIT license are common practices in software development.
*   The "dockerhub" reference indicates the use of Docker's public registry.

My email is 22f3001642@ds.study.iitm.ac.in

@Jivraj  Could you please check what’s wrong?

---

## Reply 163
**Author**: Pradeep Mondal
**Posted**: 2025-04-01T09:39:25.986Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/174

@Jivraj @carlton @Saransh_Saini any updates for the people like me whose image was run on the wrong architecture - mine was ARM ( was evaluated or ×86 ). I filled the form that was later sent for selecting the architecture.

I haven’t received any mail since then. But found many mails are sent to others in while.

---

## Reply 164
**Author**: Mayank Singh
**Posted**: 2025-04-01T09:55:48.188Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/175

**Image: Screenshot 2025-04-01 at 3.17.14 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository interface. It displays the file structure of a repository named "tds-trail-1" owned by the user "Mayank8IITM". The interface includes standard GitHub elements like navigation tabs (Code, Issues, Pull requests, etc.), branch selection, file listing, and commit history.

**2. Any text content visible:**

*   **Repository Information:**
    *   "Mayank8IITM / tds-trail-1" (Repository path)
    *   "tds-trail-1" (Repository name)
    *   "Public" (Repository visibility)
    *   "main" (Current branch)
    *   "1 Branch"
    *   "0 Tags"
*   **File Listing:**
    *   "\_pycache\_" (Directory)
    *   "data" (Directory)
    *   ".dockerignore" (File)
    *   "Dockerfile" (File)
    *   "LICENSE" (File)
    *   "README.md" (File)
    *   "datagen.py" (File)
    *   "evaluate.py" (File)
    *   "main.py" (File)
    *   "requirements.txt" (File)
*   **Commit Messages:**
    *   "Rename dockerfile to Dockerfile"
    *   "Project is done 7/10"
    *   "updated dockerfile"
    *   "Create LICENSE"
    *   "Create README.md"
    *   "A2 and A9 left"
    *   "added dockerfile"
*   **Other UI Elements:**
    *   "Code" (Tab selected)
    *   "Issues"
    *   "Pull requests"
    *   "Actions"
    *   "Projects"
    *   "Wiki"
    *   "Security"
    *   "Insights"
    *   "Settings"
    *   "Type to search" (Search bar placeholder)
    *   "Pin"
    *   "Unwatch"
    *   "Go to file"
    *   "

**Image: Screenshot 2025-04-01 at 3.19.32 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a report or evaluation of prerequisites for a project, likely a coding project. It lists several criteria related to Docker, GitHub, and licensing, and indicates whether each criterion has been met (PASS) or not (FAIL).

**2. Any text content visible:**

*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: FAIL"
*   "Is Dockerfile present in root of github repo: FAIL"
*   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"
*   "CS2006B - MAD2 Project - Ann"

**3. The context or purpose of what's displayed:**

The purpose is to provide feedback on whether the necessary components (Docker image, GitHub repository, Dockerfile, MIT license) are correctly set up for "Project 1". The evaluation checks for the presence and accessibility (public) of the GitHub repository and Docker image, as well as the existence of a Dockerfile and MIT license in the root directory of the GitHub repository. The overall "Prerequisites" status is FAIL, and the "Project 1 Score" is 0, indicating that the project cannot proceed without meeting the prerequisites.

**4. Technical details:**

*   **Docker:** The evaluation checks if a Docker image is present in Docker Hub and if it's publicly accessible.
*   **GitHub:** The evaluation checks if a GitHub repository exists and if it's publicly accessible. It also checks for the presence of a "Dockerfile" and an "MIT license" in the root directory of the repository.
*   **Dockerfile:** A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
*   **MIT License:** The MIT License is a permissive free software license, meaning it grants recipients broad rights to use, modify, and distribute the software.

Sir , I received the mail today regarding project 1 TDS scores and I have been marked fail because my repo is not public , and no docker file , no licence . but they all are present in my repo , and it is public too , , i am attaching the screenshot , you can see that too ,

My email is 23f1000598@ds.study.iitm.ac.in

Could you please check what’s wrong?

@Jivraj @Saransh_Saini @carlton

---

## Reply 165
**Author**: Carlton D'Silva
**Posted**: 2025-04-01T10:06:03.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/176

The task B6 was

[https://quotes.toscrape.com/](https://quotes.toscrape.com/) has quotes from famous people.

The .author class has the quote author’s name.

Extract and save all authors from the first page, in order, to /data/b6.json as an array of strings.

E.g. `["Douglas Adams", "J.K. Rowling", ...]`

The output in your file is not an array of double quoted strings.

Instead it is an array of an json object with the keyword author and values as an array of authors.

These are two different things. Almost there but not quite.

Kind regards

---

## Reply 166
**Author**: RAJ K BOOPATHI
**Posted**: 2025-04-01T10:15:47.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/177

Hi Course Team,

I have also received an email today saying that my Project1 failed. But few days back I received an email with evaluation log saying I got 8/20. Which one is true?

**Image: 1000112508**
Here's a detailed description of the image:

**Overall Content:**

The image is a screenshot of an email. The email is titled "TDS Jan 25 Project 1 Scores" and is an automated message providing feedback on a student's (or learner's) Project 1 submission. The email details prerequisite checks for the project and provides a score based on whether those prerequisites were met.

**UI Elements:**

*   **Email Header:** Shows the subject "TDS Jan 25 Project 1 Scores" and the "Inbox" label, indicating it's from an email client. There's also a star icon (likely for favoriting or marking the email).
*   **Sender Information:** Displays the sender as "22t1 se2002" and the timestamp "1:24 am". There's an avatar with the number "2" in it. The email is addressed "to me".
*   **Reply/More Options Icons:** Standard email icons for replying and accessing more options (three vertical dots).

**Text Content:**

*   **Subject:** "TDS Jan 25 Project 1 Scores"
*   **Salutation:** "Dear Learner,"
*   **Introduction:** Explains that Project 1 requires passing prerequisite checks, with a link to the "TDS Project 1: Evaluation" page.
*   **Prerequisite List:**
    1.  "Your GitHub repository exists and is publicly accessible"
    2.  "Your GitHub repository has a LICENSE file with the MIT license"
    3.  "Your GitHub repository has a valid Dockerfile"
    4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
    5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   **Warning:** "If you fail to meet this minimum requirement your submission will not get evaluated."
*   **Evaluation Results:**
    *   "Is Docker image present in dockerhub AND is public: PASS"
    *   "Is Github repo present AND public: PASS"
    *   "Is Dockerfile present in root of github repo: FAIL"
    *   "Is MIT

---

## Reply 167
**Author**: RAJ K BOOPATHI
**Posted**: 2025-04-01T10:18:11.331Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/178

Can someone from TA team reply to this?

---

## Reply 168
**Author**: Suhani Dubey
**Posted**: 2025-04-01T12:38:17.909Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/179

can somebody tell me how the dockerfile not running in 5 mins is my fault? i had the same requirements.txt as many other people and their file ran in given time while mine did not. what was the need for this, sorry for my harsh words but i’m frustrated, stupid rule?

---

## Reply 169
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T12:58:31.631Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/180

For your case there was problem with our script that, we have correct, and your submission have dockerfile, license and repo exisits as well, it will be evaluated.

---

## Reply 170
**Author**: ashish al rashid
**Posted**: 2025-04-01T13:11:55.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/181

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a list of prerequisite evaluations for "Project 1". Each evaluation is a statement about the presence and accessibility of certain files or resources, followed by a "PASS" or "FAIL" status.

**2. Any text content visible:**

The text content is as follows:

*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: FAIL"
*   "Is MIT license present at root of github repo: PASS"

**3. The context or purpose of what's displayed:**

The image shows the results of automated checks performed to ensure that a project meets certain requirements before it can proceed. These requirements relate to Docker images, GitHub repositories, and the presence of specific files (Dockerfile and MIT license) in the repository. The "PASS" or "FAIL" status indicates whether each requirement has been met.

**4. Technical details:**

The evaluations suggest a software development project that involves Docker and GitHub. The checks are likely automated as part of a continuous integration or continuous delivery (CI/CD) pipeline or a similar automated assessment process. The checks are verifying:

*   The existence and public accessibility of a Docker image on Docker Hub.
*   The existence and public accessibility of a GitHub repository.
*   The presence of a `Dockerfile` in the root directory of the GitHub repository.
*   The presence of an `MIT license` file in the root directory of the GitHub repository.

The project has passed the checks for Docker image and GitHub repository presence and public accessibility, as well as the presence of an MIT license. However, it has failed the check for the presence of a `Dockerfile` in the root of the repository.

my dockerfile is available in github, Please look into the issue

Thank you

---

## Reply 171
**Author**: LAKSHAY
**Posted**: 2025-04-01T13:14:42.027Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/182

@Jivraj

I also have same issue, can you check this…

[Repo link](https://github.com/21f3001076/TDS_Project_1)

**Image: 1000431136**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Top Bar:**
    *   A dropdown menu labeled "main" (likely indicating the current branch of a repository).
    *   A "Code" dropdown button (suggesting options for downloading or interacting with the code).
    *   An ellipsis icon (three dots) indicating more options.
*   **Repository Information:**
    *   A user icon and username "lakshay654" with the text "2 months ago" (likely indicating the last commit or update by this user).
    *   Icons and filenames: "Dockerfile", "LICENSE", "README.md", "app.py", "requirements.txt", "task\_handler.py" each with the text "2 months ago" (indicating the files in the repository and when they were last updated).
    *   Icons for comments and history.
*   **Tab Bar:**
    *   Tabs labeled "README" (selected) and "MIT license".
    *   Icons for editing and listing.
*   **Content Area:**
    *   The content area displays the content of the selected "README" tab.

**2. Text Content:**

*   "main" (branch name)
*   "Code"
*   "lakshay654"
*   "2 months ago"
*   "Dockerfile"
*   "LICENSE"
*   "README.md"
*   "app.py"
*   "requirements.txt"
*   "task\_handler.py"
*   "README"
*   "MIT license"
*   "TDS Project 1 -"
*   "LLM-based"
*   "Automation Agent"
*   "Create an API"

**3. Context and Purpose:**

The image shows a view of a code repository, likely on a platform like GitHub or GitLab. It displays the file structure, recent activity, and the content of the README file. The README file provides a description of the project, which is "TDS Project 1 - LLM-based Automation Agent". It also mentions "Create an API".

**4. Technical Details:**

*   The presence of "Dockerfile" suggests the project is containerized (likely using Docker).
*   "requirements.txt

---

## Reply 172
**Author**: Shreyan Chaubey
**Posted**: 2025-04-01T13:40:53.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/183

@carlton @Jivraj My P1 submission successfully passed all the basic sanity checks on February 15th and obtained a satisfactory score in the P1 evaluation, which was disclosed on March 29th. However, I received a communication today, April 1, stating that my Docker image is not present or public on DockerHub. I kindly request the TDS course team to investigate this matter at the earliest and provide a resolution for students encountering similar issues.

This situation is particularly disheartening—**seeing days of effort and dedication to Project 1 reduced to nothing, especially given the already demanding pace of the course.**

I will appreciate your prompt attention to this matter.

Kind regards

---

## Reply 173
**Author**: Jayesh Bansal
**Posted**: 2025-04-01T14:40:02.251Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/184

I understand the problem. It may be possible that the image id i gave may be different as i had multiple dockerfile and there is a possibility that i gave the wrong image id due to some confusion. Is it possible for reevaluation. I have worked very hard and I don’t want to lose my marks because of some wrong id misconfusion. I request to check my dockerfile once again and provide the marks accordingly

---

## Reply 174
**Author**: Afsal
**Posted**: 2025-04-01T14:49:37.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/185

dear @carlton @Jivraj @Saransh_Saini

Dear Sirs,

I have seen that many others have posted similar issues to mine, and you have responded to some of them. To seek your attention, I am replying to this thread.

Please consider my request as well, as I do not want to lose marks on a project I have worked hard on, while also helping others. I am expecting a timely and positive response from your end.

Thank you.

---

## Reply 175
**Author**: Rahul Pathak
**Posted**: 2025-04-01T15:14:23.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/186

Dear Sir,

I hope you’re doing well. I haven’t received any email regarding the results of Project 1. Could you please check if my result was sent or if there’s any update on this?

I would really appreciate your confirmation.

Mail id - 23f2000798@ds.study.iitm.ac.in

---

## Reply 176
**Author**: Sujith Sai K
**Posted**: 2025-04-01T15:23:46.604Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/187

@carlton

Respected Sir,

I have submitted my project following all the guidelines and fulfilling all the prerequisites. My docker file is available publicly and it is present in the root directory of github repo, still the mail says that the file is missing and my score is zero. Can you please look into this issue

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a list of files and associated metadata, likely from a code repository or file management system. The UI elements include file icons, file names, version information, and timestamps indicating when the files were last modified. The background is a dark color, typical of a dark mode interface.

**2. Any text content visible:**

The text content includes:

*   **File names:**
    *   `datagen.py`
    *   `dockerfile`
    *   `evaluate.py`
    *   `requirements.txt`
    *   `tasksA.py`
    *   `tasksB.py`
*   **Version/Commit messages:**
    *   `v1`
    *   `docker updatae`
    *   `v1.1`
*   **Timestamps:**
    *   `2 months ago` (repeated for each file)

**3. The context or purpose of what's displayed:**

The image likely shows a view of files within a directory or repository. The "version/commit messages" column provides a brief description of the last change made to each file. The timestamps indicate the last modification date. This is a common way to display files in a code repository (like GitHub, GitLab, or Bitbucket) or a file explorer with version control integration.

**4. Technical details:**

*   The `.py` extension indicates that `datagen.py`, `evaluate.py`, `tasksA.py`, and `tasksB.py` are Python source code files.
*   `dockerfile` is a file used to define a Docker image, which is a containerized environment for running applications.
*   `requirements.txt` is a file that lists the Python packages required to run a project. It's used by package managers like `pip` to install dependencies.
*   The presence of these files suggests a software development project, likely involving Python and Docker.
*   The versioning information (e.g., `v1`, `v1.1`) suggests that the project is under some form of version control.

---

## Reply 177
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T16:47:18.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/188

Name of your dockerfile doesn’t match the standard’s.

It should be `Dockerfile`(with D caps).

---

## Reply 178
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T16:48:19.889Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/189

No we are doing another run of evaluations. Results will be sent soon.

---

## Reply 179
**Author**: Vaddi Yaswanth
**Posted**: 2025-04-01T16:48:22.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/190

dockerfile name should be Dockerfile as this is the standard they are considering .so it was not evaluated you better change that, if they revaluate it will be passed

---

## Reply 180
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T16:51:25.206Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/191

Your submission have Dockerfile, LICENSE and repo exists as well, we found some problems because of redirects not handled in our script.

Your submission will be evaluated.

---

## Reply 181
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T16:53:06.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/192

We won’t be considering changes after deadline, our script looks for commits before deadline and fetches latest commits before deadline.

---

## Reply 182
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T16:54:41.830Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/193

That’s not possible, anything after deadline is not appreciated.

---

## Reply 183
**Author**: Vaddi Yaswanth
**Posted**: 2025-04-01T16:54:55.948Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/194

We have updated just files names will it be considered??

---

## Reply 184
**Author**: Veer Shah
**Posted**: 2025-04-01T16:55:11.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/195

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . @carlton sir . @Jivraj [GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.

**Image: 1000105386**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email. The email appears to be an automated message providing feedback on a student's (the "Learner") submission for "Project 1". The email details the prerequisites for the project and the results of automated checks performed on the student's submission.

**2. Text Content:**

The email contains the following text:

*   **Header:** "22t1 se2002 1:27 am to me" (This indicates the sender and timestamp of the email)
*   **Salutation:** "Dear Learner,"
*   **Body:**
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:"
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of checks and their results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context and Purpose:**

The email's purpose is to inform the student about the status of their Project 1 submission. It outlines the required criteria and provides feedback on whether the submission meets those criteria. The automated checks seem to be verifying the presence and accessibility of

---

## Reply 185
**Author**: Shashikumar Kohir
**Posted**: 2025-04-01T17:13:03.760Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/197

:cross_mark:  Did Not Receive Project 1 Score – Need Clarification

**Post Content:**

**Hello, sir**   @carlton @Jivraj

I received the evaluation email for my **Project 1 Docker Image** submission, but unlike my friend (who got an email with his score), my email did **not** include my score.

My Docker image ID: **6f446c9b84da**

The email I received only contains logs and attachments, but no information about my actual score. in the mail recieved by my friend the score is clearly mentioned,

I would really appreciate it if you could **clarify my project score** and let me know if it was properly evaluated. If there is any issue, I request a reconsideration of my project evaluation.

Thank you for your help!

**Attachments:**

but in the email which i recieved i got the below thing , there is no information about the project score

**Image: my email without score**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email. The email appears to be an evaluation report for a project submission, specifically a Docker image. The email lists several files related to the evaluation, indicates whether they were found, and provides a link to one of the files. It also discusses the performance of the Docker image and the scoring process.

**2. Text Content:**

*   **Sender:** 22t1 se2002
*   **Recipient:** to me
*   **Subject:** (Implied) Evaluation of Docker Image Submission
*   **Date:** Mar 29, 2025, 12:17 AM (3 days ago)
*   **Body:**
    *   Greeting: "Dear Learner,"
    *   Introduction: "We have evaluated your project 1 docker image submission. Please find the following files."
    *   Explanation of "MISSING": "MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us. MISSING files will result in a score of 0."
    *   Performance expectations: "Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet."
    *   List of files:
        1.  "Evaluation log file. MISSING This contains your performance report on your individual tasks."
        2.  "Docker log file. [Google Drive Link] This provides the technical performance of your container."
        3.  "Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests."
        4.  "Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism."
        5.  "Data generation file (See attachment

sir could you please clarify about my project score ???

waiting for the response

---

## Reply 186
**Author**: SAKSHI PATHAK
**Posted**: 2025-04-01T17:14:28.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/198

I am also facing the same issue sir please provide proper answer for our query. Please consider to recheck the project once again.

Docker image - 5ff55c499b54

**Image: 1000161685**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email on a mobile device. The email is a feedback message regarding a Docker image submission for a project. The email details the evaluation results, highlighting missing files and performance expectations. The email also lists several files related to the evaluation process, some of which are missing.

**2. Text Content:**

*   **Email Header:**
    *   Sender: 22t1 se2002 (sent 3 days ago)
    *   Recipient: "to me"
*   **Email Body:**
    *   Greeting: "Dear Learner,"
    *   Evaluation Summary: The email states that the project 1 Docker image submission has been evaluated. It indicates that some files are missing, which will result in a score of 0.
    *   Missing File Explanation: "MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured."
    *   Responsiveness Requirement: "Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it."
    *   Server Specifications: "The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet."
    *   List of Files:
        1.  "Evaluation log file. MISSING This contains your performance report on your individual tasks."
        2.  "Docker log file. [Google Drive URL] This provides the technical performance of your container."
        3.  "Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests."
        4.  "Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism."
        5.  "Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks."
        6.  "Docker orchestration file (See attachment). This file handles the retrieval of your

@carlton , @Jivraj , @Saransh_Saini

---

## Reply 187
**Author**: Jayaram
**Posted**: 2025-04-01T17:32:53.177Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/199

@carlton @Jivraj

Got a email stating that prereq failed stating below..

Is Docker image present in dockerhub AND is public: FAIL

but i can see that image is public as shown below image.. am i missing something..

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a table or list-like UI element, likely from a web application or platform related to software development or cloud services. It displays information about a project or repository. The table has four columns: "Name", "Last Pushed", "Contains", and "Visibility". There is one row of data visible.

**2. Any text content visible:**

*   **Column Headers:**
    *   Name
    *   Last Pushed
    *   Contains
    *   Visibility
*   **Row Data:**
    *   Name: rsjay1976/tds-project1-jan25
    *   Last Pushed: 2 days ago
    *   Contains: IMAGE (displayed in a pill-shaped badge)
    *   Visibility: Public

**3. The context or purpose of what's displayed:**

The UI appears to be displaying a list of projects or repositories. The "Name" column shows the name of the project. "Last Pushed" indicates the last time changes were uploaded to the repository. "Contains" likely indicates the type of content within the repository (in this case, an image). "Visibility" indicates whether the project is publicly accessible or private. The blue upward-pointing arrow next to "Last Pushed" suggests that the list is currently sorted by the "Last Pushed" column in ascending order.

**4. Technical details:**

The UI is likely rendered using HTML and CSS. The "IMAGE" element is styled as a badge, which is a common UI pattern. The data is structured in a tabular format, suggesting it could be retrieved from a database or API. The use of "2 days ago" indicates relative time formatting.

---

## Reply 188
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T17:35:45.124Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/200

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.

tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) <= DEADLINE
                ),
                (None, 0),
            )

This is part of our script that does the validation check for docker repo.

---

## Reply 189
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-01T17:47:02.771Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/201

Sir,

The License file is present in the github repository however i received a mail that said that it was absent.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository's file listing. It shows the user interface of a GitHub repository, displaying the files and folders within the repository, along with commit information and other repository details.

**2. Text Content Visible:**

*   **Repository Name:** `tds_project-1` (marked as "Public")
*   **Branch:** `main` (1 Branch, 0 Tags)
*   **File/Folder Names:**
    *   `_pycache_` (folder)
    *   `venv` (folder)
    *   `Dockerfile` (file)
    *   `LICENSE` (file)
    *   `MIT LICENSE` (file)
    *   `app.py` (file)
    *   `requirements.txt` (file)
    *   `test.txt` (file)
*   **Commit Messages:**
    *   `Create LICENSE`
    *   `Final Submission`
    *   `First submission`
    *   `Rename LICENSE to MIT LICENSE`
*   **Commit Hash:** `22f3000585`
*   **Other Text:**
    *   "Go to file" (search bar placeholder)
    *   "Add file" (button)
    *   "Code" (button)
    *   "Pin"
    *   "Unwatch"
    *   "6 Commits"
    *   "now"
    *   "2 months ago"

**3. Context and Purpose:**

The image shows the contents of a GitHub repository. The purpose is to allow users to browse the files, view commit history, and potentially contribute to the project. The UI elements provide functionality for searching files, adding new files, downloading the code, and managing the repository (pinning, watching).

**4. Technical Details:**

*   The presence of `requirements.txt` and `app.py` suggests that this is likely a Python project.
*   The `venv` folder indicates a virtual environment for managing Python dependencies.
*   The `Dockerfile` suggests that the project is containerized using Docker.
*   The `LICENSE` and `MIT LICENSE` files

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from an automated evaluation system. It presents a series of checks or prerequisites for a "Project 1" submission. The checks relate to the presence and accessibility of a Docker image, a GitHub repository, a Dockerfile, and an MIT license.

**2. Text Content:**

*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. Context and Purpose:**

The image displays the results of an automated check for a project submission. It indicates whether the submission meets the minimum requirements based on the presence of specific files and configurations (Docker image, GitHub repo, Dockerfile, MIT license). The overall "Prerequisites" status is "FAIL," and the "Project 1 Score" is 0, suggesting that the submission did not meet all the necessary criteria.

**4. Technical Details:**

*   The checks are related to software development and deployment practices, specifically using Docker and GitHub.
*   The "Dockerfile" is a text file that contains instructions for building a Docker image.
*   The "MIT license" is a permissive open-source license.
*   The evaluation checks if the Docker image is available on Docker Hub and is publicly accessible.
*   The evaluation checks if the GitHub repository is present and publicly accessible.
*   The evaluation checks if the Dockerfile and MIT license are present in the root directory of the GitHub repository.

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.

Can you please look into it. Thankyou!

---

## Reply 190
**Author**: LAKSHAY
**Posted**: 2025-04-01T17:48:50.614Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/202

@Jivraj

Can you also clarify my issue?

My submission meets all the prerequisites according to my Git repository and Docker image. Additionally, I can see the results in the evaluation log.

You can check the details in the images below. Screenshot of mail and repository

Roll no. : 21f3001076

[GitHub Repo link](https://github.com/21f3001076/TDS_Project_1)

**Image: 1000431410**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a report or evaluation summary, likely from an automated system, regarding the prerequisites for a "Project 1". It lists several checks related to Docker and GitHub, along with their pass/fail status.

**2. Text Content:**

*   **Title:** "These are your Project 1 Prerequisite evaluations:"
*   **Evaluation Items:**
    *   "Is Docker image present in dockerhub AND is public: PASS"
    *   "Is Github repo present AND public: FAIL"
    *   "Is Dockerfile present in root of github repo: FAIL"
    *   "Is MIT license present at root of github repo: FAIL"
*   **Summary:**
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context/Purpose:**

The image shows the results of an automated check to ensure that certain prerequisites are met before a student or developer can proceed with "Project 1". These prerequisites involve having a Docker image available on Docker Hub, a public GitHub repository, a Dockerfile in the repository's root directory, and an MIT license file also in the root directory. The overall "Prerequisites" status is FAIL, and the "Project 1 Score" is 0, indicating that the project cannot proceed until the failed prerequisites are addressed.

**4. Technical Details:**

*   The image suggests a software development or DevOps context.
*   It involves the use of Docker (containerization) and GitHub (version control and code hosting).
*   The checks are likely automated, possibly as part of a continuous integration/continuous deployment (CI/CD) pipeline or a pre-submission validation process.
*   The MIT license is a common open-source license.
*   The "Dockerfile" is a text document that contains all the commands a user could call on the command line to assemble an image.

**Image: 1000431413**
Here's a detailed description of the image:

**1. Content Overview:**

The image shows a text-based output, likely from a system or application providing information about log files. It lists three different log files with descriptions and links to access them. The background is dark, and the text is white.

**2. Text Content:**

*   **Headline:** "Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet."
*   **Log File 1:**
    *   "1. Evaluation log file."
    *   "https://drive.google.com/file/d/1AO_ycjKpZCPzaiiEHqSMGBYGg/view?usp=drivesdk" (Some parts of the URL are obscured by a red line)
    *   "This contains your performance report on your individual tasks."
*   **Log File 2:**
    *   "2. Docker log file."
    *   "https://drive.google.com/file/d/1W3gD9x8woaemahTQdtx-ovkg3z9yL/view?usp=dm.cok" (Some parts of the URL are obscured by a red line)
    *   "This provides the technical performance of your container."
*   **Log File 3:**
    *   "3. Server start log file (separate logs for arm vs x86) (See attachment)."
    *   "If your docker service did not start or respond to attempts to our" (The sentence is incomplete)

**3. Context and Purpose:**

The image appears to be part of a system or application output that provides users with access to log files for debugging or performance analysis. The initial statement about network bandwidth suggests this might be related to a cloud service or a system with high-performance requirements. The log files cover evaluation, Docker container performance, and server startup, indicating a focus on application deployment and execution.

**4. Technical Details:**

*   **Log Files:** The image references three types of log files:
    *   **Evaluation Log:** Likely contains data related to the performance of individual tasks or processes.
    *   **Docker Log:** Provides information about the technical performance of a Docker container.
    *   **Server Start Log:** Contains logs related

**Image: 1000431415**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Dropdown Menus:** There are two dropdown menus at the top. The first one, labeled "main," likely represents the current branch of a code repository. The second one, labeled "Code," probably allows the user to download or view the code in different formats.
*   **Repository Listing:** A list of files and directories is displayed. Each entry shows the file name (e.g., "Dockerfile," "LICENSE," "README.md") and the last modified date ("2 months ago").
*   **User Information:** The username "lakshay654" is displayed, along with the time since the last activity ("2 months ago").
*   **Tabs:** There are two tabs selected: "README" and "MIT license".
*   **Icons:** There are icons for editing and listing.

**2. Text Content:**

*   **File Names:** Dockerfile, LICENSE, README.md, app.py, requirements.txt, task\_handler.py
*   **Timestamps:** "2 months ago" (repeated for each file)
*   **Username:** lakshay654
*   **Project Title:** "TDS Project 1 - LLM-based"
*   **Branch:** main
*   **Code**

**3. Context/Purpose:**

The image appears to be a screenshot of a code repository, likely from a platform like GitHub or GitLab. It shows the file structure of a project, the last modified dates, and the project's README content. The project is named "TDS Project 1" and is "LLM-based," suggesting it involves Large Language Models.

**4. Technical Details:**

*   The presence of "Dockerfile" suggests the project is containerized using Docker.
*   "requirements.txt" indicates a Python project, as this file typically lists the project's dependencies.
*   "app.py" and "task\_handler.py" are likely Python source code files.
*   "LICENSE" indicates the project's licensing terms.
*   "README.md" contains the project's description and instructions.

---

## Reply 191
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T17:49:39.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/203

Standard name of dockerfile is Dockerfile that’s why it didn’t pass Dockerfile check

---

## Reply 192
**Author**: Sirimilla Karthik Balaji
**Posted**: 2025-04-01T18:24:32.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/204

@Jivraj @carlton

I understand sir Dockerfile name was misspelt sir. Since my Docker image was built and recognized, I didn’t realize this would prevent evaluation.

I worked hard on this project sir, and my Docker image was built successfully. Please consider my submission sir.

---

## Reply 193
**Author**: Ansh
**Posted**: 2025-04-01T18:24:46.558Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/205

I  have been trying to resolve all the errors but just noticed that my docker image id associated with the project is “c9dc7fbcf405” , meanwhile the mail I received mentions that some other image id was evaluated.

Can you please look into this matter and evaluate the correct Image ID.

Roll number: 23F1001012

@carlton @Jivraj

---

## Reply 194
**Author**: Shreyan Chaubey
**Posted**: 2025-04-01T19:02:11.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/206

@Jivraj @Carlton I completely understand that changes to the Docker image after the deadline cannot be accepted.

***However, there are specific cases like mine where the Project 1 submission successfully passed the sanity checks on Feb 15 and received a decent score when the evaluation results were released on Mar 29.***

**Image: image**
Here's a detailed description of the image content:

**1. Overall Content:**

The image shows a list of files and descriptions related to a Docker container evaluation. It appears to be documentation or instructions for accessing and understanding the results of an evaluation process.

**2. UI Elements:**

The image presents a numbered list, suggesting a structured set of resources or steps. The list items are formatted with a number, a title (e.g., "Evaluation log file"), and a description. Some items include hyperlinks.

**3. Text Content:**

*   **Introductory Text:** "available which is nearly 5 times faster than the fastest domestic internet."
*   **List Items:**
    1.  "Evaluation log file." Followed by a Google Drive URL: "https://drive.google.com/file/d/1GYe44D8gieDOlu9dCrKdsKwVAQ7i\_C-N/view?usp=drivesdk". Description: "This contains your performance report on your individual tasks."
    2.  "Docker log file." Followed by a Google Drive URL: "https://drive.google.com/file/d/1VTVeD-lwg3CFPFUYAcUqNzaGD7MlzyeC/view?usp=drivesdk". Description: "This provides the technical performance of your container."
    3.  "Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests."
    4.  "Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism."
    5.  "Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks."
    6.  "Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications."
    7.  "Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core concepts of

But here’s the catch:** Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:*

Implementing a ReAct-based workflow planning & orchestration agent, inspired by the paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).
Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.
Enhancing Shell-use & Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.
Adding useful API endpoints, including an **`/api/`** multipart/form endpoint, alongside the existing **`/read`** and **`/run`** endpoints from Project 1, plus a **`/clear`** endpoint to reset the agent’s conversation memory if the context window gets saturated.
**Deploying the entire project on a paid GCP VM Instance with a static IP**, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.

All this hard work evolved my project into something far beyond a simple Tool-Calling Agent—it essentially became a ReAct Principles based Computer-Using Agent capable of executing complex, non-linear workflows entirely within a container. And I’m not exaggerating: You could ask it to perform something like **hyperparameter tuning for a Random Forest Classifier, offloading the results locally on a JSON file and displaying its contents**, and it would do that for you—without **ever** declining the request. I like to think of it as a **terminal version of** [OpenAI’s Computer-Using Agent](https://openai.com/index/computer-using-agent/).

Given all the effort, time, and money that went into this, it’s incredibly discouraging to see my project **naturally fail a sanity check (Docker image digest mismatch) (because of the aforesaid updates)** and not get evaluated as a result. This is not the kind of experience that encourages students to learn, experiment, and innovate.

To clarify, **all the updates mentioned above took place after March 29**, **after Project 1 had already been evaluated, and results had been handed out.** Furthermore, we were **never informed** that a reevaluation would take place on April 1. Had I known, I would have ensured that my original submission remained unchanged and considered creating a duplicate of my Docker image and implementing all the aforementioned enhancements on it.

My only request is that if my **updated P1 submission cannot be evaluated** due to the changes made after March 29 (before the P1 reevaluation on April 1), I would really appreciate it if my **original P1 eval score could be reinstated** instead of receiving a **0**—since it was already evaluated and graded.

Would highly appreciate your prompt support in this regard @carlton @Jivraj

---

## Reply 195
**Author**: Pooja M
**Posted**: 2025-04-01T16:15:15.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/207

**Image: pro 1**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of an email or a message displayed on a mobile device. It shows the results of prerequisite evaluations for a "Project 1". The evaluations check for the presence and accessibility of a Docker image, a GitHub repository, a Dockerfile, and an MIT license.

**2. Text Content:**

The text content includes:

*   "submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: FAIL"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"
*   "--"
*   "Kind regards, TDS Team"

**3. Context and Purpose:**

The context is likely an automated evaluation system for a software development project. The purpose of the message is to inform the user about the results of the prerequisite checks. The "FAIL" status for the Dockerfile and the overall "Prerequisites: FAIL" indicate that the submission does not meet the required criteria and will not be evaluated. The "Project 1 Score: 0" further emphasizes the failure.

**4. Technical Details:**

*   The evaluations are checking for specific files and configurations related to Docker and GitHub.
*   The presence of a Docker image in Docker Hub and a public GitHub repository are required.
*   A Dockerfile must be present in the root directory of the GitHub repository.
*   An MIT license file must also be present in the root directory of the GitHub repository.
*   The "PASS" and "FAIL" statuses indicate whether each requirement is met.
*   The overall "Prerequisites" status is determined by the individual evaluation results.

Actually I got the email as my docker file is not in root git hub repository. But everything thing looks fine and my docker file also runs well.. I want to check my repo again ..sir kindly do my my evaluation again and we have put lot of efforts doing this project 1 . Hope the team evaluated and gives the deserved marks

@carlton

@ TDS TEAM

---

## Reply 196
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-02T00:45:03.921Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/208

There is no Dockerfile in the root directory of your GitHub repository. The standard naming convention for a Dockerfile is Dockerfile.

---

## Reply 197
**Author**: Jayaram
**Posted**: 2025-04-02T03:08:21.150Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/209

@carlton @Jivraj please let know if any issues in my end on the docker image not present issue.. As explained in earlier thread , the only reason docker image had to be pushed  was the removal my office proxies in the docker image which was making the container not to startup from orchestration environment.. any help is appreciated..

---

## Reply 198
**Author**: NK
**Posted**: 2025-04-02T06:51:17.887Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/210

@Jivraj @carlton  I updated google form 4 days ago on the architecture, Could you let me know when it will be re-evaluated ? Thanks

---

## Reply 199
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-02T07:35:26.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/211

Hi @thinkmachine @22f3002723

Since you updated docker repo few days ago and docker api doens’t support timestamp based pulling we will pull your GitHub repo before 18 th feb and will build through it and run evaluations.

We also have your docker repo evaluation score, will discuss which one to keep.

This is for anyone who updated their docker repo and there are around 10-20 such cases

---

## Reply 200
**Author**: Jayaram
**Posted**: 2025-04-02T08:20:36.942Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/212

Thanks for the understanding @Jivraj

---

## Reply 201
**Author**: Saransh Saini
**Posted**: 2025-04-02T09:08:13.004Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/213

Hi @thinkmachine

As we said before that changes in Docker image after deadline won’t be accepted. Even an extension of the deadline won’t help in this case, simply because Docker API doesn’t support timestamp based pulling. However we would be pulling your GitHub repositories before 18th Feb build a Docker container and run evaluations on that.

---

## Reply 202
**Author**: Atishay
**Posted**: 2025-04-02T09:12:10.439Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/214

@Jivraj @carlton @Saransh_Saini request your help in clarification for the same, the Github repo has been always present but it is marking it as fail. Thank you

---

## Reply 203
**Author**: Shreyan Chaubey
**Posted**: 2025-04-02T09:31:53.254Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/215

A sigh of relief! Thank you so much for the heads up @Jivraj.

@Saransh_Saini Yup! The Docker issue is perfectly understandable. Even I checked my Hub repo, and I couldn’t seem to find an image having the pre-18th Feb digest. Had I been aware of this issue, and the fact that a re-eval would be carried out, I would’ve tagged the updated image differently. Hopefully, cases like mine will aid in resolving any issues in the future.

Once again, thank you both!

---

## Reply 204
**Author**: LAKSHAY
**Posted**: 2025-04-02T12:59:33.351Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/216

@Jivraj @carlton @Saransh_Saini

I am still uncertain as to why I received a second email regarding my project 1 score, indicating a failure due to unmet pre-requisites. I have inquired multiple times, yet I have not received a response. Meanwhile, several other posts, both before and after mine, have been addressed. Kindly clarify about that mail.

Thankyou

---

## Reply 205
**Author**: Yashvardhan
**Posted**: 2025-04-02T13:09:36.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/217

@carlton   Sir pls see my issue

---

## Reply 206
**Author**: Swati Kapoor
**Posted**: 2025-04-02T13:38:07.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/218

I have the same issue. I also received a second mail stating I had failed due to some missing prerequisites though in the first mail my project evaluation had been carried out.

---

## Reply 207
**Author**: Carlton D'Silva
**Posted**: 2025-04-02T14:18:50.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/219

Hi @lakshaygarg654

Dont worry you passed pre-requsites. The script that was used earlier for basic checks used a stricter criteria, the newer one we wrote allowed for a looser check. You have scored very well in your latest run. 12 correct tasks.

We have not responded quickly because we are in the midst of finalising all the scores and doing normalisation etc, i.e operational work for Project 1 and 2.

We hope to have Project 2 scores out by this weekend.

Kind regards

---

## Reply 208
**Author**: Vansh Mittal
**Posted**: 2025-04-02T14:26:27.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/220

@carlton @Jivraj

Sir can you also see the case of Dockerfile name. Many students have named it dockerfile , lower case ‘d’ character instead of upper case.

Please sir see through it

---

## Reply 209
**Author**: LAKSHAY
**Posted**: 2025-04-02T14:30:33.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/221

Thanks @carlton , for your response.

I was never worried about the result, whether it comes late or early. I know you will release it once everything is processed correctly. My concern was only about getting a response. Anyway, thanks for replying.

Also, today’s session has been canceled. I wanted to ask about the issue with editing responses in the Project 2 form. Is there any update on this?

---

## Reply 210
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-04-02T18:21:51.820Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/222

Hi just wanted to know, there was no mail prior stating to keep the Dockerfile in the root folder of the repo (correct me if im wrong). Therefore i have put everything inside a folder - wont this be considered? Please clarify if possible.

**Image: Screenshot 2025-04-02 at 11.41.14 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository interface. It displays the main page of a repository named "tds_project1". The UI elements include:

*   Repository name and visibility (Public)
*   Branch selection dropdown (currently on "main")
*   Branch and tag counts (1 branch, 0 tags)
*   File search bar
*   "Add file" and "Code" buttons
*   A list of files and folders in the repository, along with their last commit message and date.
*   Pin and Unwatch buttons

**2. Text Content:**

*   **Repository Name:** tds\_project1
*   **Visibility:** Public
*   **Branch:** main
*   **Branch Count:** 1 Branch
*   **Tag Count:** 0 Tags
*   **Search Bar Text:** Go to file
*   **Commit Hash:** 21f1002409
*   **Commit Message:** done
*   **Folder Name:** tds-project-1
*   **File Names:** LICENSE, README.md, README
*   **Commit Messages:** done, Initial commit, readme changes
*   **Commit Hash (partial):** 4d2f5e5
*   **Time Since Last Commit:** 2 months ago (for multiple files/folders)
*   **Commit Count:** 14 Commits
*   **License:** MIT license
*   **Unwatch:** 1

**3. Context and Purpose:**

The image displays the file structure and recent activity of a GitHub repository. It allows users to browse the files, view commit history, and perform actions like adding files or viewing the code. The "Public" label indicates that the repository is accessible to anyone.

**4. Technical Details:**

*   The image is a screenshot of a web-based UI, specifically GitHub.
*   The commit hash (e.g., 21f1002409, 4d2f5e5) is a unique identifier for a specific version of the code.
*   The "main" branch is the primary branch of the repository.
*   The file extensions (.md) indicate that README.md is a Markdown file.
*   The

**Image: Screenshot 2025-04-02 at 11.43.17 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) of a file repository, likely from a platform like GitHub or GitLab. It displays the contents of a project directory. The UI elements include:

*   Project name and path: "tds\_project1 / tds-project-1/"
*   Commit information: A commit hash "21f1002409" and the commit message "done".
*   File listing: A table-like structure showing files and directories within the repository.
*   Column headers: "Name", "Last commit message", and "Last commit date".
*   Buttons: "Add file" and a more options button.

**2. Any text content visible:**

*   **Project Name/Path:** tds\_project1 / tds-project-1/
*   **Commit Hash:** 21f1002409
*   **Commit Message:** done
*   **Column Headers:** Name, Last commit message, Last commit date
*   **File/Directory Names:**
    *   .. (parent directory)
    *   app (directory)
    *   .gitignore (file)
    *   Dockerfile (file)
    *   README.md (file)
*   **Last Commit Messages:** done (for all files/directories)
*   **Last Commit Dates:** 2 months ago (for all files/directories)
*   **Other UI Text:** Add file, History

**3. The context or purpose of what's displayed:**

The image shows the file structure and recent commit history of a software project. It allows users to browse the files, see when they were last updated, and view the commit messages associated with those updates. The "Add file" button suggests the user can add new files to the repository. The "History" button allows the user to view the commit history.

**4. Technical details if it's a code screenshot or technical diagram:**

This is not a code screenshot or technical diagram, but rather a UI for managing files in a repository. The technical details are related to version control systems like Git, where commits are identified by unique hashes (like "21f1002409"). The UI provides a user-friendly way to

---

## Reply 211
**Author**: Aryan Tikam
**Posted**: 2025-04-02T18:26:01.598Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/223

**Image: 1000004176**
Here's a detailed description of the image:

1.  **What is shown in the image:** The image displays a JSON-formatted error message. It appears to be a server response, likely from an API endpoint. The background is black, and the text is white. There is a red circle in the top left corner.

2.  **Text Content:**
    *   `HTTP 500`
    *   `"details": "Task handling error: Failed to get LLM response after 3 attempts: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}"`
    *   `"error": "Internal server error"`

3.  **Context/Purpose:** The image shows an error response from a server. The HTTP status code is 500, indicating an internal server error. The "details" field provides more specific information about the error, indicating that the server failed to get a response from a Language Model (LLM) after three attempts. The error code 401 suggests an authentication issue. The nested "error" object further clarifies that the authentication token used is not from a valid issuer.

4.  **Technical Details:**
    *   **HTTP 500:** This is the HTTP status code, indicating a generic server error.
    *   **JSON Format:** The error message is structured in JSON (JavaScript Object Notation), a common format for data interchange.
    *   **Error Details:** The "details" field contains a string that includes a nested JSON-like structure describing the authentication error.
    *   **Authentication Error:** The error message indicates that the authentication token provided is not valid because it's not from a trusted issuer. This suggests a problem with the token's origin or configuration.
    *   **LLM:** The error message mentions "LLM response," indicating that the server was trying to interact with a Language Model.
    *   **Error Code 401:** This is an HTTP status code that indicates that the request requires user authentication.

Can anyone explain what errors of this sort mean?

---

## Reply 212
**Author**: Carlton D'Silva
**Posted**: 2025-04-03T00:30:31.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/224

You have to show which task triggered this error. Is it all of them or only one of them. Only then we can diagnose what the problem is.

---

## Reply 213
**Author**: Aryan Tikam
**Posted**: 2025-04-03T03:32:09.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/225

**Image: 1000004190**
Here's a detailed description of the image content:

**1. Overall Content:**

The image shows a terminal output or log, likely from a software development environment. It indicates a series of tasks being executed, along with HTTP requests and error messages. The context appears to be related to formatting a file using `prettier` and interacting with a local server.

**2. UI Elements:**

*   The text is displayed in a monospaced font, typical of terminal outputs.
*   There are colored circles (yellow, red) and a red "X" symbol, likely used to indicate the status of different operations (success, failure).

**3. Text Content and Analysis:**

*   **"● Running task: Format `/data/format.md` with `prettier@3.4.2` in-place"**: This indicates the start of a task to format the file `/data/format.md` using the `prettier` tool, version 3.4.2, and applying the changes directly to the file ("in-place").
*   **"HTTP Request: POST http://localhost:8365/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 500 INTERNAL SERVER ERROR"**: This shows an HTTP POST request being made to a local server at `localhost:8365`. The request is to the `/run` endpoint, and the query parameters encode the formatting task. The server responded with a "500 Internal Server Error", indicating a problem on the server-side.
*   **"• HTTP 500 { ... }"**: This section provides details about the 500 error. It's a JSON object containing:
    *   `"details"`: "Task handling error: Failed to get LLM response after 3 attempts: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_issuer'}}",
    *   `"error"`: "Internal server error"
    This indicates that the task failed because it couldn't get a response from an LLM

Here it is with the task, however the error doesn’t seem to be related to the task itself based on the returned message in the JSON. It seems to be something wrong with the OpenAI API key. From the reading I did, it seems that the key was perhaps not set properly during evaluation? Not completely sure but please look into it.

---

## Reply 214
**Author**: Carlton D'Silva
**Posted**: 2025-04-03T04:12:16.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/226

Did all tasks produce the same error?

---

## Reply 215
**Author**: Aryan Tikam
**Posted**: 2025-04-03T04:21:12.815Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/227

Yes except B1 somehow.

---

## Reply 216
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T04:53:30.583Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/228

Hi @AryanTikam

I looked at your github repo, You have used python’s `openai` module for doing project1, but AIPROXY_TOKEN is supposed to be used through anand sir’s proxy.

---

## Reply 217
**Author**: Aarush saxena 
**Posted**: 2025-04-03T04:55:29.269Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/229

@carlton @Jivraj @Saransh_Saini

Can you pls tell me my project 1 marks

My evaluation.py had 2 score

First one 1/20 where every task showed error second one had 10/20…

---

## Reply 218
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T05:00:40.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/230

Dockerfile has to be insider root directory of github repo.

---

## Reply 219
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T05:29:41.769Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/231

This was mistake from our end we rectified it and reevaluated your submission.

Your submission has a good score.

---

## Reply 220
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T05:31:50.788Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/232

[swati-iitm/project1_final](https://github.com/swati-iitm/project1_final)

This is your github repo which doesn’t have a Dockerfile. That’s why It didn’t pass Prechecks

---

## Reply 221
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T05:35:55.465Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/233

We have reevaluated it, we have scores avaliable for your submission.

---

## Reply 222
**Author**: S Smriti
**Posted**: 2025-04-03T05:43:00.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/234

Sir I understand you will be busy evaluating all the files and reevaluating them as well. I just wanted to know if its a confirm 0 for those who got evaluation log file MISSING and didnt get the other mail that many got in the past 2 days… Just to confirm… cause i think am getting 0 from that @carlton @Jivraj

---

## Reply 223
**Author**: Aryan Tikam
**Posted**: 2025-04-03T06:13:03.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/235

So can anything be done about it now as it seems to pass more tasks without the proxy requirement? It is fine if not.

---

## Reply 224
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-04-03T06:29:32.803Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/236

Please, can you put a screenshot of where it has been communicated, prior to the deadline.

---

## Reply 225
**Author**: Carlton D'Silva
**Posted**: 2025-04-03T06:51:18.604Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/237

We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.

We discussed it internally with @s.anand and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it **regardless of whether we explicitly mentioned it or not** on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.

In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by @s.anand

So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.

Kind regards,

TDS team

---

## Reply 226
**Author**: Saini Nirmal
**Posted**: 2025-03-31T21:18:59.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/238

@carlton Sir, I would like to respectfully ask if this is some sort of April Fool’s joke, as it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0 Score.

I am not the only one facing this issue; several others have encountered the same problem. I kindly request you to review my submission again.

Additionally, I have faced multiple technical issues in recent times. Initially, I was failed in the L1 viva due to a typing mistake, which was later acknowledged. Similarly, in both OPPE 1 and OPPE 2, many students experienced Google Meet issues. On March 29, during my SC OPPE, I faced camera issues in Google Meet, along with VM lagging. Many students have raised similar concerns with Proctor.

Given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

**Image: Screenshot 2025-04-01 020618**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows an email notification. It appears to be an automated email sent to a learner regarding the evaluation of their Project 1. The email details prerequisite checks and provides a summary of whether the learner passed or failed each check.

**2. Any text content visible:**

*   **Subject:** TDS Jan 25 Project 1 Scores
*   **Sender:** 22t1 se2002
*   **Recipient:** to me (presumably the learner)
*   **Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (with "TDS Project 1: Evaluation" as a hyperlink)
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of checks and their results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"

**3. The context or purpose of what's displayed:**

The email is an automated feedback mechanism for a project submission. It informs the learner whether they have met the basic prerequisites for the project. The email indicates that the learner has failed the overall prerequisites, as some of the individual checks have failed. The learner needs to address the

---

## Reply 227
**Author**: Vedant Bhanushali
**Posted**: 2025-04-01T05:52:49.180Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/239

**Image: IMG_7078**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows text, likely from a terminal or a web interface, displaying the results of a project evaluation. It includes instructions, prerequisites, and a score.

**2. Any text content visible:**

The text content includes:

*   "accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
*   "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: FAIL"
*   "Is Github repo present AND public: PASS"
*   "Is Dockerfile present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. The context or purpose of what's displayed:**

The context is a project submission evaluation. The text indicates that the submission is being checked against certain prerequisites. The evaluation checks for the presence of a Docker image in Docker Hub, a public GitHub repository, a Dockerfile in the root of the repository, and an MIT license. The project failed the prerequisites, resulting in a score of 0.

**4. Technical details if it's a code screenshot or technical diagram:**

The text includes a `podman run` command, which is used to run containers. The command sets an environment variable `AIPROXY_TOKEN` and maps port 8000. The evaluation checks for the presence of a `Dockerfile`, which is a text file that contains instructions for building a Docker image. The presence of an MIT license is also checked, which is a common open-source license.

Same for me sir, i had everything correct still its showing:- Is Docker image present in dockerhub

AND is public: FAIL

I have submitted everything correctly . Please carefully look into this and recheck the project submitted.

---

## Reply 228
**Author**: Vedant Bhanushali
**Posted**: 2025-04-01T05:55:19.131Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/240

Sir,it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0

@carlton Sir please look into this.

**Image: IMG_7078**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows text, likely from a terminal output or a webpage, related to the evaluation of a project (Project 1). It includes instructions, prerequisites, and evaluation results.

**2. Any text content visible:**

*   "accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
*   "5. Your Docker image uses the same Dockerfile as in your GitHub repository"
*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: FAIL"
*   "Is Github repo present AND public: PASS"
*   "Is `Dockerfile` present in root of github repo: PASS"
*   "Is MIT license present at root of github repo: PASS"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"

**3. The context or purpose of what's displayed:**

The image shows the results of an automated evaluation of a student's project submission. The evaluation checks for specific requirements, such as the presence of a Docker image in Docker Hub, a public GitHub repository, a `Dockerfile` in the root of the repository, and an MIT license. The overall "Prerequisites" status is "FAIL," and the "Project 1 Score" is "0," indicating that the submission did not meet all the necessary requirements.

**4. Technical details (if it's a code screenshot or technical diagram):**

*   The `podman run` command suggests that the project involves containerization using Podman.
*   The environment variable `AIPROXY_TOKEN` and the port mapping `8000:8000` indicate that the application likely involves an API proxy and runs on port 8000.
*   The mention of `Dockerfile` and Docker image implies the use of Docker for packaging and deployment.
*   The evaluation checks for the presence of a `Dockerfile` in the root of the GitHub repository, which is a common practice for Docker-based projects.
*   The

@carlton Sir, given  this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

---

## Reply 229
**Author**: Deepak kumar
**Posted**: 2025-04-01T07:24:27.184Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/241

**Image: Screenshot 2025-04-01 at 12.50.38 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email within a Gmail interface. The email is titled "TDS Jan 25 Project 1 Scores." The email contains information about the prerequisites for Project 1 and the results of prerequisite evaluations.

**2. Any text content visible:**

*   **Email Header:**
    *   Subject: "TDS Jan 25 Project 1 Scores"
    *   Sender: "22t1 se2002" ()
    *   Recipient: "to me"
    *   Timestamp: "1:27 AM (11 hours ago)"
*   **Email Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (The "TDS Project 1: Evaluation" is a hyperlink.)
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of evaluation results, all marked as "FAIL":
        *   "Is Docker image present in dockerhub AND is public: FAIL"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"
    *   "--"

@carlton sir, i would like to ask why marks showing 0 infact i am submitting all my requirements things in that form so plz look into this matter.

---

## Reply 230
**Author**: Prashant Aswani 
**Posted**: 2025-04-02T17:45:24.192Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/242

@carlton sir, similar thing happened to me as well, I had got the mail that git repo, dockerfile and lisence is not present or accessible while all the prerequisites are completed from my end. Can you please reevaluate my submission.

**Image: 1000051556**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image appears to be a screenshot of an email or a document outlining the evaluation criteria and results for "TDS Project 1". It lists prerequisites for the project and shows whether the submission met those requirements.

**2. Text Content:**

The text content includes:

*   "checks as detailed on the TDS Project 1: Evaluation page:"
*   A numbered list of prerequisites:
    *   "Your GitHub repository exists and is publicly accessible"
    *   "Your GitHub repository has a LICENSE file with the MIT license"
    *   "Your GitHub repository has a valid Dockerfile"
    *   "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
    *   "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   A warning: "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   A list of evaluation results:
    *   "Is Docker image present in dockerhub AND is public: PASS"
    *   "Is Github repo present AND public: FAIL"
    *   "Is Dockerfile present in root of github repo: FAIL"
    *   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"
*   A closing: "Kind regards, TDS Team"
*   A note: "Note: Do NOT reply to this email. It is only meant for official announcements and messages. If you need any further assistance please contact the course team via Discourse."

**3. Context and Purpose:**

The purpose of the document is to inform a student or participant about the evaluation of their "TDS Project 1" submission. It specifies the criteria used for evaluation, provides the results of the evaluation, and indicates the final score. The email also provides instructions on how to get further assistance.

**4. Technical Details:**

*   The document mentions "GitHub repository," "LICENSE file," and "Dockerfile," indicating that the project involves software

---

## Reply 231
**Author**: Carlton D'Silva
**Posted**: 2025-04-03T03:03:12.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/243

Hi Prashant,

Your prerequisites have passed and your evaluation is 6 tasks have been completed successfully. The email was auto sent because we were doing some checks with an older, stricter script. The newer script passes your evaluation.

Kind regards

---

## Reply 232
**Author**: Chinnam Goutham Nischay
**Posted**: 2025-04-03T07:07:07.893Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/244

Thanks for the quick reply, i don’t have a convincing argument to counter. Just a suggestion it would have been better if you have explicitly put in the sanity check requirements. Something so obvious to you might not be so for others.

if you are referring to this email even here, it was not explicit. Might have missed it in the gmeet. A mail would have been good.

**Image: Screenshot 2025-04-03 at 12.28.22 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of an email in an email client (likely Gmail). The email is about checking submissions for basic sanity.

**2. Text Content:**

The email's subject is "[TDS Jan 2025] Important: Please check your submissions for basic sanity".

The sender is "donot_reply@study.iitm.ac.in" and it's addressed to "25t1_se2002-announce".

The body of the email contains the following text:

*   "Dear Learners,"
*   "Before progressing to perform detailed evaluation, we check the repositories for the basic sanity checks given below:"
*   "- Is the GitHub repo public?"
*   "- Does it have an MIT license?"
*   "- Does it have a DockerFile?"
*   "- Is the Docker image accessible?"
*   "Out of the 530+ submissions, we see that only 284 submissions have cleared this basic sanity check. We have sent out emails to the 250+ learners on the errors that we observed a little while back. Please do check your Inbox and SPAM folder to see if you have received an email from the course admin id (se2002) with the subject "[IMPORTANT] Your Project 1 submission is on the risk of scoring 0 Marks". Please note that we have taken the last submission in the form for the validation."
*   "We hope that you will take immediate action to check for sanity of your submission and correct the errors that have been reported."
*   "Regards"
*   "TDS team"

The email also shows the date and time it was received: "Sun, Feb 16, 8:18 PM".

**3. Context and Purpose:**

The email is a notification to students (learners) regarding their project submissions. It informs them that their submissions are being checked for basic sanity, which includes ensuring the GitHub repository is public, has an MIT license, contains a Dockerfile, and the Docker image is accessible. The email warns that if these checks fail, the project submission is at risk of scoring 0 marks. It urges students to check their inbox and spam folder for a previous email detailing the specific errors observed in their

---

## Reply 233
**Author**: Carlton D'Silva
**Posted**: 2025-04-03T07:20:58.966Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/245

I agree with you. It should have been explicitly mentioned in the project page (even if we have mentioned it in live sessions)

---

## Reply 234
**Author**: Aarush saxena 
**Posted**: 2025-04-03T07:33:53.126Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/246

@carlton @Jivraj

Put some light on this poor soul’s message also ;')

---

## Reply 235
**Author**: Veer Shah
**Posted**: 2025-04-03T08:50:54.826Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/247

my repo has both the dockerfile with correct name (Dockerfile and in the root folder), license and is public. Please look into this . @carlton sir . @Jivraj [GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.

**Image: 1000105386**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email. The email appears to be an automated message providing feedback on a project submission, specifically Project 1. The email details the prerequisites for the project and the results of checks performed on the submission.

**2. Any text content visible:**

The email contains the following text:

*   **Headers:** "22t1 se2002 1:27 am", "to me"
*   **Salutation:** "Dear Learner,"
*   **Body:**
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:"
    *   A numbered list of prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of checks and their results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. The context or purpose of what's displayed:**

The email's purpose is to inform the "Learner" about the status of their Project 1 submission. It outlines the required prerequisites and provides a detailed breakdown of which checks passed and failed. The overall "Prerequisites" status is "FAIL," and the "Project 1 Score" is "

why is it saying i got 0? please look into it.

---

## Reply 236
**Author**: NIKHIL TEJA C
**Posted**: 2025-04-03T08:56:00.727Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/248

@carlton @jivraj Sir I received a mail like everyone that my git-hub repository is not public and not MIT licensed. I even filled the g-form correctly while submitting.

But I had fulfilled the above required criteria. Please look into this matter ASAP.

Here is my git repo link : [[GitHub - 23f1001415/llm_aa_tds_project](https://github.com/23f1001415/llm_aa_tds_project)]. ([https://github.com/23f1001415/llm_](https://github.com/23f1001415/llm_)

**Image: Screenshot (390)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a Gmail inbox. Specifically, it displays an email related to a project evaluation. The email outlines prerequisites for "Project 1" and provides an evaluation of whether those prerequisites have been met. The Gmail interface is visible, including the navigation menu on the left, the search bar, and the email content in the main area.

**2. Text Content:**

*   **Email Header:**
    *   Sender: 22t1 se2002 
    *   Recipient: to me
    *   Date: Tue, Apr 1, 1:22 AM (2 days ago)
*   **Email Body:**
    *   Greeting: "Dear Learner,"
    *   Introduction: "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (The "TDS Project 1: Evaluation page" is a hyperlink).
    *   Prerequisites (numbered list):
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   Warning: "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   Evaluation Results:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: FAIL"
        *   "Is Dockerfile present in root of github repo: FAIL"
        *   "Is MIT license present at root of github repo: FAIL"
    *   Summary:
        *   "Prerequisites: FAIL"
        *   "Project 1 Score: 0"
    *   Closing: "Kind regards,"
*   

**Image: Screenshot (391)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository page in a web browser. It shows the file structure, commit history, and repository details.

**2. Text Content:**

*   **Repository Name:** `llm_aa_tds_project` (Public)
*   **Branch:** `main` (1 Branch, 0 Tags)
*   **Files and Directories:**
    *   `_pycache_`
    *   `data`
    *   `.dockerignore`
    *   `.env`
    *   `Dockerfile`
    *   `LICENSE`
    *   `README.md`
    *   `app.py`
    *   `datagen.py`
    *   `evaluate.py`
    *   `tasksA.py`
    *   `tasksB.py`
*   **Commit Messages:**
    *   "Initial commit with Dockerfile and application code" (repeated for several files)
    *   "Create app.py"
    *   "Create tasksA.py"
*   **Commit Details:**
    *   "2 months ago" (repeated for most files)
    *   "6 Commits" (next to the initial commit)
    *   "50eacaf" (commit hash)
*   **About Section:**
    *   "No description, website, or topics provided."
    *   "Readme"
    *   "MIT license"
    *   "Activity"
    *   "0 stars"
    *   "1 watching"
    *   "0 forks"
*   **Releases:** "No releases published. Create a new release"
*   **Packages:** "No packages published. Publish your first package"
*   **Languages:** "Python 98.4% Dockerfile 1.6%"
*   **Suggested workflows:** "Based on your tech stack"

**3. Context and Purpose:**

The image shows the structure and basic information of a GitHub repository. It provides an overview of the project's files, commit history, and licensing. The "About" section indicates that the repository lacks a detailed description. The language breakdown suggests the

aa_tds_project).

I have attached screenshots for your reference.

Thank you

---

## Reply 237
**Author**: Pradeep Mondal
**Posted**: 2025-04-03T09:27:48.605Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/249

@Jivraj I too had the same issue (image was run on wrong architecture) and filled the gform that was circulated. When should we expect to get our scores?

Thanks

Pradeep Mondal

---

## Reply 238
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:32:07.849Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/250

Hi @21f2000709

We have used another approach because of architecture problem, by pulling through latest commit from github before 18th feb. Just checked we have results for you.

---

## Reply 239
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:33:34.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/251

Hi @23f1001415

This was a problem from our side and we rechecked and now we score against your submission.

---

## Reply 240
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:36:01.806Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/252

Hi @23f1001524

This was a problem from our end, we have recitified it your submission was valid.

---

## Reply 241
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:37:05.156Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/253

Your latest score through pulling from github and building image thorugh dockerfile have higher score than these 2.

---

## Reply 242
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:43:47.672Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/254

Hi @23f2004563

I checked we have scores against your submission.

---

## Reply 243
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:45:32.643Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/255

There was some problem with our script, later we correct and your submission was valid, I have just checked and confirm you.

---

## Reply 244
**Author**: Aarush saxena 
**Posted**: 2025-04-03T09:48:41.922Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/256

Can u pls share marks :') dying with curiosity

---

## Reply 245
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:49:46.945Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/257

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a code preview interface, likely from a platform like GitHub or GitLab.
*   There are tabs at the top labeled "Preview," "Code," and "Blame." "Preview" is currently selected.
*   There's a search bar with a magnifying glass icon.
*   There are icons for "Raw," "Copy," "Download," and "Edit" on the right side of the top bar.
*   A table is displayed with column headers.

**2. Text Content:**

*   **Top Bar:**
    *   "1069 lines (1069 loc) • 127 KB" - Indicates the file has 1069 lines of code and a size of 127 KB.
*   **Search Bar:**
    *   "23f1000057@ds.study.iitm.ac.in" - This appears to be an email address used as a search query.
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Data:**
    *   Row 1: "669" (likely a row number)
    *   Row 1: "2/16/2025 20:39:53" (a timestamp)
    *   Row 1: "23f1000057@ds.study.iitm.ac.in" (an email address, matching the search query)
    *   Row 1: "https://github.com/Vedant22042004/project" (a GitHub repository URL)
    *   Row 1: "vedant22042004/project" (a DockerHub image name)

**3. Context and Purpose:**

*   The image likely shows a search result within a code repository. The search query is an email address.
*   The table displays information related to the search result, specifically the timestamp,

This was your submission and we could not locate a docker repo against it.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page displaying a "404 Not Found" error. The page is styled with the Docker Hub branding. The error message is presented within a large blue circle. Below the error message, there's a cartoon illustration of a person sitting at a computer, seemingly indicating frustration or confusion.

**2. Any text content visible:**

*   **URL:** `https://hub.docker.com/r/vedant2204/project/tags`
*   **Docker Hub Navigation:** "Explore", "My Hub"
*   **Breadcrumbs:** "Explore / vedant2204 / project"
*   **Error Message:**
    *   "404" (large font)
    *   "Oops!"
    *   "The page you have requested was not found"
*   **Search Bar:** "Search Docker Hub"
*   **Keyboard Shortcut:** "Ctrl+K"
*   **Other UI elements:** "Update"

**3. The context or purpose of what's displayed:**

The image indicates that the user attempted to access a specific page on Docker Hub related to a project named "vedant2204" and its tags, but the page does not exist or is no longer available. The 404 error is a standard HTTP response code indicating that the server could not find the requested resource.

**4. Technical details:**

*   The URL `https://hub.docker.com/r/vedant2204/project/tags` suggests the user was trying to view the tags associated with a Docker Hub repository named "vedant2204/project".
*   The presence of the Docker Hub logo and navigation elements confirms that the error is occurring within the Docker Hub website.
*   The 404 error indicates a client-side error, meaning the user requested a resource that the server couldn't find. This could be due to a typo in the URL, the resource being moved or deleted, or a server-side configuration issue.

---

## Reply 246
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:54:19.130Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/258

Your submission was valid there was some issues with our script for checking. But after building your image after pulling github repo, it didn’t one `taskA` module was missing.

---

## Reply 247
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:57:36.781Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/259

If you used openai’s python module then you were needed to pass your own api key, hardcode it in code.

API key that we were sending was only valid through proxy server created by professor anand.

---

## Reply 248
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T09:58:24.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/260

mail will be sent by either today or tomorrow.

---

## Reply 249
**Author**: S Smriti
**Posted**: 2025-04-03T09:59:02.115Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/261

any idea on this sir?..

---

## Reply 250
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T10:06:24.597Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/262

No we pulled through github and build image on gcloud vm. Anyone with valid submission didn’t receive mail, your submission was valid.

---

## Reply 251
**Author**: S Smriti
**Posted**: 2025-04-03T10:08:07.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/263

but my evaluation log file was missing… so that would make it a 0 right..I have accepted my fate that it would be a 0 but just a lil hope  :melting_face:

---

## Reply 252
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T10:11:36.623Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/264

We reevaluated and found your submission was valid but it was running on a different port, 5000 but it was expected to run on 8000 port.

---

## Reply 253
**Author**: S Smriti
**Posted**: 2025-04-03T10:12:22.800Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/265

oh so… is it going to be considered? like will i get some score other than a 0… am sorry for asking so much

---

## Reply 254
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T10:13:15.214Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/266

No it won’t be considered. It was supposed to be running on 8000 port.

---

## Reply 255
**Author**: S Smriti
**Posted**: 2025-04-03T10:13:56.338Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/267

Ok got it. Thank you so much  :cry:

---

## Reply 256
**Author**: Syed Zakiyuddin
**Posted**: 2025-04-01T16:57:54.024Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/268

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface, likely from a container registry or repository hosting platform (like Docker Hub or a similar service). It displays information about a repository named "my-fastapi-app" owned by the user "zakiy7". The interface includes UI elements for navigation, filtering, and managing the repository. Specifically, the "Tags" section is active.

**2. Any text content visible:**

*   **Navigation:** "Explore / zakiy7 / my-fastapi-app"
*   **Repository Information:**
    *   "zakiy7/my-fastapi-app" (Repository name)
    *   "By zakiy7" (Owner)
    *   "Updated about 1 month ago"
    *   "IMAGE"
    *   "0" (Stars/Likes)
    *   "26" (Downloads/Pulls)
*   **Tabs:** "Overview", "Tags"
*   **Filtering and Sorting:**
    *   "Sort by"
    *   "Newest" (Dropdown for sorting options)
    *   "Filter tags" (Search input field)
*   **Tag Information:**
    *   "TAG"
    *   "latest" (Tag name)
    *   "Last pushed about 1 month by zakiy7"
    *   "Digest"
    *   "740fcf3f65bb" (Digest value)
    *   "OS/ARCH"
    *   "linux/amd64" (Operating System and Architecture)
    *   "Last pull"
    *   "5 days" (Time since last pull)
    *   "docker pull zakiy7/my-fastapi-app:latest" (Docker pull command)
    *   "Copy" (Button to copy the pull command)
    *   "Compressed size"
    *   "261.49 MB" (Compressed size of the image)
*   **Button:** "Manage Repository"

**3. The context or purpose of what's displayed:**

The image shows the "Tags" section of a container image repository. The purpose is to allow users to browse and manage different versions

Hi sir, my Architecture says amd64, in the google docs I have selected x86, i hope it is correct. Also,  I have used podman to test the pull and its working well. Please let me know if i need to do anything else.

@carlton

---

## Reply 257
**Author**: Carlton D'Silva
**Posted**: 2025-04-02T16:07:20.865Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/269

We are rebuilding all docker submissions from github commit before 18th of Feb, using your Dockerfile manifest present in the repo.

That way there is no architecture issues.

Its part of our secondary check. And more students have gotten scores in this  check. So dont worry.

---

## Reply 258
**Author**: S Smriti
**Posted**: 2025-04-03T10:27:21.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/270

I just checked from my side also, wow a very dumb mistake now costing me a 0…should have read the project document more clearly  :cry:  So sorry for asking.

Am assuming no lenient correction can be done for that? like during the evaluation …

podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:5000 $IMAGE_NAME

---

## Reply 259
**Author**: Saini Nirmal
**Posted**: 2025-04-03T10:40:03.358Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/272

**Image: Screenshot 2025-04-03 160336**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository interface. It displays a list of files and folders within the repository, along with commit messages and timestamps. The interface includes standard GitHub elements like the branch selector, search bar, "Add file" button, and "Code" button.

**2. Any text content visible:**

*   **URL:** github.com/23f1002643/llm-automation-agent
*   **Branch:** main, 1 Branch, 0 Tags
*   **Search Bar:** Go to file
*   **Buttons:** Add file, Code
*   **Commit Message:** Add files via upload, Initial commit
*   **File/Folder Names:**
    *   \_pycache\_
    *   Dockerfile
    *   LICENSE
    *   README.md
    *   app.py
    *   datagen.py
    *   evaluate.py
    *   requirements.txt
    *   tasksA.py
    *   tasksB.py
*   **Commit Hash:** c883879
*   **Time Stamps:** 2 months ago
*   **Commits:** 4 Commits

**3. The context or purpose of what's displayed:**

The image shows the file structure of a GitHub repository named "llm-automation-agent". It appears to be a project related to Large Language Model (LLM) automation. The presence of files like "app.py", "datagen.py", "evaluate.py", "requirements.txt", "tasksA.py", and "tasksB.py" suggests that the repository contains Python code for data generation, evaluation, and task execution related to LLMs. The "Dockerfile" indicates that the project is likely containerized.

**4. Technical details if it's a code screenshot or technical diagram:**

The image is not a code screenshot or technical diagram, but rather a file directory listing. The presence of a "requirements.txt" file suggests that the project uses Python dependencies, which are likely listed in that file. The "Dockerfile" suggests that the project can be built into a Docker container for easy deployment and reproducibility. The ".py" files indicate Python source code. The "LICENSE" file indicates the licensing

I checked it multiple times before submitting, I got 9/10 in task A.

---

## Reply 260
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T10:49:04.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/273

No. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

---

## Reply 261
**Author**: S Smriti
**Posted**: 2025-04-03T10:55:10.291Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/274

Ok… I do have a doubt tho, i actually have app.py and main.py in my github, my main.py is running on 8000 and app.py on 5000 …

---

## Reply 262
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T11:00:44.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/275

but in Dockerfile in your github repo you didn’t run main.py,

---

## Reply 263
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T11:02:19.716Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/276

In your Dockerfile you didn’t copy taskA.py to the container.

---

## Reply 264
**Author**: S Smriti
**Posted**: 2025-04-03T11:04:16.031Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/277

Ouch, ok sir… hopefully project 2 doesnt disappoint  :sob:

---

## Reply 265
**Author**: Swati Kapoor
**Posted**: 2025-04-03T12:01:40.520Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/278

It is there in the master branch of the repository. Now, will the previous evaluation mail that we got be considered or this one?

---

## Reply 266
**Author**: Khushi Dhankhar
**Posted**: 2025-04-03T16:52:22.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/279

@carlton @Jivraj

I recently received an email with an evaluation file for Project 1, which included a score. However, in the recent email, I noticed that my score was recorded as zero, despite fulfilling all the prerequisites.

I kindly request a re-evaluation of my project, as I believe this may be an error.

---

## Reply 267
**Author**: AYUSH SINGH
**Posted**: 2025-04-03T17:50:50.831Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/280

@Jivraj

My discrepancy is still not fixed. Please take a look at it

---

## Reply 268
**Author**: SP
**Posted**: 2025-04-03T18:35:09.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/281

@Jivraj

Hlo, could you please check and let me know how much am I scoring in Project 1 after the latest evaluation?

---

## Reply 269
**Author**: Gaurav Ghodge
**Posted**: 2025-04-04T05:21:02.368Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/282

@Jivraj @carlton

Sir,

In the mail that i got about project 1 report. In the log file it was written as TasksA.py file not found in docker, which was the case i observed with many students.

**Image: Screenshot 2025-04-04 at 10.31.02 AM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a terminal output, likely from a Python environment. It shows the installation of several Python packages using a package manager (likely pip). Following the installation logs, there's a traceback indicating an error during the execution of a Python script.

**2. Any text content visible:**

*   **Package Installation Logs:**
    *   `Building antiorm==1.2.1`
    *   `Building db==0.1.1`
    *   `Building db-sqlite3==0.0.1`
    *   `Downloading scipy (35.6MiB)`
    *   `Downloading pandas (12.1MiB)`
    *   `Downloading numpy (15.4MiB)`
    *   `Downloading pydantic-core (1.9MiB)`
    *   `Downloading duckdb (19.3MiB)`
    *   `Downloaded pydantic-core`
    *   `Built antiorm==1.2.1`
    *   `Built db==0.1.1`
    *   `Built db-sqlite3==0.0.1`
    *   `Downloaded numpy`
    *   `Downloaded duckdb`
    *   `Downloaded pandas`
    *   `Downloaded scipy`
    *   `Installed 33 packages in 56ms`
*   **Error Traceback:**
    *   `Traceback (most recent call last):`
    *   `File "/app/app.py", line 22, in `
    *   `from tasksA import *`
    *   `ModuleNotFoundError: No module named 'tasksA'`

**3. The context or purpose of what's displayed:**

The image shows the result of an attempt to run a Python script (`/app/app.py`). The script depends on a module named `tasksA`, but this module is not found in the Python environment. The initial part of the output shows the installation of other packages, which might have been an attempt to resolve dependencies before running the script.

**4. Technical details:**

*   The traceback indicates that the error occurred on line 22 of the

This is my Github repo:

**Image: Screenshot 2025-04-04 at 10.44.24 AM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository page. It displays the file structure of a repository named "tds-project1" owned by the user "GaURaVinDeX". The main content area shows a list of files and directories in the repository's root directory. On the right side, there's an "About" section, information about releases, packages, languages used, and suggested workflows.

**2. Any text content visible:**

*   **Repository Information:**
    *   Repository Name: tds-project1
    *   Owner: GaURaVinDeX
    *   Visibility: Public
    *   Branch: main (1 branch, 0 tags)
*   **File List:**
    *   \_pycache\_
    *   .gitignore
    *   Dockerfile
    *   LICENSE
    *   app.py
    *   requirements.txt
    *   tasksA.py
    *   tasksB.py
    *   README
    *   MIT license
*   **Commit Information:**
    *   Initial commit (for all files)
    *   Commit hash: 79e0ec5
    *   Last updated: 2 months ago
    *   2 Commits
*   **About Section:**
    *   "No description, website, or topics provided."
    *   "MIT license"
    *   "Activity"
    *   "0 stars"
    *   "1 watching"
    *   "0 forks"
*   **Releases:**
    *   "No releases published"
    *   "Create a new release"
*   **Packages:**
    *   "No packages published"
    *   "Publish your first package"
*   **Languages:**
    *   "Python 98.0%"
    *   "Dockerfile 2.0%"
*   **README Section:**
    *   "Add a README"
    *   "Help people interested in this repository understand your project by adding a README."
    *   "Add a README" (button)
*   **Suggested Workflows:**
    *   "Based on your tech stack"
    *   "Python package

I built the image using docker build command in vs code terminal. And pushed it same way to dockerhub using docker push command. How is it possible that the docker container missed the TasksA.py file while building or pushing it?

After getting this mail, I ran the project locally again mutliple times just to check if there was any issues in the code. It was getting 9/10 test cases passed.

---

## Reply 270
**Author**: Carlton D'Silva
**Posted**: 2025-04-04T05:46:33.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/283

This is a common mistake many, many students made. They created a working application but not a working container.

**Image: Screenshot 2025-04-04 at 11.13.32 am**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a file within a GitHub repository. Specifically, it displays the content of a `Dockerfile`. The left side of the screen shows a file explorer within the repository, and the right side shows the code of the `Dockerfile`.

**2. Any text content visible:**

*   **Repository Information:**
    *   `GaURaVinDeX / tds-project1`:  Indicates the username and repository name.
    *   `tds-project1 / Dockerfile`: Shows the path to the currently viewed file.
    *   `GaURaVinDeX Initial commit`:  Shows the author and commit message.
*   **UI Elements:**
    *   "Code", "Issues", "Pull requests", "Actions", "Projects", "Security", "Insights" are tabs at the top, indicating different sections of a GitHub repository.
    *   "Files" is selected on the left, indicating the file explorer is active.
    *   "main" is selected in a dropdown, indicating the current branch.
    *   "Go to file" is a search bar for navigating to specific files.
    *   "Code" and "Blame" are tabs for viewing the code or the commit history of each line.
*   **Dockerfile Content:**
    *   `FROM python:3.12-slim-bookworm`: Specifies the base image for the Docker container.
    *   `RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates`: Updates the package list and installs necessary dependencies.
    *   `ADD https://astral.sh/uv/install.sh /uv-installer.sh`: Downloads a script.
    *   `RUN sh /uv-installer.sh && rm /uv-installer.sh`: Executes the downloaded script and removes it.
    *   `RUN pip install fastapi uvicorn`: Installs Python packages using pip.
    *   `ENV PATH="/root/.local/bin:$PATH"`: Sets an environment variable.
    *   `WORKDIR /app`: Sets the working directory inside the container.
    *   `COPY app.py /app`: Copies the `app.py` file

You only copied `app.py` into your docker image.

How do you expect your application to run without the other files that your repo clearly shows is needed?

Thats why many people are failing this. Hope the image makes this clear.

Kind regards

---

## Reply 271
**Author**: Aryan Kumar
**Posted**: 2025-04-04T05:53:01.165Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/284

**Image: 1000050348**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email on a mobile device. The email is from "22t1 se2002" to "me" and is about Project 1 prerequisites. The email outlines the requirements for the project and provides an evaluation of whether the learner has met those requirements.

**2. Any text content visible:**

The email contains the following text:

*   **Subject:** (Implied, but likely related to Project 1)
*   **Sender:** 22t1 se2002 (sent 3 days ago)
*   **Recipient:** to me
*   **Body:**
    *   "Dear Learner,"
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (The "TDS Project 1: Evaluation page" is a hyperlink)
    *   A numbered list of 5 requirements:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of evaluations:
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: PASS"
        *   "Is Dockerfile present in root of github repo: PASS"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"
    *   "Kind regards, TDS Team"
    *   "Note: Do NOT reply to this email. It is only

**Image: 1000050349**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository page viewed on a mobile device. It displays the file structure and details of a repository named "00-Arya". The UI elements include:

*   **Header:** Displays the time (11:06), network status, battery level (23%), and the GitHub URL: "github.com/00-Arya". There are also icons for adding a tab, viewing tabs, and a menu.
*   **Repository Information:** Shows the repository's statistics: 0 stars, 0 forks, 1 watching, 1 branch, 0 tags, and an activity indicator. It also indicates that the repository is public.
*   **Branch Selection:** A dropdown menu indicates the current branch is "main".
*   **Code Button:** A green "Code" button, likely used to download or clone the repository.
*   **File Listing:** A list of files and directories within the repository.
*   **README and License:** Tabs at the bottom for viewing the README file and the MIT License.

**2. Text Content:**

*   **URL:** github.com/00-Arya
*   **Repository Stats:** 0 stars, 0 forks, 1 watching, 1 Branch, 0 Tags, Activity, Public repository
*   **Branch:** main
*   **Button:** Code
*   **Repository Name:** 00-Aryan
*   **File/Directory Names:**
    *   `__pycache__`
    *   `data`
    *   `.env`
    *   `Dockerfile`
    *   `LICENCE`
    *   `app.py`
    *   `datagen.py`
    *   `evaluate.py`
    *   `requirements.txt`
    *   `tasksA.py`
    *   `tasksB.py`
*   **Other Text:** 2 months ago, README, MIT license

**3. Context and Purpose:**

The image shows the contents of a GitHub repository. The purpose is to allow users to browse the files, understand the project structure, and potentially contribute to the project. The "Code" button suggests the user can download or clone

I am getting license not present at root of github repo but i have the license added could someone please explain why ?

---

## Reply 272
**Author**: Carlton D'Silva
**Posted**: 2025-04-04T06:06:04.491Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/285

@thinkmachine

Firstly, you have passed evaluation and got a decent score (on a more lenient script that we used for everyone.) The email was sent by a script that used a more stricter evaluation (which understandably caused some stress). So you can breathe a sigh of relief.  :slight_smile: 

*However* with regards to your long post…

Let me tell you a true story. I personally know a *very* experienced senior engineer at a top defense contractor for the US, here is some pearls of wisdom from him.

What you have done is what is called in industry as **gold plating**. Its a cardinal sin in software engineering. NEVER gold plate. ALWAYS build to spec.

In fact its a good reason to fire an engineer. Why?

Because it does not deliver what was required,
Wastes valuable time and resources
Increases technical debt (this is actually a huge cost over the expected lifetime of the project!)
Complicates testing
Leads to scope creep

His advice to me was simple: NEVER gold plate.

I hope you take this pearl of wisdom in your career. It will help you advance and make you stand out.

For personal hobbies this does not apply. But for a client (including us) if you fail to deliver the minimum spec then we cannot grant you an evaluation (by the way this post is not targetted specifically for you, it just felt like an appropriate place to explain this).

Kindest regards

---

## Reply 273
**Author**: Abhay Mehra
**Posted**: 2025-04-04T08:04:19.957Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/286

Hi Sir,

I just realized that I mistakenly submitted the image tag “abhay227/version1” instead of the correct image ID. The correct image ID is **4db729a03f74** , which is part of version1 that is already present and publicly available.

I have worked very hard on this project, and I am concerned that due to this error, my whole effort may be wasted. Unfortunately, I did not receive any notification regarding an invalid submission after I submitted the Project1 form, and I only recently became aware of this mistake. I kindly request you please consider this correct image ID.

Thank you for your understanding and assistance. I look forward to your positive response.

@carlton @Jivraj

**Image: Screenshot 2025-04-02 132214**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely from a container registry or similar platform, displaying information about a tagged container image. It presents details such as the tag name, last push date, digest, OS/architecture, last pull date, and compressed size. It also includes a command to pull the image using Docker.

**2. Any text content visible:**

*   **TAG:**
    *   `version1` (The tag name of the container image)
*   **Last pushed:** `Last pushed about 1 month by abhay227`
*   **Digest:**
    *   `4db729a03f74` (The unique identifier of the image)
*   **OS/ARCH:**
    *   `linux/amd64` (The operating system and architecture the image is built for)
*   **Last pull:**
    *   `about 1 month`
*   **Docker pull command:** `docker pull abhay227/tds_project:version1`
*   **Copy** (Button to copy the docker pull command)
*   **Compressed size:**
    *   `261.98 MB`

**3. The context or purpose of what's displayed:**

The UI is designed to provide users with information about a specific version of a container image stored in a registry. It allows users to:

*   Identify the image using its tag.
*   Verify the image's authenticity using its digest.
*   Understand the image's compatibility based on the OS/architecture.
*   Determine when the image was last updated or pulled.
*   Obtain the command to pull the image for local use.
*   See the compressed size of the image.

**4. Technical details:**

*   The image is tagged as `version1`.
*   The image was last pushed by user `abhay227` about a month ago.
*   The image's digest is `4db729a03f74`.
*   The image is built for `linux/amd64`.
*   The image was last pulled about a month ago.
*   The command to pull the image is `docker

---

## Reply 274
**Author**: Carlton D'Silva
**Posted**: 2025-04-04T09:06:11.401Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/287

Hi Abhay,

This was a basic error. Unfortunately for basic errors we are not able to relax the requirements. All students were given a clear directive on what the minimum requirements were in order to be evaluated. Failure to follow those clear instructions prevents us from making any exceptions, because then we just have to dump all those requirements for all students and that would not be fair to those that took the care to be careful about their submissions.

Kind regards

---

## Reply 275
**Author**: SP
**Posted**: 2025-04-04T21:47:18.782Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/288

Hi sir, hope you are doing well.

Could you please check and let me know if I have passed the project 1 and if yes then how much am I scoring in Project 1 after the latest evaluation?

@carlton

---

## Reply 276
**Author**: Shreyan Chaubey
**Posted**: 2025-04-04T22:16:43.757Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/289

Thanks for the clarification regarding the evaluation, @carlton. It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.

Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible **within the scope of the problem statement**.

What began as just another (pun intended) *tedious* assignment slowly evolved into a hobbyist research project on LLM agents.  :grinning_face_with_smiling_eyes: 

*(…caution: long post ahead  :sweat_smile: )*

I noticed that **test cases in Project 1 and 2 were highly specific and often overlapping on Python & Shell use**. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the **inherent randomness in LLM-generated payloads**. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.

Some might suggest using `temperature=0` to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.

**Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers**: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.

At the core of it, it’s all about **how much flexibility vs rigidity** we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.

Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,

Reason about the task, understand intent,
Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. *design* a DAG, where each node can be a python step or a shell step or something else)
Execute those workflows (*walk* the DAG) observing the feedback at each step and reiterating if needed.
Observe the final result, and repeat if needed.

Interestingly, a similar framework was suggested in [this ICLR 2022 paper](https://arxiv.org/abs/2210.03629). That was all the validation I needed to know I was stepping in the right direction.

To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of **general-purpose tools**:

A REPL executor (for quick calcs)
A Python script runner
A Shell executor

With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.

As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training & tuning ML models autonomously, reporting results etc.) — that was **emergent behavior**, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. *Frankly, I AM personally very keen about researching stuff!*

I am actually very thankful to the TDS course team & @s.anand for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. **Food for thought! Really!**

As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.

PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects: **thoughtful use of LLMs in agent design**. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride.  :grinning_face_with_smiling_eyes: 

**TL;DR**

My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.

Kind regards

---

## Reply 277
**Author**: Vansh Mittal
**Posted**: 2025-04-05T07:12:52.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/291

@carlton @Jivraj  Sir please Consider this request!

---

## Reply 278
**Author**: Srishty
**Posted**: 2025-04-05T13:32:19.021Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/292

Hello Sir,

**Image: Screenshot_2025-04-05-18-51-43-721_com.google.android.gm**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email displayed on a mobile phone. The email appears to be an automated evaluation report for a project submission. The email details the prerequisites for the project and whether the submission meets those requirements. The email also includes a score for the project.

**2. Text Content:**

The email contains the following text:

*   "Your GitHub repository exists and is publicly accessible"
*   "Your GitHub repository has a LICENSE file with the MIT license"
*   "Your GitHub repository has a valid Dockerfile"
*   "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
*   "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   "These are your Project 1 Prerequisite evaluations:"
*   "Is Docker image present in dockerhub AND is public: PASS"
*   "Is Github repo present AND public: FAIL"
*   "Is Dockerfile present in root of github repo: FAIL"
*   "Is MIT license present at root of github repo: FAIL"
*   "Prerequisites: FAIL"
*   "Project 1 Score: 0"
*   "Kind regards, TDS Team"
*   "Note: Do NOT reply to this email. It is only meant for official announcements and messages. If you need any further assistance please contact the course team via Discourse."
*   "Unsubscribe"
*   Reply, Reply all, Forward

**3. Context and Purpose:**

The email's purpose is to inform the recipient about the automated evaluation of their Project 1 submission. It outlines the prerequisites for the project and indicates whether the submission meets each requirement. The email also provides a score for the project, which in this case is 0, indicating that the submission failed to meet the minimum requirements.

**4. Technical Details:**

*   The email mentions Docker, Dockerfile, and GitHub, indicating that the project involves containerization and version control.
*   The `podman run` command suggests that the Docker image is

I got this mail regarding my project 1 scores. My github repo is present and public as well as MIT License and Dockerfile  is also present at the root of the repo

      [github.com](https://github.com/SrishtySnehi/Project_1_tds)

  [GitHub - SrishtySnehi/Project_1_tds](https://github.com/SrishtySnehi/Project_1_tds)

Contribute to SrishtySnehi/Project_1_tds development by creating an account on GitHub.

---

## Reply 279
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-05T13:43:36.526Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/293

Hi @Srishty_Snehi

Your submission is valid, we but it failed while running server, with this error.

taskA module missing

For regenerating this error:

Pull github repo(latest commit before 18th Feb)
Build image using Dockerfile of fetched repo
Run that image.

---

## Reply 280
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-05T13:45:08.530Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/294

We are not considering Dockerfile’s with wrong name(anything other than Dockerfile), and wrong location(anything other than root) in github repo.

---

## Reply 281
**Author**: Srishty
**Posted**: 2025-04-05T13:52:15.950Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/295

Will I still get a zero?

---

## Reply 282
**Author**: S Smriti
**Posted**: 2025-04-05T15:04:50.084Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/296

Can we expect the results for project 1 and 2 by tomorrow? @carlton @Jivraj

---

## Reply 283
**Author**: Aarush saxena 
**Posted**: 2025-04-05T16:02:30.289Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/297

when can we expect our project 1 result?

@Jivraj

---

## Reply 284
**Author**: S Smriti
**Posted**: 2025-04-06T10:10:34.222Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/299

I got my result!! 2/20 so happy its not a 0 thank you for the bonus @carlton @Jivraj  :sob: 

Also really great how yall have given the error logs for everyone individually  :saluting_face:

---

## Reply 285
**Author**: Shubham Atkal
**Posted**: 2025-04-06T10:19:54.144Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/300

@carlton @Jivraj in earlier evaluation of P1 in that my B1 is passed but in this final scores email it is showing as 0 for B1 pls help

**Image: finalB1**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a small portion of what appears to be a spreadsheet or table. It consists of two cells arranged vertically.

**2. Any text content visible:**

*   The top cell contains the text "B1".
*   The bottom cell contains the number "0".

**3. The context or purpose of what's displayed:**

The image likely represents a cell (B1) in a spreadsheet that currently holds the value 0. It's impossible to determine the overall purpose of the spreadsheet without more context. It could be used for data analysis, calculations, or any other task typically performed in a spreadsheet program.

**4. Technical details:**

There are no technical details visible in the image. It's a simple representation of data within a table or spreadsheet format.

**Image: b1passed**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a snippet of a log or output from a system, likely related to automated testing or task execution. It shows the status of a test ("B1 PASSED"), a task that is currently running ("Delete /data/format.md"), and an HTTP request related to that task.

**2. Any text content visible:**

*   "B1 PASSED" (preceded by a green checkmark icon)
*   "Running task: Delete /data/format.md" (preceded by a yellow circle icon)
*   "HTTP Request: POST http://localhost:8325/run?task=Delete+%2Fdata%2Fformat.md "HTTP/1.1 200 OK""

**3. The context or purpose of what's displayed:**

The image shows the progress and status of a process. "B1 PASSED" indicates that a test or stage named "B1" has successfully completed. The "Running task" line indicates that the system is currently deleting a file named "format.md" located in the "/data/" directory. The HTTP request shows the system is using a POST request to a local server (localhost:8325) to execute the delete task. The "HTTP/1.1 200 OK" indicates that the server responded successfully to the request.

**4. Technical details:**

*   **HTTP Request:** The image shows a POST request being made to a local server. The URL is `http://localhost:8325/run?task=Delete+%2Fdata%2Fformat.md`. The `task` parameter in the URL is used to specify the task to be executed, which in this case is deleting the file `/data/format.md`. The `%2F` is URL encoding for the forward slash character.
*   **HTTP Response:** The "HTTP/1.1 200 OK" indicates a successful HTTP response. "200 OK" is the standard HTTP status code for a successful request.
*   **File Path:** The file being deleted is located at `/data/format.md`. This is an absolute path, indicating the location of the file within the file system.

---

## Reply 286
**Author**: HariOm Pandey
**Posted**: 2025-04-06T10:21:36.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/301

Request for Clarification on Zero Marks Given – Repository Was Public with All Required Files

Dear @Carlton sir

I wanted to kindly request a clarification regarding the evaluation of my project submission. I noticed that I have been awarded zero marks, and I’m a bit confused because I had made sure that everything was in place.

My GitHub repository was **public** at the time of submission.
I had included the **Dockerfile** as required.
I also added the **MIT License** to the project.
For your reference, I am also attaching a **snapshot** of the repository as it was during the submission time.

Given all these were in place, I would really appreciate it if you could provide a **concrete reason** for giving **zero marks**. I’m eager to understand what went wrong so I can avoid it in the future and improve myself. But u saying in email that my repo was not public , not having dockerfile and not having mit licsence .

**Image: emailsnapshotfor_discourse**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a Gmail inbox. The email content appears to be an automated grading report for a project or assignment. It includes details about scoring, bonus criteria, repository checks, and a table showing individual task scores.

**2. Text Content:**

Here's a breakdown of the key text elements:

*   **Email Header:** Standard Gmail interface elements like "Compose," "Inbox," "Starred," "Sent," "Drafts," "Labels," and a search bar. The inbox shows a count of 8,170 unread emails.
*   **Email Body:**
    *   "You will get 1 mark for each task completed. A1-A10, B1-B10, C1-C5. C1-C5 are bonus tasks."
    *   "Your total score is out of 20."
    *   "We normalise your task scores to 20 based on the highest score in Project 1 which is 16. Therefore each task you successfully completed gives you 1.25"
    *   "Bonus is awarded for number of commits and repo size after removing all cache related and environment files. We do a power transform and scaling with weights of 2.5 for each of these features (so that outliers do not influence the scores)"
    *   "Your final score calculation is based on MIN (20, (task score + bonus))"
    *   "Github repo submitted: [URL to a GitHub repository]"
    *   "Docker repo submitted: hariompandey6388/ll-automation-agent2"
    *   "Pre-requisites check: (1 for pass, 0 for fail)"
        *   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
        *   "Github repo exists and is public (should have a timestamp before 18th of Feb): 0"
        *   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 0"
        *   "Github repo check - Dockerfile exists: 0"
    *   A table with rows labeled A1-A10, B1

**Image: repo_snapshotforDiscourse**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository page. It shows the user interface of a GitHub repository, including the file directory, repository details, and various interactive elements.

**2. Text Content:**

*   **URL:** github.com/harrypandey829/tds\_llm\_automation-agent
*   **Repository Name:** tds\_llm\_automation-agent
*   **Username:** harrypandey829
*   **Tabs:** Code, Issues, Pull requests, Actions, Projects, Wiki, Security, Insights, Settings
*   **Branch:** main
*   **Files/Directories:**
    *   \_pycache\_
    *   .env
    *   LICENSE
    *   app.py
    *   datagen.py
    *   dockerfile
    *   evaluate.py
    *   tasksA.py
    *   tasksB.py
    *   README
    *   MIT license
*   **Buttons/Links:** Add file, Code, Pin, Fork, Star
*   **About Section:**
    *   "This is my final effort towards tds project."
    *   MIT license
    *   Activity
    *   0 stars
    *   1 watching
    *   0 forks
*   **Releases:** No releases published, Create a new release
*   **Packages:** No packages published, Publish your first package
*   **Languages:** Python 100.0%
*   **Other:** "Type / to search", "Relaunch to update"

**3. Context and Purpose:**

The image displays the main page of a GitHub repository named "tds\_llm\_automation-agent". The repository appears to be a project related to "tds" (likely a specific task or domain) and uses LLM (Large Language Model) automation. The "About" section suggests that this is the final effort towards the TDS project. The presence of files like "app.py", "datagen.py", "evaluate.py", "tasksA.py", and "tasksB.py" indicates that the project likely involves Python code for data generation, evaluation, and task automation. The "dockerfile" suggests that the project

please just check my repo  manually  and clarify whether it was public or not . What is going on this degree .

---

## Reply 287
**Author**: HariOm Pandey
**Posted**: 2025-04-06T10:25:14.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/302

And also i ran the evaluate.py and got the 10/10 during submission , atleast you can give 4-5 by which i can pass this course .

---

## Reply 288
**Author**: Arun Vembu S
**Posted**: 2025-04-06T10:27:58.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/303

Hi sir

I noticed a discrepancy in my Project 1 results. In the initial results shared on March 29th, I had received 8/20 based on the evaluation logs. However, the final result I received today states that none of the tasks in Task A and B were working, and I was awarded only 1 bonus mark.

During my own testing, I was consistently getting 7/10 correct in Task A, so I’m a bit confused about the change.

Kindly request you to look into this discrepancy sir

Thank you

---

## Reply 289
**Author**: Gautam Ashish Goyal
**Posted**: 2025-04-06T10:28:00.542Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/304

Dear @carlton Sir,

I was getting 8 marks in your evaluation but today I checked the mail, I was awarded 0 marks. I am not sure what happened. Everything was in place. I would really appreciate if you can provide a reason for zero marks. I rechecked everything and looks good. Awaiting your reply. Thanks.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of a user interface, likely from a testing or evaluation environment. It displays the results of a test or process, including a failure message, a score, and details about an HTTP request.

**2. Text content visible:**

*   "BIO FAILED" (preceded by a red "X" icon)
*   "Score: 8 / 20" (preceded by a target icon with a dart in the center)
*   "HTTP Request: POST https://aipro..." (the URL is cut off)

**3. Context or purpose of what's displayed:**

The image indicates that a process or test related to "BIO" has failed. The user received a score of 8 out of 20, suggesting a partial success or a low performance. The "HTTP Request" line provides information about a network request made during the process, indicating it was a POST request to a URL starting with "https://aipro...". This suggests the system is interacting with an AI-related service or API.

**4. Technical details:**

*   The "BIO FAILED" message likely refers to a specific component or module within the system being tested. "BIO" could stand for "Basic Input/Output" or another domain-specific term.
*   The HTTP request information is useful for debugging and understanding how the system interacts with external services. The full URL would be needed to fully understand the request.
*   The score indicates a quantitative measure of performance, which could be based on various factors depending on the context of the test.

---

## Reply 290
**Author**: Bharat Choudhary
**Posted**: 2025-04-06T10:39:13.548Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/305

same i also got 8 marks but today in mail i got 0 marks

---

## Reply 291
**Author**: Abhishek
**Posted**: 2025-04-06T10:46:30.789Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/306

Same issue for me, I was getting 10/20 earlier and now, in mail it shows 1.

---

## Reply 292
**Author**: Adarsh kumar
**Posted**: 2025-04-06T10:56:01.110Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/307

Same issue for me, i had got 4/20 before but in the mail, my marks is given as 0. Please help

---

## Reply 293
**Author**: Anisha Seth
**Posted**: 2025-04-06T11:08:05.832Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/308

Respected sir,

I have passed all pre-requisites however my file wasn’t evaluated due to port error (127.0.0.1). Please allow me rectify it as it everything else has passed and is in accordance to the guidelines and I had worked really hard for it not to be evaluated only.

---

## Reply 294
**Author**: Bingi Sai Mohith
**Posted**: 2025-04-06T11:09:50.310Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/309

Dear @carlton Sir,

I’ve noticed discrepancies in my Project 1 results. During the tests I ran before submitting, I consistently got about 7/10 in Task A. In the results shared earlier, I was informed that my evaluation log file was missing. Later, a Gform regarding the architecture was sent, which I filled and submitted. Now, the final result I received today, shows that the taskA module is missing and I’ve been given a bonus of 1 mark.

I kindly request you to look into the matter and provide an explanation and solution in this regard.

Thank you.

---

## Reply 295
**Author**: Santosh Sharma
**Posted**: 2025-04-06T11:56:39.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/310

Respected Sir,

I hope you’re all doing well. I’m writing regarding my Project 1 evaluation, as I’ve encountered a discrepancy that I’d like some help with.

According to the evaluation email I received, my score was 0 for all the tasks with an additional bonus of 1 (totaling a P1 score of 1). However, when I ran the provided evaluation script before my submission, I got 7 in Phase A. Additionally, after reviewing the Docker logs, evaluation logs, and the p1_evaluation_error_logs (from the linked Google Sheets), I couldn’t find any reference to my roll number.

Could someone please help me investigate this issue? I’d really appreciate any guidance from the evaluation team.

Thank you for your time and assistance!

---

## Reply 296
**Author**: Kartikay Taunk
**Posted**: 2025-04-06T11:57:17.109Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/311

@carlton i am sure i had cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found my be but still i have been alloted 0 in all the cases , this is no small issue as project holds a significant amount of weightage in the end term

I had spent hours finishing my project and this i am sure my marks are not on par with the desired work i did

Look into this matter as it signifies if i will be able yo pass tds in this term or not.

---

## Reply 297
**Author**: Kartikay Taunk
**Posted**: 2025-04-06T11:58:19.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/312

I am facing the exact same issue

---

## Reply 298
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T12:03:01.767Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314

Hi Hari,

I just *manually* checked your repo.

**Image: Screenshot 2025-04-06 at 5.32.06 pm**
Here's a detailed description of the image:

**1. What is shown in the image:**

*   The image shows a web browser window displaying a GitHub 404 error page.
*   The main content of the page includes a large "404" text, a speech bubble with the message "This is not the web page you are looking for.", and a cartoon illustration of the GitHub Octocat dressed as a Jedi from Star Wars.
*   The background is a stylized desert landscape with a blue sky.
*   The browser's address bar is visible at the top.

**2. Any text content visible:**

*   **Address Bar:** `https://github.com/harrypandey829/tds_llm_automation-agent`
*   **Error Message:** "404"
*   **Speech Bubble:** "This is not the web page you are looking for."

**3. The context or purpose of what's displayed:**

*   The image indicates that the user has tried to access a specific GitHub repository or page, but it does not exist or is no longer available.
*   The URL in the address bar suggests the user was trying to access a repository named "tds\_llm\_automation-agent" owned by the user "harrypandey829".
*   The 404 error page is a standard response from a web server when a requested resource cannot be found.

**4. Technical details:**

*   The image is a screenshot of a web browser.
*   The URL indicates that the website is GitHub.
*   The 404 error is a standard HTTP status code.

This is what *you* submitted:

2/15/2025 21:08:32

21f3002112@ds.study.iitm.ac.in

[ https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent)

hariompandey6388/ll-automation-agent2

Kind regards

---

## Reply 299
**Author**: Avinash Kumar
**Posted**: 2025-04-06T12:16:09.978Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/315

@carlton  sir  When I submitted project 1, I was passing part A with 8/10 marks but today it is showing 0 marks on my email, but when I run it just now it is showing 4/10 on my vs code.

Whereas when I download the file from GitHub and run it, it is showing 1/10 now.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor (likely VS Code) with multiple files open. The file `app.py` is currently displayed in the editor window. The bottom panel shows the "TERMINAL" tab, displaying output from a program execution. There's a file explorer on the left showing the project structure.

**2. Text Content:**

*   **File Explorer:**
    *   `app.py`
    *   `datagen.py`
    *   `evaluate.py`
    *   `tasksA.py`
    *   `tasksB.py`
    *   `.env`
    *   `dockerfile`
    *   `LICENSE`
    *   `data`
    *   `_pycache_`
*   **`app.py` Code:**
    *   `# app.py`
    *   `# /// script`
    *   `# dependencies = [`
    *   `# "requests",`
    *   `# "fastapi",`
    *   `# "uvicorn",`
    *   `# "python-dateutil",`
    *   `# "pandas",`
*   **Terminal Output:**
    *   `the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 "HTTP/1.1 200 OK"`
    *   `HTTP 200 { "message": "A10 Task 'The SQLite database file \`/data/ticket-sales.db\` has a \`tickets\` with columns \`type\`, \`units\`, and \`price\`. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the \\"Gold\\" ticket type? Write the number in \`/data/ticket-sales-gold.txt\`' executed successfully" }`
    *   `HTTP Request: GET http://localhost:8000/read?path=/data/ticket-sales-gold.txt "HTTP/1.1 

**Image: WhatsApp Image 2025-04-06 at 17.28.47_927a687b**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a laptop screen displaying a code editor (likely VS Code) with several files open. The editor is in a dark theme. The file `app.py` is currently active. The bottom panel of the editor shows the "TERMINAL" tab, displaying output from a program execution. The laptop itself is visible in the foreground, showing the keyboard and part of the trackpad.

**2. Text Content:**

*   **File Names (Editor Tabs):** `app.py`, `evaluate.py`, `tasksA.py`, `tasksB.py`, `dockerfile`, `.env`, `datagen.py`
*   **`app.py` Code Snippet:**
    *   `from fastapi import FastAPI, HTTPException, Query`
    *   `from fastapi.responses import PlainTextResponse, JSONResponse`
    *   `from fastapi.middleware.cors import CORSMiddleware`
    *   `from tasksA import *`
    *   `from tasksB import *`
*   **Terminal Output:**
    *   `HTTP 200 { "message": "A10 Task 'The SQLite database file `/data/ticket-sales.db` has a `tickets` with columns 'type', 'units', and `price`. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the \"Gold\" ticket type? Write the number in `/data/ticket-sales-gold.txt`' executed successfully" }`
    *   `HTTP Request: GET http://localhost:8000/read?path=/data/ticket-sales-gold.txt "HTTP/1.1 200 OK"`
    *   `/data/ticket-sales-gold.txt`
    *   `EXPECTED: 177250.79`
    *   `RESULT: 200401.84`
    *   `A10 FAILED`
    *   `Score: 4 / 10`
*   **Terminal Prompt:** `PS C:\Users\avina\Desktop\TDS_Project3>`
*   **Status Bar:** Shows information like the user (`

---

## Reply 300
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T12:22:00.340Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316

To replicate the test environment:

Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.

# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&per_page=1&page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

    # Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

        # Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

        # Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

        with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

        # Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

    else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")

Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.

`docker build -t <your image name>   .`

Run new docker image using

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 <your image name>`

Keep datagen.py and evaluate.py in same folder

`uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000`

This then re-produces the exact environment how your application was  tested.

You have to provide a token from your environment for testing.

These instructions are same for everyone. So check first before posting here.

---

## Reply 301
**Author**: Kasif khan
**Posted**: 2025-04-06T12:22:16.600Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/317

I am also facing same issue cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found  but still i have been alloted 0 in all the cases

---

## Reply 302
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T12:28:18.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/318

@Arunvembu @22f2000008 @23f1000879 @22f3003201 @23f2000926 @22f3001702 @Santoshsharma @kartikay1 @Kasif

Check first by following the instructions show here:

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
git clone <your repo url> 
cd <your repo directory> 
docker build -t <your image name> 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name> 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…

Then post with your queries after testing as mentioned above.

Also check the evaluation logs first to see why it failed. Address that question.

Posting “it ran before submission” is insufficient evidence.

The whole point of deployability is that it runs anywhere at anytime.

That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).

Kind regards

---

## Reply 303
**Author**: HariOm Pandey
**Posted**: 2025-04-06T12:44:34.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/319

But in email u said n , your repo was not public, even not had dockerfile nor mit licence that’s what I mentioned.

---

## Reply 304
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T12:47:16.601Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/320

Your repo is not public! Thats why we cannot see any other files either. If its not public we cannot see if other files exist. We cannot evaluate an invisible repo.

---

## Reply 305
**Author**: HariOm Pandey
**Posted**: 2025-04-06T12:47:43.321Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/321

I got email , your repo was not public even had not a dockerfile nor mit licence, that’ what I mentioned.

---

## Reply 306
**Author**: HariOm Pandey
**Posted**: 2025-04-06T12:50:04.091Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/322

My repo is public even before it was. How can I set to public..thisis same n while creating new repo u just select the public and not private that’s it n.

---

## Reply 307
**Author**: HariOm Pandey
**Posted**: 2025-04-06T12:50:21.105Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/323

What else I can do . For public.

---

## Reply 308
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T12:53:18.888Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/324

You misspelt your repo. Did you even check the post i sent with your details?

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314) Tools in Data Science

    Hi Hari, 
I just manually checked your repo. 
 [Screenshot 2025-04-06 at 5.32.06 pm] 
This is what you submitted: 

2/15/2025 21:08:32 
21f3002112@ds.study.iitm.ac.in 
[ https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent) 
hariompandey6388/ll-automation-agent2 
Kind regards

---

## Reply 309
**Author**: Yashvardhan
**Posted**: 2025-04-06T12:58:18.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/325

Dear @Jivraj  @carlton Sir,

I run evalution  script that you provide us via mail recently, my code is actively running and able to pass 11 task but I was awarded 1 Marks pls check where is the issue,[My full code was done in linux Environment]  (github codespace)

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Terminal/Console:** The primary UI element is a terminal or console window. It displays text-based output, likely from a program execution. The prompt shows a username (`singh-yash129`), the current directory (`/workspaces/Large-Language-Model`), and the branch (`main`).
*   **Popup/Dialog Box:** A popup dialog box is present, asking if the user wants to install the recommended 'Python' extension from Microsoft for the Python language. It has "Install" and "Show Recommendations" buttons.
*   **Taskbar:** The bottom of the image shows a taskbar with various application icons (e.g., Microsoft Teams, Outlook, a file explorer, a browser, VS Code, etc.).
*   **Status Bar:** A status bar is visible at the bottom of the code editor, showing information like line number (Ln 61), column number (Col 4), spaces (4), encoding (UTF-8), line feed (LF), language mode (Python), and a "Chat limit reached" notification.

**2. Text Content:**

*   **HTTP Request (GET):** `HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 404 NOT FOUND"` This indicates a GET request to a local server (localhost:8000) to read a file named "c5.txt" located in the "/data" directory. The server returned a "404 NOT FOUND" error.
*   **Error Messages:**
    *   `C5 failed: Cannot read /data/c5.txt`
    *   `C5 FAILED`
*   **Score:** `Score: 11 / 25`
*   **HTTP Request (POST):** `HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"` This indicates a successful POST request (HTTP 200 OK) to an API endpoint related to OpenAI embeddings.
*   **Terminal Prompt:** `@singh-yash129 →/workspaces/Large-Language-Model (main) $`
*

---

## Reply 310
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T13:00:28.513Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/326

You have to replicate this test environment for testing.

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
git clone <your repo url> 
cd <your repo directory> 
docker build -t <your image name> 
Run new docker image using 
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name> 
Keep datagen.py and evaluate.py in same folder 
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000 
This then re-produces the exact environment how your application was  tested. 
You have to provide a token from your environment for testing. 
The…

Please replicate this first. We also run it on a linux server.

Kind regards

---

## Reply 311
**Author**: HariOm Pandey
**Posted**: 2025-04-06T13:01:22.911Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/327

I am not talking about this , just see the snapshot that I applied above on that email u said your repo is not public

---

## Reply 312
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T13:03:31.773Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/328

We are ONLY going to evaluate what you submitted. Its the same rule for everyone. If the repo you provided is not accessible,  you will not be evaluated.

---

## Reply 313
**Author**: HariOm Pandey
**Posted**: 2025-04-06T13:06:40.691Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/329

Okay tell me one thing if I got fail in this course then in the next term, I will have not to give roe because it’s rule for every other courses.And see provide the content of tds in Indian guy youtuber because we belong to rural areas and not able to understand the accent of foreigners youtuber . It’s kind your sympathy.

---

## Reply 314
**Author**: Tushar Jalan 
**Posted**: 2025-04-06T13:29:44.621Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/330

**Things i have done for my project to work locally:**

 carlton:

`git clone <your repo url>`

cloned my repo which looked like this after cloning(ignore those green dots)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a portion of a user interface, likely from a code editor or IDE (Integrated Development Environment). It displays a file explorer or project view. The UI elements include:

*   A project name at the top: "TDS\_PROJECT\_1"
*   A collapsible/expandable folder named "tds-project-1" (indicated by the arrow).
*   A file named "LICENSE" with a key icon next to it.
*   Icons for creating a new file, creating a new folder, refreshing, and collapsing all folders.
*   A small green circle.

**2. Any text content visible:**

*   "TDS\_PROJECT\_1"
*   "tds-project-1"
*   "LICENSE"

**3. The context or purpose of what's displayed:**

The image shows the file structure of a project named "TDS\_PROJECT\_1". The "tds-project-1" folder is likely the root directory of the project. The "LICENSE" file suggests that the project has a license agreement associated with it. The green circle might indicate the status of the project, such as whether it's connected to a source control system (e.g., Git) and if there are any uncommitted changes.

**4. Technical details if it's a code screenshot or technical diagram:**

This is not a code screenshot or technical diagram. It's a UI element displaying the file structure of a project. The key icon next to the "LICENSE" file suggests that it's a file related to licensing or security. The icons at the top are standard UI elements for file management operations within the IDE.

All the files are  in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.

 carlton:

Keep datagen.py and evaluate.py in same folder

when i do this(  :down_arrow: ) i get this error

 carlton:

`docker build -t <your image name>`

PS D:\TDS_Project_1\tds-project-1> docker build -t "tushar2k5/tds-project-1"                                                                 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

Instead,in order to run the docker image successfully  we have to do either of the two things(taken help from chatgpt  :upside_down_face: ):

1)

Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1

**OR**

2)

Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .

*Both the things work for me*( :up_arrow: )

 carlton:

`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>`

docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1

Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)

 carlton:

`uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000`

uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000 

Done this to evaluate my project

Any finally the main part (DRUM ROLLS  :drum: ,not this one  :oil_drum:  (IUKUK))

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a terminal window, likely within a code editor like VS Code. The terminal displays the output of a running task and some error messages.

**2. Any text content visible:**

*   **Task Description:** "Running task: Does the statement 'I hate you' have a positive or negative connotation? Reply as a single string containing either 'POSITIVE' or 'NEGATIVE' in uppercase. Save the result to /data/c5.txt"
*   **Error Message:** "C5 failed: Server disconnected without sending a response."
*   **Failure Indicator:** "X C5 FAILED" (with a red X icon)
*   **Score:** "Score: 6 / 25" (with a target icon)
*   **HTTP Request:** "HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK""

**3. The context or purpose of what's displayed:**

The context suggests that the user is running a task that involves analyzing the sentiment of the phrase "I hate you". The task requires the program to determine if the phrase has a positive or negative connotation and save the result (either "POSITIVE" or "NEGATIVE" in uppercase) to a file named "c5.txt" in the "/data/" directory.

The error message "C5 failed: Server disconnected without sending a response" indicates that the task failed, likely due to a network issue or a problem with the server the program is trying to communicate with.

The score "6 / 25" suggests that this is part of a larger evaluation or test, and the user has achieved a score of 6 out of a possible 25.

The HTTP request line indicates that the program is making a POST request to an OpenAI embeddings endpoint. This suggests that the program is using OpenAI's API to generate embeddings for the input text, which are then used to determine the sentiment.

**4. Technical details (code screenshot or technical diagram):**

While the image doesn't show the code itself, the terminal output provides some technical details:

*   **API Endpoint:** The program is using the OpenAI embeddings API at the endpoint "https://aiproxy.

**THATS 6/25**

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a list of pre-requisite checks, likely from a software development or deployment process. Each check is a statement about the existence or properties of a repository or file, followed by a numerical result (1 or 0).

**2. Any text content visible:**

The text content includes:

*   **Title:** "Pre-requisites check: (1 for pass, 0 for fail)"
*   **Check 1:** "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   **Check 2:** "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   **Check 3:** "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
*   **Check 4:** "Gihub repo check - Dockerfile exists: 0"

**3. The context or purpose of what's displayed:**

The purpose is to verify that certain conditions are met before proceeding with a task. The checks ensure that necessary repositories exist, are publicly accessible, and contain specific files (LICENSE and Dockerfile). The "1" or "0" indicates whether each condition is met (pass) or not (fail).

**4. Technical details:**

*   The checks relate to Docker and GitHub repositories.
*   The checks include verifying the existence of a Dockerfile and a LICENSE file (or LICENSE.md) in the GitHub repository. The LICENSE check specifically mentions an MIT License.
*   The timestamp check suggests a requirement for the repositories to have been created or updated before February 18th.
*   The last check, "Github repo check - Dockerfile exists: 0", indicates that a Dockerfile was not found in the GitHub repository, resulting in a failure.

Hopping to get a response from you guys,

Thanks a lot(wrote this much for first time for any course)

(PS:This course has some special place in my heart  :heart: )

@Jivraj @s.anand

---

## Reply 315
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T13:31:50.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/331

We fetched your latest github commit before 18th Feb and build image through that and evaluated.

Your latest github repo before 18 has:

username : `singh-yash129`

Repo : `Large-Language-Model`

commit_sha: `88f7439471151283f1218b46d209030dd7f4e5ae`

Use `https://github.com/<username>/<repo>/archive/<commit_sha>.zip` for downloading repo.

If You feel there is any problem with our evaluation script suggest edits to the scirpt.

---

## Reply 316
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T13:37:57.159Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/332

23f2003751:

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

---

## Reply 317
**Author**: Tushar Jalan 
**Posted**: 2025-04-06T13:49:39.300Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/333

Jivraj:

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

Sorry but its not possible to attend every single session and you guys haven’t informed us via email so how its our fault.For cases like this you guys should allow us to move our files to the root directory so it can work…(we just have to move files  in the repo please consider it)@carlton @Saransh_Saini @s.anand

(i have already made a rookie mistake in my dockerfile otherwise i would have got 9/25 but keeping that aside please let me get 6/25)

**Image: PuppyDogEyesSadGIF**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image features a close-up of an animated orange cat, likely from a movie or cartoon. The cat has large, expressive eyes that are wide and pleading. Its paws are held up in a gesture that suggests begging or asking for something.

**2. Any text content visible:**

The word "PLEASE" is written in white, bold capital letters at the bottom of the image.

**3. The context or purpose of what's displayed:**

The image is clearly designed to evoke a feeling of sympathy or to encourage someone to grant a request. The combination of the cat's pleading expression and the word "PLEASE" makes it a common meme or reaction image used to express a desire or a request in a humorous or endearing way.

**4. Technical details:**

The image appears to be a digital animation or a still frame from an animated movie. The cat's fur has a textured appearance, and the lighting is soft, creating a visually appealing and emotive image. The background is blurred and green, suggesting an outdoor setting.

**Image: GojoSadGojoGIF**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows an animated character sitting on a set of stairs. The character appears to be male, with white or light gray hair. He is wearing a dark, possibly black, outfit that covers his entire body. He is sitting with his legs extended and slightly spread apart, and his head is resting on his hand, suggesting a posture of sadness, exhaustion, or contemplation. The stairs are a light brown or tan color.

**2. Any text content visible:**

*   At the top of the image, there is a watermark: "WWW.BANDICAM.COM".
*   At the bottom of the image, there is a watermark: "imgflip.com".

**3. The context or purpose of what's displayed:**

The image appears to be a frame from an animated video or GIF. The character's posture and the setting (sitting alone on stairs) suggest a moment of introspection or emotional distress. The watermarks indicate the software used to record the video (Bandicam) and a website where the image may have been created or shared (imgflip.com).

**4. Technical details:**

The image is likely a digital capture from an animation. The style of the animation is somewhat simple, with clear lines and flat colors. The presence of watermarks suggests that the image has been processed or shared online.

---

## Reply 318
**Author**: Pranaav
**Posted**: 2025-04-06T14:10:37.709Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/335

Good evening sir.

My original project evaluation conducted by IITM gave me 7/20, however the new evaluation gave me 0/20.

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image appears to be a log file or output from a system evaluation process, likely related to a coding or data processing task. It's displayed within what looks like an email interface (based on the left-hand navigation). The log contains a mix of task descriptions, HTTP requests and responses, and error messages.

**2. Text Content Visible:**

*   **Email Header:** `23f1002223@ds.study.iitm.ac.in_evaluation.log` (This suggests the log is associated with a specific user/submission at an academic institution).
*   **Task Descriptions:**
    *   "Running task: Convert https://raw.githubusercontent... to `/data/b9.html`"
    *   "Running task: Run datasette via `uvx datasette /data/tickets` count the number of rows where `type`... and save it to /data/b10.csv. Then stop the datasette server."
*   **HTTP Requests:**
    *   POST requests to `http://localhost:8301/run?task=...` (various tasks)
    *   GET requests to `http://localhost:8301/read?path=/data/...`
    *   POST request to `https://aiproxy.sanand.workers.dev`
*   **HTTP Responses:**
    *   `HTTP 200 { "message": "B9 Task 'Convert... executed successfully" }` (Indicates a successful task)
    *   `HTTP 400 { "detail": "HTTPConnectionPool... Failed to establish a new connection: [Errno 111] Connection refused" }` (Indicates a failed request due to connection issues)
*   **Error Messages:**
    *   "B9 failed: Cannot read /data/b9.html"
    *   "B10 failed: Cannot read /data/b10.csv"
    *   "B9 FAILED"
    *   "B10 FAILED"
*   **Score:** "Score: 7 / 20"
*   **Email Navigation:** "Compose", "Inbox", "Starred

This was from the official evaluation sir, could you kindly look into it.

---

## Reply 319
**Author**: Bharat Choudhary
**Posted**: 2025-04-06T14:13:19.854Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/336

did everything as mentioned i got 7/25 but in mail i got 2 which is bonus?

i know i didn’t add flask in docker it was my mistake  :frowning:  but can we just for once neglect that. pleaseeeeeeeee

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a terminal window, likely from a code editor or IDE like VS Code.
*   There are tabs at the top, with "PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL", and "PORTS" visible. The "TERMINAL" tab is highlighted, indicating it's the active view.
*   The terminal prompt is visible at the bottom.

**2. Text Content:**

*   `}` (likely part of a code block)
*   `HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 404 Not Found"`
*   `C5 failed: Cannot read /data/c5.txt`
*   `X C5 FAILED` (The X is likely a visual indicator of failure)
*   `Score: 7 / 25`
*   `HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"`
*   `PS C:\Users\choud\OneDrive\Desktop\tds1\TDS_Project_1>` (This is the PowerShell prompt, showing the current directory)

**3. Context and Purpose:**

*   The terminal output indicates a program is running and making HTTP requests.
*   The first HTTP request (GET) to `http://localhost:8000/read?path=/data/c5.txt` resulted in a "404 Not Found" error. This suggests the file `/data/c5.txt` could not be found on the server running at `localhost:8000`.
*   The message "C5 failed: Cannot read /data/c5.txt" confirms the program's inability to access the file.
*   The "Score: 7 / 25" line suggests the program is being evaluated or tested, and it has achieved a score of 7 out of a possible 25.
*   The second HTTP request (POST) to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings` was successful, returning a "200

---

## Reply 320
**Author**: Sanjita Prabhu
**Posted**: 2025-04-06T14:16:52.383Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/337

Please do consider allowing us to change the position of the dockerfile to the root. We are doing nothing but changing its location in the repo. This was not mentioned anywhere in the prerequisites before the submission and it is unfair to not consider all our work for a criteria that was nowhere mentioned in the course page before the submissions. It may be standard practice but a lot of us were unaware. Please do consider this request.

---

## Reply 321
**Author**: Abhay Mehra
**Posted**: 2025-04-06T14:21:15.929Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/338

Sir, could you please fetch my latest GitHub commit before 18th Feb and build the image through that one?

I received a mail saying that the Docker image is not accessible, but it is already there. Kindly request you to evaluate my submission.

---

## Reply 322
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T14:25:38.244Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/339

Hi @Abhay222

Docker image submitted by you doesn’t exists.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page displaying a 404 error. The page is from Docker Hub, a service for finding and sharing container images. The error message is presented within a large blue circle. Below the error message is a cartoon illustration of a person sitting at a computer.

**2. Any text content visible:**

*   **URL:** `https://hub.docker.com/r/abhay227/version1/tags`
*   **Docker Hub Navigation:** "Explore / abhay227 / version1"
*   **Search Bar:** "Search Docker Hub"
*   **Error Message:**
    *   "404"
    *   "Oops!"
    *   "The page you have requested was not found"
*   **Other UI elements:** "Ctrl+K", "Update", "Sign in", "Sign up"

**3. The context or purpose of what's displayed:**

The image indicates that the user attempted to access a specific page on Docker Hub related to a repository named "abhay227" and a version named "version1", specifically the "tags" section. However, the page was not found, resulting in the 404 error. This suggests that either the repository, the version, or the tags section does not exist or is not publicly accessible.

**4. Technical details:**

*   The URL structure `hub.docker.com/r///tags` is typical for accessing the tags associated with a Docker Hub repository.
*   The 404 error is a standard HTTP status code indicating that the server could not find the requested resource.
*   The presence of "Sign in" and "Sign up" buttons suggests that the user might need to be logged in to access certain repositories or versions.

---

## Reply 323
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T14:27:42.362Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/340

Hi @23f1000879

This basically tells you didn’t validate docker Dockerfile and docker image by building and running them, otherwise you would have corrected the mistake.

---

## Reply 324
**Author**: Abhay Mehra
**Posted**: 2025-04-06T14:28:03.210Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/341

**Image: Screenshot 2025-04-02 132214**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely from a container registry or similar platform, displaying information about a tagged container image. It presents details such as the tag name, when it was last pushed, the digest, OS/architecture, last pull time, compressed size, and a command to pull the image.

**2. Any text content visible:**

*   **TAG:**
    *   `version1` (tag name)
    *   "Last pushed about 1 month by abhay227"
*   **Digest:**
    *   `4db729a03f74` (digest value)
*   **OS/ARCH:**
    *   `linux/amd64`
*   **Last pull:**
    *   `about 1 month`
*   `docker pull abhay227/tds_project:version1` (command to pull the image)
*   `Copy` (button to copy the pull command)
*   **Compressed size:**
    *   `261.98 MB`

**3. The context or purpose of what's displayed:**

The UI is designed to provide users with information about a specific version of a container image stored in a registry. It allows users to identify the image, understand its characteristics (OS/architecture, size), and easily copy the command needed to download and run the image using Docker.

**4. Technical details:**

*   **Tag:** `version1` - This is a human-readable label assigned to a specific version of the image.
*   **Digest:** `4db729a03f74` - This is a unique cryptographic hash that identifies the exact content of the image. It's a more reliable identifier than the tag, as tags can be reassigned.
*   **OS/ARCH:** `linux/amd64` - This indicates that the image is designed to run on a Linux operating system with an AMD64 (x86-64) architecture.
*   **Docker Pull Command:** `docker pull abhay227/tds_project:version1` - This is the command used to download the image from the registry. `abhay227/

but it is available under version1.

---

## Reply 325
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T14:32:55.129Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/342

repo that you submitted through google form was different then this one.

Your Gform response

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a table-like interface, likely from a code repository or data management system.
*   There are tabs at the top labeled "Preview," "Code," and "Blame." The "Preview" tab is currently selected.
*   A search bar is present, with the email address "23f1001120@ds.study.iitm.ac.in" entered as the search query.
*   There are icons for "Commit" and "Raw" on the top right.

**2. Text Content:**

*   **Header:** "Preview Code Blame 1069 lines (1069 loc) • 127 KB Raw"
*   **Search Bar:** "Q 23f1001120@ds.study.iitm.ac.in"
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Data (Row 919):**
    *   "2/16/2025 23:10:43"
    *   "23f1001120@ds.study.iitm.ac.in"
    *   "https://github.com/23f1001120/Tds\_Project1"
    *   "abhay227/version1"

**3. Context and Purpose:**

*   The image appears to be displaying data related to a project or assignment.
*   The table shows a mapping between a student's email address, a GitHub repository link, and a DockerHub image name.
*   The search bar suggests that the user is filtering or searching for entries associated with a specific email address.
*   The "Preview" tab indicates that the user is viewing a formatted or summarized version of the data.

**4. Technical Details:**

*   The GitHub repository link follows a standard format: `https://github.com//

---

## Reply 326
**Author**: RAJ K BOOPATHI
**Posted**: 2025-04-06T14:35:49.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/343

Hi, I work in the IT industry. There is no standard like “docker file has to be only in the root folder.”

If at all you are setting a requirement why was this not mentioned in the project page?

We were asked to build an app which solves the given tasks. You were OK for whatever code/tools/method to use as long as it works, there the “industry standard” didn’t show up ironically!!!

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

In the same industry that I work - we build the dockers and give it for prod push.

---

## Reply 327
**Author**: Afsal
**Posted**: 2025-04-06T14:44:59.635Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/344

@carlton @Jivraj

Dear Sir,

I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.

I debugged that I had a small issue in the dockerfile that was submitted and it is

CMD [“/root/.local/bin/uv”, “run”, “app.py”]  has an **invisible Unicode non-breaking space** (`U+00A0`) between `"run", "app.py"` instead of a regular space. This causes the shell to misread the command.

I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE.  Expecting a positive response from your end.

---

## Reply 328
**Author**: Bharat Choudhary
**Posted**: 2025-04-06T14:49:28.608Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/345

sir, but before submission i run evluate.py and it gave me 8/10 in task A. after submission i also got result mail stating that i got 8/20.

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image displays a log or output from a system that appears to be evaluating code or tasks. It shows a series of tasks being run, along with their corresponding HTTP requests and responses.  The log includes error messages, success messages, and details about the execution of each task. The UI elements suggest it's being viewed within a web browser, possibly as part of a development or debugging process.

**2. Text Content Visible:**

The log contains the following key text elements:

*   **File Path:** `23f1000879@ds.study.iitm.ac.in_evaluation.log` (likely the name of the log file)
*   **Error Messages:**
    *   "B7 failed: cannot identify image file 

also this mail result Earlier i got From your side.  :frowning:

---

## Reply 329
**Author**: Abhay Mehra
**Posted**: 2025-04-06T14:50:49.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/346

Sir, I realized that I mistakenly submitted the image tag `"abhay227/version1"` instead of the correct image ID. The correct image ID is `4db729a03f74`, which is part of version1 and is already present and publicly available.

Unfortunately, I didn’t receive any notification about this issue after submission. Receiving this mail at this stage feels disheartening after all the effort I’ve put into the project.  I kindly request you please consider this correct image ID.

---

## Reply 330
**Author**: Maithreyi
**Posted**: 2025-04-06T15:05:57.719Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/347

**Image: Screenshot 2025-04-06 202736**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from a script or program, that performs a series of pre-requisite checks. The checks are related to the existence and properties of Docker and GitHub repositories.

**2. Any text content visible:**

The text content is as follows:

*   **Pre-requisites check: (1 for pass, 0 for fail)**
*   Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
*   Gihub repo check - Dockerfile exists: 1

**3. The context or purpose of what's displayed:**

The purpose of the displayed output is to verify that certain conditions are met before proceeding with a process or task. These conditions involve the existence and accessibility of Docker and GitHub repositories, as well as the presence of specific files (LICENSE and Dockerfile) within the GitHub repository. The "(1 for pass, 0 for fail)" indicates a boolean-like result for each check.

**4. Technical details:**

*   The checks are automated, likely performed by a script or program.
*   The checks involve verifying the existence of repositories on Docker Hub and GitHub.
*   The checks also verify the presence of a LICENSE file (either LICENSE or LICENSE.md) with an MIT License and a Dockerfile within the GitHub repository.
*   The timestamp check suggests that the repositories should have been created or updated before February 18th.
*   Each check returns a "1", indicating that all the pre-requisites have been met.

Hi, all my pre-requisites have been fulfilled, and the evaluation logs say I have a score of 10/25. But I have gotten a score of 0, saying ‘Task A module missing’. This is a kind request to confirm the scores.

---

## Reply 331
**Author**: Veer Shah
**Posted**: 2025-04-06T15:10:17.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/348

@carlton @Jivraj

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a Google Sheets spreadsheet. The spreadsheet appears to be a log of errors encountered during an evaluation process, likely related to a programming or software development project. The spreadsheet has two columns: "email" and a column with error messages. The spreadsheet is titled "p1_evaluation_error_logs". The spreadsheet is in "View only" mode.

**2. Text Content:**

*   **Title:** "p1\_evaluation\_error\_logs"
*   **Column Headers:** "email" (Column A), Column B is empty
*   **Data in Column A (email):** A series of email addresses, all following the pattern "23f[some number]@ds.study.iitm.ac.in". Examples include:
    *   23f1000049@ds.study.iitm.ac.in
    *   23f1000337@ds.study.iitm.ac.in
    *   23f1000625@ds.study.iitm.ac.in
    *   ...and so on.
*   **Data in Column B (Error Messages):** A variety of error messages, including:
    *   "taskA module missing"
    *   "app module missing"
    *   "application running on 5000 port"
    *   "SyntaxError: unmatched '}'"
    *   "flask module missing"
    *   "Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside(host os)"
    *   "npx not found"
    *   ".env file missing"
    *   "openai module missing"
    *   "PhaseA module missing"
*   **Other UI Text:**
    *   "File", "Edit", "View", "Insert", "Format", "Data", "Tools", "Extensions", "Help" (Google Sheets menu)
    *   "100%" (Zoom level)
    *   "View only"
    *   "Share"

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a window of Windows File Explorer. The window is displaying the contents of a folder, specifically a ZIP archive named "docker_logs.zip". The left pane shows the navigation pane with common locations like "Home", "Gallery", "OneDrive", "Desktop", "Downloads", "Documents", "Pictures", "Music", "Videos", "Bsc Ds", and "iitm". The main content area is empty, indicating that the ZIP archive is either empty or its contents are not being displayed. There is a search bar in the top right corner with the text "23f1001524" entered.

**2. Any text content visible:**

*   **Window Title:** "23f1001524 - docker\_logs.zip"
*   **Navigation Bar:** "Downloads > docker\_logs.zip"
*   **File Explorer Menu:** "New", "Sort", "View", "Extract all"
*   **Column Headers:** "Name", "Type", "Compressed size", "Password p...", "Size", "Ratio", "Date modified"
*   **Empty State Message:** "No items match your search."
*   **Navigation Pane:** "Home", "Gallery", "OneDrive - Perso", "Desktop", "Downloads", "Documents", "Pictures", "Music", "Videos", "Bsc Ds", "iitm"
*   **Search Bar:** "23f1001524"

**3. The context or purpose of what's displayed:**

The image likely shows a user searching for a specific file or folder within the "docker\_logs.zip" archive. The search term "23f1001524" has been entered in the search bar. The "No items match your search" message suggests that the search term does not match any files or folders within the archive. The user is viewing the contents of the "docker_logs.zip" file within the "Downloads" folder.

**4. Technical details:**

*   The image shows a standard Windows File Explorer interface.
*   The file type is a ZIP archive, commonly used for compressing and archiving files.
*   The search functionality is a built-in feature of Windows File Explorer.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a window of Windows File Explorer. The window is displaying the contents of a ZIP archive file. The left pane shows the navigation pane with common locations like "Home," "Gallery," "OneDrive," "Desktop," "Downloads," "Documents," "Pictures," "Music," and "Videos." The main content area shows the contents of the "evaluation_logs.zip" archive.

**2. Any text content visible:**

*   **Title bar:** "23f1001524 - evaluation\_logs.zip"
*   **Navigation bar:** "Downloads > evaluation\_logs.zip"
*   **Menu bar:** "New," "Sort," "View," "Extract all"
*   **Column headers:** "Name," "Type," "Compressed size," "Password protected," "Size," "Ratio," "Date modified"
*   **Content area:** "No items match your search."
*   **Left pane:** "Home," "Gallery," "OneDrive - Perso," "Desktop," "Downloads," "Documents," "Pictures," "Music," "Videos," "Bsc Ds," "iitm," "cp"
*   **Search bar:** "23f1001524"
*   **Details button**

**3. The context or purpose of what's displayed:**

The user has opened a ZIP archive file named "evaluation\_logs.zip" located in the "Downloads" folder. However, the archive appears to be empty, as indicated by the message "No items match your search." The user might be trying to access log files contained within the archive.

**4. Technical details:**

*   The image is a screenshot of the Windows File Explorer interface.
*   The file type being viewed is a ZIP archive, which is a common format for compressing and storing multiple files.
*   The "No items match your search" message suggests that either the archive is genuinely empty, or there might be an issue with how the File Explorer is displaying the contents (e.g., a corrupted archive, or a filtering issue).
*   The search bar contains the text "23f1001524", which could be a search query or an identifier related to the archive.

I cannot find my docker_logs nor evaluation_logs and nor anything on the forms . The mail I got says that i received 0 in project tasks but clearly my project is not evaluated. Please look into this. during earlier evaluation i got 7 marks but this time it is 0.

**Image: image**
Here's a detailed description of the image content:

**1. UI Elements:**

*   The image appears to be a screenshot of a webpage or document viewer.
*   There are standard browser-like navigation buttons at the top (back, forward, refresh, etc.).
*   There's a page indicator showing "2 of 4,356" with left and right arrow buttons for navigation.
*   The main content area displays text, URLs, and a table.

**2. Text Content:**

*   **Title:** "Your final t score calculation is based on MIN (20, (task score + bonus))"
*   **Github repo submitted:** "https://github.com/veershah1231/tds\_proj\_1"
*   **Docker repo submitted:** "veershah1231/tdsproject1final"
*   **Pre-requisites check: (1 for pass, 0 for fail)**
    *   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
    *   "Gihub repo check - Dockerfile exists: 1"
*   **Table:** A table with headers A1-A10, B1-B10, and C1-C5. All cells in the table contain the value "0".
*   "Your task score is: 0"
*   "Your bonus is: 1"
*   "Your P1 score is: 1"
*   "We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites."
*   "You will only have an evaluation log if your API service actually started working within 5 minutes. Otherwise you will have only a docker log."

**3. Context/Purpose:**

*   The image shows the results of an automated evaluation or grading system for a project.
*   The system checks for the existence and accessibility of Github and Docker repositories.
*   It also verifies the presence of a LICENSE file and a Dockerfile in

My roll number is 23f1001524 .

---

## Reply 332
**Author**: NK
**Posted**: 2025-04-06T15:10:52.149Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/349

@carlton and @Jivraj , for Task A i had tested before and all the test cases passed, but all my A tasks has failed with 0, In the evaluation logs, i could see that all task A tests failed due to datagen.py not available.

Could you rerun the test ?

---

## Reply 333
**Author**: Santosh Sharma
**Posted**: 2025-04-06T15:16:52.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/350

Respected Sir,

Thank you for your response and for providing the steps to replicate the test environment.

Steps Taken to Replicate the Test Environment

I cloned my repository using:

bash
git clone <my_repo_url>
cd <my_repo_directory>
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=<any_email> --token_counter 1 --external_port 8000

Issue with Original Submission

After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.

However, during your evaluation, this incompatibility caused the container to fail.

I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.

Action Taken

To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:

The application initializes correctly on port 8000 within 5 minutes.

It responds to requests within the required timeframe.

I have pushed this updated image to Docker Hub under the same repository:

Docker Hub URL: santoshsharma003/tds-project-one-1:latest

Request for Re-Evaluation

I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.

Previous Message for Reference

For your convenience, here is my earlier message explaining this issue in detail:

"Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!"

---

## Reply 334
**Author**: MITALI RAJ
**Posted**: 2025-04-06T15:32:18.435Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/351

same for me

my roll number is 23f1003094

---

## Reply 335
**Author**:  KARTHIK
**Posted**: 2025-04-06T15:35:02.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/352

Same with me sir @carlton

---

## Reply 336
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T15:39:13.854Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/353

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

Because if you did, you will realise why your evaluation failed.

You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.

Kind regards

---

## Reply 337
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T15:42:44.851Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354

You can take it up with @s.anand

I did not come up with the standard.

And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand if we could make the allowance. He made the decision to enforce this protocol.

Kindest regards.

---

## Reply 338
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T15:48:47.772Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/355

@carlton

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image displays a log or output from a program or system, likely related to a data processing or evaluation task. It shows a series of HTTP requests and responses, along with error messages and a final score. The UI elements are minimal, resembling a text-based log output within a larger application window (possibly a web browser).

**2. Text Content Visible:**

*   **File Path:** `23f2001390@ds.study.iitm.ac.in_evaluation.log` (This suggests the log is associated with a user ID and an evaluation process at an institution, likely IIT Madras).
*   **Error Messages:**
    *   "B9 failed: Cannot read /data/b9.html"
    *   "B10 failed: Cannot read /data/b10.csv"
    *   "HTTP/1.1 404 Not Found" (for both `/data/b9.html` and `/data/b10.csv`)
    *   "HTTP/1.1 400 Bad Request"
    *   HTTP 400 { "detail": "HTTPConnectionPool (host='localhost', port=8001): Max retries exceeded with url: /ticket-sales.csv?sql=SELECT COUNT(*)+FROM+tickets+WHERE+type+=%22Bronze%22 (Caused by NewConnectionError(': Failed to establish a new connection: \[Errno 111] Connection refused'))" }
*   **Task Description:**
    *   "Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background."
    *   "From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv?sql=SELECT COUNT(*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv."
    *   "Then stop the datasette

Respected Sir,

see the above image its from the scores we got from mail just before the latest one, in that I had got 7/20 and now new mail shows I got 0?? how is this possible…

the link for evaluation in which i got 7/20 is : [23f2001390@ds.study.iitm.ac.in_evaluation.log - Google Drive](https://drive.google.com/file/d/1cNVy9KSfSITZg_KGLF2_wwLWjzNl8mb5/view)

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image appears to be a status report or evaluation summary for a project or assignment. It shows information about submitted repositories (GitHub and Docker), prerequisite checks, and scoring details. There's also a table-like structure with labels A1-A10, B1-B10, and C1-C5, each containing a value of 0.

**2. Text Content:**

*   **Headers:**
    *   "Github repo submitted:"
    *   "Docker repo submitted:"
    *   "Pre-requisites check: (1 for pass, 0 for fail)"
*   **Repository Information:**
    *   A GitHub repository URL: "https://github.com/23f2001390/lImagent"
    *   A Docker repository name: "23f2001390/llmagent"
*   **Prerequisite Checks:**
    *   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
    *   "Gihub repo check - Dockerfile exists: 1"
*   **Table Labels:** A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, C1, C2, C3, C4, C5
*   **Scores:**
    *   "Your task score is: 0"
    *   "Your bonus is: 1"
    *   "Your P1 score is: 1"
*   **Additional Information:**
    *   "We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites."
    *   "You will only have an evaluation log if your API service actually started working within 5 minutes.

MOST importantly mail shows :

**Your final t score** calculation is based on

MIN (20, (task score + bonus))

**Github repo submitted:** [GitHub - 23f2001390/llmagent](https://github.com/23f2001390/llmagent)

**Docker repo submitted:** 23f2001390/llmagent

**Pre-requisites check: (1 for pass, 0 for fail)**

Docker repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1

Gihub repo check - Dockerfile exists: 1

Your task score is: 0

Your bonus is: 1

Your P1 score is: 1

So according to the above, I passed the pre-requisites and also in mail u have mentioned that:

We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.

but I don’t find my mail id or roll number in the docker_logs.zip or evaluation_logs.zip  that has been given in the mail(latest), if I passed the pre requisites my logs should be there in the zip files included in this latest mail right, my roll number is 23f2001390 and email id is 23f2001390@ds.study.iitm.ac.in

and nor do i find my id in the p1_evaluation_error_logs so please help sir

Thank you

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a window from the Windows operating system's file explorer. It appears to be displaying the contents of a ZIP archive.

**2. Any text content visible:**

*   **Path:** `This PC > Downloads > docker_logs.zip` (This indicates the location of the archive being viewed)
*   **Column Headers:** `Name`, `Type`, `Compressed size`, `Password p...`
*   **Search Bar:** `23f2001390` (This suggests a search is being performed within the archive)
*   **Message:** `No items match your search.`
*   **Preview Message:** `Select a file to preview.`

**3. The context or purpose of what's displayed:**

The user is likely trying to find a specific file within the `docker_logs.zip` archive using the search term "23f2001390". The "No items match your search" message indicates that the search was unsuccessful. The "Select a file to preview" message suggests that no file is currently selected for preview.

**4. Technical details:**

*   The image shows a standard Windows file explorer interface.
*   The archive format is ZIP, as indicated by the `.zip` extension in the path.
*   The presence of a "Password p..." column suggests that the ZIP archive might be password-protected, although this is not certain.
*   The search bar indicates that the file explorer is actively searching for files within the archive.

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a window from a file explorer, likely Windows Explorer.
*   There's an address bar at the top showing the current path: "This PC > Downloads > evaluation\_logs.zip". This indicates the user is viewing the contents of a ZIP archive named "evaluation\_logs.zip" located in the Downloads folder.
*   Below the address bar are column headers: "Name", "Type", "Compressed size", and "Password p...". These are typical column headers for displaying files and folders within a file explorer.
*   On the right side, there's a preview pane with the text "Select a file to preview."
*   There's a search bar in the top right corner with the text "23f2001390" entered.

**2. Text Content:**

*   "This PC > Downloads > evaluation\_logs.zip" (Path in the address bar)
*   "Name" (Column header)
*   "Type" (Column header)
*   "Compressed size" (Column header)
*   "Password p..." (Column header - likely truncated "Password protected")
*   "No items match your search." (Message in the file listing area)
*   "23f2001390" (Text in the search bar)
*   "Select a file to preview." (Text in the preview pane)

**3. Context/Purpose:**

*   The user is likely trying to find a specific file within the "evaluation\_logs.zip" archive.
*   The search term "23f2001390" has been entered, but the message "No items match your search" indicates that no files within the ZIP archive match that search query.
*   The preview pane is empty because no file has been selected.

**4. Technical Details:**

*   The image shows a standard file explorer interface, suggesting the user is interacting with a file system.
*   The "evaluation\_logs.zip" file is a compressed archive, likely containing log files related to some kind of evaluation process.
*   The search functionality is being used to filter the contents of the ZIP archive.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a Google Sheets spreadsheet. The spreadsheet contains two columns: "email" and "error_reason". The spreadsheet appears to be a log of errors encountered during an evaluation process, likely related to a programming assignment or project. The top of the screen shows the standard Google Sheets UI elements, including the file menu (File, Edit, View, Insert, Format, Data, Tools, Extensions, Help), toolbar icons (print, undo, redo, format, etc.), zoom level, and a "View only" toggle.  There are also icons for sharing and account information in the upper right corner.

**2. Text Content:**

*   **Title:** "p1\_evaluation\_error\_logs"
*   **Column Headers:** "email", "error\_reason"
*   **Email Addresses:** A series of email addresses in the format "21f[various numbers]@ds.study.iitm.ac.in" and "22ds[various numbers]@ds.study.iitm.ac.in".
*   **Error Reasons:** A variety of error messages, including:
    *   "requests module missing"
    *   "application running on 5000 port"
    *   "functions module missing"
    *   "Usage: /app/start.sh "
    *   "/bin/sh: 1: [/root/.local/bin/uv,: not found"
    *   "app module missing"
    *   "nest\_asyncio module missing"
    *   "whisper module missing"
    *   "taskA module missing" (appears frequently)
    *   "SyntaxError: unmatched ']'"
    *   "flask\_cors module missing"
    *   "error: Failed to spawn: `app.py`, Caused by: No such file or directory (os error 2)"
    *   "Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside(host os)"
    *   "phaseA module missing"
*   **Other UI Text:** "File", "Edit", "View", "Insert", "

---

## Reply 339
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T16:00:57.299Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/356

@carlton

Same for sir. I have made my post similarly, roll number is 23f2001390 and email is 23f2001390@ds.study.iitm.ac.in

---

## Reply 340
**Author**: Dipshikha Patel
**Posted**: 2025-04-06T16:04:18.467Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/357

@carlton

i  also not found anything in this form  , but i got mail to score=0

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a Google Sheets spreadsheet. The spreadsheet appears to contain error logs from an evaluation process. The UI elements visible are typical of Google Sheets: the menu bar (File, Edit, View, Insert, Format, Data, Tools, Extensions, Help), toolbar icons (print, zoom, etc.), column headers (A, B), row numbers, and a search/filter box. The sheet is in "View only" mode.

**2. Text Content:**

*   **Title:** "p1\_evaluation\_error\_logs"
*   **Column Headers:** "email" (in column A)
*   **Data:** The spreadsheet contains two columns. Column A contains email addresses ending in "@ds.study.iitm.ac.in". Column B contains error messages. Here's a sample of the error messages:
    *   "taskA module missing"
    *   "pydub module missing"
    *   "couldn't import module app"
    *   "Could not import module 'MAIN'."
    *   "flask module missing"
    *   "PhaseA module missing"
    *   "Attribute 'app' not found in module 'app'"
    *   "ImportError: cannot import name 'logger' from 'app.utils.logger'"
    *   "Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside(host os)"
    *   "SyntaxError: unterminated string literal (detected at line 306)"
    *   "pytesseract module missing"
    *   "ImportError: libGL.so.1: cannot open shared object file: No such file or directory"
    *   "RuntimeError: Cannot install on Python version 3.12.9; only versions >=3.6,   :smiling_face_with_tear:

---

## Reply 341
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T16:05:27.961Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/358

Hi Hari,

Your docker failed to build.

Did you try to replicate the test environment as mentioned in

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

If you tried you would find that it will not build. Thats why you have no logs.

90 such cases are there where the image could not be built from your repo.

The specific error in your case is:

tried copying requirements.txt which doesn’t exists

Thats why there are no logs.

Kind regards

---

## Reply 342
**Author**: Santosh Sharma
**Posted**: 2025-04-06T16:11:26.543Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/359

Hello @carlton Sir, please reply to my query

---

## Reply 343
**Author**: Carlton D'Silva
**Posted**: 2025-04-06T16:13:31.188Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/360

We cannot allow changes to repos. This is a blanket rule for everyone. No exceptions. Since the only way to get your project to work is to make changes to it, we cannot score you for changes.

Kind regards

---

## Reply 344
**Author**: RAJ K BOOPATHI
**Posted**: 2025-04-06T16:15:38.400Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/361

Thanks for the response. We can go on endless discussions using “nice words” “professionally” with the number of questions we have. Finally we are at the receiving end as students in this setup.

What’s the take away for everyone? Let’s move on. This isn’t the end.

Positive or Negative - Real world outside will make everyone realise and everyone change their opinions (including me) as the time and environment changes.

---

## Reply 345
**Author**: LAKSHAY
**Posted**: 2025-04-06T16:39:30.463Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/362

What I observed is that most of the repositories appear to be copied from a single source. This original repository contains several issues, such as an incorrectly named Dockerfile and missing instructions to copy all necessary data. Unfortunately, many students seem to have uploaded it blindly without reviewing or fixing these problems.

---

## Reply 346
**Author**: Siddharth Kaushik
**Posted**: 2025-04-06T16:58:32.449Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/363

Hi I have my Dockerfile saved as dockerfile, given 0 for project 1 due to this. This doesn’t seem to be a big issue to grade me 0 for this. Kindly correct the score please.

---

## Reply 347
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T18:41:59.248Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/364

Most common reason for during running docker image was `taskA module was missing` which is because a lot of students blindly copied from someone with building and running image, if they would have done that they could have corrected it at early stage.

---

## Reply 348
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T18:52:33.721Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/365

For you check failed because of the naming of Dockerfile(It was named as dockerfile(d in small).

---

## Reply 349
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T18:56:17.830Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/366

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists

In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located

---

## Reply 350
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T18:59:11.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/367

MITALI_R:

23f1003094

While running docker image create by your github repo, we got following error `taskA module missing`

For regenerating it follow steps that are mentioned here : [Tds-official-Project1-discrepencies - #316](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

## Reply 351
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:02:28.148Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/368

For you naming of MIT License was not correct.

This shows naming criteria for adding License.

[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

## Reply 352
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T19:06:07.077Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/369

Sir actually my project doesn’t have requirements.txt, instead it installs automatically

when:

`uv run app.py` is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).

my dockerfile from the repo:

FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

here u can see it installs using pip install …

here it’s requiring `.env` file to be present in the project folder because my project when I was uploading to both git and docker had `.env` file for AIPROXY_TOKEN and I uploaded to docker with that `.env` file but as git doesn’t allow upload of `.env` file I couldn’t upload`.env` to git

the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because`.env` file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the `.env` file so it didn’t build so I had to create the `.env` file now to create the docker image, and for the dockerimage I had submitted, I built it with the `.env` file(it supports both`.env` file and environment variable one)

---

## Reply 353
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:15:23.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/370

After filling form you didn’t double check form.

 Abhay222:

I kindly request you please consider this correct image ID.

We can’t reconsider it.

---

## Reply 354
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:22:42.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/371

Yes problem was missing `.env` file, Your repo, was supposed to run in a test environment.

---

## Reply 355
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T19:25:48.506Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/373

Yes sir, please help me

---

## Reply 356
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:26:27.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/374

Sorry We can’t do any help, we won’t be considering for eval.

---

## Reply 357
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T19:27:12.497Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/375

But sir, It was supposed to run right…

---

## Reply 358
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:29:29.774Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/376

It Should build in any test environment using Dockerfile from your github repo.

---

## Reply 359
**Author**: Aryan Kumar
**Posted**: 2025-04-06T19:30:23.489Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/377

@Jivraj please tell me what was my mistake?

---

## Reply 360
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T19:36:51.088Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/378

It was named wrongly.

You named it LICENCE but it should be LICENSE or LICENSE.md.

---

## Reply 361
**Author**: D HARICHARAN 
**Posted**: 2025-04-06T19:54:37.949Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/379

But sir, just because the repository doesn’t have .env file it couldn’t build the dockerimage, the docker image will build in any test environment as u said but it requires the .env to be included which the git didn’t have(it doesn’t allow upload of it ofcourse), don’t rerun the evaluation again but please sir atleast give me those 7/20 marks along with the pre-requisite bonus(1mark) that was mailed earlier to me along with logs…this is my primary degree after 12th, I’m also not asking any extra marks just the marks that i got earlier:

**Image: image**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a log output or error report displayed within a web browser. The log appears to be related to a task involving a "datasette" database and HTTP requests. The log entries indicate failures in reading data files and issues with HTTP connections. The log is displayed in a white box overlaying a browser window.

**2. Text Content:**

Here's a breakdown of the key text content:

*   **File Path:** `23f2001390@ds.study.iitm.ac.in_evaluation.log` (This suggests the log is from an evaluation or assessment context, possibly related to a student at IIT Madras).
*   **Error Messages:**
    *   "B9 failed: Cannot read /data/b9.html"
    *   "B10 failed: Cannot read /data/data/b10.csv"
    *   "HTTP/1.1 404 Not Found" (repeated)
    *   "HTTP/1.1 400 Bad Request"
    *   "Connection refused"
*   **Task Description:**
    *   "Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background."
    *   "From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv?sql=SELECT COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv."
    *   "Then stop the datasette server."
*   **HTTP Requests:**
    *   GET http://localhost:8369/read?path=/data/b9.html
    *   POST http://localhost:8369/run?task=... (a long URL-encoded string describing the task)
    *   GET http://localhost:8369/read?path=/data/b10.csv
    *   POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings
*   **Score

---

## Reply 362
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T21:53:15.006Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/380

Hi @23f2002600 @21f1005908

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) Tools in Data Science

    You can take it up with @s.anand 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

## Reply 363
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:07:19.469Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/381

Runned for you, it A1 Fails.

---

## Reply 364
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:10:05.622Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/382

Your docker image and github repo are not consistent,  your docker image was not built with the latest code before 18th feb that’s present in your github repo.

---

## Reply 365
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:13:27.848Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/383

We can’t consider any changes after deadline.

---

## Reply 366
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:21:06.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/384

Your docker image and github repo are not consistent.

While running docker image we got following error: `flask module missing`

For regenerating this error follow steps mentioned in below post.

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---

## Reply 367
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:29:11.094Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/385

Anything after deadline we can’t consider any changes, it was just a matter of time, you didn’t tests running evaluate.py on docker container that was created, otherwise you would have spotted this mistake and rectified it.

---

## Reply 368
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:34:25.989Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/386

In your github repo, Dockerfile should be named as Dockerfile(D caps).

---

## Reply 369
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-06T22:39:30.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/387

I don’t know reason behind it, earlier evaluation was done by pulling docker image.

Latest one was done through github repo, if code in github repo is not consistent with docker image it might cause problems.

LLM won’t provide same results every time, for that reason we have give bonus marks.

---

## Reply 370
**Author**: Veer Shah
**Posted**: 2025-04-07T01:41:25.976Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/389

@carlton @jivraj sir it is my humble request to do something. We are losing our marks because of small negligence or mistakes like i fogot to commit my requirements.txt in my github repository. Already the course has taken tolls on our mind. Please give partial marks for the correct run of the docker image or please evaluate my latest commit with the requirements.txt. Because of this project I will lose my cgpa and the hardwork that I have done till this term. A small mistake is causing me my full marks and grades. Atleast consider partial marking for the docker image which does the tasks. I have maintained 9+ cgpa in the diploma and I took other subjects which are easy this term like BDM still is really difficult to cope with the subject. Please consider something. atleast give 50% of the marks for each task which my image passes.

---

## Reply 371
**Author**: Anisha Seth
**Posted**: 2025-04-07T01:49:33.296Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/390

Sir but i did test my project via evaluate.py and got the 8/10 in my tasks A. A simple port error has resulted in no evaluation at all after all the hardwork.

---

## Reply 372
**Author**: Bharat Choudhary
**Posted**: 2025-04-07T02:46:43.961Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/391

Sir, how my git repo is not consistent i used the same repo which i have given you in the form even i did not commit any changes after 18th feb also in my docker file there is just a simple mistake that i forgot to add flask dependency just because of that mistake i am losing my marks. I also used same docker image which i have given you through form. Its my humble request please consider or give some solution. It felt like betrayal because we put effort’s.

---

## Reply 373
**Author**: Afsal
**Posted**: 2025-04-07T04:25:33.067Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/392

Dear Sir,

I understand that this request is coming at a late stage, and I truly apologize for the timing. However, I felt it was important to express how much effort and dedication I have invested in this project and throughout the course. The recent issue has been disheartening for me, especially because the work I submitted was not a blind copy from someone else.

Had it been otherwise, I wouldn’t have had the courage to reach out. I genuinely care about this course and the learning it offers, and I’m proud of the commitment I’ve shown so far.

With utmost respect, I kindly request you to reconsider evaluating my project again, if there’s any possible way to do so. It would mean a lot to me and would really motivate me to keep pushing forward in this subject.

---

## Reply 374
**Author**: Carlton D'Silva
**Posted**: 2025-04-07T04:51:36.003Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/393

Hi @23f1001524 @afsalshah @23f1000879 @23f1002056

I understand your situation. We discussed all these scenarios in our weekly meets, and it was decided that we cannot make allowances for these because there was ample time to test your deployments and also ample sessions were conducted to address any difficulties you might have faced. A basic minimum standard was expected and we are unable to relax that threshold because then it would make evaluations meaningless.

We are not just evaluating on your agent functions. We require deployability as a minimum target. If you solution was not deployable and functional then we cannot evaluate the functioning of your application. Once again I sympathise with what might seem minor errors. But they are not minor, even though it may only be a line that needs changing or a spelling mistake. They actually cause a critical failure.

**A minor mistake is a function not working that does not prevent other things from working.**

**Critical failures prevents everything else from working** and thus most of these what seems like minor failures are missclassified. They are in fact critical failures.

I know its not of much comfort right now, but the learnings from this will be important going forward in your career.

Kindest regards

---

## Reply 375
**Author**: Telvin Varghese
**Posted**: 2025-04-07T05:54:42.672Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/394

Hi @carlton ,

I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal output, likely from a code editor like VS Code. The terminal displays information about HTTP requests and test results.

**2. Text Content:**

*   **"TERMINAL"**: Indicates the terminal window.
*   **"HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 500 Internal Server Error""**:  A GET request to a local server on port 8000, attempting to read a file named "c5.txt" from the "/data/" directory. The server returned a "500 Internal Server Error".
*   **"C5 failed: Cannot read /data/c5.txt"**: An error message indicating that the program failed to read the file "/data/c5.txt".
*   **"X C5 FAILED"**: Another indication that the test case "C5" failed. The "X" likely represents a visual marker for failure.
*   **"Score: 9 / 25"**: A score, possibly from a test suite or evaluation, showing a score of 9 out of 25.
*   **"HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK""**: A POST request to an external API endpoint related to OpenAI embeddings. The request was successful, indicated by the "200 OK" status.

**3. Context/Purpose:**

The terminal output suggests a program is being tested or debugged. It appears to be interacting with a local server and an external API (OpenAI). The program is trying to read a file, but failing, leading to an internal server error and a failed test case. The program also successfully makes a request to the OpenAI embeddings API.

**4. Technical Details:**

*   **HTTP Requests:** The output shows HTTP GET and POST requests, indicating network communication.
*   **Status Codes:** The "500 Internal Server Error" and "200 OK" are HTTP status codes that provide information about the success or failure of the requests.
*   **File Path:** The "/data/c5.

Would really appreciate it if you could take a look. Thanks in advance!

---

## Reply 376
**Author**: Carlton D'Silva
**Posted**: 2025-04-07T06:01:16.171Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/395

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:

tried copying multiple files for that you need to give directory name and it should end with a /

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that 
import requests
import pandas 
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try : 
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---

## Reply 377
**Author**: Telvin Varghese
**Posted**: 2025-04-07T06:04:15.738Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/396

@carlton  , I followed all the steps instead of `curl -LO https://github.com/<username>/<repo>/archive/<commit_sha>.zip`

`unzip <path to downloaded zipped repo>` , I used git clone .

---

## Reply 378
**Author**: Jayaram
**Posted**: 2025-04-07T06:05:46.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/397

@carlton @Jivraj

Not able to see the my id in 22f3002723 in evaluation logs or docker logs.. just curious if there was  any issues in creating the image out of github ?

---

## Reply 379
**Author**: Carlton D'Silva
**Posted**: 2025-04-07T07:27:07.331Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/398

Thanks for the fixes (I have updated the code now). It was put together quickly and not tested before we actually posted it.

---

## Reply 380
**Author**: Tushar Jalan 
**Posted**: 2025-04-07T07:33:49.534Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/399

Happy to help sir  :saluting_face: 

(Was expecting some different response from your side,but ig we need to accept our faith  :upside_down_face: )

Thank you,

(Kindest regards)

Tushar

---

## Reply 381
**Author**: Carlton D'Silva
**Posted**: 2025-04-07T07:48:28.615Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/400

We are checking you submission. We will get in touch shortly.

---

## Reply 382
**Author**: Veer Shah
**Posted**: 2025-04-07T09:26:40.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/401

@carlton @jivraj @s.anand,

I hope you’re doing well. I wanted to humbly request a reconsideration regarding the evaluation of my project submission.

I understand there was an issue with building the Docker image from the repository. However, I had successfully built and pushed the Docker image earlier, and I believe it demonstrates that my solution is deployable. If the final evaluation was solely based on building from the repository, I’m a bit confused about why the Docker image was considered earlier and why we were also asked to upload it to Docker Hub if it wasn’t going to be taken into account later. Also the earlier evaluation score where we got some marks at least and now are hopes are crushed after one night.

I do realize that in the real world, these kinds of errors can be critical, and I truly appreciate that the course is structured to prepare us for such expectations. That said, this course has been quite challenging, and for many students—including myself—it has been a source of considerable stress and demotivation.

I sincerely request that you kindly consider awarding some partial marks for the working Docker image that was built and pushed earlier. It does reflect an understanding of deployable solutions, which I’ve worked hard to demonstrate.

I know you all have our best interests in mind, and I’m grateful for the efforts put into making this a rigorous and enriching course. My only concern is that such harsh penalties—especially for a single oversight—can significantly affect our CGPA and future opportunities. I hope my request can be considered with empathy.

Thank you for your time and understanding.

---

## Reply 383
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T09:55:15.954Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/402

Issues with your submission has been resolved.

Thanks for raising the issue and checking it at your end.

---

## Reply 384
**Author**:  KARTHIK
**Posted**: 2025-04-07T09:57:43.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/403

Sir, I sincerely apologize for the mistake I made in naming the LICENSE file as “LIcense” instead of “LICENSE”. I now understand how important these details are, and it was an unintentional oversight on my part. I had put in a lot of hard work into the project, and it would mean a lot to me if you could kindly consider evaluating it, even though the deadline has passed and results are out. I completely understand if it’s not possible, but I just wanted to request a chance as this project was very important to me and I genuinely learned a lot from it.

@Jivraj @carlton

---

## Reply 385
**Author**: D HARICHARAN 
**Posted**: 2025-04-07T10:16:46.254Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/404

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows the user interface of Visual Studio Code (VS Code), a popular code editor. It's divided into several panels:

*   **Left Sidebar (Explorer):**  Displays the file structure of a project named "llmagent". The files listed include `app.py`, `datagen.py`, `Dockerfile`, `evaluate.py`, `LICENSE`, `readme.md`, `tasksA.py`, and `tasksB.py`.
*   **Center Panel (Start/Recent):**  This panel shows the VS Code start screen. It has options like "New File...", "Open File...", "Open Folder...", "Clone Git Repository...", and "Connect to...". Below that is a "Recent" section, showing a recently opened project: "llmagent-3bb328b23e37497a0117aa393731a49758a5708d" with its path.
*   **Right Sidebar (Walkthrough):**  This panel shows a walkthrough or getting started guide, with buttons for "Learn the Basics", "GitHub", and "Get Started with C#".
*   **Bottom Panel (Terminal):**  This panel displays the VS Code terminal. It shows the output of a `git clone` command.

**2. Text Content Visible:**

*   **File Names:** `app.py`, `datagen.py`, `Dockerfile`, `evaluate.py`, `LICENSE`, `readme.md`, `tasksA.py`, `tasksB.py`
*   **Start Screen:** "Start", "New File...", "Open File...", "Open Folder...", "Clone Git Repository...", "Connect to...", "Recent"
*   **Recent Project:** "llmagent-3bb328b23e37497a0117aa393731a49758a5708d", "C:\Users\USER\Dow..."
*   **Terminal Tabs:** "PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL", "PORTS"
*   **Terminal Output:**
    *   `PS C:\Users\USER\Downloads\New folder (3

cloned the repository using

git clone https://github.com/23f2001390/llmagent.git

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of the Visual Studio Code (VS Code) IDE. It's divided into three main sections:

*   **Explorer Panel (Left):**  This panel displays the file structure of a project.
*   **Editor Panel (Top Right):** This panel shows the content of a currently opened file.
*   **Terminal Panel (Bottom Right):** This panel displays the output of commands executed in a terminal.

**2. Text Content:**

*   **Explorer Panel:**
    *   "EXPLORER"
    *   "NEW FOLDER (33)"
    *   "llmagent" (Project folder)
    *   ".env"
    *   "app.py"
    *   "datagen.py"
    *   "Dockerfile"
    *   "evaluate.py"
    *   "LICENSE"
    *   "readme.md"
    *   "tasksA.py"
    *   "tasksB.py"
*   **Editor Panel:**
    *   "Welcome"
    *   ".env"
    *   "llmagent > .env"
    *   "AIPROXY\_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHku" (Likely a JWT token or similar API key)
*   **Terminal Panel:**
    *   "PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS"
    *   "PS C:\\Users\\USER\\Downloads\\New folder (33)> git clone [https://github.com/23f2001390/llmagent](https://github.com/23f2001390/llmagent)"
    *   "Cloning into 'llmagent'..."
    *   "remote: Enumerating objects: 14, done."
    *   "remote: Counting objects: 100% (14/14), done."
    *   "remote: Compressing objects: 100% (13/13), done."

created the `.env` for the aiproxy token as its needed to build the docker image as per my Dockerfile and `.env` file cannot be uploaded to git we have to create it while building docker image

**Image: evalue**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor, likely VS Code, with a file explorer on the left and a code editor window on the right.  The file explorer shows a project directory named "llmagent" with several Python files, a Dockerfile, a LICENSE, and a README.md file. The code editor window displays the contents of the "evaluate.py" file. There are also tabs at the bottom for "Outline", "Open Editors", and "Timeline".

**2. Any text content visible:**

*   **File Explorer:**
    *   `llmagent` (directory)
    *   `.env`
    *   `app.py`
    *   `datagen.py`
    *   `Dockerfile`
    *   `evaluate.py`
    *   `LICENSE`
    *   `readme.md`
    *   `tasksA.py`
    *   `tasksB.py`
    *   `datagen.py`
    *   `evaluate.py` (selected)
*   **Code Editor (evaluate.py):**
    *   `# /// script`
    *   `# requires-python = ">=3.13"`
    *   `# dependencies = [`
    *   `# "faker",`
    *   `# "httpx",`
    *   `# "lxml",`
    *   `# "numpy",`
    *   `# "pillow",`
    *   `# "python-dateutil",`
    *   `# ]`
    *   `# ///`
    *   `import sys`
    *   `import hashlib`
    *   `import httpx`
    *   `import io`
    *   `import json`
    *   `import logging`
    *   `import numpy as np`
    *   `import os`
    *   `import random`
    *   `import re`
    *   `import subprocess`
    *   `from dateutil.parser import parse`
    *   `from datagen import (`
    *   `get_markdown,`

added the new `evaluate.py` and `datagen.py` from the mail, trying to replicate the test environment

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor interface, specifically Visual Studio Code (VS Code). It's displaying a project structure in the Explorer panel on the left and the content of a Python file ("app.py") in the main editor window on the right.

**2. Any text content visible:**

*   **Explorer Panel:**
    *   "EXPLORER"
    *   "NEW FOLDER..."
    *   "Ilmagent" (project name)
    *   ".env" (file) - marked with "U" (likely indicating it's untracked or modified in Git)
    *   "app.py" (file) - highlighted, indicating it's the currently open file
    *   "datagen.py" (file) - marked with "M" (likely indicating it's modified in Git)
    *   "Dockerfile" (file)
    *   "evaluate.py" (file) - marked with "M"
    *   "LICENSE" (file)
    *   "readme.md" (file)
    *   "tasksA.py" (file)
    *   "tasksB.py" (file)

*   **Editor Window (app.py):**
    *   "Ilmagent > app.py > ..." (path to the file)
    *   Code content:
        *   `# app.py`
        *   `# /// script`
        *   `# dependencies = [`
        *   `# "requests",`
        *   `# "fastapi",`
        *   `# "uvicorn",`
        *   `# "python-dateutil",`
        *   `# "pandas",`
        *   `# "db-sqlite3",`
        *   `# "scipy",`
        *   `# "pybase64",`
        *   `# "python-dotenv",`
        *   `# "httpx",`
        *   `# "markdown",`
        *   `# "duckdb"`
        *   `# ]`
        *   `# ///`

**3.

moved the new `datagen.py` and `evaluate.py` into the project folder

**Image: image**
Here's a breakdown of the image content:

**1. UI Elements:**

*   **Code Editor:** The image shows a code editor, likely VS Code, with a file named `app.py` open.
*   **Explorer Pane:** A file explorer pane on the left displays a directory structure.
*   **Terminal Pane:** A terminal pane at the bottom shows the output of a command.
*   **Tabs:** Tabs at the top indicate open files: `.env` and `app.py`.
*   **Status Bar:** A status bar at the bottom shows the current working directory and other information.

**2. Text Content:**

*   **File Explorer:**
    *   `NEW FOLDER (33)`: The root directory.
    *   `llmagent`: A subdirectory.
    *   Files within `llmagent`: `.env`, `app.py`, `datagen.py`, `Dockerfile`, `evaluate.py`, `LICENSE`, `readme.md`, `tasksA.py`, `tasksB.py`.
*   **`app.py` Code:**
    *   `# app.py`: A comment indicating the file name.
    *   `# /// script`: A comment, possibly indicating a script file.
    *   `# dependencies = [`: Start of a list of dependencies.
    *   `"requests"`, `"fastapi"`, `"uvicorn"`, `"python-dateutil"`, `"pandas"`, `"db-sqlite3"`, `"scipy"`, `"pybase64"`, `"python-dotenv"`: A list of Python package dependencies.
*   **Terminal Output:**
    *   `PS C:\Users\USER\Downloads\New folder (33)\llmagent> docker build -t llm-agent .`: The command being executed.  This is a Docker command to build an image.
    *   `[+] Building 5.9s (15/15) FINISHED`: Indicates a successful Docker build.
    *   A series of lines starting with `=>`: These lines show the steps involved in the Docker build process.  They include:
        *   `[internal] load build definition from Dockerfile`
        *   `transferring dockerfile: 789B`
        *

docker image built successfully using

docker build -t llm-agent .

**Image: image**
Here's a breakdown of the image content:

**1. UI Elements:**

*   **Code Editor:** The image shows a code editor, likely VS Code, with a file explorer on the left and an editor window on the right.
*   **File Explorer:** The file explorer displays a project structure with a folder named "llmagent" containing files like `.env`, `app.py`, `datagen.py`, `Dockerfile`, `evaluate.py`, `LICENSE`, `readme.md`, `tasksA.py`, and `tasksB.py`.
*   **Editor Tabs:** Two files are open in the editor: `.env` and `app.py`. The `.env` file is currently selected.
*   **Terminal Panel:** A terminal panel is visible at the bottom, showing command-line output.
*   **Status Bar:** A status bar is at the very bottom, indicating that the `.env` file is open within the "llmagent" project.

**2. Text Content:**

*   **.env File:** The `.env` file contains a single line: `AIPROXY_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.MFOfvD2AwbfhpaVtd5X2LgZEidgCmJ0aRy1qWt5Y2RE`. This appears to be a JWT (JSON Web Token) used for authentication.
*   **Terminal Output:** The terminal output shows the execution of a command: `uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000`.
    *   It indicates that the script `evaluate.py` is being run with specific arguments: email, token counter, and external port.
    *   The output also shows an attempt to install `uv` (likely a package manager) and run a script from a GitHub Gist URL: `https://gist.githubusercontent.com/sanando/f19b6797f82b36da39ac44f3a7

running the evaluate.py using:

 uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a code editor, likely VS Code, with several panels visible. On the left is a file explorer showing a project named "llmagent". The main panel displays the contents of a file named ".env". Below that is a terminal window showing the output of a program.

**2. Text Content:**

*   **File Explorer:**
    *   `NEW FOLDER (33)`
    *   `llmagent` (project folder)
    *   `_pycache__`
    *   `.env`
    *   `app.py`
    *   `datagen.py`
    *   `Dockerfile`
    *   `evaluate.py`
    *   `LICENSE`
    *   `readme.md`
    *   `tasksA.py`
    *   `tasksB.py`
*   **.env file:**
    *   `AIPROXY_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.MFOfvD2AwbfhpaVtd5X` (truncated JWT token)
*   **Terminal Output:**
    *   `C4 FAILED`
    *   `Running task: Does the statement 'I hate you' have a positive or negative connotation? Reply as a single string containing 'POSITIVE' or 'NEGATIVE' in uppercase. Save the result to /data/c5.txt`
    *   `HTTP Request: POST http://localhost:8000/run?task=...` (a long URL-encoded string containing the task description)
    *   `HTTP 400 { "detail": "No connection adapters were found for 'data:text/plain; charset=utf-8, NEGATIVE'" }`
    *   `HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 200 OK"`
    *   `/data/c5.txt`
    *   `EXPECT

got consistent 6/25 after even running the file 6 times @carlton @Jivraj @s.anand Please sir check this, just because my docker image needs .env, I cannot get full 0…I need to maintain my cgpa (by getting 0 in project my grade is going too close to E grade sir and already in D, already my ROE got bad due to technical issues which on the same day around 6pm after finding way to unlock the input of answers for roe I completed the roe again in short amount of time like 10 or 20 minutes and got 10/10 but still it was rejected because it was late, max 3 minutes after 1:45PM was allowed…I’m not asking to any extra marks, just my marks) I’m trying to improve it already I have 4 subjects in a single term, please give me atleast this marks with the bonus 1 mark for prerequisites (total 7)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows text output, likely from an automated script or system, that checks the validity of submitted Github and Docker repositories. It presents the submitted repository links and then provides a series of prerequisite checks with pass/fail indicators.

**2. Text Content:**

The text content is as follows:

*   "Github repo submitted: https://github.com/23f2001390/lImagent"
*   "Docker repo submitted: 23f2001390/lImagent"
*   "Pre-requisites check: (1 for pass, 0 for fail)"
*   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
*   "Gihub repo check - Dockerfile exists: 1"

**3. Context and Purpose:**

The purpose of the displayed information is to verify that a submitted Github and Docker repository meet certain criteria. This is likely part of an automated submission process or a grading system. The checks ensure that the repositories exist, are publicly accessible, contain a license file (either LICENSE or LICENSE.md with an MIT License), and include a Dockerfile. The "1" indicates that each check has passed.

**4. Technical Details:**

*   The Github repository URL suggests a user or organization named "23f2001390" and a repository named "lImagent".
*   The Docker repository is also under the name "23f2001390" and named "lImagent".
*   The prerequisite checks include timestamp validation (before February 18th), existence of specific files (LICENSE, LICENSE.md, Dockerfile), and public accessibility.
*   The use of "1" and "0" as pass/fail indicators is a common practice in automated testing and scripting.

Thank you

---

## Reply 386
**Author**: Vaddi Yaswanth
**Posted**: 2025-04-07T10:21:38.581Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/405

Yes,the Same case happend to me also we have put lot of efforts in this project but after seeing that in mail you have no mit licence, I added that license but with name of mit license actually to just name that license file as MIT license but due to this all our hardwork is just an experience but actually we are not awarding any marks in project1 . I request the TDS team to consider this issue.

---

## Reply 387
**Author**: Sarthak Singh Gaur
**Posted**: 2025-04-07T12:10:25.546Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/406

I have passed the pre requisites, but there is no log file for my email.

At least docker logs should be there, right?

Was it missed by any chance?

@Jivraj @carlton

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based output, likely from a script or program, that performs a series of prerequisite checks. Each check is described, and a value of "1" or "0" is assigned to indicate whether the check passed or failed, respectively.

**2. Any text content visible:**

The text content includes:

*   **"Pre-requisites check: (1 for pass, 0 for fail)"** - This is the title or header, explaining the purpose of the output and the meaning of the numerical values.
*   **"Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"** - This check verifies the existence and public accessibility of a Docker repository, with a timestamp requirement before February 18th. The "1" indicates that this check passed.
*   **"Github repo exists and is public (should have a timestamp before 18th of Feb): 1"** - This check verifies the existence and public accessibility of a GitHub repository, with a timestamp requirement before February 18th. The "1" indicates that this check passed.
*   **"Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"** - This check verifies the existence of a license file (either LICENSE or LICENSE.md) in the GitHub repository, specifically an MIT License. The "1" indicates that this check passed.
*   **"Gihub repo check - Dockerfile exists: 1"** - This check verifies the existence of a Dockerfile in the GitHub repository. The "1" indicates that this check passed.

**3. The context or purpose of what's displayed:**

The purpose of this output is to ensure that certain prerequisites are met before proceeding with a process, such as building, deploying, or testing software. The checks focus on the existence and accessibility of Docker and GitHub repositories, as well as the presence of essential files like a license and a Dockerfile.

**4. Technical details:**

The checks are likely performed by a script or program that interacts with Docker and GitHub APIs or uses command-line tools to verify the existence and properties of the repositories and files. The timestamp check suggests that the script is also able to retrieve and compare timestamps associated with

---

## Reply 388
**Author**: Jayaram
**Posted**: 2025-04-07T12:26:27.239Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/407

Sorry to repeatedly ask @carlton @Jivraj

couldnt see my id (22f3002723) in any of the logs  evaluation or docker .. was there any issue in building image out of docker file in github

---

## Reply 389
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T12:43:29.133Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/408

Hi @22f3002723

 /bin/sh: 1: uv: not found 

This is error that we got on your evaluation while building docker image through github repo.

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username"  # Replace with your actual GitHub …

---

## Reply 390
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T12:44:40.099Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/409

This was error with your submission.`tried copying file named `app` which is not there in github repo`

---

## Reply 391
**Author**: S Sharmile
**Posted**: 2025-04-07T12:47:52.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/410

Respected Sir , @carlton @Jivraj

My roll number is 23f3001688

Pls check my repository properly because I have dockerfile in my repo but it is mentioned that it is not present.

Here is my repository link and screenshot for your reference sir and the dockerfile is present sir

      [github.com](https://github.com/Sharmilecholan/tds_project1)

  [GitHub - Sharmilecholan/tds_project1](https://github.com/Sharmilecholan/tds_project1)

Contribute to Sharmilecholan/tds_project1 development by creating an account on GitHub.

I think the mistake would have been because in my repo the file name is “dockerfile” and you have mentioned it as “Dockerfile” . So is it a mistake to put “D” in lowercase.

Kindly look into this sir because of this I got 0 in project 1 even though many of the tasks of my projects passed the evaluation test.

Regards,

S Sharmile

23f3001688

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a GitHub repository's file listing and sidebar. The file listing displays the files and directories in the repository, along with their commit messages and the time since the last commit. The sidebar on the right provides repository details, including the description, license, activity, stars, watchers, forks, releases, packages, and languages.

**2. Any text content visible:**

*   **Repository Owner/Name:** Sharmilecholan
*   **Commit Message:** Delete evaluate.py
*   **Commit Hash:** 548db37
*   **Commit Age:** 2 months ago
*   **Number of Commits:** 4 Commits
*   **File Names:** .env, .markdownlint.json, .prettierrc.json, LICENSE, README.md, app.py, datagen.py, dockerfile, requirements.txt, tasksA.py, tasksB.py
*   **Commit Messages for Files:** Add files via upload, Initial commit, Update and rename dockerfile.txt to dockerfile
*   **File Age:** 2 months ago
*   **Sidebar Text:** No description, website, or topics provided. Readme, MIT license, Activity, 0 stars, 1 watching, 0 forks, Report repository, Releases, No releases published, Packages, No packages published, Languages

**3. The context or purpose of what's displayed:**

The image shows the structure and recent activity of a GitHub repository. It provides an overview of the files in the repository, the commit history, and basic repository statistics. This information is useful for understanding the project's contents, development progress, and community engagement.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The file extensions suggest that the repository contains Python code (.py), configuration files (.json, .env, .txt), a Dockerfile, and a README file.
*   The presence of a `requirements.txt` file indicates that the project likely has dependencies that need to be installed.
*   The commit messages "Add files via upload" suggest that the initial files were added through the GitHub web interface.
*   The commit message "Update and rename dockerfile.txt to dockerfile" indicates a change in the Dockerfile

---

## Reply 392
**Author**: Devanshi 
**Posted**: 2025-04-07T13:37:31.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/412

@carlton sir, i want to clarify about this. I had got 9/20 in the previous mail in my evaluation log and now the recent mail say i got 1 mark. I want to ask about this. Please help me

**Image: WhatsApp Image 2025-04-07 at 15.37.17_fb28b652**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a screen capture of what appears to be a debugging or logging output from a system that is running a task involving a "datasette" instance. It displays a series of commands, HTTP requests and responses, and error messages. The output is formatted in a way that suggests it's being displayed in a terminal or console-like environment.

**2. Text Content Visible:**

*   **Email-like address:** "22f3000276@ds.s..." at the top, likely an identifier for the task or process.
*   **Error Messages:**
    *   "B9 FAILED" (with a red "X" icon)
    *   "HTTP/1.1 500 Internal Server Error"
    *   "HTTP/1.1 404 Not Found"
    *   "B10 failed: Cannot read /data/b10.csv"
    *   "B10 FAILED" (with a red "X" icon)
*   **Task Description:**
    *   "Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background."
    *   "From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv?sql=SELECT+COUNT(*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv. Then stop the datasette server."
*   **HTTP Requests:**
    *   POST http://localhost:8134/run?... (followed by a long, URL-encoded string containing task details)
    *   GET http://localhost:8134/read?path=/data/b10.csv
    *   POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings
*   **HTTP Responses:**
    *   HTTP 500 (with a JSON-like structure: `{"detail": "'filename'"}`)
    *   HTTP/1.1 404 Not Found

**Image: WhatsApp Image 2025-04-07 at 15.39.10_edb0b829**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of what appears to be a results page or feedback report for a coding assignment or project. It includes:

*   **UI Elements:** The screenshot is likely from a mobile device, given the status bar at the top (time, network signal, battery). There are also standard UI icons for back, download, delete, email, and a menu.
*   **Text Content:** The majority of the image is text, providing information about the project's scoring, submitted repositories, pre-requisite checks, and additional details.
*   **Tables:** There are three tables labeled A, B, and C, with numerical values (mostly 0) in each cell.

**2. Text Content Visible:**

Here's a breakdown of the text content:

*   "outliers do not influence the scores)"
*   "Your final t score calculation is based on MIN (20, (task score + bonus))"
*   "Github repo submitted: https://github.com/anshiraj07/TDS-Project-1-2025"
*   "Docker repo submitted: 22f3000276/task-agent"
*   "Pre-requisites check: (1 for pass, 0 for fail)"
    *   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
    *   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
    *   "Gihub repo check - Dockerfile exists: 1"
*   Tables:
    *   A1 to A10, all with value 0
    *   B1 to B10, all with value 0
    *   C1 to C5, all with value 0
*   "Your task score is: 0"
*   "Your bonus is: 1"
*   "Your P1 score is: 1"
*   "We have attached the docker logs and the evaluation logs for everyone who passed the pre-

---

## Reply 393
**Author**: Anushka Kumar
**Posted**: 2025-04-07T13:50:15.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/414

I don’t know how to check for the errors I made, @Jivraj sir can you at least show the prerequisite form that I submitted so I can check for myself ?.

---

## Reply 394
**Author**: Sarthak Singh Gaur
**Posted**: 2025-04-07T14:22:03.831Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/415

@jivraj

earlier I built the project inside app folder so it was

COPY app /app

it should have been

COPY . /app

Is there anything that can be done on your end now?

All the code is there.

---

## Reply 395
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T14:39:26.569Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/416

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a table-like UI element, likely from a database or spreadsheet application. It displays data related to project submissions, possibly from students. There's also a search bar at the top.

**2. Any text content visible:**

*   **Search Bar:** Contains the text "22f2000559" preceded by a magnifying glass icon.
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Data (Row 1):**
    *   "499" (likely an ID or index)
    *   "2/15/2025 23:56:09"
    *   "22f2000559@ds.study.iitm.ac.in"
    *   "https://github.com/AnushkaAbhishekKumar/LLM-Project"
    *   "coolsisters7/0c8a207a0c7c"
*   **Table Data (Row 2):**
    *   "1060" (likely an ID or index)
    *   "2/16/2025 23:59:44"
    *   "22f2000559@ds.study.iitm.ac.in"
    *   "https://github.com/AnushkaAbhishekKumar/LLM-Project/tree/main"
    *   "coolsisters7/4a79a3c81cd0"

**3. The context or purpose of what's displayed:**

The data appears to be a record of submissions for a project, possibly a course assignment. The columns track the submission timestamp, the submitter's email address, a link to the GitHub repository containing the project code, and the name of a Docker image associated with the project. The search bar is likely used to filter the submissions based on a specific query

Sorry for late reply,These are 2 submissions that you made we are considering the latest one.

---

## Reply 396
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T14:40:37.264Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/417

No we don’t consider any changes after deadline.

---

## Reply 397
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T14:44:08.514Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/418

There was a module missing error while lead the docker image to run.

Follow below steps for replicating test environment.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

## Reply 398
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T14:49:04.564Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/419

For dockerfile you have in repo, It was named differently, correct naming has to be Dockerfile.

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) Tools in Data Science

    You can take it up with @s.anand 
I did not come up with the standard. 
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files. 

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in. 

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

## Reply 399
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T14:51:31.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/420

@24ds1000119 and @YaswanthVaddi

We are not considering mismatch in naming for License.

---

## Reply 400
**Author**: K Senthur Kumaran 
**Posted**: 2025-04-07T14:51:53.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/421

Dear @carlton

This is Senthur. I have reviewed the logs, and it indicates that the

`/app/app/main.py`     file is missing. However, in my project directory, the

`main.py`   file is located in the   `app/`   folder, and the   `run.py`   file is in the root folder of the project, which is   `LLM_Automation_Agent`  . This structure allows the `run.py` file to run the project without any issues by calling the appropriate functions from `app/main.py`.

To run the project, the command I used is:

python run.py

Since `run.py` is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to `app/main.py`.

I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the `run.py` script located in the root folder (`llm-automation-agent`).

For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.

Here is the GitHub link to my project:

      [github.com](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

  [GitHub - ksenthurkumaran18052004/llm-automation-agent](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

Contribute to ksenthurkumaran18052004/llm-automation-agent development by creating an account on GitHub.

**Image: image**
Here's a detailed description of the image:

**Overall Structure:**

The image shows a developer's workspace, combining a code editor (likely VS Code) with a web browser (likely Chrome) displaying a GitHub repository.  The VS Code window is split into multiple panes, showing code, a file explorer, and terminal outputs. The GitHub repository is for a project named "llm-automation-agent".

**1. VS Code Window (Top Half):**

*   **File Explorer (Left Pane):**
    *   Shows the project directory structure: `LLM_AUTOMATION_AGENT`.
    *   Key directories and files listed: `app`, `data`, `venv`, `Dockerfile`, `.git`, `LICENSE`, `README.md`, `Remove-Item`, `requirements.txt`, `run.py`.
*   **Code Editor (Center Pane):**
    *   Currently displaying the `main.py` file.
    *   Code snippet includes a function `execute_task(action)`.
    *   Error handling with `try...except` block.
    *   Flask routes defined using `@app.route` for `/` and `/read` endpoints.
    *   The `/` route returns "Welcome to the LLM Automation Agent API! Use /run or /read endpoints."
*   **Terminal (Bottom Pane):**
    *   Shows the output of running the `run.py` file using `python run.py`.
    *   Indicates a Flask development server is running.
    *   Warning message: "This is a development server. Do not use it in a production deployment."
    *   Server is running on `http://127.0.0.1:8000` and `http://172.17.25.87:8000`.
    *   Logs of POST requests to `/run?task=count%20wednesdays` with HTTP status code 200.
*   **Ports Pane:**
    *   Shows the output of a `curl` command: `curl -X POST "http://localhost:8000/run?task=count%20wednesdays"`.
    *   The response is a JSON object: `{"message": "Counted 30 Wednesdays in data\\

Lookig forward towards your support.

With Regards

K Senthur Kumaran

---

## Reply 401
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-07T14:53:21.728Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/422

Same here sir, i only changed LICENSE to MIT LICENSE due to the mail i received.

The LICENSE file was already present in the repo as i submitted my project. The change too was made on the 16th of Feb.

Sir, I would highly appreciate if you consider it as the rest of the pre-requisites are working well.Due to this, the project is also not being evaulated.

Thankyou

@carlton

---

## Reply 402
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T15:00:58.659Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/423

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, likely running on a Linux-based system. It displays command-line output and commands being executed. The prompt indicates the user is "root" on a machine named "tds-course-temp-bq".

**2. Any text content visible:**

*   **Prompt:** `root@tds-course-temp-bq:/mnt/sdb/github_approach#`
*   **Command 1:** `docker images | grep "22f3002902"`
*   **Output of Command 1:**
    *   `22f3002902 latest c739ff8a3247 6 days ago 1.13GB`
*   **Command 2:** `docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 c739ff8a3247`
*   **Error Message:** `python: can't open file '/app/app/main.py': [Errno 2] No such file or directory`

**3. The context or purpose of what's displayed:**

The user is interacting with Docker. The first command lists Docker images and filters the output to find an image with the ID "22f3002902". The second command attempts to run a Docker container based on the image with ID "c739ff8a3247". The command sets an environment variable `AIPROXY_TOKEN` and maps port 8000 on the host to port 8000 in the container.

The error message indicates that the Python interpreter within the container is unable to find the file `/app/app/main.py`. This suggests that the Docker image is expected to run a Python script located at that path, but the file is missing or the path is incorrect.

**4. Technical details:**

*   **Docker:** The image involves Docker commands, indicating containerization technology.
*   **`docker images`:** This command lists available Docker images. The `grep` command filters the output.
*   **`docker run`:** This command starts a

Just checked right now. I am getting this error.

Replicate test environment following this post.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)0

---

## Reply 403
**Author**: Mishkat Chougule
**Posted**: 2025-04-07T10:31:33.573Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/424

🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

 :warning:  RESULT:

Header

Start
Mid
End

1
2
3

Paragraph has extra   spaces and trailing whitespace.

print("23f3003027@ds.study.iitm.ac.in")

 :cross_mark:  A2 FAILED

I am facing Npx error... can I know what went wrong?
@carlton @Jivraj

---

## Reply 404
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-07T15:11:38.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/425

23F300327:

I am facing Npx error... can I know what went wrong?

This `npx` error is originating from your Docker container—it’s not being generated by our script. Try to look for what caused this error.

---

## Reply 405
**Author**: Anushka Kumar
**Posted**: 2025-04-07T16:07:02.249Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/426

**Image: Screenshot 2025-04-07 213538**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) of Docker Hub, specifically the page for a repository named "coolsisters7/llm". The UI elements include:

*   **Navigation Menu (Left):** A sidebar with options like "Repositories", "Settings", "Billing", "Usage", "Pulls", and "Storage".
*   **Repository Details (Main Content Area):** Information about the "coolsisters7/llm" repository, including its name, last pushed date, repository size, and options to add a description or category.
*   **Tabs:** Tabs for "General", "Tags", "Image Management (BETA)", "Collaborators", "Webhooks", and "Settings". The "General" tab is currently selected.
*   **Tags Section:** A table displaying the tags associated with the repository.
*   **Docker Commands Section (Right):** A section providing the Docker command to push a new tag to the repository.
*   **Build Cloud Section (Right):** A section advertising Docker Build Cloud.
*   **Header:** Docker Hub logo, search bar, and user-related icons.

**2. Text Content Visible:**

*   **Docker Hub** (logo)
*   **Explore**, **My Hub** (navigation)
*   **Search Docker Hub** (search bar placeholder)
*   **coolsisters7** (username)
*   **Docker Personal** (account type)
*   **Repositories**, **Settings**, **Default privacy**, **Notifications**, **Billing**, **Usage**, **Pulls**, **Storage** (navigation menu items)
*   **Repositories / llm / General** (breadcrumb navigation)
*   **coolsisters7/llm** (repository name)
*   **Last pushed about 2 months ago**
*   **Repository size: 795.7 MB**
*   **Add a description**, **Add a category**
*   **General**, **Tags**, **Image Management (BETA)**, **Collaborators**, **Webhooks**, **Settings** (tabs)
*   **Tags**
*   **This repository contains 1 tag(s).**
*   **Tag**, **OS**, **Type**, **Pulled**, **P

Oh I see what happened, the image names are different, I don’t know how, given I pushed the latest at 11:51pm and submitted the form at 11:59pm. Thank You @Jivraj for showing me.

Question: Now that I know. how can I test the container myself, if I want to do exactly what you guys are doing?

---

## Reply 406
**Author**: Mishkat Chougule
**Posted**: 2025-04-07T16:23:03.736Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/427

My code uses `npx` to format Markdown files using Prettier, specifically via `subprocess.run(["npx", "prettier@3.4.2", "--write", ...])`, which assumes that `npx` is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or `npx`, this results in an error during evaluation.

To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

bash:` apt-get update && apt-get install -y nodejs npm`

Once installed, `npx prettier@3.4.2` should work as expected.

For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where `npx` is available by default.

---

## Reply 407
**Author**: Hilal
**Posted**: 2025-04-07T16:36:21.624Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/428

@Jivraj @carlton

Before the project evaluation, I ran the test script and successfully passed all Task A and Task B checks. I also built the Docker image as required.

But, when you gus evaluated , I get the following error:docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: “uvicorn”: executable file not found in $PATH: unknown.

Could you please help me understand why this is happening even though the evaluation script ran fine?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of the Docker Hub website, specifically the page for a repository named "llm-automation-agent" owned by the user "hilalazeez". It shows the "General" tab of the repository settings. The left sidebar displays the user's profile and navigation options within Docker Hub. The main content area shows information about the repository, including its name, last push date, repository size, and a section for tags. There's also a section on the right side with Docker commands and an advertisement for Docker Build Cloud.

**2. Any text content visible:**

*   **Header:** "dockerhub", "Explore", "My Hub", "Search Docker Hub", "CtrlK", user icon "H"
*   **Sidebar:** "hilalazeez", "Docker Personal", "Repositories", "Settings", "Default privacy", "Notifications", "Billing", "Usage", "Pulls", "Storage"
*   **Main Content:**
    *   "Repositories / llm-automation-agent / General"
    *   "hilalazeez/llm-automation-agent"
    *   "Last pushed about 2 months ago"
    *   "Repository size: 418.1 MB"
    *   "Add a description"
    *   "Add a category"
    *   "General", "Tags", "Image Management (BETA)", "Collaborators", "Webhooks", "Settings"
    *   "Tags"
    *   "This repository contains 1 tag(s)."
    *   "Tag", "OS", "Type", "Vulnerabilities", "Pulled", "Pushed"
    *   "latest", Linux icon, "Image", "0", "1", "4", "22", "0", "1 day", "about 2 months"
    *   "See all"
    *   "Analyzed by docker scout"
*   **Right Side:**
    *   "Using 0 of 1 private repositories. Get more"
    *   "Docker commands"
    *   "To push a new tag to this repository:"
    *   "Public view"
    *   "docker push

**Image: Screenshot 2025-04-07 192419**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser interface, specifically the documentation page generated by FastAPI for an API. It displays the available API endpoints, their HTTP methods (GET, POST), and a section for schemas.

**2. Text Content:**

*   **Title:** "FastAPI"
*   **Version:** "0.1.0"
*   **OAS Version:** "OAS 3.1"
*   **/openapi.json**
*   **Section Title:** "default"
*   **API Endpoints:**
    *   "GET /ask Ask"
    *   "POST /run Run Task"
    *   "GET /read Read File"
*   **Section Title:** "Schemas"
*   **Schemas:**
    *   "HTTPValidationError > Expand all object"
    *   "ValidationError > Expand all object"
*   **Browser Address Bar:** "127.0.0.1:8000/docs#/"

**3. Context and Purpose:**

This is an automatically generated API documentation page, likely created using FastAPI's built-in support for OpenAPI (formerly Swagger). The purpose is to provide developers with a clear and interactive way to understand and test the API. The "default" section likely groups endpoints that are not explicitly categorized. The "Schemas" section defines the structure of the data used in the API requests and responses.

**4. Technical Details:**

*   **FastAPI:** The framework used to build the API.
*   **OpenAPI (OAS 3.1):** The specification used to describe the API. FastAPI automatically generates the OpenAPI schema, which is then used to render the documentation.
*   **HTTP Methods:** GET (for retrieving data), POST (for creating or updating data).
*   **Endpoints:** `/ask`, `/run`, `/read` are the URL paths for the API endpoints.
*   **Schemas:** `HTTPValidationError` and `ValidationError` are likely data structures used to represent validation errors in the API. The "Expand all" link suggests that these schemas can be expanded to show their detailed structure. The "object" text indicates that these schemas represent JSON objects.
*   **IP Address:** 127.0.0.1

---

## Reply 408
**Author**: Anushka Kumar
**Posted**: 2025-04-07T17:19:51.228Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/429

Can you tell me what application is this (FastAPI) one ?

---

## Reply 409
**Author**: Bharat Choudhary
**Posted**: 2025-04-07T18:31:51.760Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/430

idk why i am doing this but this is my last request (for evaluation) with proofs. me and my friend both have same docker file code with missing flask dependency (i will try as much to not reveal his id/name) he got 12/20 even tough i tried same methods given by you and same error popped up flask module not found in his case but you gave him 12/20 marks but for me you gave 0? did i done something wrong? I know in industry level it matters much but right now we are students and for us CGPA matters. i am also uploading his docker file image and mine with 0 commits after 18th feb.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a code editor interface, specifically a view of a `Dockerfile` within a GitHub repository. The left side displays a file explorer, and the right side shows the content of the `Dockerfile`. The top of the screen shows the GitHub navigation bar.

**2. Text Content:**

*   **File Explorer:**
    *   `_pycache_`
    *   `data`
    *   `.env`
    *   `Dockerfile`
    *   `LICENSE`
    *   `README.md`
    *   `app.py`
    *   `datagen.py`
    *   `evaluate.py`
    *   `tasksA.py`
    *   `tasksB.py`
*   **Dockerfile Content:**
    The `Dockerfile` contains instructions for building a Docker image. Here's a breakdown of the key commands and their purpose:
    *   `FROM python:3.12-slim-bookworm`: Specifies the base image as Python 3.12 slim.
    *   `RUN apt-get update && apt-get install ...`: Installs system dependencies required for SciPy and other libraries.
    *   `ADD https://astral.sh/uv/install.sh /uv-installer.sh`: Adds the uv installer script.
    *   `RUN sh /uv-installer.sh && rm /uv-installer.sh`: Executes the uv installer script.
    *   `RUN pip install --no-cache-dir ...`: Installs Python packages using pip, including `fastapi`, `uvicorn`, `python-dateutil`, `requests`, `scipy`, `python-dotenv`, `httpx`, `pandas`, `db-sqlite3`, `pybase64`, `markdown`, and `duckdb`.
    *   `ENV PATH="/root/.local/bin:$PATH"`: Sets the environment variable PATH to include the location of installed binaries.
    *   `WORKDIR /app`: Sets the working directory inside the container to `/app`.
    *   `COPY . /app`: Copies all files from the current directory to the `/app` directory in the container.
    *   `EXPOSE 80

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a code repository on GitHub. It shows the file structure on the left and the content of a `Dockerfile` on the right. The GitHub interface elements are visible, including the repository name, navigation tabs (Code, Issues, Pull requests, etc.), and file browser.

**2. Text Content:**

*   **Repository Name:** `23f1000879 / TDS_Project_1`
*   **File Path:** `TDS_Project_1 / Dockerfile`
*   **File Browser:** Shows a directory structure with the following files/folders: `_pycache_`, `data`, `Dockerfile`, `LICENSE`, `README.md`, `app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, `tasksB.py`.
*   **Dockerfile Content:** The `Dockerfile` contains instructions for building a Docker image. Here's a breakdown:
    *   `# Use Python 3.12 slim version as base image`
    *   `FROM python:3.12-slim-bookworm`
    *   `# Install system dependencies required for SciPy and other libraries`
    *   `RUN apt-get update && apt-get install -y --no-install-recommends \ build-essential gfortran libatlas-base-dev curl ca-certificates \ && rm -rf /var/lib/apt/lists/*`
    *   `# Install uv`
    *   `ADD https://astral.sh/uv/install.sh /uv-installer.sh`
    *   `RUN sh /uv-installer.sh && rm /uv-installer.sh`
    *   `# Install required Python packages`
    *   `RUN pip install --no-cache-dir fastapi uvicorn python-dateutil requests scipy \ python-dotenv httpx pandas db-sqlite3 pybase64 markdown duckdb`
    *   `# Ensure the installed binary is on the 'PATH'`
    *   `ENV PATH="/root/.local/bin:$PATH"`
    *   `# Set up the application directory`
    *   `WORKDIR /app`
    *

---

## Reply 410
**Author**: Wasim Ansari
**Posted**: 2025-04-07T19:50:31.765Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/431

Dear Sirs,

@Jivraj @Saransh_Saini @carlton

As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.

**Image: Screenshot 2025-04-07 233513**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a list of instructions or requirements, likely for a software development task or assignment. The instructions are presented as bullet points. The background is a dark gray, and the text is white. The instructions involve Docker, Docker Hub, GitHub, and a Google Form.

**2. Any text content visible:**

*   "Create a Dockerfile that builds your application"
*   "Publish your Docker image publicly to Docker Hub"
*   "Ensure that running your image via"
*   `podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME automatically serves the API at http://localhost:8000/run?task=... and http://localhost:8000/read?path=...`
*   "Submit in this Google Form the URL of your GitHub repository"
*   `(https://github.com/user-name/repo-name) and your Docker image name (user-name/repo-name)`

**3. The context or purpose of what's displayed:**

The content appears to be instructions for a developer to containerize an application using Docker, publish it to Docker Hub, and then submit the GitHub repository and Docker image name. The `podman run` command suggests that the application exposes an API on port 8000.

**4. Technical details (code screenshot):**

*   The `podman run` command is used to run a Docker image.
*   `--rm` flag: This flag tells Podman to automatically remove the container when it exits.
*   `-e AIPROXY_TOKEN=$AIPROXY_TOKEN`: This sets an environment variable named `AIPROXY_TOKEN` inside the container. The value is taken from the host environment variable `$AIPROXY_TOKEN`.
*   `-p 8000:8000`: This maps port 8000 on the host to port 8000 in the container.
*   `$IMAGE_NAME`: This is a placeholder for the name of the Docker image to run.
*   The URLs `http://localhost:8000/run?task

**Github repo submitted:** [GitHub - wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent)

**Docker repo submitted:** wasimansariiitm/my-ai-agent

The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the `app.py` file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.

I would like to respectfully bring this to your kind attention that the `app.py` file does exist in the repository, but it is located inside a subfolder:

[https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py](https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py).

But as per the submission instructions, I provided the GitHub repo link only: [https://github.com/wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent).

Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.

I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.

Thank You and Regards,

24ds3000090

---

## Reply 411
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-07T20:42:10.131Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/432

@carlton @Jivraj

Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a traceback from a Python program. It shows error messages and stack traces indicating a problem with opening font resources using the PIL (Pillow) library.

**2. Text Content:**

*   "Downloaded faker"
*   "Installed 3 packages in 39ms"
*   "Traceback (most recent call last):"
*   "File "/tmp/datagen66arSL.py", line 220, in a8\_credit\_card\_image"
*   "large\_font = ImageFont.truetype("arial.ttf", size=60)"
*   "File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 880, in truetype"
*   "return freetype(font)"
*   "File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 877, in freetype"
*   "return FreeTypeFont(font, size, index, encoding, layout\_engine)"
*   "File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 285, in \_\_init\_\_"
*   "self.font = core.getfont("
*   "font, size, index, encoding, layout\_engine=layout\_engine"
*   "OSError: cannot open resource"
*   "During handling of the above exception, another exception occurred:"
*   "File "/tmp/datagen66arSL.py", line 303, in "
*   "a8\_credit\_card\_image()"
*   "File "/tmp/datagen66arSL.py", line 224, in a8\_credit\_card\_image"

I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.

Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…

But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.

Edit 2:

Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a snippet of Python code. It appears to be the main execution block of a script.

**2. Any text content visible:**

The code contains the following text:

*   `if __name__ == "__main__":`
*   `import argparse`
*   `parser = argparse.ArgumentParser()`
*   `parser.add_argument("email")`
*   `parser.add_argument("--root", default="/data")`
*   `args = parser.parse_args()`
*   `config["email"] = args.email`
*   `config["root"] = os.path.abspath(args.root)`
*   `os.makedirs(config["root"], exist_ok=True)`
*   `print("DISCLAIMER: THIS SCRIPT WILL CHANGE BEFORE THE EVALUATION. TREAT THIS AS A GUIDE.")`
*   `print("Files created at", config["root"])`
*   `a2_format_markdown()`
*   `a3_dates()`
*   `a4_contacts()`
*   `a5_logs()`
*   `a6_docs()`
*   `a7_email()`
*   `a8_credit_card_image()`
*   `a9_comments()`
*   `a10_ticket_sales()`

**3. The context or purpose of what's displayed:**

The code snippet seems to be part of a script that:

*   Uses the `argparse` module to handle command-line arguments. It expects an "email" argument and a "--root" argument (with a default value of "/data").
*   Creates a configuration dictionary (`config`) to store the values of the "email" and "root" arguments.
*   Creates a directory based on the "root" argument using `os.makedirs`. The `exist_ok=True` argument prevents an error if the directory already exists.
*   Prints a disclaimer indicating that the script is subject to change.
*   Prints a message indicating the directory where files are created.
*   Calls a series of functions named `a2_format_markdown`, `a3_dates`, `a4_contacts`,

Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.

Thank you.

Regards,

Shivaditya

---

## Reply 412
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T05:49:08.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/433

Hi Haricharan

Your Dockerfile does not build the repo. Its misconfigured.

This is the error when building it:

=> ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 > [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | >>> COPY .env /app/
  21 |     
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found

**Image: Screenshot 2025-04-08 at 11.12.18 am**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of code, likely from a Dockerfile or similar configuration file. It contains instructions for setting up an application directory and copying files into it. The code is displayed in a dark-themed text editor or IDE.

**2. Any text content visible:**

The following text is visible in the image:

*   `# Set up the application directory`
*   `WORKDIR /app`
*   `# Copy application files`
*   `COPY *.py /app/`
*   `COPY .env /app/`

**3. The context or purpose of what's displayed:**

The code snippet is part of a configuration file used to build a containerized application.

*   `WORKDIR /app` sets the working directory inside the container to `/app`.
*   `COPY *.py /app/` copies all Python files (`.py`) from the build context to the `/app` directory inside the container.
*   `COPY .env /app/` copies the `.env` file (containing environment variables) to the `/app` directory inside the container.

**4. Technical details if it's a code screenshot or technical diagram:**

The code uses Dockerfile syntax. The `WORKDIR` instruction sets the current working directory. The `COPY` instruction copies files or directories from the host machine to the container's filesystem. The first `COPY` instruction uses a wildcard (`*.py`) to copy multiple files. The second `COPY` instruction copies a specific file named `.env`. The destination `/app/` indicates that the files will be placed directly inside the `/app` directory. The line `COPY .env /app/` is highlighted with an orange border. An orange arrow points to this line.

This is because if you look at your Dockerfile .env does not exist in your repo.

Therefore it does not build.

Your docker is supposed to take the AIPROXY token from our environment not from yours.

This is passed dynamically at runtime of the Docker.

Since it fails to build, we cannot evaluate it.

Kind regards

---

## Reply 413
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T06:01:28.431Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/434

Your docker failed to build from your Dockerfile

 => ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 > [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |     
  24 |     # Verify uv installation
  25 | >>> RUN uv --version
  26 |     
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127

Since we cannot build your docker from your Docker manifest file we cannot evaluate it.

---

## Reply 414
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T06:14:06.484Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/435

Your container failed to run after building it.

docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "uv": executable file not found in $PATH: unknown

Thats why we cannot evaluate it.

---

## Reply 415
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T06:29:24.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/436

There is **clearly** *some difference* between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.

Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in <module>
    from tasksB import *
  File "/app/tasksB.py", line 83, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'

---

## Reply 416
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T06:34:10.301Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/437

Noted your concerns wrt Edit 1 and Edit 2 (and datagen.py running latest python version): Will raise it with @s.anand during our Wednesday meeting. Once we have an update, we will inform you of the outcome.

Kind regards

---

## Reply 417
**Author**: Swati Kapoor
**Posted**: 2025-04-08T08:52:53.059Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/438

Hi,

Please let me know the reason on why I have not got any bonus marks.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a results summary or report, likely from an automated grading system for a programming assignment. It includes:

*   **Score Calculation Formula:** A formula for calculating the final score.
*   **Repository Information:** Links or names of submitted GitHub and Docker repositories.
*   **Pre-requisite Checks:** A list of checks performed on the submitted repositories, with pass/fail indicators.
*   **Task Scores:** Individual scores for different parts of the assignment, including task score, bonus, and P1 score.
*   **A table of results:** A table with rows A, B, and C, and columns 1-10.

**2. Text Content:**

*   "Your final t score calculation is based on MIN (20, (task score + bonus))"
*   "Github repo submitted: https://github.com/swati-iitm/project1\_final"
*   "Docker repo submitted: swatiiitm/project1\_final"
*   "Pre-requisites check: (1 for pass, 0 for fail)"
*   "Docker repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   "Github repo exists and is public (should have a timestamp before 18th of Feb): 1"
*   "Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1"
*   "Gihub repo check - Dockerfile exists: 1"
*   "A1" through "A10"
*   "B1" through "B10"
*   "C1" through "C5"
*   "Your task score is: 3"
*   "Your bonus is: 0"
*   "Your P1 score is: 4"
*   The table contains 0s and 1s.

**3. Context and Purpose:**

The purpose of this display is to provide feedback to a student (likely "swati-iitm") on their submission for a programming assignment. It shows:

*   Whether the student submitted the correct repositories.
*   Whether the repositories meet basic requirements (public, timestamp, presence of LICENSE

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository page. It displays the repository's name, status (public), branch information, file structure, and some metadata about the repository.

**2. Text Content:**

*   **Repository Name:** "project1\_final" (labeled as Public)
*   **Branch Information:**
    *   Current branch: "master"
    *   2 branches, 0 tags
    *   "This branch is 8 commits ahead of main."
*   **File Structure:**
    *   \_pycache\_ (version\_latest, 2 months ago)
    *   data (version\_latest, 2 months ago)
    *   Dockerfile (updated, relative path, 2 months ago)
    *   LICENSE (Initial commit, 2 months ago)
    *   app.py (last\_minut, 2 months ago)
    *   datagen.py (updated relative path, 2 months ago)
    *   evaluate.py (version\_latest, 2 months ago)
    *   llm\_code.py (last\_minut, 2 months ago)
*   **Commit Information:**
    *   "swati-iitm last\_minut" (7d08160, 2 months ago, 9 Commits)
*   **Repository Metadata:**
    *   "About" section: "No description, website, or topics provided."
    *   "MIT license"
    *   "Activity"
    *   "0 stars"
    *   "1 watching"
    *   "0 forks"
*   **Releases:** "No releases published", "Create a new release"
*   **Packages:** "No packages published", "Publish your first package"
*   **UI Elements:**
    *   Buttons: "Pin", "Unwatch", "Fork", "Star", "Go to file", "Add file", "Code", "Contribute"

**3. Context and Purpose:**

The image shows the interface of a GitHub repository, allowing users to browse the files, view commit history, and contribute to the project. The "About" section indicates that the repository currently lacks a

---

## Reply 418
**Author**: Carlton D'Silva
**Posted**: 2025-04-08T09:37:52.730Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/439

We used some internal parameters with weights to auto calculate the bonus. Unless your submission met that threshold of 0.5 after scaling you would not get any bonus. Your score was normalised so instead of 3 you got 4 (3.75 got rounded up). But the metrics used to evaluate the quality of your submission only scored you at 0.007 which is far below the threshold required to get a bonus.

---

## Reply 419
**Author**: D HARICHARAN 
**Posted**: 2025-04-08T13:24:46.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/440

Respected Sir,

Yes Sir, I said the same,  `.env` was not able to be uploaded to repo as .env file was not allowed to be uploaded
when we download the repository it doesn’t have the `.env` file,
for docker image to build we need to add `.env` with `AIPROXY_TOKEN`
after that docker image will build, I had given about this in previous message
As you said Sir that you will use separate `AIPROXY_TOKEN`…you can put that in `.env` file and build the docker image
after that Sir its optional to pass `AIPROXY_TOKEN` again while running the docker Image
just the `.env` file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable

and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:

git clone https://github.com/23f2001390/llmagent.git

adding `.env` with AIPROXY token and replacing `evaluate.py` and `datagen.py` with new ones according to test environment

docker build -t llm-agent .

docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent

and in another terminal

uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

Thank you

Kind regards

---

## Reply 420
**Author**: S Sharmile
**Posted**: 2025-04-08T15:08:33.577Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/441

Respected sir

I understand it’s my mistake sir and I apologize for that sir, but please consider this time sir since because of this my entire project score went from 9/20 to 0, which would make me difficult to pass this course and continue my diploma.

Please consider this request sir, sorry sir and this would never be repeated in future. My project evaluation was 9/20 initially sir, but later it came down to 0 because of this issue. Kindly consider sir please.

Regards,

S Sharmile

23f3001688

---

## Reply 421
**Author**: Jayaram
**Posted**: 2025-04-08T18:05:49.832Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/442

Thanks for relentless efforts @carlton @Jivraj

I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..

Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of  my office environment,

**Image: image (18)**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web interface, likely for a cloud-based development environment or a container management platform. It displays information about a specific instance or node. There's also a terminal window at the bottom showing command-line activity.

**2. Text Content:**

*   **URL:** `labs.play-with-docker.com/p/cvqlfo0l2o9000cd7ic0#cvqlfo0l_cvqlfsol2o9000cd7icg`
*   **Instance Name:** `cvqlfo0l_cvqlfsol2o9000cd7icg`
*   **IP Address:** `192.168.0.13`
*   **Labels:** "IP", "Memory", "CPU", "SSH"
*   **Buttons:** "OPEN PORT", "DELETE", "EDITOR", "CLOSE SESSION"
*   **SSH Command:** `ssh ip172-18-0-93-cvqlfo0l2o9000cd7ic0@direct.labs.play-`
*   **Terminal Prompt:** `[node1] (local) root@192.168.0.13 ~`
*   **Terminal Command:** `$ docker build -t tdsproject1:latest . > tds-projlbuild.log`
*   **Timer:** 44:22

**3. Context and Purpose:**

The image depicts a user interacting with a Docker environment, likely on a platform like "Play with Docker". The user is:

*   Viewing details about a specific Docker instance (IP address, SSH access).
*   Potentially opening ports for the instance.
*   Possibly deleting or editing the instance.
*   Building a Docker image using the command line. The command `docker build -t tdsproject1:latest . > tds-projlbuild.log` suggests the user is building an image named `tdsproject1` with the tag `latest` from the current directory (`.`) and redirecting the output to a log file named `tds-projlbuild.log`.

**4. Technical Details:**

*   

build output

#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of a commit history, likely from a version control system like Git, displayed in a web-based interface (e.g., GitHub, GitLab, Bitbucket). It shows a single commit entry.

**2. Any text content visible:**

*   "Commits on Mar 30, 2025" - Indicates the date of the commits being displayed.
*   "Update Dockerfile removed hard coded proxies" - This is the commit message, describing the change made in the commit.
*   "rsjay1976 authored last week" - Indicates the author of the commit ("rsjay1976") and when it was authored ("last week").
*   "Verified" - A label indicating that the commit has been verified.
*   "a71e3a8" - A shortened version of the commit's SHA (Secure Hash Algorithm), a unique identifier for the commit.

**3. The context or purpose of what's displayed:**

The image shows a commit history, which is a record of changes made to a codebase over time. This allows developers to track changes, revert to previous versions, and understand the evolution of the project. The specific commit shown is related to updating a Dockerfile to remove hardcoded proxy settings.

**4. Technical details (if it's a code screenshot or technical diagram):**

*   The commit message "Update Dockerfile removed hard coded proxies" suggests that the Dockerfile (a script used to build Docker images) previously contained proxy settings directly within the file. This is generally considered bad practice, as it makes the Dockerfile less portable and harder to manage. The commit likely replaces these hardcoded values with environment variables or other configuration mechanisms.
*   The "Verified" label indicates that the commit has passed some form of automated checks or manual review, ensuring its quality and security.
*   The presence of a SHA (a71e3a8) confirms that this is a Git-based system.
*   The icons next to the SHA are likely links to view the commit details, copy the SHA, view the changed files, and view the code changes.

---

## Reply 422
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-08T21:11:14.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/443

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, likely running on a Linux-based system. It displays the output of a Docker build process. The build process is failing. The bottom part of the image shows a snippet of a Dockerfile.

**2. Any text content visible:**

*   **Terminal Prompts:**
    *   `root@tds-course-temp-bq:/r`
    *   `root@tds-course-temp-bq:/mnt/sdb/github_approach#`
    *   `root@tds-course-temp-bq:/mnt/sdb/github_approach/github_repos#`
    *   `root@tds-course-temp-bq:/mnt/sdb/github_approach/github_repos/22f3002723#`
    *   `root@tds-course-temp-bq:/mnt/sdb/github_approach/github_repos/22f3002723/TDS-Project1-Jan25-622ed8adf432b6c539321e6519d62da09248a542#`
*   **Docker Build Commands and Output:**
    *   `docker build -t 22f3002723:latest .`
    *   `[+] Building 8.7s (8/10)`
    *   `=> [internal] load build definition from Dockerfile`
    *   `=> => transferring dockerfile: 895B`
    *   `=> [internal] load metadata for docker.io/library/python:latest`
    *   `=> [internal] load .dockerignore`
    *   `=> => transferring context: 2B`
    *   `=> CACHED [1/7] FROM docker.io/library/python:latest`
    *   `=> [internal] load build context`
    *   `=> => transferring context: 347.68kB`
    *   `=> [2/7] RUN apt-get update && apt-

 22f3002723:

Was the latest docker file used from git lab

No, we are not allowing any changes to repo after deadline, this is consistent rule for every student. We pulled your github repo latest commit before 18th feb, I am getting following error.

---

## Reply 423
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-08T21:22:40.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/444

follow the steps mentioned in post below  :slight_smile: 

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

## Reply 424
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-08T21:24:21.083Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/445

23F300327:

To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.

---

## Reply 425
**Author**: Jayaram
**Posted**: 2025-04-09T06:36:56.097Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/446

Thanks @carlton @Jivraj

As mentioned earlier, the pre Feb 18 dockerFile commited in GIT had  my office proxy url’s set as http_proxy and https_proxy.. It worked in my office envuironment and i tested everything in my office environment but based on the results which came on March last week realised that the proxies were preventing the uv to be installed in other environments.

Post that realised we have cloud based "docker playground’ utility where docker builds can be tested agonistic of any environment.. The good thing with playground is our instances last for only 3 hrs and next day we try we are kind of gauranteed of fresh environment without any caches,

Now after March 30th checkin validated the same in docker playground and ensured that the image got tagged and createdd successfully..

It would be great if the March 30th checkin could be considered, Again appreciate all your help so far.

---

## Reply 426
**Author**: Saksham
**Posted**: 2025-04-09T08:03:10.683Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447

**Subject:** Request for Verification of Dockerfile and Reevaluation of Marks for Project 1

@carlton @Jivraj

Sir,

Regarding the recent feedback on **Project 1** for **TDS**, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named **`dockerfile`** (not **`Dockerfile`**). Please verify the repository again with this in mind.

Additionally, my Docker image architecture is *linux/amd64* (64-bit **x86**). I have also filled out the **Architecture Information Collector** form as requested.

**Pre-requisites check: (1 for pass, 0 for fail)**

Docker repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1

Gihub repo check - Dockerfile exists: 0

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository page. It shows the file structure and details of a repository named "task_agent_api". The main content area displays a list of files and directories within the repository's main branch. On the right side, there's an "About" section with repository details and statistics.

**2. Any text content visible:**

*   **Repository Name:** "task\_agent\_api" (marked as "Public")
*   **Branch:** "main" (1 Branch, 0 Tags)
*   **File/Directory List:**
    *   ".myenv"
    *   "\_\_pycache\_\_"
    *   ".env"
    *   "LICENSE"
    *   "README.md"
    *   "app.py"
    *   "datagen.py"
    *   "dockerfile" (highlighted with a tooltip also showing "dockerfile")
    *   "evaluate.py"
    *   "requirements.txt"
    *   "tasksA.py"
*   **Commit Messages:** "dockerfile update", "first commit", "Initial commit"
*   **Commit Dates:** "2 months ago"
*   **Commit Hash:** "a09023e"
*   **Number of Commits:** "4 Commits"
*   **About Section:**
    *   "No description, website, or topics provided."
    *   "Readme"
    *   "MIT license"
    *   "Activity"
    *   "0 stars"
    *   "1 watching"
    *   "0 forks"
*   **Releases:** "No releases published", "Create a new release"
*   **Packages:** "No packages published", "Publish your first package"
*   **Contributors:** "2"
*   **URL (at the bottom):** "https://github.com/23f1001822/task\_agent\_api/blob/main/dockerfile"

**3. The context or purpose of what's displayed:**

The image shows the structure of a GitHub repository, likely for a software project.

Here’s the link to my GitHub repository:

      [github.com](https://github.com/23f1001822/Task_agent_api)

  [GitHub - 23f1001822/task_agent_api](https://github.com/23f1001822/Task_agent_api)

Contribute to 23f1001822/task_agent_api development by creating an account on GitHub.

**Docker repo submitted:** *sakshamumate/task_agent_api*

I kindly request a **reevaluation of my project marks** based on these clarifications.

Thank you for your attention to this matter. Please let me know if you need any further information or clarification.

Best regards,

Saksham Umate ,

23f1001822@ds.study.iitm.ac.in

---

## Reply 427
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-09T08:53:21.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/449

Sir, I had posted the query on A8 and datagen exception. Is this a reply to that?

---

## Reply 428
**Author**: Carlton D'Silva
**Posted**: 2025-04-09T09:01:46.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/450

oh yeah sorry, hit the reply to the wrong button, but yes its to your post.

---

## Reply 429
**Author**: Carlton D'Silva
**Posted**: 2025-04-09T09:04:31.776Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451

I’ve got good news for you and 30 other students. Thanks to your diligent debugging effort that we were able to find this bug. For now the fix is that we will not evaluate you on a8 and catch the datagen exception so as to not cause cascading failures.

Thanks and kind regards.

We will let you know the outcome of the evaluations soon.

---

## Reply 430
**Author**: Jayaram
**Posted**: 2025-04-09T17:59:34.677Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/452

@carlton @Jivraj

any way out for my earlier query ?

---

## Reply 431
**Author**: Hilal
**Posted**: 2025-04-09T19:34:31.420Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/453

@carlton

Thank you for the reply .But it was working when i ran the initial evalaute.py .If you don’t  mind could you tell what may have caused this to happen.

---

## Reply 432
**Author**: Carlton D'Silva
**Posted**: 2025-04-10T05:31:59.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/454

Hi Hilal,

You have to recreate the test environment as shown in this post

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) Tools in Data Science

    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.…

That way you will be able to identify why the error was occuring.

The specific error itself means:

Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.

If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.

Kind regards

---

## Reply 433
**Author**: SP
**Posted**: 2025-04-10T19:06:44.256Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/455

sir for my project 1 i got a mail stating that the docker file isn’t public and that’s why prerequisite failed. but i checked it and it seemed absolutely perfect to me. Please look into this issue as my docker repo is public and absolutely as per the requirement.  @carlton @Jivraj

---

## Reply 434
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-10T20:32:26.287Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/456

Hi @22f3003083

Following was your submission, which is not a valid dockerrepo.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) displaying data in a tabular format. It appears to be a code repository or project management interface, possibly from a platform like GitHub, GitLab, or a similar service. The UI includes a search bar, tabs for different views (Preview, Code, Blame), and a table with data related to a project.

**2. Any text content visible:**

*   **Tabs:** "Preview", "Code", "Blame"
*   **File Information:** "1069 lines (1069 loc) • 127 KB"
*   **Search Bar:** Contains the text "22f3003083/v1" as a search query.
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Data:**
    *   Row 1: "1"
    *   Row 932: "2/16/2025 23:20:17", "22f3003083@ds.study.iitm.ac.in", "https://github.com/22f3003083/TDS\_Project\_1", "22f3003083/v1"
*   **Other UI elements:** Icons for "Raw", "Copy", "Download", and "Edit".

**3. The context or purpose of what's displayed:**

The UI is likely displaying a specific version or revision of a file within a code repository. The table seems to be tracking information related to the project, such as timestamps, email addresses of contributors, the GitHub repository link, and the name of the DockerHub image associated with the project. The search bar is being used to search for a specific version or tag within the repository.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The "1069 lines (1069 loc)" likely refers to the number of

---

## Reply 435
**Author**: SP
**Posted**: 2025-04-10T21:08:17.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/457

Now I feel so good getting 0.

0 is best.

---

## Reply 436
**Author**: Jayaram
**Posted**: 2025-04-11T03:28:59.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/458

@carlton @Jivraj

As requested earlier, Could you please reevaluate my submission.  The only change that had to be done post Feb 18 checkin was to remove my office proxies on Mar 30 from the docker file  to make it work in all environments.. It  would be great if this could be accomodated..

---

## Reply 437
**Author**: Carlton D'Silva
**Posted**: 2025-04-11T05:58:23.286Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/459

Hi Jayaram,

Unfortunately, we are not able to relax restrictions on changes to your repo, regardless of the reason. We have kept this rule uniform for everyone. If we allow this change, then everyone has a legitimate reason to request changes and would make the rule meaningless because then everyone will be able to make corrections to their submission. We do not even allow spelling changes.

Kind regards

---

## Reply 438
**Author**: Jayaram
**Posted**: 2025-04-11T06:10:41.470Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/460

Thanks for the response @carlton ..  just a small suggestion, to avoid scenarios like what i faced and also with softwares like docker/podman not being too windows friendly, i think students can find it easier if a dev/mock  linux env is provided for course term duration, instead of   everyone having to figuring out with AWS/Azure and all providers.. Anyway thanks and appreciate all the help

---

## Reply 439
**Author**: Mahesh Singh Bohra 
**Posted**: 2025-04-09T03:15:45.709Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/461

Sir, I have done everything for my project, but I am getting zero. I have uploaded my Docker file, but the email says it is not public. Sir, this is affecting my grades — please help me out. @Carlton

---

## Reply 440
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-11T09:50:21.807Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/462

These are your project 1 responses,

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a table-like user interface (UI) element, likely from a web application. It displays data related to user submissions, possibly for a project or assignment. The UI has a dark theme. There's a search bar at the top.

**2. Text Content:**

*   **Search Bar:** "Q 23f1001236" (The "Q" likely represents a magnifying glass icon for search)
*   **Table Headers:**
    *   "Timestamp"
    *   "Email Address"
    *   "What is the link to your GitHub repository which has the code for Project 1?"
    *   "What is the name of the image published on DockerHub?"
*   **Table Rows (Data):**
    *   **Row 1:**
        *   Timestamp: "2/15/2025 20:29:39"
        *   Email Address: "23f1001236@ds.study.iitm.ac.in"
        *   GitHub Repository: "https://github.com/MaheshSingh01/tds\_proj.git"
        *   DockerHub Image: "maheshsingh01/tds-proj"
    *   **Row 2:**
        *   Timestamp: "2/16/2025 21:28:12"
        *   Email Address: "23f1001236@ds.study.iitm.ac.in"
        *   GitHub Repository: "https://github.com/MaheshSingh01/tdsrepos.git"
        *   DockerHub Image: "maheshsingh01/tdsrepos"
    *   **Row 3:**
        *   Timestamp: "2/16/2025 23:53:46"
        *   Email Address: "23f1001236@ds.study.iitm.ac.in"
        *   GitHub Repository: "https://github.com/MaheshSingh01/tdsrepos.

We are considering latest submission which have docker repo `maheshsingh01/tdsrepos `

which is not accessible publically.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web page displaying a 404 error on the Docker Hub website. The page has a dark blue background with a large, bright blue circle in the center. Inside the circle is the error message and a cartoon illustration. The top of the page shows the Docker Hub header and navigation elements.

**2. Text Content:**

*   **URL:** `https://hub.docker.com/r/maheshsingh01/tdsrepos/tags`
*   **Docker Hub Header:** "dockerhub" (logo)
*   **Navigation:** "Explore / maheshsingh01 / tdsrepos"
*   **Search Bar:** "Search Docker Hub"
*   **Error Message:**
    *   "404" (large font)
    *   "Oops!"
    *   "The page you have requested was not found"
*   **Top Right Navigation:** "Ctrl+K", "?", "Update", "Sign in", "Sign up"

**3. Context and Purpose:**

The image indicates that the user attempted to access a specific page on Docker Hub related to a repository named "tdsrepos" belonging to the user "maheshsingh01", specifically the "tags" section. However, the page was not found, resulting in the 404 error. This suggests that either the repository or the "tags" section within it does not exist or is not publicly accessible.

**4. Technical Details:**

*   The image is a screenshot of a web browser displaying a Docker Hub page.
*   The URL indicates a specific path within the Docker Hub domain, suggesting a structured organization of repositories and their associated tags.
*   The 404 error is a standard HTTP status code indicating that the requested resource could not be found on the server.
*   The UI elements (search bar, navigation links, sign-in/sign-up buttons) are typical of a web application.
*   The presence of "Ctrl+K" suggests a keyboard shortcut for a search function.

---

## Reply 441
**Author**: Mahesh Singh Bohra 
**Posted**: 2025-04-11T11:11:45.772Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/463

Sir, could you please check it once more? I think the issue has been resolved. @carlton @Jivraj

---

## Reply 442
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-11T11:35:39.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/464

Since repo was not public during evaluation, we won’t be rechecking, or reevaluating.

---

## Reply 443
**Author**: Farhan Zafar
**Posted**: 2025-04-11T15:22:07.060Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/465

@Jivraj I’ve completed all the required steps, but I’m still getting 0, It was working fine before. Could you please help me identify what might be going wrong?

---

## Reply 444
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-11T15:56:08.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/466

Hi @21f3003107

You need to look it up yourself, We have sent out evaluation log and docker log files, check those out.

Evaluation script and other scripts that we have used are there in github repository over here.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1)

If there is some mistake from our end let us know about it.

To replicate test environment follow steps provided below.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

## Reply 445
**Author**: WAGISHA TANYA RAI
**Posted**: 2025-04-11T18:16:52.479Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/467

@carlton Requested sir

This is to request that in my evaluation a got 0 cause of the use of lowercase d instead of uppercase D but I have already submitted the  docker file in my git hub repo also.

**Image: WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a portion of a user interface, likely from a code repository hosting platform like GitHub or GitLab. It displays a list of files and their commit history. Each row represents a file and shows its name, the action performed (e.g., "added"), and the time since the action was performed.

**2. Text Content Visible:**

*   **User:** "wag28 added" - Indicates that the user "wag28" added the files.
*   **Commit Hash:** "eff178a" - A short commit hash, followed by "2 months ago" and a refresh icon.
*   **File Names:**
    *   ".dockerignore"
    *   ".gitattributes"
    *   ".gitignore"
    *   "LICENSE"
    *   "README.md"
    *   "app.py"
    *   "datagen.py"
    *   "dockerfile"
    *   "evaluate.py"
    *   "requirements.txt"
    *   "tasksA.py"
    *   "tasksB.py"
*   **Actions:** "added", "Initial commit"
*   **Time:** "2 months ago" (repeated for most files)
*   **Other UI elements:** "No", "L", "pro", "Rep", "Rel", "Pac", "Lar"

**3. Context and Purpose:**

The image displays the commit history of a repository. It allows users to see when files were added or modified, and by whom. This is crucial for collaboration, version control, and understanding the evolution of a project.

**4. Technical Details:**

*   The file extensions ".py" suggest that the project likely involves Python code.
*   The presence of "requirements.txt" indicates that the project uses Python packages managed by pip.
*   "dockerfile" and ".dockerignore" suggest that the project is containerized using Docker.
*   ".gitattributes" and ".gitignore" are standard files for Git repositories, used to configure Git's behavior and specify files to be ignored, respectively.
*   "LICENSE" and "README.md" are common files in open-source projects, providing licensing information

---

## Reply 446
**Author**: Hilal
**Posted**: 2025-04-12T07:38:59.014Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/468

@carlton

Thank you i found my mistake in my docker file i wrote  this  CMD [“uv”, “run”, “app.py”]  instead of

CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine

---

## Reply 447
**Author**: Mahesh Singh Bohra 
**Posted**: 2025-04-14T07:06:19.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/469

Sir my repo was public

---

## Reply 448
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-14T10:10:56.167Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/470

Sir any news on this? Did my score increase at all? My dashboard still shows the old score.

---

## Reply 449
**Author**: Adarsh kumar
**Posted**: 2025-04-14T20:39:18.125Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/471

@carlton sir, my project 1 marks have still not increased even though while during evaluation it shows 4/10 for the task 1. It was said that the docker image prerequisite will be removed and without that the evaluation would be done, but there is still no change in my marks. please look into it once, as my dashboard currently reflects 0 for project 1.

---

## Reply 450
**Author**: Carlton D'Silva
**Posted**: 2025-04-15T07:49:58.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/472

These evals are being handled separately. They have not yet been completed. Kindly bear with us till they are complete.

---

## Reply 451
**Author**: Maulik Dang
**Posted**: 2025-04-15T11:06:47.111Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/473

Same here @carlton in my evaluation logs i have scored 10 while marks being reflected are not the same neither on mail nor on site

---

## Reply 452
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-15T11:31:06.090Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/474

I looked at your evaluation logs and it says 1 score instead of 10.

---

## Reply 453
**Author**: Garima
**Posted**: 2025-04-06T15:40:39.389Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/475

Good evening!

[1000092114|690x198](/uploads/short-url/30ijyIo5UiUUEVvnPZklfYVY2mI.jpeg)

I am writing to you to request you please relook into the evaluation.

The docker image which I share is working at my end.  The size of the image is 6 GB which may take more than 5 minutes to load as I wasn’t aware of the infra level restrictions.

I request you to kindly consider my request and please re-evaluate the assignment as I have contributed a lot of effort into it.

Thanks,

Garima

---

## Reply 454
**Author**: Adarsh kumar
**Posted**: 2025-04-17T04:48:37.091Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/477

Sir, so will my score get updated because now it is marked as 0.

---

## Reply 455
**Author**: Saksham
**Posted**: 2025-04-17T06:17:58.394Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/478

@carlton @Jivraj

Sir,

I am Saksham Umate and my project 1 was to be re-evaluation because of docker file not found in root ,but it was their so you had given me confirmation that it will re-evaluate after end term. I had already shared my docker file systems configuration at docker hub

So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it

Tell me if any information is needed about project from my side

Thank you!

Best regards,

Saksham

My docker repo details in previous post:

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) Tools in Data Science

    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
@carlton @Jivraj 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…

**Image: IMG_20250417_114002**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of an email on a mobile device. The email is from "Carlton D'Silva" and is addressed to "Dear Learner." The email discusses requirements for a project (P1) and Docker-related aspects. At the bottom of the screen are typical Android navigation buttons and app icons for email, messaging, and video call.

**2. Text Content:**

The email text is as follows:

*   "Carlton D'Silva 9 Apr to bcc: me"
*   "Dear Learner,"
*   "Your P1 had failed a pre-requisite because our script could not locate Dockerfile in the base of the root directory of your github repo. We are relaxing this requirement."
*   "Your P1 submissions will be looked at separately after the end term only."
*   "We will run a script to do a directory tree search for Dockerfile in your github."
*   "No changes to the github repo after Feb 18th will be considered."
*   "No spelling deviations will be accepted for the required files."
*   "All other prerequisites will still have to be met."
*   "Your docker image has to build without errors from the Dockerfile."
*   "After building it, your docker container has to become operational within 5 minutes of starting."
*   "Then evaluations will be carried out exactly according to the test environment that was specified."

The bottom of the screen shows app icons with notification badges:
*   Email icon with "99+" notification
*   Messaging icon with "4" notification

**3. Context and Purpose:**

The email is an announcement or clarification regarding the requirements for a project (P1), likely in a software development or DevOps course. It informs students that a previous requirement about the Dockerfile location has been relaxed. It also emphasizes that submissions will only be evaluated at the end of the term, that changes to the GitHub repo after February 18th will not be considered, and that spelling errors will not be accepted. The email also outlines Docker-related requirements, such as the image building without errors and the container becoming operational within 5 minutes.

**4. Technical Details:**

*   The email mentions "Dockerfile," which is a text document that contains all

---

## Reply 456
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-17T06:30:08.297Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/479

Evaluations are done for such cases where Dockerfile(with name of Dockerfile as `Dockerfile`) was present inside other folders than root folder of your github repo.

---

## Reply 457
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-17T06:38:10.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/480

@carlton sir, any info on outcome of [this bug in P1 datagen.py](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451) ?

---

## Reply 458
**Author**: Saksham
**Posted**: 2025-04-17T07:18:36.089Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/481

Did Mark’s are updated or being update for this students ?

---

## Reply 459
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-17T07:34:59.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/482

Hi @22f3000819

We had updated datagen.py(try block for task) which affected 30 students, but scores changed only for 4 students, for others it remained the same.

---

## Reply 460
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-17T07:35:35.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/483

We will be pushing marks today.

---

## Reply 461
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-17T07:40:39.300Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/484

I probably wasn’t 1 of the 4, right? Anyways thanks for paying attention to the matter.

Regards,

Shivaditya

---

## Reply 462
**Author**: S Sharmile
**Posted**: 2025-04-17T13:58:06.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/485

@carlton @Jivraj

Respected Sir,

I hope you are doing well.

This is with reference to your confirmation mail that my project 1 will be re-evaluated after end term

I would like to sincerely apologize for the oversight in my Project 1 submission. Upon reviewing my GitHub repository, I realized that the file was named `dockerfile` (with a lowercase ‘d’) in the Github root repo instead of the required `Dockerfile` (with an uppercase ‘D’).

While the contents of the file were correct and my project passed several evaluation tests, I understand that the evaluation script could not detect the Dockerfile due to this naming issue. I genuinely did not intend to deviate from the standard, and I now fully understand the importance of following naming conventions precisely.

I humbly request you to kindly consider this as an honest mistake and allow a one-time exception, Please sir. This issue has unfortunately resulted in my project score being reduced to 0, which puts my overall course performance at risk. I assure you that I have learned from this experience and such an error will not occur again in the future.

So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it.

Thank you very much for your time and consideration.

Warm regards,

S. Sharmile

Roll No: 23f3001688

---

## Reply 463
**Author**: Adarsh kumar
**Posted**: 2025-04-17T17:03:34.931Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/486

Sir, my marks still did not get updated, please help me in that regard.

---

## Reply 464
**Author**: Carlton D'Silva
**Posted**: 2025-04-18T03:36:17.392Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/487

Hi Everyone,

We have sent the updated marks to Operations. At this time of the term they are very busy with lots of updates, so it will take time for them to push it to the dashboard. As soon as they inform us that the scores have been pushed, we will send out a discrepancy form if you find any issues with your score.

Thanks & Kind regards

---

## Reply 465
**Author**: Adarsh kumar
**Posted**: 2025-04-18T13:54:05.934Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/488

Sir, my project 1 marks are still 0 even though I had passsd few cases. Please help me sir as my final score is coming as 69.8 , it will be very valuable for me if it crosses 70, please sir help me with this regard

---

## Reply 466
**Author**: Saksham
**Posted**: 2025-04-20T09:05:20.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/489

@carlton

Hi Sir,

I hope you’re doing well. I just wanted to let you know that I put a lot of effort into completing **Project1**, but I accidentally named the **Dockerfile** as `dockerfile` (with a lowercase ‘d’).

Could you please consider evaluating it with that name? I’d really appreciate it.

Thank you!

My discourse post for more information:

    [Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) Tools in Data Science

    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1 
@carlton @Jivraj 
Sir, 
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind. 
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested. 
P…

---
