# GA1 - Development Tools - Discussion Thread [TDS Jan 2025]

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/1

## Topic Metadata
- **ID**: 161083
- **Slug**: ga1-development-tools-discussion-thread-tds-jan-2025
- **Created**: 2025-01-02T02:30:03.518Z
- **Views**: 1556
- **Replies**: 80
- **Likes**: 40
- **Tags**: announcement, term1-2025, week-1, graded-assignment

## Original Post
**Author**: Anand S
**Posted**: 2025-01-02T02:30:03.720Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/1

Please post any questions related to [Graded Assignment 1 - Development Tools](https://exam.sanand.workers.dev/tds-2025-01-ga1).

Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through Discourse Docs!  :slight_smile: 

Deadline: 26 Jan 2025, midnight IST

@carlton @Jivraj Please keep an eye on this thread for support.

---

## Reply 1
**Author**: Anand S
**Posted**: 2025-01-02T02:46:01.490Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/2

*No content*

---

## Reply 2
**Author**: Anant Kumar Singh
**Posted**: 2025-01-05T04:01:42.024Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/3

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows text content, likely part of a question or instructions within a larger document or online platform. It includes instructions for downloading and using a file, renaming files, and a question about the output of a bash command.

**2. Any text content visible:**

The text content is as follows:

*   "16 Move and rename files (0.5 marks)"
*   "Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next (i.e. a19b.txt becomes a20b.txt)"
*   "What does running grep . * | LC_ALL=C sort | sha256sum in bash on that folder show?"

**3. The context or purpose of what's displayed:**

The content appears to be part of a programming or scripting assignment or exercise. It involves file manipulation, renaming, and understanding the output of a bash command. The "(0.5 marks)" suggests it's a graded component.

**4. Technical details:**

*   **File Manipulation:** The instructions involve downloading a zip file ("q-move-rename-files.zip"), extracting it, and using the `mv` command (a standard Unix/Linux command for moving files or directories).
*   **File Renaming:** The instructions specify a renaming scheme where each digit in a filename is replaced with the next digit (e.g., '1' becomes '2', '9' becomes '0').
*   **Bash Command:** The question asks about the output of the following bash command:
    `grep . * | LC_ALL=C sort | sha256sum`
    *   `grep . *`: This part uses `grep` to find all lines in all files in the current directory that contain at least one character.
    *   `LC_ALL=C sort`: This sorts the output of `grep` using the "C" locale, which ensures consistent sorting behavior.
    *   `sha256sum`: This calculates the SHA256 checksum of the sorted output.

In summary, the image presents a task involving file manipulation, renaming, and understanding the output of

For question 16 of GA1, It says "Rename all files replacing each digit with the next "

Accepted answer is working only if file names are renamed as

2h3q9x.txt → 3h4q0x.txt

eb209nmlca.txt → eb310nmlca.txt

That means if digit is 9 then next digit should be 0. @carlton @Jivraj let me know if this is what is expected. since 9->10 or 209 → 210 is not working

---

## Reply 3
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-05T05:50:28.537Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/4

Hi anant,

Question mentions every digit should be replaced by next one.

In that case 209 would get replaced by 310

---

## Reply 4
**Author**: Anant Kumar Singh
**Posted**: 2025-01-05T07:56:17.410Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/5

Hello Sir, When I am following that logic to rename files, assessment check is giving error “Incorrect. Try again.”

---

## Reply 5
**Author**: Carlton D'Silva
**Posted**: 2025-01-08T03:45:23.020Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/6

@21f2000370 Since you have managed to get all the answers correct, I presume there are no further issues w/ Q16.

---

## Reply 6
**Author**: Nihar Panse
**Posted**: 2025-01-09T07:32:49.658Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/7

Hi, I am unable to access Graded Assignment 1. Every time I click on the given link, all I can see is this page. Please advise.

**Image: tdsga1**
Here's a detailed description of the image:

1.  **UI Elements:** The image appears to be a screenshot of a webpage or document related to an online course or assignment. It contains text elements and likely represents the introduction or instructions for a graded assignment.

2.  **Text Content:**
    *   **Title:** "Tools in Data Science - Graded Assignment 1"
    *   **Section Header:** "Deadline:"
    *   **Note:** "Every page reload randomizes the quiz. So don't copy answers from previous attempts. You can submit multiple times."

3.  **Context/Purpose:** The image likely serves as an introduction to a graded assignment within a "Tools in Data Science" course. It informs students about the assignment's deadline and provides a crucial note regarding the quiz format. The note indicates that the quiz questions are randomized upon each page reload, discouraging students from copying answers from previous attempts. It also clarifies that multiple submissions are allowed.

4.  **Technical Details:** There are no code snippets or technical diagrams in the image. The text is presented in a clean, straightforward manner, suggesting a simple webpage or document format. The note about the quiz randomization implies that the quiz is likely delivered through an online platform with dynamic question generation.

---

## Reply 7
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-09T08:21:13.611Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/8

Possible reasons for this issue.

Disable/remove Ad blocker
Disable/remove Tracking blocker (Allow third party cookies)
Use Chrome browser
Disable Browser extensions

---

## Reply 8
**Author**: Anant Kumar Singh
**Posted**: 2025-01-11T08:15:14.939Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/12

As I highlighted earlier, Its not accepting the answer  if I follow correct logic for renaming for example 209->210, but it is accepting if rename as 209->310

---

## Reply 9
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-11T09:03:17.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/13

Hi Anant,

 21f2000370:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows text content, likely part of an assignment or instructions. It includes instructions for downloading and using a file, renaming files, and running a command in bash.

**2. Text Content:**

The text content is as follows:

*   "16 Move and rename files (0.5 marks)"
*   "Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next (i.e. a19b.txt becomes a20b.txt)"
*   "What does running grep . \* | LC\_ALL=C sort | sha256sum in bash on that folder show?"

**3. Context and Purpose:**

The content appears to be a task or question related to file manipulation and command-line usage. It involves:

*   Downloading and extracting a zip file.
*   Using the `mv` command to move files.
*   Renaming files based on a specific rule (replacing digits).
*   Understanding the output of a bash command pipeline involving `grep`, `sort`, and `sha256sum`.

**4. Technical Details:**

*   **`q-move-rename-files.zip`:** This is the name of a zip file that needs to be downloaded and extracted. It likely contains files and folders for the task.
*   **`mv`:** This is a command-line utility used to move files or directories.
*   **`a19b.txt` becomes `a20b.txt`:** This provides an example of the renaming rule: each digit in the filename is replaced with the next digit.
*   **`grep . * | LC_ALL=C sort | sha256sum`:** This is a bash command pipeline:
    *   `grep . *`: This uses `grep` to find all lines in all files in the current directory.
    *   `LC_ALL=C sort`: This sorts the output of `grep` using the C locale.
    *   `sha256sum`: This calculates the SHA256 checksum of each line of the sorted output.

The question asks what

Here in question, it’s mentioned to replace every digit with next digit, that’s why 209 would be 310.

---

## Reply 10
**Author**: Suhani Dubey
**Posted**: 2025-01-11T14:56:07.023Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/14

In attempting the third question, I’m unable to download the npm package as it requires docker. When trying to install docker from the installer, it freezes in the verifying package stage. Can somebody please help solve my problem?

@carlton @Jivraj

---

## Reply 11
**Author**: Hisham Kadambot
**Posted**: 2025-01-11T15:48:35.599Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/15

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely part of an interactive coding tutorial or challenge. It presents a question related to CSS selectors and data attributes. There's a text prompt, a label, and an input field for the user to enter their answer.

**2. Any text content visible:**

*   "Let's make sure you know how to select elements using CSS selectors. Find all ``s having a `foo` class in the hidden element below. What's the sum of their `data-value` attributes?"
*   "Sum of data-value attributes:"

**3. The context or purpose of what's displayed:**

The context is a coding exercise designed to test the user's understanding of CSS selectors and how to access data attributes in HTML elements. The user is expected to inspect a hidden HTML element (not visible in the image), identify all `` elements with the class "foo", extract the values of their `data-value` attributes, sum those values, and enter the result in the input field.

**4. Technical details:**

*   The question specifically mentions CSS selectors, `` elements, the "foo" class, and `data-value` attributes. This indicates the exercise involves HTML and CSS.
*   The use of backticks (`) around ``, `foo`, and `data-value` suggests these are code snippets or keywords.
*   The input field suggests the user needs to calculate a numerical value.
*   The presence of a red border around the input field and an exclamation mark icon indicates a potential error or that the user has not yet provided a correct answer.

Which HTML content we want to take?

---

## Reply 12
**Author**: Carlton D'Silva
**Posted**: 2025-01-11T17:45:23.526Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/17

Hi Suhani,

npm does not require docker.

Kind regards

---

## Reply 13
**Author**: Carlton D'Silva
**Posted**: 2025-01-11T17:48:02.553Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/18

Hi Hisham,

Its described in the question. There is a hidden element hiding somewhere after that question. You would have to inspect the DOM to find it.

---

## Reply 14
**Author**: Mishkat Chougule
**Posted**: 2025-01-11T17:02:23.063Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/19

**Image: Screenshot 2025-01-11 at 10.29.41 PM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser window displaying a web page that appears to be part of an online assignment or course. The page focuses on CSS selectors. There's also a download notification pop-up from the browser.

**2. Text Content:**

*   **Browser Tab Titles:**
    *   "Graded Assignment 1 :: IITM C"
    *   "TDS 2025 Jan GA1 - Develop"
    *   "Latest Courses/Tools in Data"
    *   "Beginner's Guide to the Bash"
*   **URL:** "exam.sanand.workers.dev/tds-2025-01-ga1"
*   **Assignment Details:** "Due Sun, 26 Jan, 2025, 11:59 pm IST Score: 8.75 / 10 Check Save"
*   **Content:**
    *   "The Mozilla Developer Network (MDN) provides detailed documentation on the three main types of selectors:"
    *   "Basic CSS selectors: Learn about element (div), class (.container), ID (#header), and universal (\*) selectors"
    *   "Attribute selectors: Target elements based on their attributes or attribute values ([type="text"])"
    *   "Combinators: Use relationships between elements (div > p, div + p, div ~ p)"
    *   "Practice your CSS selector skills with this interactive tool:"
    *   "CSS Diner: A fun game that teaches CSS selectors through increasingly challenging levels"
    *   "Let's make sure you know how to select elements using CSS selectors. Find all s having a foo class in the hidden element below. What's the sum of their data-value attributes?"
    *   "Sum of data-value attributes:"
    *   "482"
    *   "Incorrect. Try again."
    *   "Process files with different encodings (1 mark)"
*   **Download Notification:**
    *   "q-unicode-data.zip Removed"
    *   "README (1).md Removed"
    *   "Book 2(Sheet1).csv Removed"
    *

@s.anand  please guide me through this question, my answer is showing incorrect

---

## Reply 15
**Author**: Manmeet Kaur
**Posted**: 2025-01-12T07:45:04.116Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/20

Hello Sir. I am unable to install uv in my windows system. Whenever I run the code provided at the reference link in Powershell, my anti-virus system sends a message that it was blocked. Even after blocking Real-time security, uv does not display. What am I doing wrong?

---

## Reply 16
**Author**: Samra Ahmed 
**Posted**: 2025-01-12T11:13:59.536Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/21

Hi, I’m unable to view assignments. below is the screenshot for your reference.

**Image: Screenshot 2025-01-12 150511**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a standard web browser error page. It indicates that the website the user was trying to access is currently unavailable. The page includes a broken document icon at the top, a main error message, suggestions for troubleshooting, an error code, and buttons for reloading the page or viewing details.

**2. Text Content:**

*   **"This site can't be reached"** - The main error message.
*   **"exam.sanand.workers.dev unexpectedly closed the connection."** - Specifies the website that is unreachable and the reason for the error.
*   **"Try:"** - Introduces a list of troubleshooting suggestions.
*   **"Checking the connection"** - First suggestion for troubleshooting.
*   **"Checking the proxy and the firewall"** - Second suggestion for troubleshooting.
*   **"Running Windows Network Diagnostics"** - Third suggestion for troubleshooting.
*   **"ERR\_CONNECTION\_CLOSED"** - The specific error code.
*   **"Reload"** - A button to refresh the page.
*   **"Details"** - A button to view more information about the error.

**3. Context/Purpose:**

The purpose of this page is to inform the user that the website they are trying to access is currently unavailable. It provides potential reasons for the error and suggests troubleshooting steps the user can take to resolve the issue.

**4. Technical Details:**

*   The error code "ERR\_CONNECTION\_CLOSED" indicates that the connection to the server was unexpectedly closed. This could be due to a problem with the server, the network connection, or the user's browser.
*   The troubleshooting suggestions point to common causes of connection problems, such as network connectivity issues, proxy server problems, or firewall interference.
*   The website address "exam.sanand.workers.dev" suggests that this is a development or testing environment, possibly using Cloudflare Workers (indicated by "workers.dev").

Please suggest me a way to view it. I have allowed third-party cookies as well.

Thanks

---

## Reply 17
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-12T21:29:25.964Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/23

Hi manmeet,

I don’t know about solution to this.

Some network setting might be causing problem.

Alternatively you can make use of GitHub codespaces which provides 120 hours of free run time in a month. With GitHub codespaces you can use Ubuntu os, and visually it gives you feel of vs code. You can also active your GitHub student developer pack and get 180 hours of GitHub codespaces and some more benefits such as cloud resources and domains.

I have done all questions of week1 and week2 on codespaces only, codespaces works very well if you have good internet connection.

---

## Reply 18
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-12T21:32:38.881Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/24

Hi samra,

Try installing some other browser see if that works.

---

## Reply 19
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-12T21:34:19.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/25

Hi mishkat,

Without sharing code, can you pls share your approach how you are trying to solve this question.

---

## Reply 20
**Author**: Manmeet Kaur
**Posted**: 2025-01-13T00:51:15.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/26

Ok, thanks. I turned off many security features including anti-virus system’s security and windows security options etc. Then it allowed me to download uv on the system. Now it is running, and I got output as json for Q2.

---

## Reply 21
**Author**: Nelson Jochim DSouza
**Posted**: 2025-01-13T06:35:28.617Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/27

2 days ago I  attempted TDS 2025 Jan GA1 - Development Tools and scored 8.5. I didn’t submit as I wanted to attempt incorrect answer questions.

When I logged in today it says score is 0.

Shall I submit or not? Do I have to attempt all questions again?

Why the assignment and submissions are two separate pages/links?

If [seek] ([Nptel Seekh](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002)) can access [TDS exam] ([Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga1)) then why we need to submit from seek?

---

## Reply 22
**Author**: Carlton D'Silva
**Posted**: 2025-01-13T07:21:41.338Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/28

The seek portal question is to confirm that the student has seen the GA. It does not actually give you a score. Otherwise students sometimes claim that they looked and did not find any GAs (this has happened in the past). Hence the two stage verification. You still need to 

**Image: Screenshot 2025-01-13 at 12.50.02**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, specifically a button.

**2. Any text content visible:**

The button contains the text "Save".

**3. The context or purpose of what's displayed:**

The button is likely intended to allow a user to save data or changes within an application or website. It's a common UI element used to trigger a save operation.

**4. Technical details:**

*   **Color:** The button has a blue background.
*   **Border:** It has a rounded rectangular shape with a white border.
*   **Text:** The text "Save" is in white.
*   **Appearance:** The button has a slightly blurred or glowing effect around the text and border, suggesting a possible focus or hover state.

 the submissions to get a score for the GA.

The actual GA questions are on [https://exam.sanand.workers.dev/](https://exam.sanand.workers.dev/) via the seek portal or

on the [Tools in Data Science](https://tds.s-anand.net/#/) introduction page.

Its just a more robust way of ensuring that students have indeed viewed the GAs.

As far your submission goes, we have your last submission and the score.  :white_check_mark: 

We will check on our end why your submission has not reloaded into your browser.

Normally these are stored in session storage. So if your browser has deleted them, it might have not loaded from our back end server. @s.anand will be able to confirm the reason for this problem.

**For the time being if you are making a fresh submission, just fill in all the answers in again, so that your latest submission will be marked correctly.**

Kind regards

---

## Reply 23
**Author**: Nelson Jochim DSouza
**Posted**: 2025-01-13T07:43:26.594Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/29

Thanks @carlton.

I answered questions on [https://exam.sanand.workers.dev/](https://exam.sanand.workers.dev/) but didn’t click on the button “Submit Answers” on seek as my answers for 2 questions were incorrect.

My question is whether I need to submit on seek to save answers on Exam? (I checked my score and saved it on the exam site.)

---

## Reply 24
**Author**: Carlton D'Silva
**Posted**: 2025-01-13T09:05:08.554Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/30

Hi @Nelson

Your answers on the [exam](https://exam.sanand.workers.dev/) site that have been submitted will be saved and used as the basis for your score. Saying yes/no on seek does not materially impact scoring. Its just an awareness question. Even if you answered yes on the seek portal, you can still revise your answers on the exam site. The final submission is always whats locked in for the score (until the deadline passes).

Kind regards

---

## Reply 25
**Author**: Carlton D'Silva
**Posted**: 2025-01-13T09:26:22.507Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/31

It might be because you are not adding up the correct tags with attribute `data-value`. There may be other tags within the same DOM and having the attribute `data-value`.

Kind regards

---

## Reply 26
**Author**: Nelson Jochim DSouza
**Posted**: 2025-01-13T12:52:10.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/32

I am stuck with the last question. SQLite question.

It gives the error:

Error: Got [[121510.39]]...

Is it possible to have a more descriptive error? It’s a simple SQL query. I tried various options in my query. I didn’t succeed.  :thinking:

---

## Reply 27
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-13T13:53:22.401Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/33

Hi Nelson,

I checked your set of questions, you are using wrong query to get answer.

kind regards

---

## Reply 28
**Author**: Shouvik Roy 
**Posted**: 2025-01-13T15:55:39.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/34

@carlton @Jivraj

In this picture for the given question i have tried in python and chatgpt both are giving same answer still showing wrong. GA1 question

**Image: Neutral Minimal Photo Collage Mood Board Instagram Story**
Here's a detailed description of the image:

**1. UI Elements and Content:**

*   **Question/Prompt:** The image starts with a question: "How many Wednesdays are there in the date range 1986-08-09 to 2012-06-19?" This appears to be part of an assessment or coding challenge.
*   **User Input and Feedback:** There's a field where the user has entered "1349" as the answer. The feedback is "Incorrect. Try again." There's also a hint: "The dates are in the year-month-day format. Include both the start and end date in your count."
*   **Code Snippet:** A Python code snippet is displayed. It's designed to calculate the number of Wednesdays within the specified date range.
*   **Terminal Output:** A terminal window shows the output of running the Python code. It prints "Number of Wednesdays: 1349".
*   **AI Response:** An AI response is shown, answering the question "How many Wednesdays are there in the date range 1986-08-09 to 2012-06-19?" with "There are 1349 Wednesdays in the date range from August 9, 1986, to June 19, 2012."

**2. Text Content:**

*   **Question:** "How many Wednesdays are there in the date range 1986-08-09 to 2012-06-19?"
*   **User Input:** "1349"
*   **Feedback:** "Incorrect. Try again."
*   **Hint:** "The dates are in the year-month-day format. Include both the start and end date in your count."
*   **Python Code:**
    *   `from datetime import date, timedelta`
    *   `# Define the date range`
    *   `start_date = date(1986, 8, 9)`
    *   `end_date = date(2012, 6, 19)`
    *   `# Find the first Wednesday on or after the start_date`
    *   `current

---

## Reply 29
**Author**: Shouvik Roy 
**Posted**: 2025-01-13T16:09:20.419Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/35

@Jivraj @carlton

The same issue is happening in the question 12 of GA1. I have given the answer by using collab and gemini , its giving the proper result but showing wrong.

**Image: Minimal Square Photo Collage Photography Instagram Post**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a split screen. The left side shows a code editor (likely VS Code or a similar IDE) displaying a Python script. The right side shows a screenshot of a YouTube video. Below the code editor is a terminal window showing the output of the script.

**2. Text Content:**

*   **Python Code:** The Python code appears to be designed to read data from two CSV files and a TXT file, extract specific values based on symbols, and calculate a total sum. Key parts of the code include:
    *   File reading using `open()` in binary mode (`'rb'`) to detect encoding.
    *   Using the `chardet` library to detect the encoding of the files.
    *   Error handling for `FileNotFoundError` and `UnicodeDecodeError`.
    *   Splitting lines into symbol and value based on a comma delimiter.
    *   Checking if the symbol is in a list of target symbols (including '€' and ' ').
    *   Converting the value to a float and adding it to a `total_sum`.
    *   Printing the final `total_sum`.
*   **Terminal Output:** The terminal output shows prompts for the user to enter the paths to the CSV and TXT files. It also displays the final calculated sum: "The sum of all values associated with the specified symbols is: 31512.0".
*   **YouTube Video Screenshot:** The YouTube video screenshot shows a man (presumably the video creator) and the title "COMPUTER STUFF THEY DIDN'T TEACH YOU". Subtitles include "Code Pages, Character Encoding, Unicode, UTF-8 and the BOM PART 2".
*   **Video Description Snippet:** Below the video, there's a snippet of the video description:
    *   "Download and process the files in q-unicode-data.zip which contains three files with different encodings."
    *   "data1.csv: CSV file encoded in CP-1252"
    *   "data2.csv: CSV file encoded in UTF-8"
    *   "data3.txt: Tab-separated file encoded in UTF-16"
    *   "Each file has 2 columns: symbol and value

---

## Reply 30
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-13T16:09:33.840Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/36

Hi Shouvik,

Your code seems correct to me. I think there is an extra space before your answer in input box.

Btw instead of using a while loop, there is a much more optimal, which uses difference of dates and doesn’t require a loop at all. Try to figure it out.

kind regards

---

## Reply 31
**Author**: Shouvik Roy 
**Posted**: 2025-01-13T16:12:22.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/37

yeah thank you sir. now please say for the 2nd problem

---

## Reply 32
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-13T16:20:28.415Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/38

Try copy pasting exact symbols `— OR † OR €` Can you share code in code block, it’s difficult to read symbols that are present.

Also have a look at what `all_content` variable contains, see if there are some problem with content.

---

## Reply 33
**Author**: Shouvik Roy 
**Posted**: 2025-01-13T16:24:09.236Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/39

!pip install chardet==5.1.0  # Install the chardet library

import chardet
def read_files():
  """Gets two CSV files and one TXT file from the user and reads them.

  Returns:
    A tuple containing the contents of the three files.
  """
    # Get the file paths from the user.
  csv_file_1_path = input("Enter the path to the first CSV file: ")
  csv_file_2_path = input("Enter the path to the second CSV file: ")
  txt_file_path = input("Enter the path to the TXT file: ")

  # ... (Get file paths from user - same as before)

  # Read the CSV files.
  try:
    with open(csv_file_1_path, 'rb') as f:  # Open in binary mode
      rawdata = f.read()
      encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1:  # Use detected encoding
      csv_data_1 = csv_file_1.read()

    # Repeat for csv_file_2_path using the same pattern
    with open(csv_file_2_path, 'rb') as f:
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']
    with open(csv_file_2_path, 'r', encoding=encoding) as csv_file_2:
        csv_data_2 = csv_file_2.read()

  except FileNotFoundError:
    print("Error: One or both of the CSV files could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode one or both of the CSV files.")
    return None

  # Read the TXT file.
  try:
    with open(txt_file_path, 'rb') as f:  # Open in binary mode to detect encoding
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(txt_file_path, 'r', encoding=encoding) as txt_file:  # Open in text mode with detected encoding
        txt_data = txt_file.read() # Read the content of the file
  except FileNotFoundError:
    print("Error: The TXT file could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode the TXT file.")
    return None

  # Return the contents of the files.
  return csv_data_1, csv_data_2, txt_data

# Call the function to read the files.
file_contents = read_files()
if file_contents:
  csv_data_1, csv_data_2, txt_data = file_contents
  #print("Content of the first CSV file:\n", csv_data_1)
  #print("\nContent of the second CSV file:\n", csv_data_2)
  #print("\nContent of the TXT file:\n", txt_data)

  # Combine the content of all files into a single string
  all_content = csv_data_1 + csv_data_2 + txt_data

  # Split the content into lines
  lines = all_content.split('\n')

  # Initialize the total sum
  total_sum = 0

  # Iterate through each line
  for line in lines:
    # Split the line into symbol and value, handling potential extra spaces
    try:
      parts = line.strip().split(',')
      symbol = parts[0].strip()  # Remove leading/trailing spaces from symbol
      value = parts[1].strip()   # Remove leading/trailing spaces from value

      # Check if the symbol matches the criteria (using a more robust check)
      if symbol in ['€', 'ˆ', '’'  # Euro symbol variations
                     # Add any other known variations of the target symbols
                   ]:
        # Convert the value to a number and add it to the total sum
        total_sum += float(value)

    except (IndexError, ValueError):
      # Ignore lines with incorrect formatting or non-numeric values
      pass

  # Print the total sum
  print("The sum of all values associated with the specified symbols is:", total_sum)

---

## Reply 34
**Author**: Shouvik Roy 
**Posted**: 2025-01-13T16:28:28.341Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/40

i have given all the symbols correctly sir

---

## Reply 35
**Author**: Samra Ahmed 
**Posted**: 2025-01-13T18:44:00.191Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/41

Hi Jivraj,

I have tried with a different browser, but still not working. Below is the screenshot for your reference.

**Image: Screenshot 2025-01-13 224057**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a browser error page. It features a cartoon-like graphic at the top, followed by text indicating a network connection problem and a "Refresh" button.

**2. Any text content visible:**

*   **"Your connection was interrupted"** - This is the main error message.
*   **"A network change was detected."** - This provides a possible reason for the interruption.
*   **"ERR\_NETWORK\_CHANGED"** - This is a technical error code.
*   **"Refresh"** - This is the text on the button, suggesting a way to resolve the issue.

**3. The context or purpose of what's displayed:**

The image is a standard error message displayed by a web browser when it detects a change in the network connection while trying to load a webpage. This could be due to a temporary loss of internet connectivity, a change in the network the device is connected to (e.g., switching from Wi-Fi to cellular data), or a network configuration issue. The purpose is to inform the user about the problem and offer a potential solution (refreshing the page).

**4. Technical details:**

*   The error code "ERR\_NETWORK\_CHANGED" is a specific error code used by Chromium-based browsers (like Chrome and Edge) to indicate that the network connection has changed during the page loading process.
*   The presence of a "Refresh" button suggests that the browser believes the issue might be temporary and that reloading the page could resolve it.

Thanks

---

## Reply 36
**Author**: Nelson Jochim DSouza
**Posted**: 2025-01-14T05:16:52.135Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/42

One unicode character is in both UPPERCASE and lowercase. Do a case sensitive search.

---

## Reply 37
**Author**: Anand S
**Posted**: 2025-01-14T09:44:05.573Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/43

@Samra this is almost certainly due to a (typically corporate) firewall or antivirus. Please try with a personal laptop from a public / home network.

(I face this problem at office often. Once, our company’s firewall blocked our own company website  :confused: )

---

## Reply 38
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-14T11:29:34.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/44

Hi Nelson,

I checked with your dataset for this particular question. Using correct query I am able to get correct answer. Pls check sql query that you are using.

Kind regards

---

## Reply 39
**Author**: Siva Bhaskaran
**Posted**: 2025-01-14T14:09:51.502Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/45

What is the windows equivalent of sha256sum?

npx -y prettier@3.4.2 README.md | sha256sum.
sha256sum. : The term 'sha256sum.' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct 
and try again.
At line:1 char:35
+ npx -y prettier@3.4.2 README.md | sha256sum.
+                                   ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (sha256sum.:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

---

## Reply 40
**Author**: Samra Ahmed 
**Posted**: 2025-01-14T16:07:42.455Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/46

@s.anand Actually, I’m using a personal laptop. Is this country dependent or restricted?

---

## Reply 41
**Author**: Jayakrishnan
**Posted**: 2025-01-14T17:01:24.559Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/47

Check [this link from akamai](https://techdocs.akamai.com/download-ctr/docs/verify-checksum#:~:text=In%20a%20command%20line%2C%20run,in%20the%20Download%20Center%20interface.)

---

## Reply 42
**Author**: Jayakrishnan
**Posted**: 2025-01-14T17:16:08.652Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/48

Did you try the following:

`ping exam.sanand.workers.dev`
`tracert exam.sanand.workers.dev`

This is what I got while doing this:

ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms

tracert exam.sanand.workers.dev

Tracing route to exam.sanand.workers.dev [104.21.31.149]
over a maximum of 30 hops:

  1     2 ms     2 ms     2 ms  192.168.18.1
  2     5 ms     6 ms     4 ms  10.122.0.1
  3     *        *        6 ms  172.17.0.2
  4     5 ms     5 ms     4 ms  172.17.0.109
  5    16 ms     8 ms     8 ms  10.8.1.2
  6    21 ms     8 ms     8 ms  103.70.37.171
  7    10 ms     8 ms     8 ms  104.21.31.149

Trace complete.

You could also [try switching Google Public DNS](https://developers.google.com/speed/public-dns/docs/using) and see if the site is getting picked up in your next query.

Helpful Resources

[Ping+Tracert](https://www.okta.com/identity-101/ping-trace/#:~:text=Ping%20traceroute%20test.%20Traceroute%20is%20like%20a,takes%20them%20to%20get%20from%20each%20point.) for troubleshooting network connections
[Product pages](https://docs.nexthink.com/platform/user-guide/applications/managing-applications/configuring-web-applications/common-web-application-errors/err_network_changed) for `err_network_changed` error
[Network Troubleshooting](https://www.comptia.org/content/guides/a-guide-to-network-troubleshooting) skills and commands

---

## Reply 43
**Author**: Siva Bhaskaran
**Posted**: 2025-01-14T17:23:26.237Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/49

Thank you JK. I have another question. I should have asked that before this

npx -y prettier@3.4.2 README.md 
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/README.md - Not found
npm ERR! 404 
npm ERR! 404  'README.md@latest' is not in the npm registry.
npm ERR! 404 Your package name is not valid, because 
npm ERR! 404  1. name can no longer contain capital letters
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\sivab\AppData\Roaming\npm-cache\_logs\2025-01-14T17_22_04_622Z-debug.log
Install for [ 'README.md@latest' ] failed with code 1

This is throwing an error. Please help

---

## Reply 44
**Author**: Siva Bhaskaran
**Posted**: 2025-01-14T17:28:24.767Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/50

**This is regarding Question 11.**

I have extracted all the elements and added them manually. Tried all the options. Not even one appears to be correct . I evne tried ChatGPT which gave the answer as 411. Which of the following should be chosen?

<div class="d-none" title="This is the hidden element with the data-value attributes">
        <div class="bar baz" data-value="17">
          <div class="baz foo" data-value="29"></div>
          <div class="foo" data-value="20"></div>
        </div>
        <div class="bar foo baz" data-value="71">
          <div class="foo" data-value="48"></div>
          <span class="foo" data-value="30"></span>
          <div class="foo bar" data-value="90">
            <div class="bar" data-value="8"></div>
            <div class="" data-value="48"></div>
          </div>
        </div>
        <div class="baz foo" data-value="58">
          <div class="baz foo" data-value="19"></div>
          <div class="foo bar" data-value="76"></div>
        </div>
        <div class="bar baz" data-value="89">
          <div class="foo bar" data-value="38"></div>
          <div class="foo bar" data-value="9"></div>
        </div>
      </div>

---

## Reply 45
**Author**: Jayakrishnan
**Posted**: 2025-01-14T17:30:56.568Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/51

siva.bhaskaran:

`npx -y prettier@3.4.2 README.md`

Shouldn’t it be `npx -y prettier@3.4.2 --write README.md` or `npx prettier README.md` (Depending on whether to write or read)?

Apologies, I may not know full context of the question, as I haven’t attempted GA1 fully yet

---

## Reply 46
**Author**: Sakthivel S
**Posted**: 2025-01-15T05:06:11.291Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/52

I had this same doubt, I tried by adding the “span” tag’s value too it showed correct for me. I’d suggest you to try that.

---

## Reply 47
**Author**: Anand S
**Posted**: 2025-01-15T06:33:32.561Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/53

Oh, good catch, @23f2000237 and @siva.bhaskaran - I made a mistake in the evaluation script. It included the `span`.

I fixed it. Note: None of the earlier answers are affected, i.e. if you got it right earlier, it’ll stay right.

---

## Reply 48
**Author**: Andrew David
**Posted**: 2025-01-15T12:46:45.751Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/54

**It’s hackable**. It’s possible to get the answer to *some* questions by hacking the code for this quiz. That’s allowed.

What does exactly mean, if someone could elaborate without giving it away, please?

@carlton

---

## Reply 49
**Author**: Daksh Agarwal
**Posted**: 2025-01-16T15:27:41.211Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/55

I have tried but still am unable to do only that question if someone can help me with the code because everytime im getting a different answer its my last question

---

## Reply 50
**Author**: Daksh Agarwal
**Posted**: 2025-01-16T15:29:18.243Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/56

@21f2000370 i hope you wouldve completed it

---

## Reply 51
**Author**: 23F3002987 J SRI BALAJI PRABHU
**Posted**: 2025-01-17T10:39:40.125Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/57

Use Git bash the problem will be resolved

---

## Reply 52
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-17T22:25:12.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/58

Hi Daksh,

Did you solve it or still facing some issues with it ?

Kind regards

---

## Reply 53
**Author**: Daksh Agarwal
**Posted**: 2025-01-18T08:28:25.019Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/59

im still facing issue in that questioneven after watching the youtube video given and taking help of chatgpt im unable to solve that question only

---

## Reply 54
**Author**: 24DS1000121 ULAGAOOZHIAN
**Posted**: 2025-01-18T09:57:08.186Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/60

Hello Gentlemen Instructors,

In all the video lectures, I am first required to download the tools, install them on my computer ? Is it not going to overload my computer’s RAM etc.,

In one of the classes, you said that there is something  - colab like cloud wherein we can go and practice without overloading our own computers. Will you please let me know how to go about it ??

Thanks and regards,

ULAGAOOZHIAN,

France

24ds1000121

---

## Reply 55
**Author**: Kaif Fazal
**Posted**: 2025-01-18T11:40:38.844Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/61

**Image: Screenshot 2025-01-18 154321**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, specifically a PowerShell terminal, within a code editor environment (likely VS Code, given the UI elements).  The terminal displays a series of commands and their outputs.

**2. Text Content:**

The terminal displays the following commands and their outputs:

*   **`PS C:\Users\kaiff> Get-FileHash -Path formatted.md -Algorithm SHA256`**
    *   This command uses the `Get-FileHash` cmdlet to calculate the SHA256 hash of the file `formatted.md`.
    *   The output shows:
        *   `Algorithm`: SHA256
        *   `Hash`: `216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175`
        *   `Path`: `C:\Users\kaiff\formatted.md`

*   **`PS C:\Users\kaiff> npx -y prettier@3.4.2 "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md" > formatted.md`**
    *   This command uses `npx` to run the `prettier` code formatter on the file `README.md` located in the specified directory. The output is redirected to overwrite the file `formatted.md`.
    *   The `-y` flag likely auto-confirms any prompts from `npx`.
    *   `prettier@3.4.2` specifies the version of the `prettier` package to use.

*   The `Get-FileHash` command is repeated after the `prettier` command, showing the same hash value.

*   **`PS C:\Users\kaiff> certutil -hashfile formatted.md SHA256`**
    *   This command uses the `certutil` utility to calculate the SHA256 hash of the file `formatted.md`.
    *   The output shows:
        *   `SHA256 hash of formatted.md:`
        *   `

In question 3 of GA-1 while checking the answer  it’s showing incorrect answer.

216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175

This was the output which I got after the execution of the given code in the question.Kindly guide If I did some error or error in entering the value.

---

## Reply 56
**Author**: Divyasree
**Posted**: 2025-01-18T17:41:31.939Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/63

how to calculate How many Wednesdays are there in the date range 1981-08-30 to 2017-07-17?

The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).

---

## Reply 57
**Author**: Huzaifa Faizee
**Posted**: 2025-01-19T05:53:14.881Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/64

=SUM(TAKE(SORTBY({3,7,13,8,7,7,11,11,13,14,0,13,9,14,10,7}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 16))

I do not have the required excel version can someone please tell how can I find the solution to this one?

---

## Reply 58
**Author**: Sudhanshu Shekhar
**Posted**: 2025-01-19T10:52:20.968Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/65

@carlton @Jivraj

Sir i have saved the answers 2 days ago and scored around 7.5 . now when i open the portal today it is showing as 0 and all the answers has been cleared. how can i restore it.

---

## Reply 59
**Author**: Tushar Jalan 
**Posted**: 2025-01-19T10:58:50.978Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/66

yes same issue with me as well.2 3 days back i have answered and saved all the questions and today it is showing me 0 and all the answers are gone

---

## Reply 60
**Author**: Anand S
**Posted**: 2025-01-19T12:20:46.664Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/67

@23f2005067 @23f2003751 I added a “Recent saves” feature.

This will show the time and score for the last 3 times you saved. You can load from any of these.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a user interface (UI) element, specifically a list of recent saves. Each save entry includes a "Reload" button and information about the save time and score.

**2. Any text content visible:**

*   **Title:** "Recent saves"
*   **Button Label:** "Reload" (repeated for each save entry)
*   **Save Information:**
    *   "from 19/1/2025, 8:17:25 pm. Score: 1.25"
    *   "from 19/1/2025, 8:01:54 pm. Score: 0.25"
    *   "from 14/1/2025, 9:23:11 pm. Score: 0"

**3. The context or purpose of what's displayed:**

The UI element likely belongs to a game or application where users can save their progress. The "Recent saves" list allows users to quickly reload a previous save point. The date, time, and score associated with each save provide context for choosing which save to reload.

**4. Technical details:**

*   The UI uses buttons labeled "Reload" to trigger the action of loading a specific save.
*   The save information includes a date and time stamp (in the format DD/MM/YYYY, HH:MM:SS am/pm) and a numerical score.
*   The background color appears to be a light green or teal.
*   The button color is a light blue.

Do remember to click the “Check” button to calculate your score. That is not automatic.

Please check this out and let me know if there are any bugs. Thanks.

---

## Reply 61
**Author**: Sudhanshu Shekhar
**Posted**: 2025-01-19T13:47:07.641Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/69

**Image: Screenshot_2025-01-19-19-15-29-055_com.android.chrome**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of a mobile application, possibly an educational or assessment platform. It displays a list of questions and some recent save history. The UI elements include:

*   A header with the due date and time.
*   A menu icon (three horizontal lines).
*   A "Score" button.
*   A section for "Recent saves" with "Reload" buttons and timestamps.
*   A section for "Questions" with a numbered list of questions.

**2. Text Content:**

*   **Header:** "Due Sun, 26 Jan, 2025, 11:59 pm IST"
*   **Recent Saves:**
    *   "Recent saves"
    *   "Reload" (repeated three times)
    *   "from 19/01/2025, 16:22:36. Score: 0"
    *   "from 19/01/2025, 16:16:38. Score: 0"
    *   "from 19/01/2025, 16:16:02. Score: 0"
*   **Questions:**
    *   "Questions"
    *   A numbered list of questions, each with a point value in parentheses:
        1.  "VS Code Version (0.25 marks)"
        2.  "Make HTTP requests with uv (1 mark)"
        3.  "Run command with npx (0.5 marks)"
        4.  "Use Google Sheets (0.25 marks)"
        5.  "Use Excel (0.25 marks)"
        6.  "Use DevTools (0.5 marks)"
        7.  "Count Wednesdays (0.5 marks)"
        8.  "Extract CSV from a ZIP (0.25 marks)"
        9.  "Use JSON (0.75 marks)"
        10. "Multi-cursor edits to convert to JSON (0.5 marks)"
        11. "CSS selectors (0.5 marks)"
        12. "Process

Sir i might already clicked 3 save todays. So the previous clicks dates are of today. And the same 0 score is showing this.

---

## Reply 62
**Author**: Rohit Kumar 
**Posted**: 2025-01-19T17:02:23.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/70

Sha256sum is not recognized as an internal or external command how to solve this plzz answer

@carlton

---

## Reply 63
**Author**: Harsh Shah
**Posted**: 2025-01-20T05:27:14.301Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/71

If you are on windows, you might not be able to use sha256sum.

Here are two disussions that might help you out.

[Discussion 1](https://stackoverflow.com/questions/72087842/windows-equivalent-to-sha256sum-c-cryptographic-hash-digest-file-recursive)
[Discussion 2](https://stackoverflow.com/questions/11746287/compare-filehash-in-powershell)

---

## Reply 64
**Author**: Carlton D'Silva
**Posted**: 2025-01-20T07:26:25.067Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/72

@Rohitkumar7463 @23f2003845

If you are on Windows Powershell

Then instead of `sha256sum` you can simply use `Get-FileHash`

Send the output of the `npx -y prettier@3.4.2 README.md` to a text file eg. `output.txt` and then use `Get-FileHash` on powershell with the `output.txt` and it will use sha256 by default and give you the exact same output.

You might be able to pipe the data directly to `Get-FileHash` but I have not tried direct piping. The above method works guaranteed.

Kind regards

---

## Reply 65
**Author**: Sarthak Singh Gaur
**Posted**: 2025-01-20T12:44:15.933Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/73

@s.anand Sir

as you said in the previous post, the evaluation script is also updated based on errors other students point out.

I am submitting my answers as soon as the GA is released and stopping once I get 10/10.

Will you reevaluate the answers once the deadline is over? Or the marks I see right now will be set in stone?

If you will, then it will be based on the updated evaluation script which can reduce my marks.

**Image: image**
Here's a detailed description of the image:

1.  **UI Elements:** The image shows a portion of a user interface (UI), likely from a web application or mobile app. It includes text labels, a button, and information about recent saves.

2.  **Text Content:**
    *   "6 Jan 2025 at 11:59 PM IST" - This indicates a date and time (January 6, 2025, at 11:59 PM Indian Standard Time).
    *   "Score: 10 / 10" - This suggests a scoring system, where the user has achieved a perfect score.
    *   "Recent saves" - This is a heading indicating a section displaying recently saved items.
    *   "Reload" - This is a button label, suggesting an action to reload or refresh a saved item.
    *   "from 20/1/2025, 6:05:24 PM. Score: 10" - This provides details about a specific save, including the date and time (January 20, 2025, at 6:05:24 PM) and the score associated with that save.

3.  **Context/Purpose:** The UI appears to be related to a game, quiz, or learning application where users can save their progress and scores. The "Recent saves" section allows users to access and potentially reload previous attempts or saved states. The score indicates performance in the game or activity.

4.  **Technical Details:** There are no code snippets or technical diagrams in the image. It's purely a UI screenshot.

---

## Reply 66
**Author**: Anand S
**Posted**: 2025-01-20T13:09:10.672Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/74

@iamsarthak – as long as you don’t save again, your score will stay 10, even if I modify the evaluation script   :slight_smile: 

We don’t re-evaluate previous results in the graded assignments.

---

## Reply 67
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-01-20T13:16:50.351Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/75

@s.anand sir,

Question 15 is under the section for linux

I got the file which needs to be processed to answer the question

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a table-like structure, likely output from a command-line interface or a text-based file manager. It shows information about a set of files.

**2. Any text content visible:**

The table has the following column headers:

*   **Length:** Represents the size of the file.
*   **Date:** Represents the date of the file.
*   **Time:** Represents the time of the file.
*   **Name:** Represents the name of the file.

Below the headers, there are four rows of data, each representing a file:

*   **File 1:** Length: 4094, Date: 2004-03-10, Time: 07:49, Name: file0.txt
*   **File 2:** Length: 8410, Date: 2007-02-11, Time: 18:46, Name: file1.txt
*   **File 3:** Length: 8062, Date: 2000-01-26, Time: 13:40, Name: file2.txt
*   **File 4:** Length: 9748, Date: 2010-09-27, Time: 00:34, Name: file3.txt

**3. The context or purpose of what's displayed:**

The image shows a listing of files with their metadata (size, date, time, and name). This is a common way to display file information in a terminal or file manager. The purpose is to provide the user with a quick overview of the files and their attributes.

**4. Technical details if it's a code screenshot or technical diagram:**

This is not a code screenshot or a technical diagram. It's a representation of data, likely generated by a command-line tool or a file system browser. The data is formatted in a tabular way for easy readability. The date format is YYYY-MM-DD, and the time format is HH:MM.

I can solve this now using pandas.

From learning perspective, is this question aimed at making students to use something like awk or is it fine if i can carry on with pandas?

---

## Reply 68
**Author**: Anand S
**Posted**: 2025-01-20T13:22:56.326Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/76

@23f2000573 You can solve it with any tool you’re comfortable with, including pandas.

But since you *already* know how to do it with pandas, I suggest you explore how to do it with something like `awk` (or any other tool) to get a broader exposure into different approaches.

---

## Reply 69
**Author**: Rohit Kumar 
**Posted**: 2025-01-20T15:16:02.988Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/77

**Image: 20250120_203950**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a screenshot of a PowerShell terminal window. The terminal displays command-line interactions, error messages, and the output of a file hashing operation.

**2. Any text content visible:**

*   **Top:** "Try the new cross-platform PowerShell https://aka.ms/pscore6"
*   **Command History:**
    *   `PS C:\Users\HP> cd downloads`
    *   `PS C:\Users\HP\downloads> cd Downloads`
    *   **Error Message:** "Cannot find path 'C:\Users\HP\downloads\Downloads' because it does not exist."
        *   `At line:1 char:1`
        *   `cd Downloads`
        *   `CategoryInfo : ObjectNotFound: (C:\Users\HP\downloads\Downloads:String) [Set-Location]`
        *   `FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand`
    *   `PS C:\Users\HP\downloads> npx -y prettier@3.4.2 README.md >output.txt`
    *   `PS C:\Users\HP\downloads> Get-FileHash .\output.txt`
*   **File Hash Output:**
    *   `Algorithm Hash Path`
    *   `SHA256 7EA1921D69EAA2FDA9F6B5143A291C894CDC59E6CF6DBAA9EC8FFD4449A8F7E5 C:\Users\HP`
    *   `PS C:\Users\HP\downloads>>>>`
    *   `>> Algorithm Hash Path`
    *   `>> SHA256 7EA1921D69EAA2FDA9F6B5143A291C894CDC59E6CF6DBAA9EC8FFD4449A8F7E5 C:\Users\`

**3. The context or purpose of what's displayed:**

The user is attempting to navigate to a directory named "Downloads" within their "downloads" directory using the `

Sir is it right of sha sum question

---

## Reply 70
**Author**: Divyasree
**Posted**: 2025-01-20T17:05:52.439Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/78

to pass the graded 1 how much points are required for 10 ?

---

## Reply 71
**Author**: Andrew David
**Posted**: 2025-01-20T18:28:45.385Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/79

use chatgpt for the solution(sum(take(sortby))), it will give you the wrong answer but explain the concepts, use that go to colab and code one solution(will take abt 2 mins)

---

## Reply 72
**Author**: B R GIRI SUBRAHMANYA
**Posted**: 2025-01-20T18:31:41.213Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/80

I used

[https://www.microsoft365.com/launch/excel?auth=1](https://www.microsoft365.com/launch/excel?auth=1)

---

## Reply 73
**Author**: Carlton D'Silva
**Posted**: 2025-01-21T04:01:30.251Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/81

@Rohitkumar7463 The hash code is exactly what you see under the column Hash,

7E…E5

Thats the Hash code for the file output.txt

A Hash is a *nearly* unique representation of some data within some range dependent on the type of hashing algorithm and the amount of unique pieces of data that need to be encoded. (just my colloquial definition of it, i am sure you are able to ask GPT to give you a much better explanation)

Kind regards

---

## Reply 74
**Author**: Parmeet Singh
**Posted**: 2025-01-21T09:57:52.249Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/82

**Time Zone Issues with the “List Files and Attributes” Question**

quick heads‐up about Question 15 (the one asking for files at least 8143 bytes, modified on or after Sun, 19 Nov 2006, 7:38 am GMT‑5). I’m physically in a different time zone, but I eventually discovered the question seems to expect you to be located in India and to interpret that files date/time accordingly.

I got the correct answer once i localized the files timestamp to IST.

thanks

---

## Reply 75
**Author**: Gokul Vasudevan
**Posted**: 2025-01-21T21:18:33.350Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/83

GA1 Q18. What is the total sales of all the items in the “Gold” ticket type? Write SQL to calculate it.

I always get the answer in a nested array. Error: Got [[51006.69]]…

I could not use cursor in that shell, to extract the value also.

@carlton @Jivraj Please help me with this.

---

## Reply 76
**Author**: Sahil Parashar
**Posted**: 2025-01-22T00:55:39.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/84

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a block of text formatted as a JSON (JavaScript Object Notation) object. This JSON object contains information about an HTTP request.

**2. Text Content:**

The JSON object has the following key-value pairs:

*   **"args"**: This is an object containing arguments passed in the URL.
    *   **"email"**: "241001769@ds.study.iitm.ac.in"
*   **"headers"**: This is an object containing the HTTP request headers. The headers include:
    *   **"Accept"**: Specifies the accepted content types.
    *   **"Accept-Encoding"**: Specifies the accepted encoding types.
    *   **"Accept-Language"**: Specifies the preferred languages.
    *   **"Dnt"**: "1" (Do Not Track)
    *   **"Host"**: "httpbin.org"
    *   **"Priority"**: "u=0, i"
    *   **"Sec-Ch-Ua"**: User-Agent Client Hints related to the browser and its version.
    *   **"Sec-Ch-Ua-Mobile"**: Indicates if the request is from a mobile device.
    *   **"Sec-Ch-Ua-Platform"**: Indicates the platform.
    *   **"Sec-Fetch-Dest"**: Indicates the request destination.
    *   **"Sec-Fetch-Mode"**: Indicates the request mode.
    *   **"Sec-Fetch-Site"**: Indicates the request site.
    *   **"Sec-Fetch-User"**: Indicates if the request was initiated by a user.
    *   **"Upgrade-Insecure-Requests"**: "1"
    *   **"User-Agent"**: A string identifying the browser and operating system.
    *   **"X-Amzn-Trace-Id"**: An Amazon trace ID.
*   **"origin"**: "45.118.156.154" (The IP address from which the request originated)
*   **"url"**: "https://httpbin.org/get?email=

I am getting error in the uv question.

I have got the output json but I cant understand what part do I need to submit in the answer section.

---

## Reply 77
**Author**: Arnav Raj 
**Posted**: 2025-01-22T16:45:35.859Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/85

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question or task presented within a user interface, likely part of an online course or assessment. It includes instructions, an input field for an answer, and feedback on a previous attempt.

**2. Text Content:**

*   **Title:** "16 Move and rename files (0.5 marks)"
*   **Instructions:** "Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt."
*   **Question:** "What does running grep . * | LC\_ALL=C sort | sha256sum in bash on that folder show?"
*   **User Input:** "f1056c0b734ac835d17e8129fe9dc9a85ebcca45a82de42b13d18b7816808b7d \*"
*   **Feedback:** "Incorrect. Try again."

**3. Context and Purpose:**

The context is a programming or scripting exercise. The task involves:

1.  Downloading and extracting a zip file.
2.  Using the `mv` command to move files.
3.  Renaming files based on a specific rule (incrementing digits).
4.  Determining the output of a bash command pipeline involving `grep`, `sort`, and `sha256sum`.

The purpose is to test the user's understanding of file manipulation, command-line tools, and scripting concepts.

**4. Technical Details:**

*   The instructions mention the `mv` command, which is used to move or rename files in Unix-like operating systems.
*   The renaming rule involves replacing each digit in a filename with the next digit (e.g., 1 becomes 2, 9 becomes 0).
*   The question asks about the output of a bash command pipeline:
    *   `grep . *`: This searches for lines containing at least one character in all files.
    *   `LC

Sir I’m facing issue in this question even though i have done every thing as it mentioned. Can I get hint of the mistake for my code snippet.

My code: -

mkdir all_files
find parent/ -type f -exec mv {} all_files/ \;
for file in all_files/*; do
    new_name=$(echo "$file" | sed 's/[0-9]/\n&\n/g' | awk '
    { 
        if ($0 ~ /^[0-9]$/) print ($0 == "9") ? 0 : $0+1; 
        else print $0 
    }' | tr -d "\n")
    mv "$file" "$new_name"
done

---

## Reply 78
**Author**: Sudhish Narayan S
**Posted**: 2025-01-22T17:49:14.094Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/86

Good Evening, I have a doubt regarding the SQL Question I have attached my query. Please clarify me where I got wrong. I tried changing the gold string to lower and checking it. Even,  that didn’t work.

**Image: Screenshot 2025-01-22 231718**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely from a coding environment or a tool that allows users to write and execute SQL queries. It includes:

*   A question prompt.
*   A code editor area containing an SQL query.
*   An error message.
*   A description of the task.

**2. Any text content visible:**

*   **Question:** "What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it."
*   **SQL Query:** "SELECT SUM(Units\*Price) FROM tickets WHERE TYPE == 'Gold';"
*   **Error Message:** "Error: Got \[\[42810.5]]..."
*   **Task Description:** "Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units \* Price, and sum them up."

**3. The context or purpose of what's displayed:**

The context is a task where the user is asked to write an SQL query to calculate the total sales of "Gold" tickets. The provided SQL query attempts to do this, but it results in an error. The error message suggests that the query returned a specific value (42810.5), but it's presented as an error. The task description clarifies the requirements, including handling variations in the "Gold" ticket type name.

**4. Technical details (SQL query):**

*   The SQL query aims to calculate the sum of the product of "Units" and "Price" from a table named "tickets".
*   It filters the rows based on the "TYPE" column, selecting only those where the type is exactly equal to "Gold".
*   The error suggests that the query executed successfully and returned a value, but the system interpreted this as an error. This could be due to the way the system handles the output of the query or a mismatch between the expected and actual data types.
*   The task description indicates that the query should be more robust by handling variations in the "Gold" ticket type name (e.g., "GOLD", "gold"). This could be achieved using functions like `UPPER()` or `LOWER()` to

Thank You.

---

## Reply 79
**Author**: Sudhish Narayan S
**Posted**: 2025-01-22T17:56:51.809Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/87

I have another doubt regarding the CSS Selector question. I know how to select elements using CSS Selector but i don’t know how to get the sum using CSS Selectors as it cannot perform arithmetic operations. And also, I didn’t understand the question completely about the ‘hidden element’. Please clarify it. Thank you so much.

**Image: Screenshot 2025-01-22 232338**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface element, likely part of an interactive coding tutorial or challenge. It includes a question, a text input field, and an error message.

**2. Any text content visible:**

*   **Question:** "Let's make sure you know how to select elements using CSS selectors. Find all ``s having a `foo` class in the hidden element below. What's the sum of their `data-value` attributes?"
*   **Label:** "Sum of data-value attributes:"
*   **Input Field:** A text input field is present, currently empty.
*   **Error Message:** "Incorrect. Try again."

**3. The context or purpose of what's displayed:**

The image represents a coding challenge where the user needs to use CSS selectors to find specific `` elements (those with the class "foo") within a hidden HTML element. The user then needs to extract the values of the `data-value` attributes from those elements, sum them up, and enter the result in the input field. The "Incorrect. Try again." message indicates that the user's previous attempt was wrong.

**4. Technical details:**

*   The challenge involves CSS selectors, HTML elements (``), and HTML data attributes (`data-value`).
*   The user needs to understand how to target elements based on their class using CSS.
*   The user needs to be able to access the value of a data attribute in HTML.
*   The challenge requires basic arithmetic (summation).
*   The input field is likely designed to accept a numerical value.
*   The presence of the error message suggests that the system is validating the user's input.

---

## Reply 80
**Author**: Yogesh
**Posted**: 2025-01-23T03:08:20.003Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/88

It can be GOLD,gold, or even GoLD.

"  Get all rows where the Type is “Gold”. Ignore spaces and treat mis-spellings like GOLD, gold, etc. as “Gold”. Calculate the sales as Units * Price, and sum them up.  "

---

## Reply 81
**Author**: Arnav Raj 
**Posted**: 2025-01-23T07:05:58.642Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/89

Try to go through the given video of css selector and go through all foo classes carefully(using inspect) and sum them up!

---

## Reply 82
**Author**: Arnav Raj 
**Posted**: 2025-01-23T07:08:00.410Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/90

Try to remove the White spaces in your code!

---

## Reply 83
**Author**: Lakshika Sheoran
**Posted**: 2025-01-24T05:03:53.843Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/92

@carlton @Jivraj

sir i have gone through the process of solving the ques but still ans is showing wrong even i have used chatgpt and used cmd also. the cmd is is showing the result still ans is wrong

**Image: Untitled design**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a combination of a terminal/command-line interface output and a web-based question/answer interface.

*   **Terminal Output:** The top portion of the image displays output from a Windows command prompt or PowerShell terminal. It shows a directory listing of files, followed by the execution of a `for` loop and a PowerShell command. The PowerShell command filters files based on size and last modified time, then calculates the sum of their lengths.
*   **Web Interface:** The bottom portion of the image shows a question from a web-based assessment or quiz. It asks the user to determine the total size of files meeting specific criteria. There's an input field where the user has entered a value, and an error message indicating the answer is incorrect.

**2. Text Content:**

*   **Terminal Output:**
    *   File listings with date, time, and file size (e.g., "24-01-2025 09:57 5950 file84.txt").
    *   "100 File(s) 513187 bytes"
    *   "2 Dir(s) 74610814976 bytes free"
    *   Windows command prompt commands:
        *   `for /F "tokens=5*" %A in ('dir /T:W /-C ^| findstr /R "^[ ]*[1-9][0-9]{3,}"') do @echo %A %B`
        *   `powershell -Command "& { Get-ChildItem -Path . -File | Where-Object { $_.Length -ge 1235 and $_.LastWriteTime -ge '11/06/2019 10:48:00' } | Measure-Object -Property Length -Sum }"`
        *   `powershell -Command "& { Get-ChildItem -Path . -File | Where-Object { $_.Length -ge 1235 and $_.LastWriteTime -ge '11/06/2019 10:48:00' } | Out-File -FilePath result.txt }"`

---

## Reply 84
**Author**: saravanan chinna
**Posted**: 2025-01-24T10:37:08.553Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/94

In GA1, Question no: 9.

when i sort the json it says incorrect. but i validated that json using validator and also manually

admin : could you pls validate my answer pls

---

## Reply 85
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-25T05:04:27.652Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/95

You need to submit whole json becausae In this image `headers` is part of response, not request headers.

---

## Reply 86
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-25T05:40:24.502Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/96

Hi Arnav,

I tried your script on your dataset.

Problem might be you are not executing `grep . * | LC_ALL=C sort | sha256sum` in correct directory, you would need to execute it from `all_files` directory also there should not be any extra file other than that gets generated.

---

## Reply 87
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-25T05:46:17.852Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/97

22f2001175:

**Image: Untitled design**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a combination of a terminal/command-line interface and a web-based question/answer interface.

*   **Terminal/Command-Line:** The top portion displays output from a Windows command prompt or PowerShell session. It shows a directory listing of files, followed by commands executed and their output.
*   **Web Interface:** The bottom portion shows a question from an online assessment or quiz. It includes instructions, a question, an answer field, and feedback on the answer.

**2. Text Content:**

*   **File Listing (Terminal):**
    *   A series of lines showing date, time, and filenames (e.g., "24-01-2025 09:57 5950 file84.txt"). The files appear to be named "fileXX.txt" where XX is a number.
    *   "100 File(s) 513187 bytes"
    *   "2 Dir(s) 74610814976 bytes free"
*   **Command Prompt/PowerShell Commands (Terminal):**
    *   `C:\Users\lakshika\Downloads\q-list-files-attributes>for /F "tokens=5*" %A in ('dir /T:W/-C ^| findstr /R "^[ ]*[1-9][0-9]{3,}"') do @echo %A %B`
    *   `C:\Users\lakshika\Downloads\q-list-files-attributes>powershell -Command "& { Get-ChildItem -Path . -File | Where-Object { $_.Length -ge 1235 and $_.LastWriteTime -ge '11/06/2019 10:48:00' } | Measure-Object -Property Length -Sum }"`
    *   `C:\Users\lakshika\Downloads\q-list-files-attributes>powershell -Command "& { Get-ChildItem -Path . -File | Where-Object { $_.Length -ge 1235 and $_.LastWriteTime -ge '11/06/2

Untitled design1414×2000 349 KB

Time of modification of each of these files is 14 Jan 2025 which might be the day you unzipped them. Depending upon what software you use it might change modification date while unzipping. use unzip command line tool or winrar extractor, these are 2 tools we have tested.

kind regards

---

## Reply 88
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-01-25T06:05:38.597Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/98

Hi Saravanan,

I noticed an issue with your submission. In the question, there is a name `Bob`, but it doesn’t appear in your answer after applying the required sorting. Since the data for each student is dynamically generated and unique, the answer you submitted seems inconsistent with your dataset.

We encourage collaboration among students, but copying answers is not acceptable. Instead, I suggest reaching out to your friend to understand the script they used, run it on your dataset, and ensure you fully grasp the solution.

kind regards

---

## Reply 89
**Author**: saravanan chinna
**Posted**: 2025-01-25T06:39:59.261Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/99

Thanks lot jivraj. i updated my script and answers too

Thanks

---

## Reply 90
**Author**: SAKSHI PATHAK
**Posted**: 2025-01-24T13:26:45.607Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/100

**Image: Screenshot 2025-01-24 184222**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for a JSON hash tool. It includes:

*   **Title:** "JSON Hash"
*   **Text Area:** A large text area containing what appears to be a series of key-value pairs. The content within this area is scrollable.
*   **Button:** A green button labeled "Hash".
*   **Error Message:** A red box displaying an error message.

**2. Text Content:**

*   **Title:** "JSON Hash"
*   **Text Area Content:** The text area contains a long string of characters that look like key-value pairs separated by commas. The keys and values are seemingly random strings of alphanumeric characters. Here's a breakdown of some of the visible content:
    *   "IQtajk: DCIVYWY, Z: DMG, Zyselw: 169GFKIVIX, C: IXYVIDASET, v: Can, imup: URUSIQI, SIYNcajti F, QUI: CHINI46M, VMZQIKIM:"
    *   "ybCLb85bY2, aNbP76ziv: sBQOK1, 4x5UK: Ee, OlJsMcBmN: AM, c: f87lhjpU, vxl2xROEf: 6AtHge, D9Oh3u: CNMccZwTjM, WYQ:"
    *   "BoTRdy, 34jW0iee: N80sybsVoR, bSmt6kBkBH: Do9KIGnT, Amcn: hwK7xwwS, r: V0hRife, fu4VxHz: 1ER5wrY, j5dT4: j5B, w: czu,"
    *   "TesBfbosJr: QOD, HGMF: Cy7le, E: 4Vg6, VArd1Mw: uSoz9wyUny, e: M5At5z5K, h2k: Ud1, bV: qCDIEQKq, AeYpQ8n: EnbvW,"
    *   "

In the question 10 what should be the correct format for jason data as I edited the data according to given conditions but in Hash I am facing problem again and again

Also, in Q11 What is meaning of element below given in the question " Let’s make sure you know how to select elements using CSS selectors. Find all `<div>` s having a `foo` class in the hidden element below. What’s the sum of their `data-value` attributes?"

---

## Reply 91
**Author**: Pratul Garg
**Posted**: 2025-01-25T09:05:37.365Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/101

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) element, likely part of a tutorial or interactive learning platform related to AI-powered code editors. It includes text instructions, a question, an input field, and an error message.

**2. Text Content:**

*   **Title:** "AI Editors: Copilot, Cursor"
*   **Note:** "Note: AI Editors like Cursor, Cody, and GitHub Copilot use LLMs to help you write code faster."
*   "These are built on top of VS Code. These are now a standard tool in every developer's toolkit. Please use them."
*   "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type `code -s` and press Enter. Copy and paste the entire output below."
*   "What is the output of `code -s`?"
*   "Incorrect. Try again."

**3. Context and Purpose:**

The image appears to be part of an interactive tutorial or exercise designed to teach users about AI-powered code editors like Cursor, Cody, and GitHub Copilot. The tutorial instructs the user to run a specific command (`code -s`) in their terminal and then paste the output into the provided input field. The "Incorrect. Try again." message indicates that the user's previous attempt was unsuccessful. The purpose is likely to familiarize users with the command-line interface of Visual Studio Code and how it interacts with these AI editors.

**4. Technical Details:**

*   The command `code -s` is a command-line instruction for Visual Studio Code. The `-s` flag likely has a specific function or purpose within the VS Code environment.
*   The input field is designed for the user to paste the output from the terminal after running the command.
*   The presence of an error message suggests that the system is validating the user's input against the expected output of the command.

what sort of response am i supposed to put ?? the response i am getting ,it says incorrect, basically  after doing code -s ,i get like info about the version of vs code and info about cpu gpu etc…

---

## Reply 92
**Author**: Saniya Naaz
**Posted**: 2025-01-25T11:42:28.917Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/102

**Image: Screenshot 2025-01-25 171014**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a UI element, likely from a coding challenge or tutorial. It presents instructions, a question, a user's answer, and feedback.

**2. Text Content:**

*   **Instructions:** "Download `q-replace-across-files.zip` and unzip it into a new folder, then replace all "IITM" (in upper, lower, or mixed case) with "IIT Madras" in all files. Leave everything as-is - don't change the line endings."
*   **Question:** "What does running `cat * | sha256sum` in that folder show in bash?"
*   **User's Answer:** "63144b28ad1d2bd5b9b4b0855cab6a4a4fa8d57ed2ed826b4f5b36d12ae97347"
*   **Feedback:** "Incorrect. Try again."

**3. Context and Purpose:**

The context is a coding exercise where the user needs to download a file, perform a specific text replacement operation on its contents, and then calculate the SHA256 checksum of the resulting files. The question asks for the output of a bash command that concatenates all files in the folder and pipes the result to `sha256sum`. The purpose is to test the user's ability to follow instructions, manipulate files, and use command-line tools.

**4. Technical Details:**

*   The instructions involve downloading a ZIP file, extracting its contents, and performing a find-and-replace operation.
*   The bash command `cat * | sha256sum` is used to calculate the SHA256 checksum of the concatenated contents of all files in the current directory. `cat *` concatenates all files, and `|` pipes the output to `sha256sum`, which calculates the checksum.
*   The user's answer is a hexadecimal string, which is the expected format for a SHA256 checksum.
*   The "Incorrect. Try again." message indicates that the provided checksum does not match the expected checksum after performing the specified operations.

The answer is wrong but I have done every step correctly. Help

---

## Reply 93
**Author**: Yogaswetha
**Posted**: 2025-01-25T18:32:03.063Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/104

**Image: image**
Here's a detailed description of the image:

**1. Visual Elements:**

*   **Top Section:** The top portion of the image features a promotional graphic. It includes the text "package/project manager" and the letters "uv" in a stylized font. There's also a Python logo. A man is pointing towards the "uv" logo.
*   **Bottom Section:** The lower part of the image shows text and what appears to be a code snippet or output.

**2. Text Content:**

*   **Title:** "package/project manager"
*   **Command Description:** "Running `uv run --with httpie -- https [URL]` installs the Python package `httpie` and sends a HTTPS request to the URL."
*   **Request Instruction:** "Send a HTTPS request to `https://httpbin.org/get` with the URL encoded parameter `email` set to `23f2000098@ds.study.iitm.ac.in`"
*   **Question:** "What is the JSON output of the command? (Paste only the JSON body, not the headers)"
*   **User Input (JSON):** `{'args':{'email':'23f2000098@ds.study.iitm.ac.in'},'origin':'106.197.103.245','url':'https://httpbin.org/get?email=23f2000098%40ds.study.iitm.ac.in'}`
*   **Error Message:** "SyntaxError: Expected property name or '}' in JSON at position 1 (line 1 column 2)"

**3. Context and Purpose:**

The image appears to be part of a tutorial or exercise related to using the "uv" package/project manager, likely in the context of Python development. The user is instructed to run a command that installs the `httpie` package and makes an HTTPS request. They are then asked to provide the JSON output of the command. The presence of a syntax error suggests that the user's input is not valid JSON.

**4. Technical Details:**

*   The command `uv run --with httpie -- https [URL]` suggests that "uv" is a tool that can execute Python code or

Not sure how to resolve this error… any sugessions ?

---

## Reply 94
**Author**: Arshad ALI
**Posted**: 2025-01-25T18:55:30.353Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/105

first convert in into jason using bash or other terminal then paste the converted json content to this page and generate the json hash

---

## Reply 95
**Author**: Yogaswetha
**Posted**: 2025-01-25T19:24:50.295Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/106

I am getting errors for the host part please guide me

---

## Reply 96
**Author**: SAKSHI PATHAK
**Posted**: 2025-01-25T19:45:45.630Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/107

But I have converted the file as it says in the question still i am getting error that I am unable to understand. Can you just tell me please what formatted answer should be that is just the type of answer it’s asking?

---

## Reply 97
**Author**: Saravanan
**Posted**: 2025-01-25T22:26:09.529Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/108

I tried this. For me still the answer is incorrect.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a command-line interface (CLI) or terminal window, likely from a Windows PowerShell environment. It displays a series of commands and their outputs.

**2. Text Content:**

The text content consists of commands entered by a user and the responses from the system. Here's a breakdown:

*   `PS C:\Users\sarva>` `cd downloads`:  Changes the current directory to the "downloads" folder within the user's "sarva" directory.
*   `PS C:\Users\sarva\downloads>` `certutil -hashfile C:\Users\sarva\downloads\README.md SHA256`:  Uses the `certutil` command to calculate the SHA256 hash of the file "README.md" located in the downloads directory.
*   `SHA256 hash of C:\Users\sarva\downloads\README.md:`:  Indicates the output that follows is the SHA256 hash.
*   `eef23369e30d7bd99173ef4988c65a59b80bf56f60da4c9ab95c1903be312317`:  The calculated SHA256 hash value.
*   `CertUtil: -hashfile command completed successfully.`:  Confirmation that the `certutil` command executed without errors.
*   `PS C:\Users\sarva\downloads>` `npx -y prettier@3.4.2 README.md > output.txt`:  Executes the `prettier` code formatting tool (version 3.4.2) on the "README.md" file and redirects the formatted output to a new file named "output.txt". The `-y` flag likely auto-confirms any prompts.
*   `PS C:\Users\sarva\downloads>` `Get-FileHash -Algorithm SHA256 output.txt`:  Uses the `Get-FileHash` PowerShell cmdlet to calculate the SHA256 hash of the "output.txt" file.
*   A table-like output follows, with columns labeled "Algorithm", "Hash", and "Path".

---

## Reply 98
**Author**: Saravanan
**Posted**: 2025-01-25T22:33:14.271Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/109

Finally. Got the correct one in bit dash.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a terminal window, likely running in a Unix-like environment (possibly within Windows using something like Git Bash or WSL). It displays command-line input and output.

**2. Any text content visible:**

*   **Prompt:** `sarva@SURIYA MINGW64 ~/downloads`
    *   `sarva@SURIYA`:  Username and hostname.
    *   `MINGW64`: Indicates a MinGW64 environment (Minimalist GNU for Windows).
    *   `~/downloads`: The current working directory, which is the "downloads" directory within the user's home directory.
*   **Command:** `$ npx -y prettier@3.4.2 README.md | sha256sum`
    *   `npx`:  A tool to execute npm package binaries.
    *   `-y`:  An option likely used to automatically confirm any prompts.
    *   `prettier@3.4.2`:  Specifies the "prettier" package at version 3.4.2. Prettier is a code formatter.
    *   `README.md`:  The input file, a Markdown file named "README.md".
    *   `|`:  A pipe, which redirects the output of the "prettier" command to the input of the "sha256sum" command.
    *   `sha256sum`:  A command-line utility that calculates the SHA256 hash of its input.
*   **Output:** `2ccd877ded5f031c251d3319bc1b266018635156db88e63105943dbef7e106a1 *-`
    *   This is the SHA256 hash generated by the `sha256sum` command. The `*-` at the end likely indicates that the input was read from standard input (the pipe).

**3. The context or purpose of what's displayed:**

The user is using `npx` to run the `prettier` code formatter on the `README.md` file. The `-y` flag suggests

---

## Reply 99
**Author**: Saravanan
**Posted**: 2025-01-25T22:44:44.192Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/110

I ran this directly in the console and got the correct answer.

// Select all 
 and  elements with the ‘foo’ class

const fooElements = document.querySelectorAll(“div.foo, span.foo”);

// Initialize a variable to store the sum

let sum = 0;

// Iterate through the selected elements

fooElements.forEach(element => {

// Get the ‘data-value’ attribute and convert it to a number

const value = parseFloat(element.getAttribute(“data-value”));

// Add the value to the sum

if (!isNaN(value)) {

sum += value;

}

});

console.log(“Sum of data-value attributes:”, sum);

---

## Reply 100
**Author**: Sahil Parashar
**Posted**: 2025-01-26T09:33:05.487Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/112

@Jivraj Sir I have tried pasting the entire json but I am still getting incoorect answer

---

## Reply 101
**Author**: Arshad ALI
**Posted**: 2025-01-26T10:10:21.039Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/113

6630ecbfc252fa2bd39d26737fc1d4e1d22574c8792112b28cdf4ff128d4c605

---

## Reply 102
**Author**: Arshad ALI
**Posted**: 2025-01-26T10:59:36.818Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/114

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a section of a user interface, likely from a coding challenge or tutorial. It presents instructions, a question, a user's answer, and feedback on that answer. There's also a warning about how to properly extract files.

**2. Text Content:**

*   **Instructions:** "Download `q-list-files-attributes.zip` and extract it. Use `ls` with options to list all files in the folder along with their date and file size."
*   **Question:** "What's the total size of all files at least 2404 bytes large and modified on or after Mon, 18 Mar, 2002, 1:02 am IST?"
*   **User's Answer:** "485969" (displayed within a text input field)
*   **Feedback:** "Incorrect. Try again."
*   **Warning:** "Don't `copy` from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using `unzip`, `7-Zip` or similar utilities and `check the timestamps`."

**3. Context and Purpose:**

The context is a coding or data analysis challenge. The user is instructed to download a ZIP file, extract its contents, and then use a command-line tool (`ls`) to analyze the files. The challenge involves calculating the total size of files that meet specific criteria (size and modification date). The user has provided an answer, but it's marked as incorrect. The warning suggests that the user might be extracting the files incorrectly, which could affect the file timestamps and lead to an incorrect calculation.

**4. Technical Details:**

*   **`q-list-files-attributes.zip`:** This is the name of the ZIP file that needs to be downloaded and analyzed. The name suggests it contains a list of files and their attributes.
*   **`ls`:** This is a command-line utility commonly used in Unix-like operating systems (Linux, macOS) to list files in a directory. The instructions imply that the user needs to use `ls` with specific options to display file sizes and modification dates.
*   **`unzip`, `7-Zip`:** These are utilities used to

help me with this

---

## Reply 103
**Author**: Bhargav Chavda
**Posted**: 2025-01-26T15:24:26.021Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/115

Q18 GA1

I don’t get what’s wrong with this:

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of a coding environment, likely a platform for practicing SQL queries. It presents a table of data and a SQL query designed to analyze that data. There's also an error message displayed.

**2. Text Content:**

*   **Context:** "There is a `tickets` table in a SQLite database that has columns `type`, `units`, and `price`. Each row is a customer bid for a concert ticket."
*   **Table Headers:** `type`, `units`, `price`
*   **Table Data (Partial):**
    *   `Silver`, `589`, `1`
    *   `gold`, `559`, `1.18`
    *   `gold`, `74`, `1.03`
    *   `gold`, `361`, `1.76`
    *   `BRONZE`, `673`, `1.94`
    *   `...` (indicating more rows)
*   **Question:** "What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it."
*   **SQL Query:**
    ```sql
    select sum(units*price)
    from tickets
    where type='gold' collate nocase;
    ```
*   **Error Message:** "Error: Got [[124944.59]]..."
*   **Hint:** "Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units * Price, and sum them up."

**3. Context and Purpose:**

The image is part of an interactive coding exercise or tutorial. The user is presented with a database table and asked to write a SQL query to answer a specific question about the data. The error message suggests that the provided query is not producing the expected result. The hint provides guidance on how to correct the query.

**4. Technical Details (SQL Query):**

*   The SQL query attempts to calculate the sum of `units * price` for all rows in the `tickets` table where the `type` column is equal to 'gold

Can anyone help me understand? Thanks

---

## Reply 104
**Author**: Yogaswetha
**Posted**: 2025-01-26T18:11:25.002Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/116

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a snippet of instructions or a tutorial, likely related to software development or command-line usage. It includes text instructions, a downloadable link, and a question with a provided answer.

**2. Text Content:**

*   "Let's make sure you know how to use `npx` and `prettier`."
*   "Download `README.md`. In the directory where you downloaded it, make sure it is called `README.md`, and run `npx -y prettier@3.4.2 README.md | sha256sum`."
*   "What is the output of the command?"
*   "SHA256"
*   "AC06784D6825497650083DDFD6746A2CDD561B6A1FF45241C6A354035244A75C"

**3. Context and Purpose:**

The context appears to be a tutorial or guide that aims to teach users how to use `npx` and `prettier`, which are tools commonly used in JavaScript development. `npx` is a package runner, and `prettier` is a code formatter. The instructions guide the user to download a `README.md` file, then use `npx` to run `prettier` on it and pipe the output to `sha256sum`. The question then asks for the output of this command, and provides the SHA256 hash.

**4. Technical Details:**

*   **`npx -y prettier@3.4.2 README.md | sha256sum`**: This is a command-line instruction.
    *   `npx`: Executes a Node.js package.
    *   `-y`: Automatically confirms any prompts.
    *   `prettier@3.4.2`: Specifies the `prettier` package version to use.
    *   `README.md`: The file to be formatted by `prettier`.
    *   `|`: The pipe operator, which takes the output of the previous command and uses it as input for the next command.
    *   `sha256sum

i dont know what is the error is plss guide me

---

## Reply 105
**Author**: Ajit
**Posted**: 2025-01-26T18:34:51.478Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/117

I have attempted the quiz, but missed marking this question - I have seen the Graded Assignment 1 available at [this link](https://exam.sanand.workers.dev/tds-2025-01-ga1) and have attempted it. Hope the scores saved would be considered

---

## Reply 106
**Author**: Tanya kamboj
**Posted**: 2025-01-25T08:24:31.783Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/118

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a question or task presented within a user interface, likely part of an online assessment or tutorial. It includes instructions, downloadable resources, a text input field, and feedback on the user's answer.

**2. Any text content visible:**

*   **Title:** "Multi-cursor edits to convert to JSON (0.5 marks)"
*   **Instructions:** "Download q-multi-cursor-json.txt and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}."
*   **Question:** "What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?"
*   **User Input:** "c0b9426a7f358720f193d3806497ec0d81d10d835085d0f284f804bf3a6a1536"
*   **Feedback:** "Incorrect. Try again."

**3. The context or purpose of what's displayed:**

The context is a programming or data science exercise. The user is expected to:

1.  Download a text file ("q-multi-cursor-json.txt").
2.  Use a text editor with multi-cursor functionality to transform the content of the file.
3.  Convert the transformed content into a valid JSON object.
4.  Paste the JSON object into a specific online tool ("tools-in-data-science.pages.dev/jsonhash").
5.  Click a "Hash" button on that tool.
6.  Enter the resulting hash value as the answer.

The image indicates that the user's initial attempt was incorrect.

**4. Technical details:**

*   The task involves JSON (JavaScript Object Notation), a common data format.
*   The use of "multi-cursors" suggests that the initial text file likely contains data that needs to be edited in a repetitive way.
*   The reference to a "Hash" button implies that the online tool calculates a cryptographic hash of the JSON data

i am not getting why my answer is showing incorrect.

can you help me in this ? @Saransh_Saini @Jivraj

---

## Reply 107
**Author**: Saransh Saini
**Posted**: 2025-01-25T09:03:21.149Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/119

Check the structure of your json object. It should be {key1: value1, key2: value2}. Also make sure you enclose the keys and values in double-quotes, and after every key-value pair put a comma.

---

## Reply 108
**Author**: Tanya kamboj
**Posted**: 2025-01-25T16:02:51.992Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/120

i am doing so only … i can send u the example -

{   “0”: “wEfsmtde”,

“83”: “NghqzO3DL”,

“NqN7EcM”: “I”,

“vFD2C”: “KAB”}

i am not able to find what’s the mistake

---

## Reply 109
**Author**: Saransh Saini
**Posted**: 2025-01-25T16:44:17.023Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/121

Your format seems to be correct, but cause you are still facing that problem then these are the few reasons I can think of

Check the entire JSON object and make sure that each and every element follows this format.
Use Chrome for getting that hash code, it could be the case that some other browser may not be pasting the object as intended.

---

## Reply 110
**Author**: Tanya kamboj
**Posted**: 2025-01-25T17:09:51.432Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/122

Okay, i will go through my json object once.

And for hash code i am using chrome only

---

## Reply 111
**Author**: Tanya kamboj
**Posted**: 2025-01-26T07:29:05.341Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/123

It worked.

Thank you

---

## Reply 112
**Author**: Divyasree
**Posted**: 2025-01-27T13:46:00.779Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/124

After passing the deadline , my scores aren’t there …Is it same for all?

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a webpage or screen displaying instructions for an online assessment or quiz. The page includes a title, instructions, and some advice.

**2. Any text content visible:**

*   **Header:** "Ended at Sun, 26 Jan, 2025, 11:59 pm IST"
*   **Title:** "TDS 2025 Jan GA1 - Development To" (The title is cut off, but it seems to be about a Development Tool assessment)
*   **Section Title:** "Instructions"
*   **Instructions (numbered list):**
    1.  "Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure)"
    2.  "Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times."
    3.  "Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated."
    4.  "Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters."
    5.  "Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser."
    6.  "Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want."
    7.  "It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed."
*   **Question:** "Should you take TDS this term?"
*   **Advice (bullet points):**
    *   "If this assignment takes you under 2 hours to complete, you will likely do OK in TDS."
    *   "If you score above 8 / 10, you might get an S or A grade, with effort and luck."

**3. The context or purpose of what's displayed:**

The image shows the instructions and some advice for a "TDS" (likely a course or program) assessment. The instructions are designed to guide the user on how to approach the assessment

---

## Reply 113
**Author**: Naga durga prasad E
**Posted**: 2025-01-27T14:44:32.781Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/125

wow, thats so true…  :rofl:

---

## Reply 114
**Author**: Carlton D'Silva
**Posted**: 2025-01-28T08:04:54.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/126

3 posts were merged into an existing topic: [Graded assignment 1 - Submission not shown](/t/graded-assignment-1-submission-not-shown/165396/13)

---

## Reply 115
**Author**: Sai 
**Posted**: 2025-01-29T05:20:50.309Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/127

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Text Display:** The image shows text indicating the user is logged in.
*   **Button:** There's a "Logout" button.
*   **List/Box:** A light green box contains a list of "Recent saves."
*   **Links/Buttons:** Each save entry has a "Reload" button/link.

**2. Text Content:**

*   "You are logged in as 22f3001740@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves"
*   "Reload" (repeated three times)
*   "from 1/23/2025, 9:33:02 PM. Score: 8"
*   "from 1/23/2025, 9:32:59 PM. Score: 8"
*   "from 1/23/2025, 9:32:55 PM. Score: 8"

**3. Context/Purpose:**

The image appears to be a screenshot from a web application or system. It shows a user's logged-in status and provides a list of their recent saves, likely related to some task or activity within the application. The "Reload" buttons suggest the user can revert to or load these saved states. The "Score" indicates a performance metric associated with each save.

**4. Technical Details:**

*   The email address "22f3001740@ds.study.iitm.ac.in" suggests the user is affiliated with the Indian Institute of Technology Madras (IITM) and is likely a student in a data science program ("ds.study").
*   The timestamps (1/23/2025, 9:33:02 PM, etc.) indicate the date and time when the saves were created.
*   The "Score: 8" suggests a numerical evaluation of the saved state, possibly related to progress, accuracy, or some other performance indicator.

Hi Sir,

I completed the GA 1 before the time and saved it as mentioned above, but forgot to give “submit”  button on iit bs week 1 graded assignment portal.

Will it might be a problem ?

I

---

## Reply 116
**Author**: Himanshu Tripathi
**Posted**: 2025-01-29T12:41:00.221Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/128

I have seen the Graded Assignment 1 available at [this link](https://exam.sanand.workers.dev/tds-2025-01-ga1) and have attempted it.

Yes

No

i have forgot the submit  here on the portal but i have got 9 marks on the test will it be a problem  in my marks?

---

## Reply 117
**Author**: Sai 
**Posted**: 2025-01-31T03:27:35.397Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/129

Hi @Jivraj  sir,

For me, in dashboard , it is showing the assignment was not submitted.

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Module Header:** The page is titled "Module 1: Development Tools".
*   **Assignment Section:** This section displays information about an assignment. It includes the assignment name ("Graded Assignment 1"), the due date ("Assessment (Due: 26 Jan 2025)"), and a status ("Not Submitted").
*   **Score Table:** A table displays scores related to the assignment. It has columns for "Your Score", "Peer Average", and "Median Score".
*   **Login Information:** The page indicates that the user is logged in with the email address "22f3001740@ds.study.iitm.ac.in".
*   **Logout Button:** A "Logout" button is present.
*   **Recent Saves Section:** This section displays a list of recent saves. Each entry includes a "Reload" button, a timestamp, and a score.

**2. Text Content:**

*   "Module 1: Development Tools"
*   "Assignment"
*   "Graded Assignment 1"
*   "Assessment (Due: 26 Jan 2025)"
*   "Not Submitted"
*   "Your Score"
*   "Peer Average"
*   "Median Score"
*   "-" (Your Score)
*   "99%" (Peer Average)
*   "100" (Median Score)
*   "You are logged in as 22f3001740@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves"
*   "Reload"
*   "from 1/23/2025, 9:33:02 PM. Score: 8"
*   "from 1/23/2025, 9:32:59 PM. Score: 8"
*   "from 1/23/2025, 9:32:55 PM. Score: 8"

**3. Context and Purpose:**

The image appears to be a screenshot of a student's dashboard or progress page within an online learning platform. It

But I have completed it and got saved before the deadline

I havent answered the (yes / No ) in seek portal. If that might be a reason ?

Can you please help me resolve this issue

---

## Reply 118
**Author**: Carlton D'Silva
**Posted**: 2025-01-31T03:47:24.324Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/130

Dear Sai,

This is NOT the picture of your dashboard.

 22f3001740:

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Module Header:** "Module 1: Development Tools" is displayed as a header, likely indicating the current section of a learning platform.
*   **Assignment Section:** A section dedicated to assignments, specifically "Graded Assignment 1."
*   **Score Table:** A table-like structure showing "Your Score," "Peer Average," and "Median Score" for the assignment.
*   **Login Information:** Text indicating the logged-in user's email address.
*   **Logout Button:** A button labeled "Logout."
*   **Recent Saves Section:** A section displaying recent saves, with "Reload" buttons and timestamps.

**2. Text Content:**

*   **Module 1: Development Tools**
*   **Assignment**
*   **Graded Assignment 1**
*   **Assessment (Due: 26 Jan 2025)**
*   **Not Submitted**
*   **Your Score**
*   **Peer Average**
*   **Median Score**
*   **-** (under Your Score)
*   **99%** (under Peer Average)
*   **100** (under Median Score)
*   **You are logged in as 22f3001740@ds.study.iitm.ac.in.**
*   **Logout**
*   **Recent saves**
*   **Reload** (repeated multiple times)
*   **from 1/23/2025, 9:33:02 PM. Score: 8** (repeated with slightly different timestamps)
*   **from 1/23/2025, 9:32:59 PM. Score: 8**
*   **from 1/23/2025, 9:32:55 PM. Score: 8**

**3. Context and Purpose:**

The image appears to be a screenshot from an online learning platform or course management system. It shows a student's view of an assignment, their score (or lack thereof), and how it compares to the peer average and median score. The "Recent Saves" section suggests that the student has been working on something within the platform

This picture is the score in your seek portal.

The dashboard has the final correct score. Please check your dashboard.

The dashboard has all your courses on it, when you log in.

Kind regards

---

## Reply 119
**Author**: Sai 
**Posted**: 2025-01-31T05:46:24.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/131

Got it , Thank you sir

---

## Reply 120
**Author**: Shashank Tripathi
**Posted**: 2025-02-19T09:23:01.247Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/132

Hello Sir,

I am writing to bring to your attention a discrepancy I’ve noticed regarding my Week 1 graded assignment for the Tools in Data Science course.

I successfully completed the assignment and received a score of **80 out of 100**. However, when I checked the course portal, it is showing my status as “**absent**” for this particular assignment.

I wanted to ensure that this information is corrected in the system to accurately reflect my participation and performance. Could you please look into this matter and update my grade accordingly?

**Image: Screenshot 2025-02-18 191335**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Browser Interface:** The image shows a web browser interface, including the address bar.
*   **Header:** A header section indicates the exam has ended.
*   **Question/Discussion Link:** A prominent link encourages users to join a discussion on Discourse if they have questions.
*   **Login Information:** The user's login information is displayed, along with a "Logout" button.
*   **Recent Saves:** A section titled "Recent saves" lists the user's save history.
*   **Buttons:** There are buttons labeled "Check all" and "Save" in the header.
*   **Reload Links:** Each save entry has a "Reload" link.

**2. Text Content:**

*   **URL:** `exam.sanand.workers.dev/tds-2025-01-ga1`
*   **Exam End Time:** "Ended at Sun, 26 Jan, 2025, 11:59 pm IST"
*   **Score:** "Score: 0"
*   **Question Prompt:** "Have questions? Join the discussion on Discourse"
*   **Login Message:** "You are logged in as 23f3001601@ds.study.iitm.ac.in."
*   **Logout:** "Logout"
*   **Recent Saves Title:** "Recent saves (most recent is your official score)"
*   **Save History Entries:**
    *   "Reload from 1/27/2025, 12:00:05 AM. Score: 8"
    *   "Reload from 1/26/2025, 11:59:55 PM. Score: 8"
    *   "Reload from 1/26/2025, 11:59:55 PM. Score: 8"

**3. Context/Purpose:**

The image appears to be a screenshot of an online exam interface after the exam has ended. It shows the user's final score (0), provides a link to a discussion forum for questions, displays login information, and lists the user's save history during the exam. The

**Image: Screenshot 2025-02-19 145423**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image appears to be a screenshot of a course announcement or module introduction, likely from an online learning platform. It features a title section with course information and a subsequent section indicating a specific assignment.

**2. Any text content visible:**

*   **"Tools in Data Science"**: This is the main title, suggesting the subject matter of the course.
*   **"NEW COURSE"**: This indicates that the course is recently launched or new to the platform.
*   **"Week 1 Assignment - Absent"**: This suggests that the image is displaying information about the first week's assignment, and the user is currently marked as "Absent" for it.

**3. The context or purpose of what's displayed:**

The image is likely part of a course interface, providing students with information about the course title, its newness, and the status of their assignments. The "Absent" status for Week 1 Assignment suggests that the student may have missed the deadline or has not yet submitted the assignment.

**4. Technical details:**

The background of the title section is a dark red color with a pattern of small red dots. The text is white and appears to be in a sans-serif font. The "Week 1 Assignment" section is on a white background. The overall design is clean and simple, typical of online learning platforms.

---

## Reply 121
**Author**: Aniruddha Mukherjee
**Posted**: 2025-02-19T09:33:43.694Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/133

@s.anand Linking [this tutorial](https://www.markdowntutorial.com/lesson/1/) for markdown. Maybe you can consider including it in the next iteration of the course?

I’ve created a PR for the same on GitHub! Please have a look and let me know what you think Prof!

---

## Reply 122
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-19T11:36:55.423Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/134

*No content*

---

## Reply 123
**Author**: Ayush Kumar Shaw 
**Posted**: 2025-02-19T16:32:55.050Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/135

I also came here for the same issue…

---

## Reply 124
**Author**: Ayush Kumar Shaw 
**Posted**: 2025-02-19T16:33:47.136Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/136

Sir i have scored 9.25 in the week 1 assingment but now it is showing absent…

---

## Reply 125
**Author**: Carlton D'Silva
**Posted**: 2025-02-19T17:06:25.239Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/137

@23f3001601 Dont worry, it is 8 on our backend server. The dashboard will have the result soon.

Kind regards.

---

## Reply 126
**Author**: Carlton D'Silva
**Posted**: 2025-02-19T17:07:56.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/138

@232001286

Yes our backend server shows that it is 9.25 dont worry. It will be fixed in the dashboard soon.

Kind regards

---

## Reply 127
**Author**: Carlton D'Silva
**Posted**: 2025-05-13T03:59:38.899Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/140

2 posts were merged into an existing topic: [GA2 - Deployment Tools - Discussion Thread [TDS May 2025]](/t/ga2-deployment-tools-discussion-thread-tds-may-2025/173525/9)

---

## Reply 128
**Author**: Carlton D'Silva
**Posted**: 2025-05-13T03:57:21.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/142

*No content*

---

## Reply 129
**Author**: Carlton D'Silva
**Posted**: 2025-05-13T03:57:56.589Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/143

*No content*

---

## Reply 130
**Author**: Carlton D'Silva
**Posted**: 2025-05-13T04:00:05.963Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga1-development-tools-discussion-thread-tds-jan-2025/161083/144

*No content*

---
