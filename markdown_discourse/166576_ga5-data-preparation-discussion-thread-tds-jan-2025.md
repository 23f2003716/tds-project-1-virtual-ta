# GA5 - Data Preparation - Discussion Thread [TDS Jan 2025]

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/1

## Topic Metadata
- **ID**: 166576
- **Slug**: ga5-data-preparation-discussion-thread-tds-jan-2025
- **Created**: 2025-02-08T14:39:41.393Z
- **Views**: 864
- **Replies**: 61
- **Likes**: 30
- **Tags**: term1-2025, graded-assignment, week-5

## Original Post
**Author**: Anand S
**Posted**: 2025-02-08T14:39:41.571Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/1

Please post any questions related to [Graded Assignment 5 - Data Preparation](https://exam.sanand.workers.dev/tds-2025-01-ga5).

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline:  2025-02-15T18:30:00Z

@Jivraj @Saransh_Saini @carlton

---

## Reply 1
**Author**: Anand S
**Posted**: 2025-02-08T14:40:01.609Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/2

*No content*

---

## Reply 2
**Author**: Hisham Kadambot
**Posted**: 2025-02-10T06:17:22.155Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/3

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a web page or application interface.
*   There are three distinct sections, each contained within a rounded rectangle with different background colors.
*   A "Logout" button is present.
*   A loading indicator (a circular "C" with animation implied by the text "Loading questions...") is visible.

**2. Text Content:**

*   **Top:** "You are logged in as 23f1002630@ds.study.iitm.ac.in."
*   **Button:** "Logout"
*   **Section 1 (Green):**
    *   "Recent saves (most recent is your official score)"
    *   "No recent saves"
*   **Section 2 (Blue):**
    *   "Loading questions..."
*   **Section 3 (Red):**
    *   "Error!"
    *   "Sorry, we couldn't load the questions. That's strange."
    *   "Cannot read properties of undefined (reading '1')"
    *   "Please contact the exam team for assistance."

**3. Context and Purpose:**

*   The interface appears to be related to an online exam or assessment system.
*   The user is logged in with a specific ID/email address.
*   The "Recent saves" section suggests the ability to save progress during the exam.
*   The "Loading questions..." section indicates that the system is attempting to retrieve the exam questions.
*   The "Error!" section indicates that there was a problem loading the questions, and the user is advised to contact the exam team.

**4. Technical Details:**

*   The error message "Cannot read properties of undefined (reading '1')" is a common JavaScript error. It means that the code is trying to access a property (specifically, the property at index '1') of a variable that is currently `undefined`. This often happens when data is expected but not received, or when there's a problem with data structure.
*   The error suggests a potential issue with the data being fetched from the server or with the way the data is being processed on the client-side.

i can’t load my questions

---

## Reply 3
**Author**: Anand S
**Posted**: 2025-02-10T07:29:12.849Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/4

@23f1002630 - thanks for raising this. It’s fixed and won’t re-occur for anyone.

**What happened?** I picked random duration from the video of 10-40 seconds, but forgot to ensure that the end time should not exceed the video length. That’s what I fixed.

---

## Reply 4
**Author**: Hisham Kadambot
**Posted**: 2025-02-10T11:25:56.044Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/5

**Image: image**
Here's a detailed description of the image:

**1. UI Elements:**

*   The image shows a user interface (UI) with a dark background.
*   There are three distinct rectangular sections, each with a different background color.
*   At the bottom, there are two buttons: "Check all" (green) and "Save" (blue).

**2. Text Content:**

*   **Top Section (Green):**
    *   "Recent saves (most recent is your official score)"
    *   "No recent saves"
*   **Middle Section (Blue):**
    *   "Loading questions..." (accompanied by a loading spinner icon)
*   **Bottom Section (Red):**
    *   "Error!"
    *   "Sorry, we couldn't load the questions. That's strange."
    *   "Cannot read properties of undefined (reading '1')"
    *   "Please contact the exam team for assistance."
*   **Buttons:**
    *   "Check all"
    *   "Save"

**3. Context/Purpose:**

*   The UI appears to be part of an online exam or quiz platform.
*   The top section displays recent saves, but currently, there are none.
*   The middle section indicates that the questions are being loaded.
*   The bottom section displays an error message, indicating that the questions could not be loaded due to a technical issue (specifically, a "Cannot read properties of undefined" error).
*   The user is advised to contact the exam team for assistance.
*   The "Check all" and "Save" buttons suggest that the user would normally be able to select all questions and save their progress.

**4. Technical Details:**

*   The error message "Cannot read properties of undefined (reading '1')" is a common JavaScript error. It means that the code is trying to access a property (in this case, '1') of a variable that is currently undefined. This often happens when data is not loaded correctly or when there's a problem with the data structure.
*   The error suggests a bug in the front-end code of the exam platform.

It was solved but again I’m facing the same issue

---

## Reply 5
**Author**: Hisham Kadambot
**Posted**: 2025-02-10T18:54:19.804Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/6

@s.anand @Jivraj  I’m still facing the issue.

---

## Reply 6
**Author**: Nilay Chugh
**Posted**: 2025-02-11T16:21:34.546Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/7

i guess there’s some issue in 5th question as i have correctly filtered the data in OpenRefine 2-3 times but still getting incorrect in the portal.

---

## Reply 7
**Author**: Carlton D'Silva
**Posted**: 2025-02-12T12:52:01.867Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/8

OpenRefine question has historically been a tricky question to get right. Check out some past TA sessions in previous term for solving it, or previous discourse posts.

Kind regards

---

## Reply 8
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-13T08:51:51.360Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/9

DOUBT IN -Q 9 Sir @carlton

Miranda followed the elusive figure.  In the dim corridor,......................

I listened it ,every words and spellings are matching still this error:

**Error: Words are too different**

---

## Reply 9
**Author**: Nelson Jochim DSouza
**Posted**: 2025-02-13T13:56:56.738Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/10

Cleaning Data with OpenRefine

Kindly check the question and the answer. I found below cities for São Paulo.

However, it says my answer is incorrect.

How many units of Bacon were sold in São Paulo on transactions with at least 151 units?

city
Sao Paolo
Sao Paoulo
Sao Paulo
Sao Pualo
Sau Paulo
São Paulo

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a portion of a spreadsheet, likely from a program like Microsoft Excel or Google Sheets. It displays tabular data with columns and rows. The first row appears to be a header row, defining the columns. There are several rows of data below the header. Filter icons are visible in the header row, indicating that filtering is enabled for each column.

**2. Any text content visible:**

*   **Column Headers:**
    *   A1: "city"
    *   B1: "product"
    *   C1: "sales"
*   **Data:**
    *   A2: "Sau Paulo"
    *   A3: "Sao Pualo"
    *   A4: "Sao Paoulo"
    *   A5: "Sao Paolo"
    *   A6: "Sao Pualo"
    *   B2: "Bacon"
    *   B3: "Bacon"
    *   B4: "Bacon"
    *   B5: "Bacon"
    *   B6: "Bacon"
    *   C2: "488"
    *   C3: "522"
    *   C4: "650"
    *   C5: "275"
    *   C6: "936"
    *   C7: "2871"

**3. The context or purpose of what's displayed:**

The spreadsheet appears to be tracking sales data for a specific product (Bacon) across different cities. The columns represent the city, the product sold, and the sales amount. The last row shows the sum of the sales column.

**4. Technical details if it's a code screenshot or technical diagram:**

This is not a code screenshot or technical diagram. It's a visual representation of data within a spreadsheet application. The filter icons suggest that the user can sort or filter the data based on the values in each column. The sum in the last row is likely calculated using a formula within the spreadsheet program.

---

## Reply 10
**Author**: Aniruddha Mukherjee
**Posted**: 2025-02-14T16:15:42.519Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/11

Wrong / Confusing question Prof

The top line mentions “Saturdays” whereas the bottom line mentions “Sundays”

Please clarify “SUNDAY” or “SATURDAY”?

**Image: grab-IIT-Madras--Microsoft Edge_at_21.44.39_on__14-02-2025__003253**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a document outlining a data analysis task related to web server logs. It describes the context, the data source, the task itself, and the potential benefits of completing the task. It also provides details about the structure and format of the log files.

**2. Text Content:**

The document contains the following key text elements:

*   **Title:** "Peak Usage Analysis for Regional Content"
*   **Website Description:** `s-anand.net` is described as a personal website with region-specific music content, with a popular "telugu" section.
*   **Motivation:** The author noticed unusual traffic patterns on weekend evenings and wants to optimize server resources.
*   **Specific Interests:** The analysis focuses on successful requests to the "telugu" section during peak hours on Saturdays.
*   **Analysis Parameters:**
    *   Time Window: From 13:00 until before 23:00.
    *   Request Type: Only GET requests.
    *   Success Criteria: HTTP status codes between 200 and 299.
    *   Data Source: Apache logs for May 2024 (GZipped, 258,074 rows).
*   **Log File Characteristics:**
    *   GMT-0500 timezone.
    *   Fields separated by spaces, most fields quoted by double quotes (except the Time field).
    *   Some lines have formatting issues (41 rows with unique quoting).
*   **"Your Task":** As a data analyst, determine the number of successful GET requests for "telugu" pages on Saturdays between May 13 and 23, 2024.
*   **Benefits of Analysis:**
    *   Scale Resources.
    *   Content Planning.
    *   Marketing Insights.
*   **Log File Details:**
    *   GZipped Apache log file (61MB) with 258,074 rows.
    *   Each row is an Apache web log entry for `s-anand.net` in May 2024.
*   **Field Descriptions:**
    *   IP: IP address of the visitor.
    *

---

## Reply 11
**Author**: Aniruddha Mukherjee
**Posted**: 2025-02-14T16:19:36.462Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/12

Update: I tried for both (thank god for filters in Excel) and Sunday is what the question is asking for. The Instruction above for “Saturday” is incorrect- maybe the logic generating different questions for different students can be tweaked-

Thank you

---

## Reply 12
**Author**: Aniruddha Mukherjee
**Posted**: 2025-02-14T17:47:55.912Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/13

I’ve attempted this question several times and I’m fairly certain that the answer to this question is incorrect. I’d be grateful if the answer to this question was re-checked. I can share the answer I’m certain about here, however I do not think it would be prudent to do so given this is a public forum.

Please consider my request and double check-

@Jivraj, @carlton

Thank you

**Image: grab-IIT-Madras--Microsoft Edge_at_23.15.25_on__14-02-2025__003255**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a case study document. It outlines a problem faced by a company called ReceiptRevive Analytics, a data recovery and business intelligence firm, and the task assigned to a data recovery analyst to solve it.

**2. Text Content:**

The document contains the following text:

*   **Title:** Case Study: Recovering Sales Data for ReceiptRevive Analytics
*   **Introduction:** ReceiptRevive Analytics is described as a company specializing in processing legacy sales data from paper receipts using OCR. The OCR process sometimes produces incomplete JSON data due to the condition of the receipts.
*   **Client:** One of ReceiptRevive's major clients is RetailFlow Inc., which operates brick-and-mortar stores and has an archive of old receipts. RetailFlow Inc. needs to recover total sales information from digitized receipts.
*   **Data Structure:** The provided JSON data contains 100 rows, with each row representing a sales entry. Each entry is expected to include four keys:
    *   **city:** The city where the sale was made.
    *   **product:** The product that was sold.
    *   **sales:** The number of units sold (or sales revenue).
    *   **id:** A unique identifier for the receipt.
*   **Problem:** Due to damage during digitization, the JSON entries are truncated, and the `id` field is missing. RetailFlow Inc. is primarily interested in the aggregate sales value.
*   **Your Task:** This section outlines the tasks for the data recovery analyst:
    1.  **Parse the Sales Data:** Read the provided JSON file (100 rows) and extract the `sales` figures from each row, even with the missing `id`.
    2.  **Data Validation and Cleanup:** Ensure the data is properly handled, focusing on the `sales` values since the `id` is missing.
    3.  **Calculate Total Sales:** Sum the `sales` values across all 100 rows.
*   **Benefits:** Successfully recovering and aggregating the sales data will enable RetailFlow Inc. to:
    *   Reconstruct Historical Sales Data
    *   Inform Business Decisions
    *   Enhance Data Recovery Processes
    *   Build Client Trust
*   **Download Link:**

---

## Reply 13
**Author**: NamanBeri
**Posted**: 2025-02-15T16:24:23.831Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/14

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a portion of a spreadsheet, likely from a program like Microsoft Excel or Google Sheets. It shows data organized into columns and rows. The columns are labeled with headers, and the rows contain specific data entries.

**2. Any text content visible:**

Here's a breakdown of the text content:

*   **Column Headers:**
    *   H: "Country (Normalised)"
    *   I: "DATE"
    *   J: "Product"
    *   K: "Sales"
    *   L: "Cost"

*   **Data Rows:** The data rows contain the following information:
    *   **Country (Normalised):** All rows visible show "United Arab Emirates"
    *   **DATE:** A series of dates in YYYY-MM-DD format, including:
        *   2023-07-02
        *   03-15-2023
        *   2023-04-02
        *   06-29-2022
        *   2023-02-04
        *   2023-07-13
        *   2023-10-18
        *   03-28-2023
        *   03-22-2023
        *   11-17-2023
        *   2023-10-13
        *   2023-04-06
        *   2022-10-11
        *   2023-05-29
        *   2022-06-04
        *   2023-01-15
        *   2023-04-28
    *   **Product:** All rows visible show "Kappa"
    *   **Sales:** Numerical values representing sales figures (e.g., 1314.00, 4853.00, 8676.00, etc.)
    *

this is my data before date filter - for question 1 please conform am i doing correct. and tell how to do the date filtering as some are in mm-dd-yyyy or yyyy-mm-dd format.

as this data is less i did it manually

SUM OF COST
14891.00

SUM OF SALES
31004.00

TOTAL
45895.00

TOTAL MARGIN
0.351083996

but this is not correct please guide

---

## Reply 14
**Author**: Anand S
**Posted**: 2025-02-15T16:45:07.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/15

@23f1003186 – thanks for flagging this. You’re right. I’ve fixed this error.  :pray:

---

## Reply 15
**Author**: Aniruddha Mukherjee
**Posted**: 2025-02-15T17:05:24.887Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/16

Any signal for this question?

@s.anand @carlton

---

## Reply 16
**Author**: Anand S
**Posted**: 2025-02-15T17:13:23.480Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/17

@23f1003186 thanks again for flagging this. This is fixed, too.  :pray:

---

## Reply 17
**Author**: NamanBeri
**Posted**: 2025-02-15T17:19:27.591Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/18

tried google sheets - it autoformatted my date data, also i realized later i was applying the formula the wrong way.

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a table of data, likely from a spreadsheet or data visualization tool. The table has several columns: "Country (Normalised)", "DATE", "Product", "Sales", and "Cost".  The table contains multiple rows of data.

**2. Any text content visible:**

*   **Column Headers:**
    *   Country (Normalised)
    *   DATE
    *   Product
    *   Sales
    *   Cost
*   **Data Rows:**
    *   United Arab Emirates
    *   2023-02-07, 2022-06-29, 2023-02-04, 2022-11-10, 2022-06-04, 2023-01-15
    *   Kappa (repeated in each row)
    *   Sales figures: 1314.00, 9370.00, 5488.00, 6307.00, 7810.00, 2029.00
    *   Cost figures: 4892.00, 2214.00, 2744.00, 287.00, 4755.00, 4891.00

**3. The context or purpose of what's displayed:**

The table appears to be a sales report or a data extract showing sales and cost information for a specific product ("Kappa") in the United Arab Emirates over a period of time. The data includes the date of the sale, the sales amount, and the associated cost. The "Country (Normalised)" column suggests that the country names might have been standardized for consistency.

**4. Technical details:**

*   The presence of filter icons (funnel-shaped) next to the "DATE", "Product", "Sales", and "Cost" column headers indicates that the table is likely interactive, allowing users to filter the data based on specific criteria.
*   The data is formatted with decimal places for the "Sales" and "Cost

Date formatted and filtered successfully

---

## Reply 18
**Author**: Ansh bansal
**Posted**: 2025-02-15T23:22:12.712Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/19

Can you provide the link for that session.

---

## Reply 19
**Author**: NamanBeri
**Posted**: 2025-02-16T04:42:44.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/20

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a table or grid-like structure, likely from a data visualization or reporting tool. It presents data organized into columns and rows. The columns appear to represent different categories or dimensions of data.

**2. Any text content visible:**

*   **Column Headers:**
    *   "\_ \_ \_ - city" (with a dropdown arrow)
    *   "\_ \_ \_ - product" (with a dropdown arrow)
    *   "\_ \_ \_ - sales" (with a dropdown arrow)
*   **Data Rows:**
    *   "London" (repeated in the "city" column)
    *   "Computer" (repeated in the "product" column)
    *   Numerical values in the "sales" column: 406, 916, 821, 457, 922, 610, 111, 109, 866, 975

**3. The context or purpose of what's displayed:**

The table seems to represent sales data, broken down by city and product. Each row likely represents a specific instance of a product sale in a particular city, with the "sales" column indicating the quantity or value of that sale. The repeated "London" and "Computer" values suggest that the data is filtered or grouped to show sales of computers in London.

**4. Technical details:**

*   The presence of dropdown arrows in the column headers suggests that the table is interactive, allowing users to filter, sort, or group the data based on the values in each column.
*   The data is structured in a relational format, with each row representing a record and each column representing an attribute.
*   The consistent formatting and alignment of the data indicate that it is likely generated by a software application or database system.

How many units of Computer were sold in London on transactions with at least 39 units?

please check my answer is not correct - (6193)

please guide

---

## Reply 20
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-16T13:52:28.891Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/21

How many units of Computer were sold in Shenzhen on transactions with at least 43 units?

city
product
sales

Shenzheen
Computer
296

Shenzhen
Computer
824

ShenZhen
Computer
931

Shenzheen
Computer
976

Shenzheen
Computer
108

Shenzheen
Computer
623

Shenzen
Computer
386

Shenzheen
Computer
827

4971

why is this incorrect ? what am i missing ? @s.anand @carlton

---

## Reply 21
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-16T13:56:30.308Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/22

This one is matching every word still  that error . why sir @s.anand

---

## Reply 22
**Author**: Saniya Naaz
**Posted**: 2025-02-16T14:15:04.290Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/23

yes I`m also getting the incorrect answer for question 5 even though I have clustered the city jakarta correctly.

How many units of Bike were sold in Jakarta on transactions with at least 163 units?

---

## Reply 23
**Author**: Ansh bansal
**Posted**: 2025-02-16T17:02:59.166Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/24

Same for me . I am also getting error of the answer i am getting from OpenRefine

---

## Reply 24
**Author**: Carlton D'Silva
**Posted**: 2025-02-18T04:21:53.103Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/26

*No content*

---

## Reply 25
**Author**: Guddu Kumar Mishra 
**Posted**: 2025-02-18T05:48:36.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/27

Sir please check Q 5,8,9 also

---

## Reply 26
**Author**: 23f3001356
**Posted**: 2025-02-18T12:23:57.766Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/28

@s.anand @carlton I have tried every method for the 5th question even brute force still I am getting same answer but it is saying incorrect.

---

## Reply 27
**Author**: ABHIJEET KUMAR 
**Posted**: 2025-02-18T14:06:03.082Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/30

@carlton i am also not able to do que 5th question …

Any hint

---

## Reply 28
**Author**: LAKSHAY
**Posted**: 2025-02-18T14:44:43.999Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/31

Respected @carlton

I am facing an issue with GA5 Q5, as my answer is being marked incorrect despite multiple attempts. I have processed data at OpenRefine .

To ensure accuracy, I also tried a manual approach by converting the JSON file to Excel and filtering the data, but I arrived at the same answer each time. However, the assignment portal still shows it as incorrect.

Sir Could you please check portal expected answer for this question.

Thankyou

---

## Reply 29
**Author**: Yogaswetha
**Posted**: 2025-02-19T09:33:34.904Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/32

@carlton Respected sir,

I have tried the 5 th question n no. of times but getting error as incorrect answer can i get any guidance on this please. Thankyou

---

## Reply 30
**Author**: Srividhya
**Posted**: 2025-02-19T08:24:26.521Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/34

@jivraj , @carlton, @s.anand

q5 give same answer which i am getting is incorrect. but i tried manually, python and openrefine, excel everything gives the same answer. please look into it.

---

## Reply 31
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-19T10:48:39.486Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/35

We have noted this issue and are looking into it.

---

## Reply 32
**Author**: Shashank Tripathi
**Posted**: 2025-02-19T11:07:26.313Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/36

In Question 8

I am getting this error

Please tell me how do i tackle this errror

Error: At root: Array length mismatch

---

## Reply 33
**Author**: Srividhya
**Posted**: 2025-02-19T11:30:59.015Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/37

thanku sir also q6 i got 52747 after cleaning the json and trying to extract using all methods 96 lines where reconstructed. but portal keep saying wrong for evry answer.pls check on this also

---

## Reply 34
**Author**: Maheshwar Ture
**Posted**: 2025-02-19T13:59:18.136Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/38

Q5 I tried with openfire and python script , both are giving me same answer but its not accepted please check . Also in task the ask is to identify " **Top-Performing City:** Determine which city has the highest total unit sales for the selected product and report the unit sales number." but on top of input box question is different “How many units of Table were sold in Mexico City on transactions with at least 159 units?”

---

## Reply 35
**Author**: Udipth
**Posted**: 2025-02-19T14:23:22.401Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/39

i think there is some bug in Q 1… it shows correct if in percentage I pass comma instead of decimal. kindly check. secondly by multiple logics i checked q 5 & Q 6… but it shows incorrect only. Kindly help

---

## Reply 36
**Author**: Nilay Chugh
**Posted**: 2025-02-19T15:45:17.806Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/40

can we get more specified error in q9? it just says, words are too different.

---

## Reply 37
**Author**: Saransh Saini
**Posted**: 2025-02-19T15:56:24.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/41

This message is for everyone struggling with Q5

Due to a backend error, the script was incorrectly evaluating your answers. That problem has been fixed and you must check once again.

If you are still getting it incorrect, better watch [Open Refine - Live Session ](https://drive.google.com/file/d/1iTygvMAQdNY9O09An0LZMyt2sFZufcLl/view?usp=sharing&t=4431)

---

## Reply 38
**Author**: Vicky Kumar
**Posted**: 2025-02-19T16:56:47.689Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/43

hellor sir my answer is 4764 after so many verification like excel python open refine etc but still it was saying it is wrong sir check answer please question no 4 related to 1. **Aggregate Sales by City:** After clustering city names, group the filtered sales entries by city and calculate the total units sold for each city.

2. **Identify the Top-Performing City:** Determine which city has the highest total unit sales for the selected product and report the unit sales number.

By performing this analysis, GlobalRetail Insights will be able to:

**Improve Data Accuracy:** Correct mis-spellings and inconsistencies in the dataset, leading to more reliable insights.
**Target Marketing Efforts:** Identify high-performing regions for the specific product, enabling targeted promotional strategies.
**Optimize Inventory Management:** Ensure that inventory allocations reflect the true demand in each region, reducing wastage and stockouts.
**Drive Strategic Decision-Making:** Provide actionable intelligence to clients that supports strategic planning and competitive advantage in the market.

How many units of Bacon were sold in Beijing on transactions with at least 28 units?

---

## Reply 39
**Author**: Udipth
**Posted**: 2025-02-19T17:11:49.323Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/44

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image is a screenshot of a web interface, specifically the "Get API key" section of Google AI Studio. It displays information related to API keys for the Gemini API. The UI elements include:

*   A sidebar on the left with navigation links (e.g., "Prompt," "Realtime," "Apps," "Model," "Create chat history," "Gallery," "Documentation," "User forum," "Blog").
*   A main content area with the title "API keys" and a subtitle "Quickly test the Gemini API."
*   A code snippet showing how to use the Gemini API with a `curl` command.
*   A button labeled "Create API key."
*   A table-like structure with column headers "Project number," "Project name," "API key," and "Created."
*   An error message displayed in a red box.

**2. Any text content visible:**

*   **Titles/Headings:** "AI Studio," "Get API key," "API keys," "Quickly test the Gemini API," "API quickstart guide," "Project number," "Project name," "API key," "Created."
*   **Code Snippet:** A `curl` command demonstrating how to make a request to the Gemini API. The request includes the API endpoint, content type, HTTP method (POST), and a JSON payload with a prompt "Explain how AI works."
*   **Button Label:** "Create API key"
*   **Error Message:** "APPLICATION\_ERROR;google.cloud.resourcemanager.v3/ProjectsV3.CreateProject;com.google.apps.Resource Manager project creation is disabled. Contact your administrator to enable this setting in th information.;AppErrorCode=9;StartTimeMs=1739985063200;unknown;ResFormat=uncompressed;[2002:a05:6a04:459d:b0:271:d3d1:83e3]:4004"
*   **Other Text:** "Your API keys are listed below. You can also view and manage your project and API keys in Google Cloud.", "Use code with caution.", "Remember to use API keys securely.

I am getting this error when trying to generate API key… Who I need to connect to allow me generate a key on my iitm email id

---

## Reply 40
**Author**: Saransh Saini
**Posted**: 2025-02-19T17:23:55.406Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/45

Hi @Algsoch

I have checked your dataset along with your params, and its perfectly correct. Try again and check your step.

Otherwise go and watch 18-Feb Live Session

---

## Reply 41
**Author**: LAKSHAY
**Posted**: 2025-02-19T17:35:57.454Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/46

@Saransh_Saini

Q5 fixed, thanks for fixing the issue.

Now we are struggling with Q8.

MY q8 is : Write a DuckDB SQL query to find all posts IDs after 2025-01-09T12:36:14.085Z with at least 1 comment with 4 useful stars, sorted. The result should be a table with a single column called `post_id` , and the relevant post IDs should be sorted in ascending order.

when i use below query, i get some some result, a table of post_id but error : **Error**: At root: Array length mismatch

**Reason**:  below query checking only 1st comment (`$[0]` refers to the first comment in the array) we have to check all comments not 1st.

But when i change the query to check any one comment its giving different types of error.

WITH filtered_posts AS (
  SELECT post_id
  FROM social_media
  WHERE timestamp >= '2025-01-09T09:48:01.303Z'
    AND EXISTS (
      SELECT 1
      FROM social_media AS sm
      WHERE json_extract_path_text(sm.comments, '$[0].stars.useful') IS NOT NULL
        AND CAST(json_extract_path_text(sm.comments, '$[0].stars.useful') AS INTEGER) > 4
    )
)
SELECT post_id
FROM filtered_posts
ORDER BY post_id ASC;

Kindly check if any issue with Q8.

May be my query is wrong or may be not.

Thankyou

---

## Reply 42
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T03:21:58.527Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/47

@lakshaygarg654

Your query construction is unnecessarily complicated and therefore will be difficult to debug.

Query construction is best done by thinking what you want at the end.

In this case its an ordered `post_id`

So thats where you begin:

SELECT post_id
FROM (
...
)
ORDER BY post_id

Doing this, produces the actual result without giving the logic yet.

Then at each stage you add the next stage of complexity.

You will still need the `post_id` for the *outermost layer* so you have to continue extracting it from the *inner layers* of the nested query.

...
...
FROM (
   SELECT post_id, ( ... ) as max_stars
   FROM social_media
   WHERE time_stamp >= (whatever the parameter you have been given)
      AND max_stars >= (whatever the parameter for min stars you have been given)
)
...
...

Then the final layer of the nest

...
...
(

) as max_stars
...
...

You are not expecting me to solve the whole question right? (Hint: the inner most extraction involves JSON or “structure” extraction, which is a powerful capability)

But I hope you understand the logic of SQL which is a very elegant set theory language which is why it has lasted for over 4 decades.

Think clearly at each stage what do you need. Start with the answer and work backwards, extracting at each stage the logical items you require for the outer layer to be functional.

Kind regards

---

## Reply 43
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T03:31:24.326Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/48

Its been done. You will get a more detailed error now. And we have relaxed the number of errors allowed (it actually did have a tolerance limit but it was fairly tight)

---

## Reply 44
**Author**: Daksh Agarwal
**Posted**: 2025-02-20T05:33:29.345Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/49

sir even after applying this logic im getting error at root: array length mismatch

---

## Reply 45
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T05:41:41.335Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/50

@daksh76 thats because your innermost logic layer must not return a long list of results.

If you think about it logically each row cannot have a column field where one of the columns is a whole row of results right?

Thats why you are getting the error.

Check your innermost layer is returning a single value or a row of results.

Kind regards

---

## Reply 46
**Author**: LAKSHAY
**Posted**: 2025-02-20T06:00:14.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/51

Thank you for your response @carlton. You are absolutely right—my query was unnecessarily complex. Initially, I attempted a simpler approach, using various JSON extraction functions. However, I encountered multiple errors, including:

**`json_extract`**: *“Table Function with name ‘json_extract’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
**`json_each`**: *“Table Function with name ‘json_each’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
**`json_extract_path_text`**: *“Table Function with name ‘json_extract_path_text’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*

Since the simple approach did not work, I attempted a more complex query to achieve the desired result. However, that too did not yield the expected output. To gain better insight, I extracted ten values into a table using the console and then reconstructed the query accordingly. Unfortunately, I am still facing issues related to functions not being recognized in the catalog.

I would appreciate any guidance on resolving this issue. I do not need the exact answer; I just want to know if there is any issue with the portal for **Q8**.

Thankyou

---

## Reply 47
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T06:18:50.624Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/52

@lakshaygarg654

This might help  :wink: 

      [DuckDB](https://duckdb.org/docs/sql/query_syntax/unnest.html)

[Unnesting](https://duckdb.org/docs/sql/query_syntax/unnest.html)

Examples Unnest a list, generating 3 rows (1, 2, 3): SELECT unnest([1, 2, 3]); Unnesting a struct, generating two columns (a, b): SELECT unnest({'a': 42, 'b': 84}); Recursive unnest of a list of structs: SELECT unnest([{'a': 42, 'b': 84}, {'a': 100,...

Kind regards

---

## Reply 48
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T06:20:14.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/53

lakshaygarg654:

I just want to know if there is any issue with the portal for **Q8**.

Nope no issues with portal for Q8

---

## Reply 49
**Author**: LAKSHAY
**Posted**: 2025-02-20T06:22:37.305Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/54

Thanks @carlton

I found the correct query.

---

## Reply 50
**Author**: RAJ K BOOPATHI
**Posted**: 2025-02-20T10:09:25.727Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/55

I am still getting the answer as incorrect, though the answer for my dataset : 1187 (951+236) is correct. Would you be able to check again please?

---

## Reply 51
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T11:33:15.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/56

@23ds2000092

Can you just logout and login and reload your GA? (maybe clear cookies and cache) Because I get the correct answer for your GA.

Kind regards

---

## Reply 52
**Author**: RAJ K BOOPATHI
**Posted**: 2025-02-20T11:39:57.548Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/57

Done. it works now. thanks!

---

## Reply 53
**Author**: Vedant Baburao Kornule
**Posted**: 2025-02-20T11:20:14.335Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/58

**Image: {5C759A23-7CA1-4955-9D41-41F8E33D28E2}**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image displays a task description for improving sales data accuracy for a company called RetailWise Inc. It outlines the problem, the task to be performed, the challenges involved, and the benefits of completing the task. There's also a section for entering an answer and an error message indicating an incorrect answer.

**2. Text Content:**

The image contains the following text:

*   **Title:** "Improving Sales Data Accuracy for RetailWise Inc."
*   **Introduction:** A paragraph describing RetailWise Inc. as a retail analytics firm and the problem of messy data in an Excel sheet containing 1,000 transaction records.
*   **Excel File Columns and Issues:**
    *   "Customer Name: Contains leading/trailing spaces."
    *   "Country: Uses inconsistent representations..."
    *   "Date: Uses mixed formats..."
    *   "Product: Includes a product name followed by a slash and a random code..."
    *   "Sales and Cost: Contain extra spaces and the currency string ("USD")..."
    *   "TransactionID: Though formatted as four-digit numbers, this field may have inconsistent spacing."
*   **Your Task:**
    *   "You need to clean this Excel data and calculate the total margin for all transactions that satisfy the following criteria:"
    *   "Time Filter: Sales that occurred up to and including a specified date (Tue Jun 14 2022 04:52:52 GMT+0530 (India Standard Time))."
    *   "Product Filter: Transactions for a specific product (Theta). (Use only the product name before the slash.)"
    *   "Country Filter: Transactions from a specific country (US), after standardizing the country names."
    *   "The total margin is defined as: Total Margin = (Total Sales - Total Cost) / Total Sales"
*   **Your solution should address the following challenges:**
    *   A numbered list of challenges, including:
        *   Trimming and normalizing strings
        *   Standardizing date formats
        *   Extracting the product name
        *   Cleaning and converting sales and cost
        *   Filtering the data
        *   Calculating the margin
*   **Benefits of

In this question, I am asked to find the total margin for transactions before **Tue, Jun 14, 2022, 04:52:52 GMT+0530 (India Standard Time)** for **Theta** sold in **the US** (which may be spelled in different ways).

However, when I filter in Excel for **US** and **Theta**, there are no entries for **Sales** and **Cost**. But **0** as the answer is not accepted—it says the answer is incorrect.

(I cross-checked this using GPT.)

---

## Reply 54
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T11:39:56.594Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/59

@23f2004313

US is also called

United States

United States of America

USA

These are all valid references to US

Kind regards

---

## Reply 55
**Author**: Vedant Baburao Kornule
**Posted**: 2025-02-20T11:43:19.595Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/60

I have replaced all the different names of US (all ) as “US” .

also sorted the dates as asked in the question .

---

## Reply 56
**Author**: Carlton D'Silva
**Posted**: 2025-02-20T11:54:05.994Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/61

I have checked your GA and I do get sales entries for the criteria in your GA.

Please remember that this module is about data cleaning. And that data needs to be sanitised before you start filtering.

Kind regards

---

## Reply 57
**Author**: Shambhavi Verma
**Posted**: 2025-02-20T13:35:18.214Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/62

@carlton Sir , I have tried reconstructing the image in ques 10 multiple times and even still the output shows error: image pixels do not match…how can I fix this?

**Image: reconstructed**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image depicts a futuristic cityscape at night. It's a high-angle view, giving a sense of the scale and density of the urban environment. The city is filled with towering skyscrapers of various designs, many adorned with neon lights and futuristic architectural elements. There are elevated highways with streaks of light indicating fast-moving traffic. In the sky, there are several flying vehicles, resembling futuristic cars or spacecraft.

**2. Any text content visible:**

There is no clearly legible text in the image. There are some signs or displays on the buildings, but the resolution and style make it difficult to discern any specific words or characters.

**3. The context or purpose of what's displayed:**

The image is likely intended to evoke a sense of a technologically advanced and vibrant future. It showcases a world where transportation is seamless, architecture is bold and innovative, and the city is alive with light and activity. It could be used for science fiction illustration, concept art, or as a visual representation of technological progress.

**4. Technical details:**

*   **Lighting:** The image is dominated by neon and artificial lighting. The color palette is primarily blues, purples, and pinks, creating a cyberpunk aesthetic.
*   **Perspective:** The high-angle perspective provides a comprehensive view of the city's layout and infrastructure.
*   **Style:** The image has a slightly painterly or digital art style, with soft edges and a focus on capturing the overall atmosphere rather than hyper-realistic detail.
*   **Composition:** The composition is dynamic, with the elevated highways and flying vehicles creating a sense of movement and energy. The skyscrapers are arranged to create depth and visual interest.

Edit: I got it correct

---

## Reply 58
**Author**: Jayesh Bansal
**Posted**: 2025-02-20T14:48:33.358Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/63

i am also facing the same problem and i have cross verified the pixels but it is still showing the same

---

## Reply 59
**Author**: Vicky Kumar
**Posted**: 2025-02-20T15:09:11.708Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/64

Now my answer is same and correct i think problem was in TDS matching question like it was matched to other number now programmer correct it and matched to correct value like 4764

---

## Reply 60
**Author**: Vicky Kumar
**Posted**: 2025-02-20T15:11:02.705Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/65

**Image: reconstructed1_vicky**
Here's a detailed description of the image, focusing on the visible elements and text:

**Overall Impression:**

The image is a collage or mosaic of various sketches and diagrams, all rendered in a sepia tone, giving it a vintage or blueprint-like aesthetic. The content appears to be related to professional profiles, resumes, or perhaps a concept for a "perfect" candidate. There's a strong emphasis on technical skills, experience, and personal attributes.

**Specific Elements and Text:**

*   **Portraits:** Several portraits of men are visible. They are depicted in professional attire (suits, graduation gowns, military uniforms).
*   **Diagrams and Schematics:** The image is filled with technical diagrams, including gears, cogs, and flowcharts. These suggest a focus on mechanical or engineering concepts.
*   **Bar Graphs and Charts:** There are bar graphs and charts, likely representing skills, experience, or performance metrics.
*   **Text Snippets:** Several text fragments are scattered throughout the image. Here's a breakdown of the readable ones:
    *   "UTY WOLA"
    *   "BATEKIDOUINO HOFLE EAANING" (Likely "Background Profile Earning" with some distortion)
    *   "A SUTICAE" (Possibly "A Suitcase" or a misspelling of "Suitable")
    *   "LODOU"
    *   "MABGE NOR"
    *   "VIRON CAMO"
    *   "ADOBIM EXEBIONEO" (Likely "Adding Experience" with some distortion)
    *   "JENGTEBROGRAND"
    *   "ΑΠΟСТКОМОВНE DELATHINAGO"
    *   "TBSUN BRECHT ОРОО"
    *   "Ο ετσιτέστη"
    *   "11 תשע"

**Context and Purpose:**

The image seems to be a conceptual representation of a professional profile or resume. The portraits represent potential candidates, while the diagrams and charts illustrate their skills and experience. The text snippets may be keywords or phrases related to their qualifications. The overall aesthetic suggests a focus on technical expertise and a structured, analytical approach to evaluating candidates.

**Technical Details:**

The image is likely digitally created, possibly using AI or image editing software. The sepia tone

this is my image i coded corrrect mapped to correct pixel but it was saying pixel do not match what is meaning of it

---

## Reply 61
**Author**: Vicky Kumar
**Posted**: 2025-02-20T15:15:04.145Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/66

sorry i found correct answer i was thinking differently

---

## Reply 62
**Author**: Shashannk
**Posted**: 2025-02-20T16:51:25.392Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/67

can someone share the answer for the 9th question as i am facing some errors

---

## Reply 63
**Author**: Shambhavi Verma
**Posted**: 2025-02-20T17:24:10.305Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/68

Create your gemini api, convert the video into MP4 and then write the Collab code for the question or ask gpt to write it for you…finally run it on google collab

---

## Reply 64
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-20T17:33:18.129Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/69

Hi @Algsoch @24f2003130

While saving image you might need to pass lossless = True as argument.

`img.save("filename", lossless=True)`

kind regards

---

## Reply 65
**Author**: Jayesh Bansal
**Posted**: 2025-02-20T17:58:51.598Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/70

u can use openai whisper free and use yt-dlp package to extract the video and using whisper convert it

---

## Reply 66
**Author**: Bhashwar Sengupta
**Posted**: 2025-02-21T06:16:52.406Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/71

For Q8, I wrote the following query,

SELECT smo.post_id
FROM social_media as smo
WHERE smo.timestamp >= '2024-11-15T06:02:28.656Z'
AND EXISTS (
   SELECT 1
   FROM LATERAL (
       SELECT UNNEST(json_extract(comments, '$[*]'))
       FROM social_media as sm
       WHERE sm.post_id = smo.post_id
       ) AS c(value)
    WHERE json_extract(c.value, '$.stars.useful')::DOUBLE = 4)
order by smo.post_id;

What it does is for each post_id, checks the timestamp and then checks the presence of a json object in comments that has 4 stars useful rating for this post_id. Finally returns all the post_id’s in ascending order.

But it’s giving me an `Array length mismatch` error. I’m stuck here. Any hints would be helpful. @Jivraj @carlton

P.S. I also noticed that the timestamp given in the question keeps changing with each page reload. But the output from the query stays the same.

---

## Reply 67
**Author**: Shashannk
**Posted**: 2025-02-21T06:17:43.112Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/72

yeah i did the same but the transcript was not the same. it had many differences

---

## Reply 68
**Author**: Thereasa Joe J
**Posted**: 2025-02-21T06:55:36.025Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/73

Sir @s.anand @carlton the answer is correct but still getting as incorrect sir

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a web browser interface, specifically a question from an online assignment or quiz. The UI elements include:

*   **Browser Tabs:** Multiple tabs are open, including "My Dashboard - IIT Madras Online", "Graded Assignment 5 :: IITM Online", and "TDS 2025 Jan GA5 - Data Preparation".
*   **Address Bar:** The URL is "exam.sanand.workers.dev/tds-2025-01-ga5".
*   **Navigation Buttons:** Standard browser back, forward, and refresh buttons.
*   **Assignment Header:** Displays the time remaining ("11:35:28 left"), score ("Score: 0/10"), and "Check all" and "Save" buttons.
*   **Question Text:** A question is posed, asking for the number of successful GET requests under specific conditions.
*   **Input Field:** A text box is provided for the user to enter their answer.
*   **Check Button:** A button to submit the answer.
*   **Error Message:** An error message indicating that the provided answer is incorrect.
*   **Taskbar:** The Windows taskbar is visible at the bottom, showing the time, date, and weather.

**2. Text Content:**

*   **Assignment Information:** "My Dashboard - IIT Madras Online", "Graded Assignment 5 :: IITM Online", "TDS 2025 Jan GA5 - Data Preparation", "exam.sanand.workers.dev/tds-2025-01-ga5", "11:35:28 left", "Score: 0/10", "Check all", "Save".
*   **Definitions:** A list of definitions related to web server logs, including:
    *   "Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1"
    *   "Status:

after trying python codes chatgpt i tried using linux commands

bash-5.2$ zgrep ‘GET /malayalammp3/’ s-anand.net-May-2024.gz 

| grep -E ‘[(04|11|18|25)/May/2024:(10|11|12|13|14|15|16):[0-5][0-9]:[0-5][0-9]’ 

| grep -E ’ “(GET|POST) .* HTTP/1.[01]” (2[0-9][0-9]) ’ | wc -l

2316

i’m getting 2316 but when i enter in the answer box it says incorrect

---

## Reply 69
**Author**: Naga durga prasad E
**Posted**: 2025-02-21T07:27:57.245Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/74

Q9 , extracted text from yt and processed the srt file,  getting 77 differences  adding any word the diff count is increasing . Please tell what i am missing here.

---

## Reply 70
**Author**: Naga durga prasad E
**Posted**: 2025-02-21T07:49:59.333Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/75

downloading and using this image will given an error,  better generate it yourself.

---

## Reply 71
**Author**: Naga durga prasad E
**Posted**: 2025-02-21T07:50:53.403Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/76

AE means UAE and so on…

---

## Reply 72
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-21T10:02:46.400Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/77

Hi @23f3004114

Question 9 might not be solved 100% automatically, Manually listen to audio once or twice and correct few things.

Kind regards

---

## Reply 73
**Author**: GOVARDHANAN N 
**Posted**: 2025-02-21T13:21:23.359Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/78

**Q9**

Note : I found that punctuations are also checked. So make sure you include punctuations inside the paragraph wherever it is effective according to the voice in the paragraph

---

## Reply 74
**Author**: Naga durga prasad E
**Posted**: 2025-02-21T13:43:41.687Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/79

@21f3001379 @Jivraj  , thank you for the replies  :heart: . i stopped after 8/10. need to prepare for Quiz 1.

---

## Reply 75
**Author**: Nanditha
**Posted**: 2025-02-21T14:02:24.904Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/80

This case is the same with me

---

## Reply 76
**Author**: Shambhavi Verma
**Posted**: 2025-02-21T14:12:22.441Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/81

Yeah I did…I am done with that

---

## Reply 77
**Author**: Jayesh Bansal
**Posted**: 2025-02-21T14:50:35.844Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/82

it is asking successful GET requests, you can know if a request is successful or not by checking the status data given in the file

---

## Reply 78
**Author**: Rishit
**Posted**: 2025-02-21T15:00:51.144Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/83

Sir, Q8 is giving errors everytime.

---

## Reply 79
**Author**: Thereasa Joe J
**Posted**: 2025-02-21T15:07:41.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/84

It’s mentioned that 200-299 is successful requests

---

## Reply 80
**Author**: Nanditha
**Posted**: 2025-02-21T15:12:55.673Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/85

@carlton My answer for question 3 seems correct but it shows incorrect. Could you please clarify.

---

## Reply 81
**Author**: JAIDEEP M
**Posted**: 2025-02-21T15:14:01.655Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/86

No, for me It ran successfully and gave me the correct answer

Try to  use an LLM I have used qwen 2.5 max if you are not comfortable with that stick to chatgpt and your console for debugging

---

## Reply 82
**Author**: Nanditha
**Posted**: 2025-02-21T16:18:50.474Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/87

Is the issue still pertaining for you?

---

## Reply 83
**Author**: Akshit Mittal
**Posted**: 2025-02-21T17:47:52.518Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/88

Are there bonus marks for GA5?

---

## Reply 84
**Author**: Maheshwar Ture
**Posted**: 2025-02-21T17:52:10.732Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/89

I am also facing same issue with Q3. I tried with with shell as well as python script to find GET requests for pages under **/telugu/** from **11:00** until before **20:00** on Mondays

---

## Reply 85
**Author**: Aryan Bartwal
**Posted**: 2025-02-21T18:36:54.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/90

Hello sir,

With each passing assignment we are learning many new tools.

This way of teaching is actually amazing as it will make us remember for long.

Fortunate to be a part of this course!

Thanks to the team

---

## Reply 86
**Author**: Thereasa Joe J
**Posted**: 2025-02-21T18:38:01.291Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/91

Yes … For u … u fixed it???

---

## Reply 87
**Author**: Nanditha
**Posted**: 2025-02-22T00:35:40.515Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/92

No

I couldn’t fix it

---

## Reply 88
**Author**: Nanditha
**Posted**: 2025-02-22T00:36:33.922Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/93

That question is same for me.

---

## Reply 89
**Author**: Swapnila Chakrabarty
**Posted**: 2025-02-22T04:48:06.113Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/94

**QUESTION 9**

I was supposed to transcribe the audio of the provided video for a certain time period. After several attempts my submission still generated differences from the supposed answers. I have tried all forms of re-punctuations but the error wont budge. I even compared the generated transcript with the actual audio several times. I BELIEVE MY ANSWER IS CORRECT. If not I wish to know what the correct answer is. Because compared to the video I have provided the exact and well punctuated transcription of the audio between 397.2 and 505.5 seconds.

Here was my transcription - " Determined to confront the mystery, Miranda followed the elusive figure. In the dim corridor, fleeting glimpses of determination and hidden sorrow emerged, challenging her assumptions of friends and foes alike. The pursuit led her to a narrow, winding passage beneath the chapel. In the oppressive darkness, the air grew cold and heavy, and every echo of her footsteps seemed to whisper warnings of secrets best left undisturbed.

In a subterranean chamber, the shadow finally halted. The figure’s voice emerged from the gloom, “You are close to the truth, but be warned some secrets, once uncovered, can never be buried again.”

The mysterious stranger introduced himself as Victor, a former confidant of Edmund. His words painted a tale of coercion and betrayal—a network of hidden alliances that had forced Edmond into an impossible choice.

Victor detailed clandestine meetings, cryptic codes, and a secret society that manipulated fate from behind the scenes. Miranda listened, each revelation tightening the knots of suspicion around her mind.

From within his warm coat, Victor produced a faded journal brimming with names, dates, and enigmatic symbols. Its contents mirrored Edmund’s diary, strengthening the case for a conspiracy rooted in treachery. The journal hinted at a hidden hall beneath the manor, where the secret society stored evidence of their manipulations.

Miranda’s pulse quickened at the thought of unmasking those responsible for decades of deceit. Returning to the manor’s main hall, Miranda retraced her steps with renewed resolve. Every shadow in the corridor now seemed charged with meaning, each creak of wood a prelude to further revelations. In the manor’s basement, beneath a concealed panel, Miranda discovered another revelation "

---

## Reply 90
**Author**: Vicky Kumar
**Posted**: 2025-02-23T14:10:48.269Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/95

Can anyone provide solution of question 5 related to duckdb module

please

---

## Reply 91
**Author**: Andrew David
**Posted**: 2025-02-24T05:44:46.473Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/96

is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I had exams and would like do week 4,week 5 before week 6 and doing the assignment is a huge part in learning, any on the just doing the assignments or answers for the assignments? I understand that each set of students get different questions. @Jivraj @carlton @s.anand

---

## Reply 92
**Author**: PRAKHAR PANDEY
**Posted**: 2025-02-24T16:09:24.346Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/97

**Image: Screenshot 2025-02-22 at 12.32.27 AM**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a user interface (UI) for an online quiz or assessment. It includes:

*   **Title:** "TDS 2025 Jan GA5 - Data F" (likely truncated)
*   **Instructions:** A list of instructions for the user.
*   **Question/Discussion Link:** A link to a discussion forum for questions.
*   **User Information:** Information about the logged-in user.
*   **Save History:** A list of recent saves with timestamps and scores.
*   **UI Elements:** Buttons ("Check all", "Save", "Logout", "Reload"), text labels, and a container for the discussion link.

**2. Text Content:**

*   "Ended at Fri, 21 Feb, 2025, 11:59 pm IST"
*   "Score: 0"
*   "Check all"
*   "Save"
*   "TDS 2025 Jan GA5 - Data F"
*   "Instructions"
*   Numbered list of instructions:
    *   "Learn what you need. Reading material is provided, but feel free to skip it if you can answer the..."
    *   "Check answers regularly by pressing Check. It shows which answers are right or wrong. You..."
    *   "Save regularly by pressing Save. You can save multiple times. Your last saved submission will..."
    *   "Reloading is OK. Your answers are saved in your browser (not server). Questions won't change..."
    *   "Browser may struggle. If you face loading issues, turn off security restrictions or try a different..."
    *   "Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. U..."
    *   "It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz"
*   "Have questions? Join the discussion on Discourse"
*   "You are logged in as 23f1002709@ds.study.iitm.ac.in."
*   "Logout"
*   "Recent saves (most recent is your official score)"
*   

recent score shows the points, but overall score is 0. Please take a look.

---

## Reply 93
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-24T20:20:54.776Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/98

You can load answers using reload button on every assignment.

You can enable check answers button.

---

## Reply 94
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-24T20:21:29.900Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/99

No need to worry about that.

---

## Reply 95
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-24T20:22:21.934Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/100

SELECT DISTINCT post_id 
FROM (
   SELECT timestamp, post_id, UNNEST (comments->'$[*].stars.useful') AS useful
   FROM social_media
) AS temp
WHERE useful >= 2.0 
   AND timestamp > '2024-12-08T05:30:31.073Z'

---

## Reply 96
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-24T20:27:11.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/101

Hi @22f3002498

Yes, there is some issues with question3 we are working on it.

Thanks and kind regards

---

## Reply 97
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-02-24T20:32:06.446Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/102

Hi @23f3004024

There is some problem with question 3 of GA5, we are working on it. Marks will be pushed to dashboard once we resolve this issue.

Thanks and kind regards

---

## Reply 98
**Author**: Andrew David
**Posted**: 2025-02-25T06:51:01.549Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/103

I didn’t attempt it to reload the answers. How do i enable check answers button? @Jivraj

EDIT: I just went to the html and removed disabled from each relevant check box and also the form-control  input part, It works now, Thank you @Jivraj

---

## Reply 99
**Author**: HARISH. S
**Posted**: 2025-03-02T12:29:46.578Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/104

hi this is harish. mail id 23f3000975@ds.study.iitm.ac.in.

week 5 GA marks and project 1 marks are not visible. kindly check on that.

---

## Reply 100
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-03T08:13:30.879Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/105

*No content*

---

## Reply 101
**Author**: Carlton D'Silva
**Posted**: 2025-03-04T09:21:02.853Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/106

Hi Harish,

I have informed the operations team last week. I will follow up with them and see where they are with regards to pushing the scores.

Thanks and kind regards

---

## Reply 102
**Author**: Jivraj Singh Shekhawat
**Posted**: 2025-03-11T22:41:00.273Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga5-data-preparation-discussion-thread-tds-jan-2025/166576/107

A post was merged into an existing topic: [Programming Quiz 1 in Student Dashboard (label for ROE scores) - showing absent or incorrect](/t/programming-quiz-1-in-student-dashboard-label-for-roe-scores-showing-absent-or-incorrect/169369/24)

---
