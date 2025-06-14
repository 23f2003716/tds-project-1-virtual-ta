# PYQ doubt

**Topic URL**: https://discourse.onlinedegree.iitm.ac.in/t/pyq-doubt/172373/1

## Topic Metadata
- **ID**: 172373
- **Slug**: pyq-doubt
- **Created**: 2025-04-10T14:21:56.165Z
- **Views**: 60
- **Replies**: 0
- **Likes**: 1
- **Tags**: clarification

## Original Post
**Author**: Dhruv Agrawal
**Posted**: 2025-04-10T14:21:56.393Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/pyq-doubt/172373/1

**Image: image**
Here's a detailed description of the image:

**1. What is shown in the image:**

The image shows a multiple-choice question (MCQ) from what appears to be an online test or quiz. It presents a question related to identifying if a log entry's timestamp corresponds to a Saturday, using methods from the datetime library. The image displays the question text, followed by four possible answer options. Each option includes a numerical identifier and a code snippet. The correct answer is marked with a green checkmark, while the incorrect answers are marked with a red asterisk.

**2. Text Content:**

*   **Question Number:** 307
*   **Question Id:** 6406531045319
*   **Question Type:** MCQ
*   **Correct Marks:** 1
*   **Question Label:** Multiple Choice Question
*   **Question:** Which of the following methods is best for identifying if a log entry's timestamp corresponds to a Saturday? (timestamp is a method in datetime library)
*   **Options:**
    *   6406533529040. \* Check if `timestamp.weekday() == 5`
    *   6406533529041. ✓ Check if `timestamp.weekday() == 6`
    *   6406533529042. \* Check if `timestamp.strftime('%A') == 'Saturday'`
    *   6406533529043. \* Check if `timestamp.dayname() == 'Saturday'`

**3. Context and Purpose:**

The image is part of an assessment or learning module, likely focused on programming or software development. The question tests the understanding of how to work with timestamps and date/time manipulation in a programming context, specifically using the `datetime` library (likely in Python). The purpose is to evaluate the test-taker's ability to choose the most appropriate method for determining if a given timestamp falls on a Saturday.

**4. Technical Details (Code Snippets):**

The code snippets in the options use methods related to date and time manipulation. Let's break them down:

*   `timestamp.weekday()`: This method returns the day of the week as an integer, where Monday is 0

@carlton sir plz review it

i think the correct answer should be A

---

## Reply 1
**Author**: Carlton D'Silva
**Posted**: 2025-04-10T14:50:28.002Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/pyq-doubt/172373/2

yes saturday is 5 when using weekday ()

---
