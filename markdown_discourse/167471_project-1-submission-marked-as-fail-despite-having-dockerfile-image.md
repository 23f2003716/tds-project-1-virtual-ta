# Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1

## Topic Metadata
- **ID**: 167471
- **Slug**: project-1-submission-marked-as-fail-despite-having-dockerfile-image
- **Created**: 2025-02-17T10:07:56.585Z
- **Views**: 85
- **Replies**: 6
- **Likes**: 0
- **Tags**: operational, term1-2025, tds-project-1

## Original Post
**Author**: Arnav Mehta 
**Posted**: 2025-02-17T10:07:56.783Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1

Dear TDS Team,

I have verified my submission, and my repository **does include a Dockerfile**, and the **Docker image is accessible on DockerHub**. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.

Looking forward to your confirmation.

Best regards,

Arnav Mehta

(21f3002647)

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a file explorer or directory listing, likely from a code editor or IDE. It shows a list of files and folders within a project. The background is dark, suggesting a dark theme.

**2. Any text content visible:**

The following files and folders are listed:

*   `..` (Indicates the parent directory)
*   `LLM_PROJECT1` (Folder)
*   `__pycache__` (Folder)
*   `Dockerfile` (File)
*   `LICENSE` (File)
*   `app.py` (File)
*   `datagen.py` (File)
*   `evaluate.py` (File)
*   `requirements.txt` (File)
*   `tasksA.py` (File)
*   `tasksB.py` (File)

**3. The context or purpose of what's displayed:**

The content suggests a Python project related to Large Language Models (LLMs). The presence of `app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, and `tasksB.py` indicates that the project likely involves creating an application (`app.py`), generating data (`datagen.py`), evaluating model performance (`evaluate.py`), and performing specific tasks (`tasksA.py`, `tasksB.py`). The `requirements.txt` file suggests that the project has dependencies that need to be installed. The `Dockerfile` indicates that the project is containerized, likely using Docker. The `LICENSE` file specifies the licensing terms for the project.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The `.py` file extension indicates that these are Python source code files.
*   `requirements.txt` is a standard file used in Python projects to list the project's dependencies, which can be installed using `pip`.
*   `Dockerfile` is a text file that contains instructions for building a Docker image.
*   `__pycache__` is a directory that Python creates to store compiled bytecode files.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a UI element, likely from a website or application that hosts projects or repositories. It displays information about a specific project. The UI element includes:

*   A stylized icon of a cube.
*   The project's name and owner.
*   Metadata about the project (author, update date).
*   A label indicating the project type (image).
*   Statistics related to the project (stars, downloads).

**2. Any text content visible:**

The text content includes:

*   **arnavmehta2025/llm\_project1:** This is the project's name, likely in the format "username/repository\_name".
*   **By arnavmehta2025:** Indicates the project's author or owner. The username is hyperlinked.
*   **Updated 2 days ago:** Shows the last time the project was updated.
*   **IMAGE:** A label indicating the project is an image.
*   **0:** The number of stars the project has received.
*   **16:** The number of downloads the project has.

**3. The context or purpose of what's displayed:**

The UI element is designed to provide a quick overview of a project. It allows users to identify the project, its owner, its type, and its popularity (based on stars and downloads). This type of display is common on platforms like GitHub, GitLab, or similar code/project hosting services.

**4. Technical details (if applicable):**

While there's no code or technical diagram directly visible, the structure suggests a web-based UI. The use of "username/repository\_name" is a common convention for identifying projects in version control systems. The "Updated 2 days ago" indicates dynamic content that is updated based on the project's activity. The star and download counts are metrics used to gauge the project's popularity and usage.

---

## Reply 1
**Author**: Arnav Mehta 
**Posted**: 2025-02-17T12:30:15.244Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2

@Saransh_Saini sir what should i do?

---

## Reply 2
**Author**: Saransh Saini
**Posted**: 2025-02-17T15:43:39.614Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3

@carlton Kindly have a look into this.

---

## Reply 3
**Author**: Satvik  Sawhney
**Posted**: 2025-02-18T00:48:03.881Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8

Good Morning Sir,

Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.

Looking forward to your reply.

Thank you

Satvik Sawhney

23f2003680

---

## Reply 4
**Author**: Carlton D'Silva
**Posted**: 2025-02-18T05:00:31.191Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9

So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e *yesteday*, you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a file explorer or directory listing, likely from a code editor or IDE. It shows a list of files and folders within a project. The icons indicate whether each item is a folder or a file.

**2. Any text content visible:**

The following files and folders are listed:

*   `..` (Indicates the parent directory)
*   `LLM_PROJECT1` (Folder)
*   `__pycache__` (Folder)
*   `Dockerfile` (File)
*   `LICENSE` (File)
*   `app.py` (File)
*   `datagen.py` (File)
*   `evaluate.py` (File)
*   `requirements.txt` (File)
*   `tasksA.py` (File)
*   `tasksB.py` (File)

**3. The context or purpose of what's displayed:**

The directory listing suggests a Python project related to Large Language Models (LLMs). The presence of files like `app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, and `tasksB.py` indicates that the project likely involves:

*   A main application (`app.py`)
*   Data generation (`datagen.py`)
*   Evaluation of models (`evaluate.py`)
*   Specific tasks related to the LLM (`tasksA.py`, `tasksB.py`)
*   A `requirements.txt` file suggests that the project uses external Python libraries.
*   A `Dockerfile` indicates that the project is containerized, likely using Docker.
*   A `LICENSE` file indicates the project has a license associated with it.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The `.py` file extensions indicate that the project is written in Python.
*   The `__pycache__` folder is automatically created by Python to store compiled bytecode files for faster execution.
*   The `requirements.txt` file is a standard way to specify the Python packages required to run the project.
*   The `Dockerfile` is a text file that contains instructions for building a Docker image.

[/quote]

showing that your files are in the correct place.

We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.

Kind regards

---

## Reply 5
**Author**: Arnav Mehta 
**Posted**: 2025-02-18T06:35:49.560Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10

@carlton sir

Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.

I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered  :frowning: 

Kind regards,

Arnav Mehta

21f3002647

---

## Reply 6
**Author**: Satvik  Sawhney
**Posted**: 2025-02-18T08:28:16.577Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11

Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.

Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.

Sir it is a humble request to please consider it.

Warm Regards,

Satvik Sawhney

23f2003680

**Image: Screenshot 2025-02-18 at 1.53.10 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a file directory structure, likely from a code repository or file management system. It shows a list of folders and files with associated descriptions and timestamps. The UI has a dark theme.

**2. Text Content:**

Here's a breakdown of the text visible in the image:

*   **Folders:**
    *   Business
    *   Operations
    *   app
*   **Files:**
    *   Dockerfile
    *   LICENSE
    *   README.md
*   **Descriptions:**
    *   Reconfigured taskB8 taskB9 taskB10
    *   Reconfigured taskA8 taskA9 taskA10
    *   Updated Dockerfile and requirements.txt
    *   Rename dockerfile to Dockerfile
    *   MIT License
    *   Project Structure
*   **Timestamps:**
    *   2 days ago (appears three times)
    *   yesterday
    *   3 days ago (appears twice)
*   **Other:**
    *   Re (partially visible, likely the beginning of a word like "Repository")

**3. Context and Purpose:**

The image shows a snapshot of a project's file structure and recent changes. It's likely part of a version control system (like Git) or a file management interface that tracks modifications and provides descriptions of those changes. The timestamps indicate when the files or folders were last modified.

**4. Technical Details:**

*   The presence of "Dockerfile" and "requirements.txt" suggests that this project involves containerization (using Docker) and Python dependencies.
*   The "LICENSE" file indicates the project's licensing terms (in this case, MIT License).
*   The "README.md" file is a common file used to provide an overview and instructions for the project.
*   The descriptions like "Reconfigured taskB8 taskB9 taskB10" suggest that the project involves tasks or processes that are being managed and reconfigured.

---
