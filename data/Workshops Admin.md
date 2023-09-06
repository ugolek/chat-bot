# Workshops Admin

## Creating workshop flow (short version)

1. Choose the relevant section in Django admin “Workshops”, then click “add Workshops”
2. Be sure you already create “Partner” and “Person” entities 
3. Fill the all necessary fields on the page which opened after the click “add Workshop”. (This step will be described detailed)
4. Click the “Save” button 

<aside>
⚠️ Before creating **the workshop page**, we need to create the Partner entity and the Person entities, which we will connect to the workshop page

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
    
    ---
    
    ## Field description and cases while creating or editing workshop page
    
    We will describe the functions of the fields in sections, as they are displayed in the workshop creation/editing section In the Django admin
    
    <aside>
    💡 All fields which have EN/UK switcher means these fields must be filled in both languages.
    
    - Switcher preview
        
        ![Untitled](Untitled%202.png)
        
    </aside>
    
    ### The “Base info” section
    
    ![Untitled](Untitled%2033.png)
    
    1. Workshop name* 
    2. Workshop short description*
    3. Language* — choice of course teaching language
    4. Start Date* — choice of workshop start date— [https://cln.sh/V8CRsHj9](https://cln.sh/V8CRsHj9)
        - if the field is empty, on the website instead of dates will show a “coming soon” placeholder
    5. Number of sessions* — this field shows how many sessions will be on the workshop (*text near this number is hard coded. For changing the text please ask developers*)
    6. Spots available* — this field shows how many slots for students are available on the workshop (*text near this number is hard coded. For changing the text please ask developers*)
    7. Tags (*the field is not required*) 
        - you can choose relevant tags from the list provided
        - if the desired tags are not listed, you can easily add them by clicking the green plus button
    
    *- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create
    
    ### The “Hosts” section
    
    ![Untitled](Untitled%2034.png)
    
    1. Main host* - use the dropdown list for choosing the Main host of the workshop. Be sure you already add information about the coach in the “Person” entity. All information in this dropdown list is from the “Persons” entity.
    2. Main host about - in this field, a biography about the teacher, his achievements, and everything that is important to highlight for the audience is added
    3. Contact person — choose Person from the list, to show it on the website in “Get in touch section” — [https://cln.sh/1hkRbYFC](https://cln.sh/1hkRbYFC)

### The “Schema” and “schema block” section

To fully fill out the scheme on the site, you need to fill in information from 2 different blocks of the admin. The "Schema" block and the "Schema block" block.

The “Schema” section description

![Untitled](Untitled%2035.png)

1. Schema titile — [https://cln.sh/cG3SRTzJ](https://cln.sh/cG3SRTzJ)
2. Schema button clock — [https://cln.sh/263VcK1H](https://cln.sh/263VcK1H)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

The “Schema block” section description

![Untitled](Untitled%2036.png)

**! All fields are required!** Each of the marked fields in the admin is responsible for the circle on the site section interface — [https://cln.sh/yflYqNB9](https://cln.sh/yflYqNB9)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### The “Video block” section

![Untitled](Untitled%2037.png)

1. Video preview of the workshop (*the field is not required*)
    - when we add the YouTube video ID, 2 additional elements appear in the interface: 1) a button on the first screen, 2) a separate block with videos on the workshop page
2. Showing/hiding promo videos about the workshop. This is the checkbox “Video active” that shows (if it’s checked) or hides (if it’s unchecked) all video components like a video section with a header and button on the first screen.
3. Video section title
4. Video section description

### “**FAQ”** section

If we want to add FAQ to the page, this is exactly the section we need. This section is optional. There is no limit to the number of questions displayed on the page

- Website “**FAQ**” preview
    
    ![Untitled](Untitled%2023.png)
    

![Untitled](Untitled%2024.png)

1. Add another FAQ button — Press the button to add pair of question and answer to the page (you can add any amount of pairs you want)
2. The question you want to show — [https://cln.sh/HKfDVKqP](https://cln.sh/HKfDVKqP)
3. Answer you provide for relevant question — [https://cln.sh/5cLHf8YC](https://cln.sh/5cLHf8YC)
4. Delete control — control for deleting the question (activate checkbox and click save)

### “**PROGRAM TOPICS”** section

This section is required to display on the website. This section is detailed information about the course program. If we don’t have information about the course session yet, we can use “TBA” or “Coming soon” placeholders.

- Website “Program topic” preview
    
    ![Untitled](Untitled%2014.png)
    

![Untitled](Untitled%2015.png)

1. Title* — The name of the session — [https://cln.sh/27Pj0lr5](https://cln.sh/27Pj0lr5)
2. Time* — session start and end time — [https://cln.sh/8jpDbBQY](https://cln.sh/8jpDbBQY)
3. Date* — session start and end date — [https://cln.sh/2bPC5wZd](https://cln.sh/2bPC5wZd)
4. Position* — selects automatically
5. Action items* — list of what will be learned in the relevant session — [https://cln.sh/yJ3l088F](https://cln.sh/yJ3l088F). For normal display on the site, you need to use the [bullet list tool](https://cln.sh/tmYd7Mdq) in the Django admin
6. Delete control — control for deleting the program (activate checkbox and click save)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create