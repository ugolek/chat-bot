# Models

# Models

## AboutUs Model:

- `cover_image`: The cover image for the About Us section.
- `header_title`: The title for the header section.
- `header_subtitle`: The subtitle for the header section.
- `header_description`: The description for the header section.
- `photo_1`: The URL of the first photo.
- `photo_2`: The URL of the second photo.
- `horizontal_blocks_title`: The title for the horizontal blocks section.
- `questions_block_title`: The title for the questions block section.
- `questions_block_description`: The description for the questions block section.
- `contact_email`: The contact email address.
- `contact_person`: The person to contact.
- `for_ukrainian_title`: The title for the Ukrainian section.
- `for_ukrainian_description`: The description for the Ukrainian section.
- `for_ukraine_photo`: The photo for the Ukrainian section.
- `related_companies`: The list of related companies.
- `office_address_title`: The title for the office address section.
- `office_address`: The office address.
- `statistics`: The list of statistics, each with a title and description.
- `email_blocks`: The list of email blocks, each with a title and email address.
- `info_for_block_with_photos`: The list of info blocks with photos, each with a title, description, and photo URL.
- `info_blocks`: The list of info blocks, each with a title, description, and button title.

## Business Model:

- `id`: The ID of the business.
- `title`: The title of the business.
- `main_image`: The URL of the main image for the business.
- `description`: The description of the business.
- `button_link`: The link for the button.
- `navigation_title`: The title for the navigation section.
- `navigation_blocks`: The list of navigation blocks, each with a title, description, button title, link, and link target.
- `statistics`: The list of statistics, each with a title and description.
- `partners_title`: The title for the partners section.
- `partners`: The list of partner companies.
- `statistics_title`: The title for the statistics section.
- `statistics_description`: The description for the statistics section.
- `courses_title`: The title for the courses section.
- `contact_title`: The title for the contact section.
- `contact_description`: The description for the contact section.
- `contact_persons`: The person(s) to contact.
- `contact_button`: The title for the contact button.
- `contact_link`: The link for the contact button.
- `contact_link_target`: The target attribute for the contact button link.

## Company Model

- `id` (number): The unique identifier of the company.
- `name` (string): The name of the company.
- `linked_in_link` (string): The LinkedIn profile link of the company.
- `web_site_link` (string): The website link of the company.
- `logo` (string): The path or URL to the logo of the company.

## Company Employment Model

- `company` (object of type Company): The company associated with the employment.
- `profession` (string): The profession or job title of the employment.

## Course Model

- `id` (number): The unique identifier of the course.
- `slug` (string): The slug or URL-friendly version of the course name.
- `name` (string): The name of the course.
- `subtitle` (string): The subtitle or brief description of the course.
- `description` (string): The detailed description of the course.
- `video_id` (string): The ID of the video associated with the course.
- `video_active` (boolean): Indicates whether the video is active or not.
- `price` (string): The price of the course.
- `language` (string): The language of the course.
- `numberOfSessions` (number): The number of sessions in the course.
- `mainCoach` (object of type Person): The main coach or instructor of the course.
- `is_checkout_enable` (boolean): Indicates whether the checkout is enabled for the course.
- `designedForTitle` (string): The title of the target audience for the course.
- `designedForDescription` (string): The description of the target audience for the course.
- `courseAboutContent` (string): The content or information about the course.
- `member_discount_price` (string): The discounted price for members.
- `discount_end_date` (Date): The end date of the discount.
- `end_registration_date` (Date): The end date for registration.
- `freeSessionTopic` (string): The topic of the free session.
- `freeSessionDate` (Date): The date of the free session.
- `freeSessionDateString` (string): The formatted date string of the free session.
- `freeSessionFormat` (string): The format of the free session.
- `freeSessionCoach` (object of type Person): The coach or instructor of the free session.
- `freeSessionLink` (string): The link to the free session.
- `meetTheTopContent` (string): The content or information about meeting the top.
- `actual_price` (string): The actual price of the course.
- `duration` (string): The duration of the course.
- `session_duration` (string): The duration of each session.
- `spots_available` (string): The number of available spots.
- `schedule` (array): The schedule or timetable of the course.
- `start_date` (string): The start date of the course.
- `end_date` (Date): The end date of the course.
- `date_placeholder` (string): The placeholder for the date.
- `time_status` (object of type TimeStatus): The status of the time.
- `coaches` (array): The coaches or instructors of the course.
- `faq` (array): The frequently asked questions and their answers.
- `program_steps` (array): The steps or actions in the program.
- `course_reviews` (array): The reviews or feedback for the course.
- `skills_bullet_points` (array): The bullet points or key skills of the course.
- `additional_behavior` (object of type AdditionalBehaviors): Additional behaviors associated with the course.

## Event Model

- `id`: The unique identifier of the event.
- `slug`: The URL-friendly version of the event name.
- `name`: The name of the event.
- `title`: The title of the event.
- `start_date`: The start date of the event.
- `start_date_str`: The start date of the event as a string.
- `number_of_sessions`: The number of sessions for the event.
- `description`: The description of the event.
- `type`: The type of the event (Online, Offline, Virtual).
- `speakers`: An array of persons who are speakers at the event.
- `tags`: An array of tags associated with the event.
- `form_title`: The title of the event form.
- `event_description_title`: The title of the event description.
- `event_description_content`: The content of the event description.
- `who_is_for_title`: The title of the target audience for the event.
- `who_is_for_content`: The content describing the target audience for the event.
- `speakers_title`: The title of the event speakers.
- `what_you_get_title`: The title of what attendees will get from the event.
- `what_you_get_bullet_points`: An array of bullet points describing what attendees will get from the event.
- `event_speakers`: An array of objects containing content and speaker information.

## PaperClub Model

- `id`: The unique identifier of the paper club.
- `slug`: The URL-friendly version of the paper club name.
- `name`: The name of the paper club.
- `description`: The description of the paper club.
- `format`: The format of the paper club.
- `time_status`: The time status of the paper club (coming soon, completed, ongoing).
- `time_placeholder`: The placeholder for the time of the paper club.
- `start_date`: The start date of the paper club.
- `end_date`: The end date of the paper club.
- `end_registration_date`: The end registration date of the paper club.
- `price`: The price of the paper club.
- `main_host`: The main host of the paper club.
- `main_host_about`: The information about the main host of the paper club.
- `hosts`: An array of persons who are hosts of the paper club.
- `partners`: An array of companies who are partners of the paper club.
- `tags`: An array of tags associated with the paper club.
- `paperLinkLabel`: The label for the paper club link.
- `paperLink`: The link for the paper club.
- `partner_infos`: An array of objects containing partner, author, description, citation, and picture information.
- `paper_club_reviews`: An array of paper club reviews.
- `additional_behavior`: Additional behaviors of the paper club.

## Person Model

- `first_name`: The first name of the person.
- `last_name`: The last name of the person.
- `avatar`: The avatar of the person.
- `avatar_big`: The big avatar of the person.
- `profession`: The profession of the person.
- `current_company`: The current company of the person.
- `companies`: An array of company employments of the person.
- `linkedin_link`: The LinkedIn link of the person.
- `hosted_tracks`: An array of hosted tracks by the person.

## Tag Model

- `name`: The name of the tag.
- `id`: The unique identifier of the tag.

## TimeStatus Model

- `COMING_SOON`: The time status indicating that an event is coming soon.
- `COMPLETED`: The time status indicating that an event is completed.
- `ONGOING`: The time status indicating that an event is ongoing.

## Workshop Model

- `id`: The unique identifier of the workshop.
- `slug`: The URL-friendly version of the workshop name.
- `name`: The name of the workshop.
- `start_date`: The start date of the workshop.
- `language`: The language of the workshop.
- `number_of_sessions`: The number of sessions for the workshop.
- `description`: The description of the workshop.
- `main_host`: The main host of the workshop.