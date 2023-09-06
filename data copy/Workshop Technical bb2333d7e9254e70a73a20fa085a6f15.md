# Workshop Technical

# Workshop Technical

The Workshop page is a detailed view of a specific workshop. It provides comprehensive information about the workshop, including its name, description, language, start date, and the number of sessions.

## Front End: Next.js

The front end of the Workshop page is built using Next.js, a popular React framework. The main file for this page is `gathers-FE/pages/workshops/[workshopId].tsx`. This file exports a default function `WorkshopId` which is a React component that renders the page.

The `WorkshopId` function receives a `WorkshopProps` object as props, which includes details about the workshop, locale, initialProps, and breadcrumbs. These props are used throughout the component to render the workshop details.

The `WorkshopId` function uses the `useTranslation` hook from `next-i18next` to provide localization for the page. It also uses several components from the `common/components` directory to build the page, including `BaseLayout`, `RichText`, `CheckMarkText`, and `QuestionsAccordion`.

The `getServerSideProps` function is used to fetch the workshop details from the backend before the page is rendered. It uses the `getWorkshopDetails` function from `common/utils/apiHandlers` to make the API call.

## Back End: Django

The back end of the Workshop page is built using Django. The main file for this page is `gathers-BE/apps/workshops/models.py`. This file defines the `Workshop` model which represents a workshop in the database.

The `Workshop` model includes fields for the workshop's name, description, language, start date, number of sessions, and other details. It also includes a `ForeignKey` field for the main host and contact person of the workshop, which are instances of the `Person` model.

The `Workshop` model also includes a `GenericRelation` field for the FAQ items of the workshop, which are instances of the `FAQ` model.

The `Workshop` model uses the `WorkshopManager` as its manager, which provides additional methods for querying the database.

## Connection Between Front End and Back End

The front end fetches the workshop details from the backend using the `getWorkshopDetails` function in `getServerSideProps`. This function makes an API call to the backend and passes the workshop ID and locale as parameters.

The backend receives this API call and queries the database for the workshop with the given ID. It then returns the workshop details as a JSON response.

The front end receives this response and uses it to set the props of the `WorkshopId` component. These props are then used to render the workshop details on the page.

The fields from the `Workshop` model that are used in the front end include `name`, `description`, `language`, `start_date`, `number_of_sessions`, `main_host`, `main_host_about`, `contact_person`, and `faq`.

In the Django admin, these fields can be edited directly. Any changes made in the admin will be reflected on the Workshop page after the next API call.