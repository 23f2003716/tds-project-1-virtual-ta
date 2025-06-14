# Why Failed?

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/1

## Topic Metadata
- **ID**: 171672
- **Slug**: why-failed
- **Created**: 2025-04-03T10:44:03.220Z
- **Views**: 121
- **Replies**: 3
- **Likes**: 0
- **Tags**: miscellaneous

## Original Post
**Author**: Viraj Pitale
**Posted**: 2025-04-03T10:44:03.443Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/1

**Image: Screenshot 2025-04-03 161302**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a text-based email or notification, likely related to a project submission for a course or assignment. It outlines prerequisite checks for "Project 1" and provides an evaluation of whether those prerequisites have been met.

**2. Text Content:**

The text content can be broken down as follows:

*   **Greeting:** "Dear Learner,"
*   **Project Requirements:**
    *   "Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:" (The "TDS Project 1: Evaluation" is a hyperlink)
    *   A numbered list of 5 prerequisites:
        1.  "Your GitHub repository exists and is publicly accessible"
        2.  "Your GitHub repository has a LICENSE file with the MIT license"
        3.  "Your GitHub repository has a valid Dockerfile"
        4.  "Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME"
        5.  "Your Docker image uses the same Dockerfile as in your GitHub repository"
    *   "If you fail to meet this minimum requirement your submission will not get evaluated."
*   **Evaluation Results:**
    *   "These are your Project 1 Prerequisite evaluations:"
    *   A list of checks and their status (PASS or FAIL):
        *   "Is Docker image present in dockerhub AND is public: PASS"
        *   "Is Github repo present AND public: PASS"
        *   "Is Dockerfile present in root of github repo: PASS"
        *   "Is MIT license present at root of github repo: FAIL"
    *   "Prerequisites: FAIL"
    *   "Project 1 Score: 0"

**3. Context and Purpose:**

The purpose of the email is to inform the "Learner" about the prerequisites for Project 1 and to provide feedback on whether their submission meets those requirements. The email indicates that the project will not be evaluated if the prerequisites are not met. The evaluation results show that the learner has failed to meet all the prerequisites, specifically the requirement

[virajpitale/tds-project1](https://github.com/virajpitale/tds-project1)

on github you can clearly see i added mit license still it is showing failed

---

## Reply 1
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-04-03T10:47:22.621Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/2

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a GitHub Docs page. It shows a tutorial or guide on how to add a license to a repository. The screenshot includes UI elements from the GitHub website, specifically the file creation interface within a repository. It also includes numbered instructions explaining the steps.

**2. Any text content visible:**

*   **Page Title/URL:** `https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a...`
*   **GitHub Docs**
*   **Version:** Free, Pro, & Team
*   **Breadcrumbs:** Building communities / Healthy contributions / Add a license to a repo
*   **File Navigation:**
    *   `main` (branch dropdown)
    *   `Q Go to file`
    *   `.devcontainer`
    *   `.github`
*   **File List:**
    *   `octocat Delete test.md`
    *   `Name`
    *   `Last commit message`
    *   `Last commit date`
*   **Instructions:**
    *   `3 In the file name field, type LICENSE or LICENSE.md (with all caps).`
    *   `4 Under the file name, click Choose a license template.`
    *   `octo-repo/ LICENSE`
    *   `in main`
    *   `Edit`
    *   `Preview`
    *   `Choose a license template`
    *   `1 Enter file contents here`
    *   `5 On the left side of the page, under "Add a license to your project," review the available licenses, then select a license from the list.`
    *   `6 Click Review and submit.`
*   **In this article:**
    *   `Including an open sou`
    *   `Further reading`

**3. The context or purpose of what's displayed:**

The image is part of a tutorial on the GitHub Docs website. The purpose is to guide users through the process of adding a license file (LICENSE or LICENSE.md) to their GitHub repository. The instructions are numbered to provide a step-by-step

I checked your github repo MIT License file is named as `Licenese.md` but standard naming for License is LICENSE or LICENSE.md (with all caps).

---

## Reply 2
**Author**: Viraj Pitale
**Posted**: 2025-04-03T11:00:47.042Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/3

So, should I edit the filename now, or will you count it as missing?

---

## Reply 3
**Author**: Viraj Pitale
**Posted**: 2025-04-03T12:27:21.792Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/4

@Jivraj please reply

---

## Reply 4
**Author**: Viraj Pitale
**Posted**: 2025-04-07T12:15:01.305Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/why-failed/171672/5

**Image: Screenshot 2025-04-07 174256**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a user interface (UI) element, specifically a commit history log, likely from a version control system like Git, visualized through a platform like GitHub or GitLab. It shows a series of commits to a repository, grouped by date.

**2. Any text content visible:**

*   **Date Headers:** "Commits on Apr 3, 2025", "Commits on Feb 17, 2025", "Commits on Feb 15, 2025"
*   **Commit Messages:**
    *   "Rename License.md to LICENSE.md"
    *   "Update License.md"
    *   "Update and rename README.md to License.md"
    *   "project"
*   **Author Information:**
    *   "virajpitale authored 4 days ago"
    *   "virajpitale authored on Feb 17"
    *   "virajpitale authored on Feb 15"
    *   "virajpitale committed on Feb 15"
*   **Verification Status:** "Verified" (appears next to each commit)
*   **Commit Hashes:** "d62d2ee", "762400b", "26f75aa", "c94aac6"
*   **Icons:** There are icons for copying the commit hash and viewing the commit details.

**3. The context or purpose of what's displayed:**

The purpose is to provide a chronological view of changes made to a software project. Each entry represents a commit, showing the author, date, commit message (describing the change), and a unique identifier (the commit hash). The "Verified" status likely indicates that the commits are signed and can be trusted.

**4. Technical details if it's a code screenshot or technical diagram:**

*   The image is not a code screenshot or technical diagram. It's a UI representation of Git commit history.
*   The commit hashes (e.g., "d62d2ee") are hexadecimal strings, which are typical for Git commit identifiers.
*   The UI elements (buttons, icons, labels) are designed to allow users

I submitted the project **within the deadline**, and I ensured that **all requirements were fulfilled**, including correctly adding the MIT License file. The license file was named properly and contained the correct content.

However, I received a message stating that the MIT License was not present, and that the prerequisites were not completed — resulting in a failed status. This is surprising and feels unfair, as I’ve double-checked my submission and confirmed that everything, including the license file, is in place and named correctly.

Here is my GitHub repo for your reference: [GitHub - virajpitale/tds-project1](https://github.com/virajpitale/tds-project1)

I kindly request a re-evaluation of my submission, as I believe I’ve met all the required criteria. I would really appreciate your time in looking into this matter again.

Thank you for your understanding.

@Jivraj

---
