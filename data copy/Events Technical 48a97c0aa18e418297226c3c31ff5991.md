# Events Technical

## Front End: Next.js

The front end of the Events page is built using Next.js, a popular React framework. The main file for this page is `gathers-FE/pages/events/[eventId].tsx`. This file is responsible for rendering the event details to the user.

The Event page uses several components from the `common` directory, including `BaseLayout`, `RichText`, `IconText`, `SmallCard`, `BigCard`, and `EventRegistrationFormComponent`. These components are used to structure the page and display the event data in a user-friendly manner.

The Event page fetches data from the backend using the `getEventDetails` and `handleFormSubmit` functions from the `common/utils/apiHandlers` module. The `getEventDetails` function is used to fetch the details of a specific event based on its `eventId`, while the `handleFormSubmit` function is used to handle the submission of the event registration form.

The Event page also uses the `useTranslation` hook from the `next-i18next` package to provide multilingual support.

## Back End: Django

The backend of the Events page is built using Django. The main file for this page is `gathers-BE/apps/events/models.py`. This file defines the data models for the events, including the `Event`, `SkillsBulletPoint`, and `EventEnrollmentApplication` models.

The `Event` model stores the details of each event, including the name, description, start date, speakers, and other relevant information. The `SkillsBulletPoint` model stores the bullet points for what users will gain from attending the event. The `EventEnrollmentApplication` model stores the enrollment applications submitted by users through the event registration form.

The `Event` model also includes several methods for querying the database, such as `get_upcoming` for fetching upcoming events and `get_past` for fetching past events.

## Connection Between Front End and Back End

The front end fetches data from the backend using the `getEventDetails` function. This function sends a GET request to the backend with the `eventId` as a parameter. The backend responds with the details of the specified event, which are then displayed on the Event page.

When a user submits the event registration form, the front end sends a POST request to the backend using the `handleFormSubmit` function. The backend saves the submitted data in the `EventEnrollmentApplication` model and responds with a confirmation message.

The fields displayed on the Event page correspond to the fields in the `Event` model. For example, the `name` field in the `Event` model corresponds to the event name displayed on the page, the `description` field corresponds to the event description, and so on.

The Django admin interface is used to manage the data in the `Event`, `SkillsBulletPoint`, and `EventEnrollmentApplication` models. Admin users can create, update, and delete events, add or remove bullet points, and view or delete enrollment applications.

##