# Course Admin

This document provides detailed instructions for creating and editing course pages in Django admin. It includes sections on creating partners and persons, as well as detailed descriptions of various fields within the course page creation form. The document is intended for those involved in the creation and management of courses on the [Gathers.ai](http://gathers.ai/) platform.

## Creating course flow (short version)

1. Choose the relevant section in Django admin “Courses”, then click “add course” - [https://cln.sh/YR6fwsJb](https://cln.sh/YR6fwsJb)
2. Be sure you already create “Partner” and “Person” entities 
3. Fill the all necessary fields on the page which opened after the click “add course”. (This step will be described detailed)
4. Click the “Save” button 

---

<aside>
⚠️ Before creating **the course page**, we need to create the Partner entity and the Person entities, which we will connect to the course page

</aside>

## Creating the Partner

⚠️ While creating the Partner entity all the fields are required.

1. Choose the “Partner” section in the left sidebar of Django admin and click the “Add partner” button - [https://cln.sh/PqGXTyBz](https://cln.sh/PqGXTyBz)
2. Fill all the fields on the Create Partner page - [https://cln.sh/Jtl21135](https://cln.sh/Jtl21135) and click the “save button”
    - upload partner logo (recommended size 230x40)
    - set the partner name in English
    - set the link to the partner website
    - activate the checkbox “active”

## Creating the Person

⚠️ While creating the Person entity all the fields are required.

1. Choose the “Person” section in the left sidebar of Django admin and click the “Add person” button - [https://cln.sh/JBqK0jy2](https://cln.sh/JBqK0jy2)
2. Fill all the fields on the Create Partner page - [https://cln.sh/fkB56n0m](https://cln.sh/fkB56n0m) and click the “save button”
    - fill in the first and last name of the added person in both languages - EN/UK
    - add an avatar for the partner (recommended size 500x720 without background)
        - here is the template link for preparing a photo to the website page — [https://www.figma.com/file/S5q783s3haQRRJ1qDu94T7/PC-%2F-Courses-photo-templates?type=design&node-id=0%3A1&t=wHK2Efhjt4oH0HSM-1](https://www.figma.com/file/S5q783s3haQRRJ1qDu94T7/PC-%2F-Courses-photo-templates?type=design&node-id=0%3A1&t=wHK2Efhjt4oH0HSM-1)
    - add profession in English
    - choose “current company” - we already add a company in the “Partner section” You only need to choose relevant from the dropdown list
    - add a link to the LinkedIn profile of the person
    - ℹ️ If you need to add one more company, where the person worked before, you need to add information in the [“Companies” section](https://cln.sh/NH1kg4gn). *This field is not required for creating the Person entity*

## Field description and cases while creating or editing course page

We will describe the functions of the fields in sections, as they are displayed in the course creation/editing section In the Django admin

<aside>
💡 All fields which have EN/UK switcher means these fields must be filled in both languages.

- Switcher preview
    
    ![Untitled](Untitled%202.png)
    
</aside>

### The “Base info” section

Part 1 of the base info section

![Untitled](Untitled%203.png)

1. Course name* — [https://cln.sh/yR16b9Tz](https://cln.sh/yR16b9Tz)
2. Course short description* — [https://cln.sh/YqDtzHxY](https://cln.sh/YqDtzHxY)
3. Video preview of the course (*the field is not required*) — [https://cln.sh/Jx5yztCJ](https://cln.sh/Jx5yztCJ)
    - when we add the YouTube video ID, 2 additional elements appear in the interface: 1) a button on the first screen, 2) a separate block with videos on the course page
4. Main coach* - use the dropdown list for choosing the Main Coach of the course. Be sure you already add information about the coach in the “Person” entity. All information in this dropdown list is from the “Persons” entity.
5. Spots available* — this field shows how many slots for students are available on the course — [https://cln.sh/v03c6nWt](https://cln.sh/v03c6nWt) (*text near this number is hard coded. For changing the text please ask developers*)
6. Number of sessions* — this field shows how many sessions will be on the course — [https://cln.sh/dd6vgWLR](https://cln.sh/dd6vgWLR) (*text near this number is hard coded. For changing the text please ask developers*)
7. Tags (*the field is not required*) — used for creating the filtering on the [all courses page](https://www.gathers.ai/courses)
    - you can choose relevant tags from the list provided
    - if the desired tags are not listed, you can easily add them by clicking the green plus button

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

Part 2 of the base info section

![Untitled](Untitled%204.png)

1. Active check-box*
    1. if the checkbox is checked it means this course page will show on the website
    2. if the checkbox is not checked it means this course page will not show on the website
2. Time status - the field is not editable. The field automatically sets the course status based on the entered course start and end dates. The course status affects the sorting of all courses on the page [https://www.gathers.ai/courses](https://www.gathers.ai/courses)
3. Language* — choice course teaching language — [https://cln.sh/SQVgHfZk](https://cln.sh/SQVgHfZk)
4. Start Date* — choice of course start date— [https://cln.sh/V8CRsHj9](https://cln.sh/V8CRsHj9)
    - if the field is empty, on the website instead of dates will show a “coming soon” placeholder
5. End date — choice of the course end date
6. Start registration date — the date when registration for the course opens. Usually coincides with the start date of the course
7. End registration date — the date when registration for the course ends. Usually 1 day before the course start date
    - if this field is filled in, a countdown timer will appear on the site, next to the registration form — [https://cln.sh/xlT9hc1N](https://cln.sh/xlT9hc1N)
8. Price* — the field in which the price for the course is displayed. In this field, you can add information about discounts or the price for early booking — [https://cln.sh/jx8bx04n](https://cln.sh/jx8bx04n) (*text near this input is hard coded. For changing the text please ask developers*)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

⚡️ UPD 04/05/2023

Added a new feature of showing/hiding promo videos about the course. This feature is located in the “Base info” section under the field “link to the video”. — [https://cln.sh/zcv6HCWr](https://cln.sh/zcv6HCWr)

This is the checkbox “Video active” that shows (if it’s checked) or hides (if it’s unchecked) all course video components like a video section with a header and button on the first screen.

### “Design for…” and “**What skills will I get?”** sections

On the website, we have a section “Design for” where we describe for whom this course will be more suitable, and what skills students will get after passing the course. In the Django admin information in the "Design for" sections adds via 2 sections “Design for” and “What skill will I get”

- Website “Design for” section preview
    
    ![Untitled](Untitled%205.png)
    

![Untitled](Untitled%206.png)

1. Design for title* — the field in which we add a list of professions for which the course is most suitable — [https://cln.sh/78H7TzYH](https://cln.sh/78H7TzYH)
2. Design for description (*not required*) — any additional information related to the list of professions or skills can be added to this field

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

![Untitled](Untitled%207.png)

The recommended amount of fields is from 3 to 6

1. button with which objects are added to the What skills will I get component
2. field to which we add information about the skill that the student will receive in the course

### “Course about**”** section

A section on the website that briefly describes which course program. It is displayed on the website as follows — [https://cln.sh/m0ctKQP5](https://cln.sh/m0ctKQP5)

![Untitled](Untitled%208.png)

1. Course about the title — Field doesn’t work. We made an automatic title that contains hardcoded text and course name *(for instance About live online course by Dmytro Voitekh, where “About live online course by” is hardcoded text)*
2. Course about the content (*not required*) — here is the field where we can put a short description of course program

### “Free session**”** section

This section can optionally display on the website. In this section is information about a free pre-course session. If the information in the block is filled, it is displayed on the website. If the fields in the block are empty, the block is not displayed on the site.

- Website “Free session” preview
    
    ![Untitled](Untitled%209.png)
    

![Untitled](Untitled%2010.png)

1. Free session topic — the name of the free online session — [https://cln.sh/ZxKK2qBW](https://cln.sh/ZxKK2qBW)
2. Free session END date — this field is not displayed on the site. The field is required for the operation logic of the СTA button in the block. If the session has already passed, the text of the button will be "Get free recording". If the session has not yet passed, the text of the button will be “Join”. The automatic sending of letters after registration is tied to the logic of the button.
3. Free session date string — the date when there will be a free session —  [https://cln.sh/y2VHKdzq](https://cln.sh/y2VHKdzq)
4. Free session video ID — this field is not displayed on the site. The field is needed so that after the free session has passed, people automatically get a link to the recording of the session.
5. Free session format — the format in which the free session will be held — [https://cln.sh/gcMDpQXv](https://cln.sh/gcMDpQXv)
6. Free session coach — host of the free session — [https://cln.sh/G7DzG19m](https://cln.sh/G7DzG19m)
7. Free session link (temporary field) — link to the registration on the free event (now we using the Typeform service which manages by Sofia)

### “Meet the Experts**”** section

This section can optionally display on the website. In this section is information about the main coach of the course. If the information in the block is filled, it is displayed on the website. If the fields in the block are empty, the block is not displayed on the site.

ℹ️ The photo of the coach, company logo, teacher job title, and LinkedIn has added automatically if the section “Meet the experts” is filled in Django admin.

- Website “Meet the Experts” preview
    
    ![Untitled](Untitled%2011.png)
    

![Untitled](Untitled%2012.png)

1. Meet the top content — in this field, a biography about the teacher, his achievements, and everything that is important to highlight for the audience is added — [https://cln.sh/NSBRYS5z](https://cln.sh/NSBRYS5z)

### ❌ “Event**”** section — doesn’t work

![Untitled](Untitled%2013.png)

This section is currently inactive. In the future, we will use it for the free session page

### “**PROGRAM TOPICS”** section

This section is required to display on the website. This section is detailed information about the course program. If we don’t have information about the course session yet, we can use “TBA” or “Coming soon” placeholders.

- Website “Program topic” preview
    
    ![Untitled](Untitled%2014.png)
    

![Untitled](Untitled%2015.png)

1. Title* — The name of the session within the course — [https://cln.sh/27Pj0lr5](https://cln.sh/27Pj0lr5)
2. Time* — session start and end time — [https://cln.sh/8jpDbBQY](https://cln.sh/8jpDbBQY)
3. Date* — session start and end date — [https://cln.sh/2bPC5wZd](https://cln.sh/2bPC5wZd)
4. Position* — selects automatically
5. Action items* — list of what will be learned in the relevant session — [https://cln.sh/yJ3l088F](https://cln.sh/yJ3l088F). For normal display on the site, you need to use the [bullet list tool](https://cln.sh/tmYd7Mdq) in the Django admin
6. Delete control — control for deleting the program (activate checkbox and click save)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### “**GUEST LECTURERS”** section

If we have a course with more than 1 teacher, and we need to show them on the website, we use this section for the relevant course.

⚠️ Before adding be sure the coaches you want to add as guest lecturers are already added in the “Persons” section of the Django admin.

- Website “Guest lecturers” preview
    
    ![Untitled](Untitled%2016.png)
    
    ![Untitled](Untitled%2017.png)
    

![Untitled](Untitled%2018.png)

1. Add another lecturer button — Press the button to add a guest lecture to the course page (you can add any amount of lecturers you want)
2. The dropdown list of choosing relevant lecturer
3. Delete control — control for deleting the lecturer (activate checkbox and click save)

### “**COURSE REVIEWS”** section

If we want to add feedback to the course page, this is exactly the section we need. This section is optional. There is no limit to the number of reviews displayed on the course page

- Website “course review” preview
    
    ![Untitled](Untitled%2019.png)
    

⚠️Before adding be sure the author you want to add as a reviewer is already added in the “Persons” section of the Django admin.

![Untitled](Untitled%2020.png)

1. Add another Course review button — Press the button to add a student review to the course page (you can add any amount of reviews you want)
2. Content* — the text of the review — [https://cln.sh/pL4Fp3qv](https://cln.sh/pL4Fp3qv)
3. Video ID — the field in which the ID of the video feedback is added, if we want it to appear on the page — [https://cln.sh/9MlpC1Ph](https://cln.sh/9MlpC1Ph)
4. Author* — the review author (choosing from the dropdown list of the “Persons” entity)
5. Delete control — control for deleting the review (activate checkbox and click save)

*- if you decided to add a review to the course page, there are several required fields while adding. All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### ❌ “**BULLET POINTS”, “WHAT WILL I GET AS A RESULT?”, and “WHO IS THIS COURSE FOR”** section — doesn’t work. Need to delete from Django admin ([task](https://www.notion.so/Delete-unnecessary-sections-from-Django-admin-3b26423af1ca4e35a5500e64fe75cfdd?pvs=21))

![Untitled](Untitled%2021.png)

![Untitled](Untitled%2022.png)

### “**FAQ”** section

If we want to add FAQ to the course page, this is exactly the section we need. This section is optional. There is no limit to the number of questions displayed on the course page

- Website “**FAQ**” preview
    
    ![Untitled](Untitled%2023.png)
    

![Untitled](Untitled%2024.png)

1. Add another Faq button — Press the button to add pair of question and answer to the course page (you can add any amount of pairs you want)
2. The question you want to show — [https://cln.sh/HKfDVKqP](https://cln.sh/HKfDVKqP)
3. Answer you provide for relevant question — [https://cln.sh/5cLHf8YC](https://cln.sh/5cLHf8YC)
4. Delete control — control for deleting the question (activate checkbox and click save)

## Creating course flow (short version)

1. Choose the relevant section in Django admin “Courses”, then click “add course” - [https://cln.sh/YR6fwsJb](https://cln.sh/YR6fwsJb)
2. Be sure you already create “Partner” and “Person” entities 
3. Fill the all necessary fields on the page which opened after the click “add course”. (This step will be described detailed)
4. Click the “Save” button 

---

<aside>
⚠️ Before creating **the course page**, we need to create the Partner entity and the Person entities, which we will connect to the course page

</aside>

## Creating the Partner

⚠️ While creating the Partner entity all the fields are required.

1. Choose the “Partner” section in the left sidebar of Django admin and click the “Add partner” button - [https://cln.sh/PqGXTyBz](https://cln.sh/PqGXTyBz)
2. Fill all the fields on the Create Partner page - [https://cln.sh/Jtl21135](https://cln.sh/Jtl21135) and click the “save button”
    - upload partner logo (recommended size 230x40)
    - set the partner name in English
    - set the link to the partner website
    - activate the checkbox “active”

## Creating the Person

⚠️ While creating the Person entity all the fields are required.

1. Choose the “Person” section in the left sidebar of Django admin and click the “Add person” button - [https://cln.sh/JBqK0jy2](https://cln.sh/JBqK0jy2)
2. Fill all the fields on the Create Partner page - [https://cln.sh/fkB56n0m](https://cln.sh/fkB56n0m) and click the “save button”
    - fill in the first and last name of the added person in both languages - EN/UK
    - add an avatar for the partner (recommended size 500x720 without background)
        - here is the template link for preparing a photo to the website page — [https://www.figma.com/file/S5q783s3haQRRJ1qDu94T7/PC-%2F-Courses-photo-templates?type=design&node-id=0%3A1&t=wHK2Efhjt4oH0HSM-1](https://www.figma.com/file/S5q783s3haQRRJ1qDu94T7/PC-%2F-Courses-photo-templates?type=design&node-id=0%3A1&t=wHK2Efhjt4oH0HSM-1)
    - add profession in English
    - choose “current company” - we already add a company in the “Partner section” You only need to choose relevant from the dropdown list
    - add a link to the LinkedIn profile of the person
    - ℹ️ If you need to add one more company, where the person worked before, you need to add information in the [“Companies” section](https://cln.sh/NH1kg4gn). *This field is not required for creating the Person entity*

## Field description and cases while creating or editing course page

We will describe the functions of the fields in sections, as they are displayed in the course creation/editing section In the Django admin

<aside>
💡 All fields which have EN/UK switcher means these fields must be filled in both languages.

- Switcher preview
    
    ![Untitled](Untitled%202.png)
    
</aside>

### The “Base info” section

Part 1 of the base info section

![Untitled](Untitled%203.png)

1. Course name* — [https://cln.sh/yR16b9Tz](https://cln.sh/yR16b9Tz)
2. Course short description* — [https://cln.sh/YqDtzHxY](https://cln.sh/YqDtzHxY)
3. Video preview of the course (*the field is not required*) — [https://cln.sh/Jx5yztCJ](https://cln.sh/Jx5yztCJ)
    - when we add the YouTube video ID, 2 additional elements appear in the interface: 1) a button on the first screen, 2) a separate block with videos on the course page
4. Main coach* - use the dropdown list for choosing the Main Coach of the course. Be sure you already add information about the coach in the “Person” entity. All information in this dropdown list is from the “Persons” entity.
5. Spots available* — this field shows how many slots for students are available on the course — [https://cln.sh/v03c6nWt](https://cln.sh/v03c6nWt) (*text near this number is hard coded. For changing the text please ask developers*)
6. Number of sessions* — this field shows how many sessions will be on the course — [https://cln.sh/dd6vgWLR](https://cln.sh/dd6vgWLR) (*text near this number is hard coded. For changing the text please ask developers*)
7. Tags (*the field is not required*) — used for creating the filtering on the [all courses page](https://www.gathers.ai/courses)
    - you can choose relevant tags from the list provided
    - if the desired tags are not listed, you can easily add them by clicking the green plus button

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

Part 2 of the base info section

![Untitled](Untitled%204.png)

1. Active check-box*
    1. if the checkbox is checked it means this course page will show on the website
    2. if the checkbox is not checked it means this course page will not show on the website
2. Time status - the field is not editable. The field automatically sets the course status based on the entered course start and end dates. The course status affects the sorting of all courses on the page [https://www.gathers.ai/courses](https://www.gathers.ai/courses)
3. Language* — choice course teaching language — [https://cln.sh/SQVgHfZk](https://cln.sh/SQVgHfZk)
4. Start Date* — choice of course start date— [https://cln.sh/V8CRsHj9](https://cln.sh/V8CRsHj9)
    - if the field is empty, on the website instead of dates will show a “coming soon” placeholder
5. End date — choice of the course end date
6. Start registration date — the date when registration for the course opens. Usually coincides with the start date of the course
7. End registration date — the date when registration for the course ends. Usually 1 day before the course start date
    - if this field is filled in, a countdown timer will appear on the site, next to the registration form — [https://cln.sh/xlT9hc1N](https://cln.sh/xlT9hc1N)
8. Price* — the field in which the price for the course is displayed. In this field, you can add information about discounts or the price for early booking — [https://cln.sh/jx8bx04n](https://cln.sh/jx8bx04n) (*text near this input is hard coded. For changing the text please ask developers*)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

⚡️ UPD 04/05/2023

Added a new feature of showing/hiding promo videos about the course. This feature is located in the “Base info” section under the field “link to the video”. — [https://cln.sh/zcv6HCWr](https://cln.sh/zcv6HCWr)

This is the checkbox “Video active” that shows (if it’s checked) or hides (if it’s unchecked) all course video components like a video section with a header and button on the first screen.

### “Design for…” and “**What skills will I get?”** sections

On the website, we have a section “Design for” where we describe for whom this course will be more suitable, and what skills students will get after passing the course. In the Django admin information in the "Design for" sections adds via 2 sections “Design for” and “What skill will I get”

- Website “Design for” section preview
    
    ![Untitled](Untitled%205.png)
    

![Untitled](Untitled%206.png)

1. Design for title* — the field in which we add a list of professions for which the course is most suitable — [https://cln.sh/78H7TzYH](https://cln.sh/78H7TzYH)
2. Design for description (*not required*) — any additional information related to the list of professions or skills can be added to this field

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

![Untitled](Untitled%207.png)

The recommended amount of fields is from 3 to 6

1. button with which objects are added to the What skills will I get component
2. field to which we add information about the skill that the student will receive in the course

### “Course about**”** section

A section on the website that briefly describes which course program. It is displayed on the website as follows — [https://cln.sh/m0ctKQP5](https://cln.sh/m0ctKQP5)

![Untitled](Untitled%208.png)

1. Course about the title — Field doesn’t work. We made an automatic title that contains hardcoded text and course name *(for instance About live online course by Dmytro Voitekh, where “About live online course by” is hardcoded text)*
2. Course about the content (*not required*) — here is the field where we can put a short description of course program

### “Free session**”** section

This section can optionally display on the website. In this section is information about a free pre-course session. If the information in the block is filled, it is displayed on the website. If the fields in the block are empty, the block is not displayed on the site.

- Website “Free session” preview
    
    ![Untitled](Untitled%209.png)
    

![Untitled](Untitled%2010.png)

1. Free session topic — the name of the free online session — [https://cln.sh/ZxKK2qBW](https://cln.sh/ZxKK2qBW)
2. Free session END date — this field is not displayed on the site. The field is required for the operation logic of the СTA button in the block. If the session has already passed, the text of the button will be "Get free recording". If the session has not yet passed, the text of the button will be “Join”. The automatic sending of letters after registration is tied to the logic of the button.
3. Free session date string — the date when there will be a free session —  [https://cln.sh/y2VHKdzq](https://cln.sh/y2VHKdzq)
4. Free session video ID — this field is not displayed on the site. The field is needed so that after the free session has passed, people automatically get a link to the recording of the session.
5. Free session format — the format in which the free session will be held — [https://cln.sh/gcMDpQXv](https://cln.sh/gcMDpQXv)
6. Free session coach — host of the free session — [https://cln.sh/G7DzG19m](https://cln.sh/G7DzG19m)
7. Free session link (temporary field) — link to the registration on the free event (now we using the Typeform service which manages by Sofia)

### “Meet the Experts**”** section

This section can optionally display on the website. In this section is information about the main coach of the course. If the information in the block is filled, it is displayed on the website. If the fields in the block are empty, the block is not displayed on the site.

ℹ️ The photo of the coach, company logo, teacher job title, and LinkedIn has added automatically if the section “Meet the experts” is filled in Django admin.

- Website “Meet the Experts” preview
    
    ![Untitled](Untitled%2011.png)
    

![Untitled](Untitled%2012.png)

1. Meet the top content — in this field, a biography about the teacher, his achievements, and everything that is important to highlight for the audience is added — [https://cln.sh/NSBRYS5z](https://cln.sh/NSBRYS5z)

### ❌ “Event**”** section — doesn’t work

![Untitled](Untitled%2013.png)

This section is currently inactive. In the future, we will use it for the free session page

### “**PROGRAM TOPICS”** section

This section is required to display on the website. This section is detailed information about the course program. If we don’t have information about the course session yet, we can use “TBA” or “Coming soon” placeholders.

- Website “Program topic” preview
    
    ![Untitled](Untitled%2014.png)
    

![Untitled](Untitled%2015.png)

1. Title* — The name of the session within the course — [https://cln.sh/27Pj0lr5](https://cln.sh/27Pj0lr5)
2. Time* — session start and end time — [https://cln.sh/8jpDbBQY](https://cln.sh/8jpDbBQY)
3. Date* — session start and end date — [https://cln.sh/2bPC5wZd](https://cln.sh/2bPC5wZd)
4. Position* — selects automatically
5. Action items* — list of what will be learned in the relevant session — [https://cln.sh/yJ3l088F](https://cln.sh/yJ3l088F). For normal display on the site, you need to use the [bullet list tool](https://cln.sh/tmYd7Mdq) in the Django admin
6. Delete control — control for deleting the program (activate checkbox and click save)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### “**GUEST LECTURERS”** section

If we have a course with more than 1 teacher, and we need to show them on the website, we use this section for the relevant course.

⚠️ Before adding be sure the coaches you want to add as guest lecturers are already added in the “Persons” section of the Django admin.

- Website “Guest lecturers” preview
    
    ![Untitled](Untitled%2016.png)
    
    ![Untitled](Untitled%2017.png)
    

![Untitled](Untitled%2018.png)

1. Add another lecturer button — Press the button to add a guest lecture to the course page (you can add any amount of lecturers you want)
2. The dropdown list of choosing relevant lecturer
3. Delete control — control for deleting the lecturer (activate checkbox and click save)

### “**COURSE REVIEWS”** section

If we want to add feedback to the course page, this is exactly the section we need. This section is optional. There is no limit to the number of reviews displayed on the course page

- Website “course review” preview
    
    ![Untitled](Untitled%2019.png)
    

⚠️Before adding be sure the author you want to add as a reviewer is already added in the “Persons” section of the Django admin.

![Untitled](Untitled%2020.png)

1. Add another Course review button — Press the button to add a student review to the course page (you can add any amount of reviews you want)
2. Content* — the text of the review — [https://cln.sh/pL4Fp3qv](https://cln.sh/pL4Fp3qv)
3. Video ID — the field in which the ID of the video feedback is added, if we want it to appear on the page — [https://cln.sh/9MlpC1Ph](https://cln.sh/9MlpC1Ph)
4. Author* — the review author (choosing from the dropdown list of the “Persons” entity)
5. Delete control — control for deleting the review (activate checkbox and click save)

*- if you decided to add a review to the course page, there are several required fields while adding. All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### ❌ “**BULLET POINTS”, “WHAT WILL I GET AS A RESULT?”, and “WHO IS THIS COURSE FOR”** section — doesn’t work. Need to delete from Django admin ([task](https://www.notion.so/Delete-unnecessary-sections-from-Django-admin-3b26423af1ca4e35a5500e64fe75cfdd?pvs=21))

![Untitled](Untitled%2021.png)

![Untitled](Untitled%2022.png)

### “**FAQ”** section

If we want to add FAQ to the course page, this is exactly the section we need. This section is optional. There is no limit to the number of questions displayed on the course page

- Website “**FAQ**” preview
    
    ![Untitled](Untitled%2023.png)
    

![Untitled](Untitled%2024.png)

1. Add another Faq button — Press the button to add pair of question and answer to the course page (you can add any amount of pairs you want)
2. The question you want to show — [https://cln.sh/HKfDVKqP](https://cln.sh/HKfDVKqP)
3. Answer you provide for relevant question — [https://cln.sh/5cLHf8YC](https://cln.sh/5cLHf8YC)
4. Delete control — control for deleting the question (activate checkbox and click save)