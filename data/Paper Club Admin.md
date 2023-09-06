# Paper Club Admin

## Creating PC (short version)

1. Choose the relevant section in Django admin “Papers club”, then click “Add papers club” 
2. Be sure you already create “Partner” and “Person” entities 
3. Fill the all necessary fields on the page which opened after the click “add papers club”. (This step will be described detailed)
4. Click the “Save” button 

<aside>
⚠️ Before creating **the PC page**, we need to create the Partner entity and the Person entities, which we will connect to the page

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

## Field description and cases while creating or editing PC

We will describe the functions of the fields in sections, as they are displayed in the PC creation/editing section In the Django admin

<aside>
💡 All fields which have EN/UK switcher means these fields must be filled in both languages.

- Switcher preview
    
    ![Untitled](Untitled%202.png)
    
</aside>

### The “Base info” section

Part 1 of the base info section

![Untitled](Untitled%2025.png)

1. Title* — the PC name
2. Start Date* — choice of PC start date — [https://cln.sh/TyZ0KCjC](https://cln.sh/TyZ0KCjC) 
    - if the field is empty, on the website instead of dates will show a “coming soon” placeholder
    - this field also uses for automotive emails
3. Time placeholder* — information from this field is shown on the site. The field is customizable so that it is possible to specify different timezones without excessive technical implementation — [https://cln.sh/wLrfbK76](https://cln.sh/wLrfbK76)
4. End date — choice of the PC end date
5. End registration date — the date when registration for the PC ends. Usually, 1 day before the event start date
    - if this field is filled in, a countdown timer will appear on the site, next to the registration form — [https://cln.sh/HLrVCLfB](https://cln.sh/HLrVCLfB)
6. Price* — the field in which the price for the course is displayed. In this field, you can add any information you want — [https://cln.sh/csfZwVfZ](https://cln.sh/csfZwVfZ)(*text near this input is hard coded. For changing the text please ask developers*)

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

Part 2 of the base info section

![Untitled](Untitled%2026.png)

1. Tags (*the field is not required*) — used for creating the filtering on the all PC page
    - you can choose relevant tags from the list provided
    - if the desired tags are not listed, you can easily add them by clicking the green plus button
2. Format* — the event format online or offline
3. Club recording — after the end of the event, a link to its recording is added to this field. We do not show it on the site. The field is necessary in order not to manually insert videos in automatic mailings, but to constantly take them from the same place
4. Active check-box*
    1. if the checkbox is checked it means this PC page will show on the website
    2. if the checkbox is not checked it means this PC page will not show on the website

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### The “Content” section

![Untitled](Untitled%2027.png)

1. The papers club short description* — [https://cln.sh/89RLZfqy](https://cln.sh/89RLZfqy)
2. Paper link* — link to the relevant paper which will be discussed in the relevant event
3. The paper link label* — the name of the papers added in the previous step. The name will show on the website — [https://cln.sh/MfKvCj1G](https://cln.sh/MfKvCj1G)
4. link to the source — link to google calendar. The link is used to add it to the automatic mailing list for all registered users. It should be a link that, when clicked, the user immediately opens a slot reservation in his calendar.

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create

### The “Host” section

![Untitled](Untitled%2028.png)

1. Main host — use the dropdown list for choosing the Main Host of the PC. Be sure you already add information about the host in the “Person” entity. All information in this dropdown list is from the “Persons” entity.
2. Main host about — in this field, a biography about the host, his achievements, and everything that is important to highlight for the audience is added — [https://cln.sh/XRrWRzGV](https://cln.sh/XRrWRzGV) 

### The “Partners” section

![Untitled](Untitled%2029.png)

Partners (*the field is not required*) — used for showing the partner's logos on the relevant papers club page — [https://cln.sh/dzYBYc9T](https://cln.sh/dzYBYc9T)

- you can choose relevant partners from the list provided (up to 3 partners recommended)
- if the desired partners are not listed, you can easily add them by clicking the green plus button

### The “Hosts” section

A section where you can add guest speakers.

![Untitled](Untitled%2030.png)

1. Add another host button — clicking this button brings up a drop-down list of people you can add as guest speakers
2. The list from which the guest speaker for the PC is selected. Be sure you already add information about the coach in the “Person” entity. All information in this dropdown list is from the “Persons” entity.

### The “PC Review” section

![Untitled](Untitled%2031.png)

1. Content — the text of the review
2. Author — the review author. Be sure you already add information about the coach in the “Person” entity. All information in this dropdown list is from the “Persons” entity.
3. Add another PC review — with this button, you can add one more review to the PC page

### The “Partners info” section (optional section)

![Untitled](Untitled%2032.png)

1. Partner* — you can choose relevant partners from the list provided. Be sure you already add information about the coach in the “Partners” entity. All information in this dropdown list is from the “Partners” entity. — [https://cln.sh/Wqg96jNv](https://cln.sh/Wqg96jNv)
2. Description* — short description of the partner — [https://cln.sh/86T7dPnl](https://cln.sh/86T7dPnl)
3. Citation* — the quote from the partner representative — [https://cln.sh/9vJdzr3F](https://cln.sh/9vJdzr3F)
4. Author* — the custom field with the name of the quoted author — [https://cln.sh/0cWKDRgy](https://cln.sh/0cWKDRgy)
5. Picture*— the ability to upload a custom picture to the block — [https://cln.sh/psnzfhnw](https://cln.sh/psnzfhnw)
6. Add another Partner info — adding the same block of content for another partner on this page

*- All fields marked with “*” are required for creating the course page. If fields are empty the page does not create