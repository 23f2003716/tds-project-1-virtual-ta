# Sudo permission needed to create data folder in root?

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1

## Topic Metadata
- **ID**: 167072
- **Slug**: sudo-permission-needed-to-create-data-folder-in-root
- **Created**: 2025-02-14T03:57:16.661Z
- **Views**: 44
- **Replies**: 0
- **Likes**: 0
- **Tags**: clarification

## Original Post
**Author**: Vikram Suriyanarayanan
**Posted**: 2025-02-14T03:57:16.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1

@Jivraj @carlton sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?

needs sudo permission all the time…

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, likely running on a Linux or Unix-like system. It displays command-line interactions.

**2. Any text content visible:**

*   **Title Bar:** "Professionals Corner" (partially visible)
*   **User Prompt:** `vikramjncasr@ANJANEYA:/mnt/c/IIT_Madras/TDS_Project_1$`
*   **Commands:**
    *   `sudo rm -rf /data` (partially visible)
    *   `ls /`
*   **Output of `ls /`:** A list of directories in the root directory (`/`). These include:
    *   `bin`
    *   `boot`
    *   `etc`
    *   `init`
    *   `lib.usr-is-merged`
    *   `lost+found`
    *   `mnt`
    *   `proc`
    *   `run`
    *   `sbin.usr-is-merged`
    *   `srv`
    *   `tmp` (highlighted in green)
    *   `var`
    *   `bin.usr-is-merged`
    *   `dev`
    *   `home`
    *   `lib`
    *   `lib64`
    *   `media`
    *   `opt`
    *   `root`
    *   `sbin`
    *   `snap`
    *   `sys`
    *   `usr`

**3. The context or purpose of what's displayed:**

The image shows a user (`vikramjncasr`) working in a terminal environment. The user is currently in the `/mnt/c/IIT_Madras/TDS_Project_1` directory. The user has executed the `ls /` command, which lists the contents of the root directory. The highlighted `tmp` directory suggests the user might be focusing on temporary files or directories. The partially visible `sudo rm -rf /data` command indicates a potentially dangerous operation involving deleting data.

**4. Technical details:**

*   The terminal uses a dark color

---

## Reply 1
**Author**: Carlton D'Silva
**Posted**: 2025-02-14T04:53:36.939Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2

Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py

Inside the docker container, permission for the data folder is set by the Dockerfile

which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

You create your application server that serves 2 endpoints on localhost:8000
You create a docker image that runs this application server.
You run the docker image using podman as described in the project page.
For mimicking the testing conditions. You need two files:

evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.

Kind regards

---
