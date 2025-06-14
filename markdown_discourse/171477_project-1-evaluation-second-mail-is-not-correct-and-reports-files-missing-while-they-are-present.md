# Project 1 Evaluation second mail is not correct and reports files missing while they are present

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/1

## Topic Metadata
- **ID**: 171477
- **Slug**: project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present
- **Created**: 2025-04-01T03:38:04.214Z
- **Views**: 153
- **Replies**: 8
- **Likes**: 3
- **Tags**: term1-2025, tds-project-one

## Original Post
**Author**: Aryan Kohli
**Posted**: 2025-04-01T03:38:04.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/1

Mail I received Yesterday:

**Image: Screenshot from 2025-04-01 09-01-07**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based email or document outlining the prerequisites for a project (Project 1) and the results of an automated evaluation of those prerequisites. It appears to be feedback given to a learner or developer.

**2. Text Content:**

The text content includes:

*   "Dear Learner," (Salutation)
*   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (Introduction and reference to external documentation)
*   A numbered list of prerequisites:
    1.  "Your GitHub repository exists and is publicly accessible"
    2.  "Your GitHub repository has a LICENSE file with the MIT license"
    3.  "Your GitHub repository has a valid Dockerfile"
    4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
    5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
*   "If you fail to meet this minimum requirement your submission will not get evaluated." (Warning)
*   "These are your Project 1 Prerequisite evaluations:" (Heading for the evaluation results)
*   A list of evaluation results, each in the format "Is [condition]: [result]":
    *   "Is Docker image present in dockerhub AND is public: PASS"
    *   "Is Github repo present AND public: FAIL"
    *   "Is Dockerfile present in root of github repo: FAIL"
    *   "Is MIT license present at root of github repo: FAIL"

**3. Context and Purpose:**

The purpose of the document is to inform the learner about the requirements for Project 1 and to provide feedback on whether their submission meets those requirements. The automated evaluation results indicate which prerequisites have been met (PASS) and which have not (FAIL). This allows the learner to identify and address any issues before submitting their final project.

**4. Technical Details:**

*   The prerequisites involve using GitHub for version control and Docker for containerization.
*   The "podman run" command in prerequisite #4 suggests that the

Previous Correct Evaluation Mail:

**Image: Screenshot from 2025-04-01 09-02-35**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based email or document. It appears to be feedback on a project submission, specifically a Docker image. The document lists several files related to the evaluation, including log files, scripts, and data generation files. It also provides context about the evaluation environment and scoring criteria.

**2. Text Content:**

The document begins with "Dear Learner," and then proceeds to inform the recipient that their project 1 Docker image submission has been evaluated. Key text elements include:

*   **"MISSING"**: This indicates that a file was not available, potentially due to evaluation failure or misconfiguration. Missing files result in a score of 0.
*   **Performance expectations**: The Docker image is expected to be responsive within 5 minutes of launch. The evaluation was performed on an 8 core Xeon Google Cloud compute unit with 1 Gigabit of dedicated network bandwidth.
*   **List of files**:
    *   Evaluation log file (with a Google Drive link): Contains performance report.
    *   Docker log file (with a Google Drive link): Provides technical performance.
    *   Server start log file (attachment): Logs for arm vs x86.
    *   Evaluation script file (attachment): Contains the tests and scoring mechanism.
    *   Data generation file (attachment): Used to create data for tasks.
    *   Docker orchestration file (attachment): Handles Docker image retrieval and instance launching.
    *   Solution script (attachment zip): Solves the project using prompt engineering.
*   **Docker image ID**: The ID of the evaluated Docker image is provided: "48299f48f66b".
*   **Scoring information**: The scores are not final but indicate current evaluation standards. There's an opportunity to report bugs or discrepancies until Tuesday. The document mentions a final marking schema and normalization based on the highest scores.
*   **Closing**: The document expresses anticipation for feedback and apologizes for delays.
*   **Call to action**: "Post all your concerns on this discourse thread".

**3. Context and Purpose:**

The document serves as feedback on a Docker image submission. Its purpose is to:

*   Inform the learner about the evaluation results.
*   Provide access to relevant files for review.

Good Morning Sir,

This is my github repo: [GitHub - kohliaryan/TDS_Project_1](https://github.com/kohliaryan/TDS_Project_1) ()You can verify that it is public, MIT License is present and Dockerfile is also present.)

I also got a mail 2 days ago in which everything is mentioned correctly but the mail I got yesterday worry me.  Sir, I have worked really hard for project 1. Please look into this matter.

@carlton

---

## Reply 1
**Author**: Aryan Kohli
**Posted**: 2025-04-03T12:03:07.447Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/2

@Jivraj Sir, Please look into in this matter, no reply from your side till now and 2 days have been passed.

---

## Reply 2
**Author**: Carlton D'Silva
**Posted**: 2025-04-04T06:10:31.239Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/3

Apologies for that,

The second email was an automated script that used a stricter criteria. You have passed evaluation and also have a score. So dont worry. We will push scores over this weekend. We are currently doing normalisation.

Kind regards

---

## Reply 3
**Author**: Kshitij Pandey
**Posted**: 2025-04-04T14:22:43.915Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/4

Hi @carlton,

I’m experiencing the same issue mentioned in this thread regarding Project 1 evaluation emails:

The first email I received confirmed all requirements were met (public repo, MIT License, Dockerfile, etc.)
The second email incorrectly flagged missing files despite their presence in my repository

Here are screenshots of both emails showing the discrepancy:

**Image: First Evaluation Email**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email in a web-based email client (likely Gmail). The email is titled "TDS Jan 25 Project 1 Scores" and is from "22t1 se2002" with the email address se2002@study.iitm.ac.in. The email is addressed to "me".

**2. Text Content:**

The email body contains the following information:

*   **Subject:** TDS Jan 25 Project 1 Scores
*   **Sender:** 22t1 se2002 
*   **Recipient:** to me
*   **Date:** Mar 29, 2025, 12:21 AM (6 days ago)
*   **Greeting:** Dear Learner,
*   **Body:**
    *   An evaluation of a project 1 docker image submission has been completed.
    *   A list of files is provided:
        1.  Evaluation log file (with a Google Drive link). This file contains a performance report.
        2.  Docker log file (with a Google Drive link). This file provides the technical performance of the container.
        3.  Server start log file (separate logs for arm vs x86) (See attachment).
        4.  Evaluation script file (separate logs for arm vs x86) (See attachment).
        5.  Data generation file (See attachment).
        6.  Docker orchestration file (See attachment).
        7.  Solution script (See attachment zip).
    *   "MISSING" indicates that the file is not available. Missing files result in a score of 0.
    *   The docker image is expected to be responsive in 5 minutes.
    *   The images were run on an 8 core Xeon Google Cloud compute unit with 1 Gigabit of dedicated network bandwidth.
    *   The Docker image ID is provided.
    *   The scores are not final.
    *   There is an opportunity to report bugs or discrepancies.
    *   A deadline of Tuesday is given to report any problems.
    *   The email mentions a final

**Image: Second Evaluation Email**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email. The email is about the scores for "TDS Jan 25 Project 1". The email details the prerequisites for the project and the results of the evaluation of those prerequisites.

**2. Any text content visible:**

*   **Subject:** TDS Jan 25 Project 1 Scores
*   **Sender:** 22t1 se2002 
*   **Recipient:** to me
*   **Date:** Tue, Apr 1, 1:25 AM (3 days ago)
*   **Body:**
    *   Dear Learner,
    *   Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
        1.  Your GitHub repository exists and is publicly accessible
        2.  Your GitHub repository has a LICENSE file with the MIT license
        3.  Your GitHub repository has a valid Dockerfile
        4.  Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
        5.  Your Docker image uses the same Dockerfile as in your GitHub repository
    *   If you fail to meet this minimum requirement your submission will not get evaluated.
    *   These are your Project 1 Prerequisite evaluations:
        *   Is Docker image present in dockerhub AND is public: PASS
        *   Is Github repo present AND public: FAIL
        *   Is Dockerfile present in root of github repo: FAIL
        *   Is MIT license present at root of github repo: FAIL
    *   Prerequisites: FAIL
    *   Project 1 Score: 0

**3. The context or purpose of what's displayed:**

The email is an automated notification to a student (the "Learner") regarding their score on Project 1. The email outlines the prerequisites for the project, which involve having a public GitHub repository with a Dockerfile and MIT license, and a publicly accessible Docker image. The email then provides a breakdown of whether each prerequisite was met, and the final project

My GitHub repo remains publicly accessible with all required components:

[GitHub repo](https://github.com/23f2000345/TDS_final)

Could you please confirm this was an automated error and that my submission will be evaluated based on the actual repository contents? Your clarification would be greatly appreciated.

Thank you for your time and assistance!

---

## Reply 4
**Author**: Carlton D'Silva
**Posted**: 2025-04-04T16:03:11.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/5

Hi,

Prerequisite checks have passed. But your docker image was missing a dependency that you forgot to copy into the image. so it failed to evaluate because it failed to run.

---

## Reply 5
**Author**: Aryan Kohli
**Posted**: 2025-04-04T17:00:40.743Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/6

You talking about me or @23f2000345 ?

---

## Reply 6
**Author**: Sudhish Narayan S
**Posted**: 2025-04-12T05:11:08.122Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/8

Good Morning Sir, Actually even I got the mail regarding Project-1 Evaluation, where I got the message like the prerequisites were not met. But, sir actually I have uploaded my MIT License file, requirements.txt file, my Project.py file and the Dockerfile. Sir, and when I sent a request to my API from my device, it worked sir. I have got 0 in my project 1 sir, but I have met the pre-requisites Can you please check this once sir?

My GitHub repository for Project-1: [GitHub - sudhishssn134/project_1_tds](https://github.com/sudhishssn134/project_1_tds)

Thanking You

Just attaching the mail I recieved.

**Image: Screenshot 2025-04-12 104211**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of an email. The email appears to be a notification or report related to a project submission, specifically a Docker image. The email provides scores and feedback on the submitted Docker image. It includes links to evaluation logs and mentions attached files containing scripts and other relevant data.

**2. Text Content:**

*   **Subject:** TDS Jan 25 Project 1 Scores
*   **Sender:** 22t1 se2002
*   **Recipient:** to me
*   **Salutation:** Dear Learner,
*   **Body:**
    *   An introductory paragraph stating that the project 1 docker image submission has been evaluated and the following files are provided.
    *   "MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us. MISSING files will result in a score of 0."
    *   Information about the Docker image responsiveness requirement (5 minutes from launch) and the hardware used for evaluation (8 core Xeon Google Cloud compute unit, 1 Gigabit network bandwidth).
    *   A numbered list of files:
        1.  Evaluation log file (with a Google Drive link). Description: "This contains your performance report on your individual tasks."
        2.  Docker log file (with a Google Drive link). Description: "This provides the technical performance of your container."
        3.  Server start log file (See attachment). Description: "(separate logs for arm vs x86) If your docker service did not start or respond to attempts to our requests."
        4.  Evaluation script file (See attachment). Description: "(separate logs for arm vs x86) This file has the actual tests that were run against your submission and the scoring mechanism."
        5.  Data generation file (See attachment). Description: "The evaluation file depends on this file to create the data for the tasks."
        6.  Docker orchestration file (See attachment). Description: "This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications."
        7.  Solution script

---

## Reply 7
**Author**: Carlton D'Silva
**Posted**: 2025-04-12T05:19:47.384Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/9

Your Dockerfile was misconfigured. When we try to build the docker image from your github repo, we get this error:

`tried copying parent folder(COPY failed: forbidden path outside the build context: .. ())`

You have to replicate the test environment. If it works when you follow this test setup then you should get in touch with us.

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

---

## Reply 8
**Author**: Sudhish Narayan S
**Posted**: 2025-04-12T05:22:31.404Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/10

Oh OK Sir. I will try it out. Thank You so much sir

---

## Reply 9
**Author**: Sudhish Narayan S
**Posted**: 2025-04-12T06:28:33.110Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/11

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below

**Image: Screenshot 2025-04-12 115342**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a terminal output, likely from a Docker build and run process. It displays a series of commands and their corresponding outputs, followed by information about the running application.

**2. Text Content:**

*   **Docker Build Output:**
    *   Lines starting with "=>" indicate Docker build steps.
    *   `sha256:` followed by a long hexadecimal string represents the hash of a Docker image layer.
    *   File sizes (e.g., "3.51MB / 3.51MB", "28.23MB / 28.23MB") indicate the size of the layers being processed.
    *   "extracting sha256:" indicates the extraction of a layer.
    *   "[internal] load build context" and "transferring context: 9.24kB" show the loading of the build context.
    *   "WORKDIR /app", "COPY . /app", "COPY requirements.txt /app/", "RUN pip install --no-cache-dir -r requirements.txt" are Dockerfile instructions.
    *   "exporting to image" and "exporting layers" indicate the finalization of the image build.
    *   "exporting manifest sha256:", "exporting config sha256:", "exporting attestation manifest sha256:", "exporting manifest list sha256:" show the exporting of different manifests.
    *   "naming to docker.io/library/sha256:" and "unpacking to docker.io/library/sha256:" indicate the image is being pushed to Docker Hub.
    *   Times (e.g., "1.5s", "2.8s") show the duration of each step.
    *   "View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/4btzhep5n0ttsar3bibf4z96c" provides a link to view the build details in Docker Desktop.
*   **Docker Run Command and Application Output:**
    *   `C:\SSNFun\IITM\sudhishssn134-project_1_td

Sir, But I couldn’t run the last command you gave,

uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

As I dont have evaluate.py

But, the DockerImage is built and is running without error sir.

Please guide me after this sir

Thank You So much sir

---

## Reply 10
**Author**: Sudhish Narayan S
**Posted**: 2025-04-29T14:34:47.914Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/12

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below

**Image: Screenshot 2025-04-12 115342**
Here's a detailed description of the image content:

**1. What is shown in the image:**

The image shows a terminal output, likely from a Docker build and run process. It displays the steps involved in building a Docker image, followed by the execution of a Docker container.

**2. Text Content:**

*   **Docker Build Log:** The initial part of the output shows a Docker build process. Key steps include:
    *   Extracting layers (identified by SHA256 hashes)
    *   Transferring context (9.24kB)
    *   Setting the working directory (`WORKDIR /app`)
    *   Copying files (`COPY . /app`, `COPY requirements.txt /app/`)
    *   Running `pip install --no-cache-dir -r requirements.txt`
    *   Exporting the image and layers
    *   Naming and unpacking the image to `docker.io/library/...`
*   **Build Details URL:** `View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/4btzhep5n0ttsar3bibf4z96c`
*   **Docker Run Command:** `C:\SSNFun\IITM\sudhishssn134-project_1_tds-b240fec>docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49`
*   **Application Startup Logs:**
    *   `INFO: Started server process [1]`
    *   `INFO: Waiting for application startup.`
    *   `INFO: Application startup complete.`
    *   `INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`

**3. Context and Purpose:**

The image captures the process of building a Docker image for a Python application (likely using `requirements.txt` for dependencies) and then running that image. The application appears to be

Sir, But I couldn’t run the last command you gave,

uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

As I dont have evaluate.py

But, the DockerImage is built and is running without error sir.

Please guide me after this sir

Thank You So much sir

---

## Reply 11
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-29T15:19:06.622Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present/171477/13

[URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/32) Tools in Data Science

    Project 1 : You tried to copy parent folder(Ref:line number 8 in your [Dockerfile](https://github.com/sudhishssn134/project_1_tds/blob/main/Dockerfile)) but there is no parent folder with respect to github repo’s root folder, so it fails evaluation. 
Project 2 : Response we received through google form was [http://127.0.0.1:8000/api](http://127.0.0.1:8000/api) which is local host url not a vercel endpoint.

---
