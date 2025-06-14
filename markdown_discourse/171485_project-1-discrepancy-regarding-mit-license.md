# Project 1 discrepancy regarding mit license

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1

## Topic Metadata
- **ID**: 171485
- **Slug**: project-1-discrepancy-regarding-mit-license
- **Created**: 2025-04-01T05:16:56.405Z
- **Views**: 91
- **Replies**: 7
- **Likes**: 1
- **Tags**: clarification, diploma-level, tds-project-1

## Original Post
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-01T05:16:56.562Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1

Sir,

The License file is present in the github repository however i received a mail that said that it was absent.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub repository interface. It displays the file structure and commit history of a repository named "tds_project-1". The interface shows the main branch, along with options to add files, view code, and search within the repository.

**2. Any text content visible:**

*   **Repository Name:** tds\_project-1 (Public)
*   **Branch:** main, 1 Branch, 0 Tags
*   **Search Bar:** Go to file
*   **Buttons:** Add file, Code
*   **Commit Information:**
    *   22f3000585 Create LICENSE
    *   c61a6ef - now
    *   6 Commits
*   **File/Directory List:**
    *   \_pycache\_
    *   venv
    *   Dockerfile
    *   LICENSE
    *   MIT LICENSE
    *   app.py
    *   requirements.txt
    *   test.txt
*   **Commit Messages:**
    *   Final Submission
    *   First submission
    *   Create LICENSE
    *   Rename LICENSE to MIT LICENSE
*   **Time Since Last Commit:**
    *   now
    *   2 months ago (repeated for several files)
*   **Other:** Pin, Unwatch

**3. The context or purpose of what's displayed:**

The image shows the contents of a GitHub repository, likely a Python project. It allows users to browse the files, view commit history, and contribute to the project. The presence of files like "app.py", "requirements.txt", and "Dockerfile" suggests a Python application that can be containerized. The LICENSE and MIT LICENSE files indicate the project's licensing.

**4. Technical details (based on the file names):**

*   **\_pycache\_:** This is a directory automatically created by Python to store compiled bytecode files.
*   **venv:** This is a Python virtual environment, used to isolate project dependencies.
*   **Dockerfile:** This file contains instructions for building a Docker image, allowing the application to be run in a containerized environment.
*   **app.py:** This is likely the main Python application file.
*

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

The image displays the results of an automated check for a project submission. The system verifies if certain requirements are met before the submission can be fully evaluated. The checks focus on the presence and accessibility of key components like a Docker image, a GitHub repository, a Dockerfile, and an MIT license. The final "Prerequisites: FAIL" and "Project 1 Score: 0" indicate that the submission did not meet all the necessary requirements and therefore received a score of zero.

**4. Technical Details:**

The checks are related to software development and deployment practices.

*   **Docker image:** Docker is a platform for containerizing applications. The check verifies if a Docker image is available on Docker Hub (a public registry) and is publicly accessible.
*   **GitHub repo:** GitHub is a popular platform for version control and collaboration. The check verifies if a GitHub repository exists and is publicly accessible.
*   **Dockerfile:** A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. The check verifies if a Dockerfile is present in the root directory of the GitHub repository.
*   **MIT license:** The MIT License is a permissive free software license. The check verifies if an MIT license file is present in the root directory of the GitHub repository.

The fact that the MIT license check failed is the reason for the overall "Prerequisites

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.

Can you please look into it. Thankyou!

---

## Reply 1
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-01T20:57:59.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/3

Hi @22f3000585

Standard MIT License naming criteria is to be named as LICENSE or LICENSE.md(all caps).

[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

Kind regards

---

## Reply 2
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-02T04:12:14.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/4

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based notification or message, likely from an automated system. It indicates that a submission (presumably code or a project) has failed.

**2. Text Content:**

The text content is as follows:

*   "We see that your submission [URL] has a result of FAIL due to the below reasons:"
*   "No such repo; No "MIT" in LICENSE; No Dockerfile"

**3. Context and Purpose:**

The context is likely a code submission or project evaluation system. The purpose of the message is to inform the user that their submission has failed and to provide specific reasons for the failure. The URL is a link to the submitted project on GitHub.

**4. Technical Details:**

*   The URL `https://github.com/22f3000585/tds_project-1.git` suggests that the submission is a Git repository hosted on GitHub.
*   The reasons for failure indicate that:
    *   "No such repo" means the repository at the given URL could not be found.
    *   "No "MIT" in LICENSE" means that the LICENSE file in the repository does not contain the string "MIT", suggesting that the project is not licensed under the MIT license.
    *   "No Dockerfile" means that the repository does not contain a Dockerfile, which is a file used to automate the creation of a container image for deploying the application.

Sir, this is why i renamed it to ‘MIT LICENSE’.

Sir can you please consider it. Thank you!

---

## Reply 3
**Author**: PalakAnand
**Posted**: 2025-04-02T11:20:10.590Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/5

Same here. I also added and saved the file as MIT license because of the following message. I request you to please consider evaluating the project.

**Image: Screenshot 2025-04-02 at 4.49.23 PM**
Here's a detailed description of the image:

**1. Content Overview:**

The image contains text, likely part of a submission guideline or feedback for a coding project or assignment. It outlines specific requirements and considerations for submissions.

**2. Text Content:**

*   **"No "MIT" in LICENSE; No Dockerfile"**: This suggests a checklist item or a requirement that the submission should not include the "MIT" license or a Dockerfile.
*   **"Please ensure that your submission passes the above checklist for it to be even considered for scoring."**: This is a clear instruction emphasizing the importance of meeting the specified criteria for the submission to be evaluated.
*   **"Note: We've only considered your latest submissions, as we permitted students to submit more than once."**: This is a note clarifying that only the most recent submission from each student will be considered, even though multiple submissions were allowed.

**3. Context and Purpose:**

The content suggests that this is part of a feedback or instruction set for a coding assignment or project. The "checklist" likely refers to a set of requirements that submissions must meet. The note about "latest submissions" indicates that students were allowed to submit multiple times, but only the most recent one will be graded.

**4. Technical Details (Inferred):**

*   The mention of "LICENSE" and "Dockerfile" implies that the project involves software development.
*   The "MIT" license is a common open-source license. The instruction to avoid it might be due to specific requirements of the assignment or project.
*   A "Dockerfile" is used for creating containerized applications using Docker. Its absence might be a requirement or a consequence of the project's design.

---

## Reply 4
**Author**: Carlton D'Silva
**Posted**: 2025-04-02T15:04:59.106Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/6

@24ds2000125 @22f3000585

I completely appreciate that you feel these are minor issues.

But the team has decided that we cannot allow students to make changes to their repos. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

Unfortunately we cannot allow submissions that fail the prerequisites.

Changing it now will not suddenly make it eligible.

These things do matter when done at scale.  Its an important lesson Anand wants students to understand. These “minor” things matter.

Its a bit like assembling a rocket and forgetting the checklist for the pilot. Minor detail, costs Rs 2, but the rocket cannot leave without it.

We had a significant discussion about it internally. For the sake of fairness to everyone who got it right, we cannot allow edits after the Project deadline. It makes the prerequisites meaningless, especially when it was clearly stressed upon in the sessions and the Project page.

I know you will feel very disappointed but it is the decision the team has made and I have shared the reasons why.

Kindest regards

---

## Reply 5
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-02T15:20:45.985Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/7

Sir,

Thankyou for your prompt reply to my query.

I wanted to let you know that i had made change of ‘LICENSE’ to ‘MIT LICENSE’ on the 16th of Feb itself as that was the day that i had received the mail and because I saw that the submission date had been extended by one day(i.e the 16th of Feb itself).

I completely understand what you are trying to convey but that was the sole reason i made that change on the 16th.

I completely respect your decision but if there is even a slight possibility that you consider it (only because I did it on the 16th) I would highly appreciate it.

Thankyou!

---

## Reply 6
**Author**: Carlton D'Silva
**Posted**: 2025-04-02T15:55:00.653Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/8

One thing we are doing is looking at the latest commit before the 18th of Feb. So if it was correct before the 18th of Feb then we will consider it and evaluate it, but it has to be precisely what is expected. If so, then your submission will be evaluated by building the image from the docker manifest in the github present at the version before the 18th.

---

## Reply 7
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-02T16:02:57.956Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/9

Well noted sir. Thanks a lot!

---

## Reply 8
**Author**: Reva Lakshmy Paul
**Posted**: 2025-04-06T13:59:53.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/10

Sir, I received the mail today -

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a list of prerequisite checks, likely from a software development or deployment process. Each check is a statement about the existence and properties of repositories (Docker and GitHub) and files within a GitHub repository. The result of each check is indicated by a "1" for pass or "0" for fail.

**2. Text Content:**

The text content is as follows:

*   **Pre-requisites check: (1 for pass, 0 for fail)**
*   Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo check - LICENSE or LICENSE.md file exists (MIT License): 0
*   Github repo check - Dockerfile exists: 1

**3. Context and Purpose:**

The purpose of this display is to show the status of necessary conditions before a process can proceed. It's a form of validation or pre-flight check. The checks ensure that the required repositories exist, are publicly accessible, and contain specific files (LICENSE and Dockerfile). The timestamp check suggests a requirement for the repositories to have been created or updated before a certain date (February 18th).

**4. Technical Details:**

*   **Repositories:** The checks involve Docker and GitHub repositories, indicating a project that likely uses containerization (Docker) and version control (GitHub).
*   **Public Repositories:** The requirement for public repositories suggests that the project or its components are intended to be accessible to a wider audience.
*   **Timestamp:** The timestamp requirement (before February 18th) could be related to a deadline, a specific version of the code, or a point in time when certain configurations were established.
*   **LICENSE File:** The check for a LICENSE or LICENSE.md file (specifically mentioning MIT License) indicates that the project is intended to be open-source and uses the MIT license.
*   **Dockerfile:** The check for a Dockerfile confirms that the project is containerized using Docker.
*   **Pass/Fail:** The "1" and "0" values represent boolean results, where "1" means the condition is met (pass) and "0

Sir, I had already added the LICENSE and changed it to’MIT LICENSE’ due to this reason before the deadline itself.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of text, likely from a web page or application, that provides feedback on a submission. The feedback indicates that the submission has failed.

**2. Any text content visible:**

The text content is as follows:

*   "We see that your submission [https://github.com/22f3000585/tds\_project-1.git](https://github.com/22f3000585/tds_project-1.git) has a result of FAIL due to the below reasons:"
*   "No such repo; No "MIT" in LICENSE; No Dockerfile"

**3. The context or purpose of what's displayed:**

The context is likely an automated submission system, possibly for a coding assignment or project. The system has checked a submitted GitHub repository and found issues that caused the submission to fail. The reasons for failure are:

*   "No such repo": The repository at the provided URL might not exist or is inaccessible.
*   "No "MIT" in LICENSE": The system is likely checking for the presence of the MIT license in a file named "LICENSE" within the repository. The license is either missing or doesn't contain the string "MIT".
*   "No Dockerfile": The repository is missing a Dockerfile, which is a file containing instructions for building a Docker image.

**4. Technical details:**

*   The URL `https://github.com/22f3000585/tds_project-1.git` suggests that the submission is a Git repository hosted on GitHub. The "22f3000585" part is likely a username or organization name, and "tds\_project-1" is the repository name.
*   The mention of "Dockerfile" indicates that the project might involve containerization using Docker.
*   The check for "MIT" in the LICENSE file suggests that the system requires the project to be licensed under the MIT license.

Sir,the rest of my prerequistes are working well.Can you please check as due to this my project has also not been evaluated.The MIT LICENSE file was already present in the github repo as I submitted my project’s github repo in the google form that was provided.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a version control system like Git, specifically a repository browser. It displays a list of files and directories within a project, along with information about their last modification or commit.

**2. Text Content:**

The image contains the following text:

*   **22f3000585 Create LICENSE:** This is likely a commit identifier and a brief description of the commit.
*   **c61a6ef . 5 days ago:** This is a shortened commit hash and the time since the last commit.
*   **6 Commits:** Indicates the total number of commits in the repository.
*   **_pycache_:** A directory name.
*   **venv:** A directory name.
*   **Dockerfile:** A file name.
*   **LICENSE:** A file name.
*   **MIT LICENSE:** A file name.
*   **app.py:** A file name.
*   **requirements.txt:** A file name.
*   **test.txt:** A file name.
*   **Final Submission:** A commit message.
*   **First submission:** A commit message.
*   **Create LICENSE:** A commit message.
*   **Rename LICENSE to MIT LICENSE:** A commit message.
*   **2 months ago:** Indicates the time since the last modification of a file or directory.
*   **5 days ago:** Indicates the time since the last modification of a file or directory.

**3. Context and Purpose:**

The image displays the contents of a software repository. It allows users to browse the files and directories, see when they were last modified, and view the commit history. This is a standard feature of version control systems like Git, often accessed through web-based interfaces like GitHub, GitLab, or Bitbucket.

**4. Technical Details:**

*   The presence of `_pycache_`, `venv`, and `.py` files suggests that the project is likely written in Python.
*   `requirements.txt` indicates that the project uses Python packages managed by pip.
*   `Dockerfile` suggests that the project is containerized using Docker.
*   The presence of `LICENSE` and `MIT LICENSE` indicates that

Sir can you please check.

Thankyou

---
