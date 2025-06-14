# Queries regarding End Term exam solutions

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/1

## Topic Metadata
- **ID**: 172707
- **Slug**: queries-regarding-end-term-exam-solutions
- **Created**: 2025-04-15T09:59:50.919Z
- **Views**: 295
- **Replies**: 10
- **Likes**: 17
- **Tags**: clarification, end-term-exam

## Original Post
**Author**: Shambhavi Verma
**Posted**: 2025-04-15T09:59:51.136Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/1

Hi @carlton and @Jivraj sir,

I appeared for the end term examination held on 13th April 2025 during the FN shift. I would like to bring to your attention that the exam interface did not provide an option for multiple selections. However, a few questions appeared to have multiple correct answers.

I have noted down the specific questions and the corresponding options I believe to be correct.So, kindly review them and let me know if there were any errors in my understanding of the questions. The questions are as follows:

**Image: 1000042547**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question (MCQ) from a test or quiz. The question asks the user to identify a valid log entry based on a provided format. The image presents the question text, followed by four options, each representing a potential log entry. The first three options are marked in red, while the last option is marked in green, suggesting it is the correct answer.

**2. Text Content:**

*   **Question Header:**
    *   Question Number: 300
    *   Question Id: 6406531231221
    *   Question Type: MCQ
    *   Correct Marks: 2
    *   Question Label: Multiple Choice Question
*   **Question Text:** "Which of the following is a valid log entry based on the provided format?"
*   **Options:**
    *   Each option starts with a number (e.g., 6406534159824).
    *   Each option then presents a string that resembles a log entry. The log entries contain elements like:
        *   IP addresses (e.g., 192.168.1.1, 203.0.113.7)
        *   Date and time (e.g., \[12/Dec/2024:14:05:59 -0500], \[14/Dec/2024:16:45:11 -0500])
        *   HTTP request information (e.g., "GET /image.jpg HTTP/1.1", "POST /image.jpg INVALID")
        *   Status codes (e.g., 200)
        *   Bytes transferred (e.g., 1234, 3500)
        *   User agent string (e.g., "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

Question 2: Fields needed to filter “POST requests under /images/ from 15:00 to 18:00 on Mondays”

To filter such logs, we need:

Time → for the hour and the day (Monday)

Method → to filter POST

URL → to filter /images/

So, the correct minimal set is:

 :white_check_mark:  Time, Method, URL

Time → needed  :white_check_mark: 

Method → needed  :white_check_mark: 

URL → needed  :white_check_mark: 

Referer → not needed, but not harmful

So this option includes all the necessary fields, just with one extra — which doesn’t invalidate it.

**Image: 1000042548**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a multiple-choice question, likely from an online quiz or test. It presents a question related to filtering HTTP POST requests based on specific criteria. The image shows the question text, followed by a list of four possible answer options. Each option is preceded by a numerical identifier and a symbol indicating whether it's the correct answer (green checkmark) or an incorrect answer (red "X").

**2. Text Content:**

*   **Question Label:** Multiple Choice Question
*   **Question:** "Which of the following fields are necessary to filter "POST requests made for pages under /images/ from 15:00 to 18:00 on Mondays"?"
*   **Options:**
    *   6406534159828. ✅ Time, Request, Method, URL
    *   6406534159829. ❌ Time, Method, Status, Size
    *   6406534159830. ❌ Time, Method, URL, Referer
    *   6406534159831. ❌ Time, Status, URL, Server

**3. Context and Purpose:**

The image is designed to assess the user's understanding of HTTP requests and the fields that are relevant for filtering them. The question focuses on filtering POST requests for a specific directory ("/images/") within a certain time frame (15:00 to 18:00) and on a specific day (Mondays). The purpose is to determine if the user knows which fields in an HTTP request are essential for applying these filters.

**4. Technical Details:**

The question pertains to web development and network analysis. The fields mentioned in the options (Time, Request, Method, URL, Status, Size, Referer, Server) are all attributes associated with HTTP requests and responses.

*   **Time:** The timestamp of the request.
*   **Request:** This is a general term, but in this context, it likely refers to the type of request (POST).
*   **Method:** The HTTP method used (e.g., POST, GET).
*   **URL:** The Uniform Resource Locator, specifying

Acc to solutions only option 6406534159827 is valid:

Status is numeric (200)

Method (GET), Protocol (HTTP/1.1), and URL (/index.html) are correct

All required fields are present and properly formatted

The other options were as follows:

9825 uses invalid protocol (INVALID)

9826 uses invalid status code (OK instead of numeric)

9824 has no critical issue — it is technically also valid (only uses a private IP 192.168.1.1, which is unusual but not invalid). So both 9824 and 9827 are valid, but the answer marked only 9827

**Image: 1000042545**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a multiple-choice question, likely from an online quiz or exam. It includes the question text, possible answers, and some metadata related to the question itself.

**2. Text Content:**

*   **Correct Marks: 2**
*   **Question Label: Multiple Choice Question**
*   **Question:** "Which HTTP method is idempotent, meaning multiple identical requests have the same effect as a single request?"
*   **Options:**
    *   6406534159747. \* POST
    *   6406534159748. ✓ PUT
    *   6406534159749. \* GET
    *   6406534159750. \* DELETE
*   **Sub-Section Number: 4**
*   **Sub-Section Id: 640653189815**
*   **Question Shuffling Allowed: Yes**

**3. Context and Purpose:**

The image is a snapshot of a question from a test or quiz focused on web development or computer science concepts, specifically HTTP methods and their properties. The question tests the understanding of the "idempotent" property of HTTP methods. The metadata (Sub-Section Number, Sub-Section ID, Question Shuffling Allowed) is likely used for organizing and managing the questions within the test system.

**4. Technical Details:**

*   The question is about HTTP methods (POST, PUT, GET, DELETE).
*   The key concept is "idempotency," which means that making the same request multiple times has the same effect as making it once.
*   The correct answer, as indicated by the checkmark (✓), is "PUT." PUT requests are idempotent because they replace the resource at a specific URI with the data provided in the request. Subsequent identical PUT requests will simply overwrite the resource with the same data, resulting in the same final state.
*   The asterisk (*) next to the other options (POST, GET, DELETE) likely indicates that they are incorrect. POST is not idempotent, as multiple POST requests can create multiple resources. GET requests are idempotent because they only retrieve data and don't modify

Correct Answer(s):

 :white_check_mark:  PUT – Correct: It replaces the resource entirely. Multiple identical PUTs = same result.

 :white_check_mark:  GET – Also correct: It only fetches data, no side-effects. Multiple GETs = same result.

 :white_check_mark:  DELETE – Technically correct: Deleting the same resource multiple times has the same result as deleting once (resource stays deleted).

Incorrect Answer:

 :cross_mark:  POST – Not idempotent. Each POST usually creates a new resource or changes server state.

(This is the mistake on my part that I put the ans as POST as I thought since 3/4 are idempotent and one is not I should select the odd one out but I hope this could be resolved)

Thank you

---

## Reply 1
**Author**: Koustubh Ramakrishnan
**Posted**: 2025-04-15T17:19:29.506Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/2

Agree & second all thoughts shared by @24f2003130 above.

I also wanted to clarify on this question on filtered entries. The question mentions that a list filtered_entries is being created , and with the way the question is structured it seems like the filtering conditions mentioned in the question have already been applied. In that case `len(filtered entries)` seems to be correct. However the right answer is marked ‘None of these’ .

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a multiple-choice question (MCQ) from what appears to be an online exam or quiz. It includes the question number, ID, type, correct marks, the question itself, and a set of possible answers.

**2. Text Content:**

*   **Question Number:** 309
*   **Question Id:** 6406531231230
*   **Question Type:** MCQ
*   **Correct Marks:** 1
*   **Question Label:** Multiple Choice Question
*   **Question:** "After filtering the log entries (in a list filtered\_entries), which of the following is the best way to count the number of requests with a 404 status code for pages under /error/?"
*   **Options:**
    *   6406534159860. ❌ Use len(filtered\_entries)
    *   6406534159861. ❌ Use len(entries)
    *   6406534159862. ❌ Use sum(1 for entry in entries)
    *   6406534159863. ✅ None of these

**3. Context and Purpose:**

The image presents a question related to programming or data analysis, specifically dealing with log entries and HTTP status codes. The question asks for the best way to count the number of 404 errors for pages under the "/error/" directory after the log entries have been filtered. The options provide different code snippets or approaches to achieve this.

**4. Technical Details:**

*   The question involves understanding how to process a list of log entries.
*   The term "filtered\_entries" suggests that a list has already been created containing only the relevant log entries.
*   The options use Python-like syntax:
    *   `len()` is a function to get the length of a list.
    *   `sum(1 for entry in entries)` is a generator expression that sums 1 for each entry in the list, effectively counting the entries.
*   The question is asking about the most efficient or appropriate way to count the entries after filtering.

The valid log entry had me stumped too, option 1 and 4 both look absolutely fine yet only option 4 is marked correct.

Also, only POST request is not idempotent, all other requests are idempotent yet only PUT is marked correct.

Request you to please clarify and consider these points.

---

## Reply 2
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-15T18:13:03.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/3

Yes @carlton the wording of the question made it seem like the filters were already applied on the list `filtered_entries`.

---

## Reply 3
**Author**: Prasanna
**Posted**: 2025-04-16T10:08:58.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/4

Clarifications on Queries

**Which of the following is a valid log entry based on the provided format?**

Due to a technical issue in the portal, both options 1 and 4 are correct answers. The final scoring has been adjusted accordingly, and full marks will be awarded for either response.

**HTTP method is idempotent**

This question has been excluded from scoring as three methods (GET, PUT, and DELETE) are idempotent, with only POST being non-idempotent.

**Entries with 404 status code**

Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.

**Which of the following fields are necessary to filter “POST requests made for pages under /images/ from 15:00 to 18:00 on Mondays”?**

Option A (Time, Request, Method, URL) is correct because:

Option B includes Size and Status, which aren’t needed for filtering by time, method, and URL
Option C includes Referer, which is unnecessary unless filtering by source page
Option D includes Status and Server, which aren’t relevant for this specific filtering requirement

---

## Reply 4
**Author**: Shambhavi Verma
**Posted**: 2025-04-16T10:15:01.944Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/5

Thank you for the clarification provided regarding Question 4 and resolution of errors in other questions. I understand the reasoning behind choosing Option A (Time, Request, Method, URL). However, I respectfully believe Option C (Time, Method, URL, Referer) is more accurate for the following reasons:

Redundancy in Option A:

The Request field already contains the HTTP method, URL, and protocol (e.g., “POST /images/logo.png HTTP/1.1”). Including both Request and separate Method and URL fields introduces redundancy. If we already extract Method and URL separately for filtering, the full Request field becomes unnecessary.

Simplicity in Filtering:

Filtering for “POST requests under /images/” from 15:00 to 18:00 on Mondays can be done using:

Time → for checking the hour and weekday.

Method → to filter only POST.

URL → to ensure the request is under /images/.

Thus, Option C (Time, Method, URL, Referer) already includes all needed fields. While Referer is not essential, it doesn’t interfere with the filtering and might be useful in future extended filtering cases (e.g., source tracking). Therefore, Option C is complete and accurate without being redundant.

Consistency with Log Parsing Practices:

In most log analysis scripts or systems (e.g., Python’s re or pandas parsing of logs), Method and URL are parsed from Request for separate use. This further supports the idea that including Request alongside Method and URL is not best practice.

---

## Reply 5
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-16T18:28:35.206Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/6

Sir, regarding point 3, score-checker tells a different story. While all the other changes have been made with the same reflecting in the score, that question still says “The question and answer remain the same . No changes required”, which is different from your post.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a row from a table or spreadsheet. It contains several columns with different types of data. The background is a light gray.

**2. Any text content visible:**

The text content in each column is as follows:

*   **Column 1:** "31"
*   **Column 2:** "6406531231230"
*   **Column 3:** "MCQ"
*   **Column 4:** "W"
*   **Column 5:** "0"
*   **Column 6:** "6406534159860"
*   **Column 7:** "6406534159863"
*   **Column 8:** "1.00"
*   **Column 9:** "Not Modified"
*   **Column 10:** "The question and answer remain the same. No changes required"

**3. The context or purpose of what's displayed:**

The content appears to be related to a question bank or assessment system. Here's a possible interpretation:

*   "31" could be an item number or ID.
*   "6406531231230" and "6406534159860", "6406534159863" are likely unique identifiers for the question and related data.
*   "MCQ" likely stands for Multiple Choice Question, indicating the question type.
*   "W" could represent the weight or difficulty level of the question.
*   "0" could be a flag or status code.
*   "1.00" might represent a score or point value for the question.
*   "Not Modified" indicates that the question has not been changed.
*   "The question and answer remain the same. No changes required" further confirms that no updates are needed for this particular question.

**4. Technical details:**

Given the context, the data likely resides in a database or data store. The columns represent fields in a table. The image is a snapshot of a single record from that

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a multiple-choice question, likely from an online test or quiz. It includes the question number, ID, type, correct marks, the question text, and the possible answer options.

**2. Text Content:**

*   **Question Number:** 309
*   **Question Id:** 6406531231230 (highlighted in green)
*   **Question Type:** MCQ (Multiple Choice Question)
*   **Correct Marks:** 1
*   **Question Label:** Multiple Choice Question
*   **Question Text:** "After filtering the log entries (in a list filtered\_entries), which of the following is the best way to count the number of requests with a 404 status code for pages under /error/?"
*   **Options:**
    *   6406534159860. Use `len(filtered_entries)`
    *   6406534159861. Use `len(entries)`
    *   6406534159862. Use `sum(1 for entry in entries)`
    *   6406534159863. None of these (marked with a green checkmark)

**3. Context and Purpose:**

The image presents a question related to programming or data analysis, specifically dealing with log entries and counting requests with a specific status code (404) for a particular URL path (/error/). The question aims to assess the understanding of how to efficiently count elements in a filtered list or collection.

**4. Technical Details:**

The question involves Python-like syntax. The options suggest different ways to count elements in a list:

*   `len(filtered_entries)`: This would return the number of elements in the `filtered_entries` list.
*   `len(entries)`: This would return the number of elements in the `entries` list.
*   `sum(1 for entry in entries)`: This is a list comprehension that iterates through the `entries` list and sums 1 for each entry, effectively counting the number of elements.

The correct answer is marked as "None of these",

Can you please look into it?

Thanks

Regards,

Shivaditya

---

## Reply 6
**Author**: Shambhavi Verma
**Posted**: 2025-04-16T18:47:03.645Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/7

@iamprasna sir , the scores have been updated on the dashboard as well and the answer for the question in point 3 is still the same

Additionally , sir I have attached the snapshot of a dec’24 TDS PYQ which is a replica of this question and the answer for the same is mention the first option.

**Image: 1000042796**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question (MCQ) from what appears to be an online exam or quiz. It presents a programming-related problem and four possible solutions. The first option is marked as correct with a green checkmark, while the other three are marked as incorrect with a red "x".

**2. Text Content:**

*   **Question Number:** 351
*   **Question Id:** 6406531040283
*   **Question Type:** MCQ
*   **Correct Marks:** 1
*   **Question Label:** Multiple Choice Question
*   **Question Text:** "After filtering the log entries (in a list `filtered_entries`), which of the following is the best way to count the number of successful GET requests for pages under `/telugump3/?`"
*   **Options:**
    *   `6406533514340.` Use `len(filtered_entries)` (Marked as correct)
    *   `6406533514341.` Use `len(entries)` (Marked as incorrect)
    *   `6406533514342.` Use `sum(1 for entry in entries)` (Marked as incorrect)
    *   `6406533514343.` Use `count(filtered_entries)` (Marked as incorrect)

**3. Context and Purpose:**

The question is designed to test the user's understanding of how to count elements in a list after filtering. The context is likely related to web server log analysis, where you might want to count the number of successful requests for a specific page.

**4. Technical Details:**

The question involves Python code snippets.

*   `len(filtered_entries)`: This is the correct way to get the number of elements in the `filtered_entries` list.
*   `len(entries)`: This would count the number of elements in the original `entries` list, not the filtered one.
*   `sum(1 for entry in entries)`: This is a valid way to count the number of elements in the `entries` list

The link for the same has been attached for your referance

      [drive.google.com](https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk)

      [](https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk)

[IIT M FOUNDATION DIPLOMA FN EXAM QDF2 22 Dec 2024.pdf](https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk)

Google Drive file.

---

## Reply 7
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-16T19:04:11.803Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/8

That’s a great find. They’re the same question with just different parameters. Please look into it @iamprasna sir.

---

## Reply 8
**Author**: Shambhavi Verma
**Posted**: 2025-04-17T04:17:09.060Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/9

@carlton sir and @Jivraj sir please look into this question and clarify this

Thank you

---

## Reply 9
**Author**: Swati Kapoor
**Posted**: 2025-04-17T04:20:13.544Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/10

Hi,

From where are you checking the transcripts? I’m not able to see the answer transcripts in the score checker app.

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   **Header:** A dark blue header contains the university logo (Indian Institute of Technology Madras) on the left and the title "SCORE CHECKER" next to it. On the right side of the header, there are three links: "Transcript," "Home," and "Logout," each with a corresponding icon (document, house, and arrow pointing out of a box, respectively).
*   **Information Banner:** A light blue banner displays a message to the user.
*   **Data Table:** A table displays score information. The table has the following columns:
    *   EMAIL
    *   HALLTICKET
    *   COURSE CODE
    *   TOTAL SCORE
    *   VIEW (with an eye icon)

**2. Text Content:**

*   **Header:**
    *   SCORE CHECKER
    *   Transcript
    *   Home
    *   Logout
*   **Information Banner:** "This is before the sign-off of scores; it may change after the sign-off."
*   **Table Headers:**
    *   EMAIL
    *   HALLTICKET
    *   COURSE CODE
    *   TOTAL SCORE
    *   VIEW
*   **Table Data:**
    *   EMAIL: 23ds3000185@ds.study.iitm.ac.in
    *   HALLTICKET: S2DAD23DS3000185
    *   COURSE CODE: SE2002
    *   TOTAL SCORE: 70

**3. Context/Purpose:**

The image shows a user interface (UI) for a score checking system, likely for students at the Indian Institute of Technology Madras (IITM). The system allows students to view their scores for different courses. The banner indicates that the scores displayed are preliminary and subject to change before the official sign-off.

**4. Technical Details:**

*   The image appears to be a screenshot of a web application.
*   The table structure suggests the use of HTML tables or a similar UI framework for displaying data.
*   The presence of "Transcript," "Home," and "Logout" links indicates a user authentication and navigation system.
*   The "VIEW" column with the eye icon likely provides a link or

---

## Reply 10
**Author**: Shambhavi Verma
**Posted**: 2025-04-17T04:22:31.946Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/11

Click on the eye button …then you will be able to view your transcript

---

## Reply 11
**Author**: Swati Kapoor
**Posted**: 2025-04-17T04:25:22.034Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/12

Thanks for the reply, but I only see the question id’s and answer id’s, not able to find the transcripts.

**Image: image**
Here's a detailed description of the image:

**1. Overall Content:**

*   The image shows a user interface (UI) table or grid displaying the results of a "SCORE CHECKER" application. It appears to be a web-based application.
*   The table presents data related to individual questions, including the question ID, type, result, score, selected option, correct option, mark, modification status, and remarks.

**2. UI Elements:**

*   **Table/Grid:** The primary element is a table with columns for various question attributes.
*   **Headers:** The table has clear column headers: "S.NO.", "Question ID", "Question Type", "Result", "Score", "Selected Option", "Correct Option", "Mark", "Modification of Question", and "Remarks".
*   **Rows:** Each row represents a single question and its associated data.
*   **Highlighting:** Row 4 is highlighted in yellow, drawing attention to a specific question.
*   **Navigation:** In the top right corner, there are navigation links: "Transcript", "Home", and "Logout".

**3. Text Content:**

*   **Title:** "SCORE CHECKER" is prominently displayed at the top.
*   **Column Headers:** As mentioned above, the table has descriptive column headers.
*   **Data:** The table contains data for each question, including:
    *   Question IDs (e.g., "6406531252398")
    *   Question Type: "MCQ" (Multiple Choice Question)
    *   Result: "C" (Correct) or "W" (Wrong)
    *   Score: Numerical scores (e.g., "0", "1.00")
    *   Selected Option: Option IDs (e.g., "6406534219005")
    *   Correct Option: Option IDs (e.g., "6406534219005")
    *   Mark: Numerical marks (e.g., "0", "1.00")
    *   Modification of Question: "Not Modified" or a Question ID (in the highlighted row)
    *   Remarks: Comments or notes (e.g., "-", "Remains the

---

## Reply 12
**Author**: Shambhavi Verma
**Posted**: 2025-04-17T04:28:25.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/13

It seems that the option to download the answer key has been removed. However, you could consider reaching out to someone in the group or checking the dashboard for  solution pdf of question paper. You can then match the questions in order, even if the IDs don’t align exactly—it should still give you a general idea. From there, you can proceed accordingly.

---

## Reply 13
**Author**: Shivaditya Bhattacharya
**Posted**: 2025-04-17T18:05:30.227Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/14

@iamprasna @carlton Please look into it once. According to point 3 of @iamprasna’s post, I should get full credit for that question and it will take me to a perfect 100 score in ET from the current 97. I brought this into attention before the scores were pushed to the dashboard.

Regards,

Shivaditya

---

## Reply 14
**Author**: Prasanna
**Posted**: 2025-04-21T10:46:35.817Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/15

The correction has been done to the following question for both the FN and AN sessions. You must be able to see the change in scores shortly

**Entries with 404 status code**

Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.

---

## Reply 15
**Author**: Shambhavi Verma
**Posted**: 2025-04-21T13:51:30.076Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/queries-regarding-end-term-exam-solutions/172707/16

Thank you sir for acknowledging our requests and resolving the error

---
