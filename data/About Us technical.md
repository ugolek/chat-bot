# About Us technical

# Technical Documentation for the About Us Page

## Frontend

The frontend of the About Us page is built using Next.js, a popular React framework. The main file for this page is `gathers-FE/pages/about-us/index.tsx`.

### Key Components

- `BaseLayout`: This is the main layout component that wraps the entire page content.
- `RichText`: This component is used to display rich text content fetched from the backend.
- `Image`: This component from the `next/image` package is used to optimize image loading.

### Hooks

Several custom hooks are used to handle button click events:

- `useExploreCoursesButton`: Handles the click event for the "Explore Courses" button.
- `useAllPcButton`: Handles the click event for the "All PC" button.
- `useNewDemoButton`: Handles the click event for the "Book Demo" button.

## Server-Side Rendering

The `getServerSideProps` function fetches the data needed for the page from the backend. It uses the `getAboutUsDetails` function to fetch the details of the About Us page.

## Backend

The backend of the About Us page is built using Django. The main model for this page is `AboutUs` in `gathers-BE/apps/content/models.py`.

### Key Fields

The `AboutUs` model contains several fields that store the content displayed on the About Us page:

- `header_title`, `header_subtitle`, `header_description`: These fields store the main title, subtitle, and description of the page.
- `statistics`, `info_for_block_with_photos`, `info_blocks`, `email_blocks`: These fields are related fields that store the data for the statistics, photo information blocks, information blocks, and email blocks on the page.
- `related_companies`: This field stores the related companies displayed on the page.

### Connection Between Frontend and Backend

The frontend fetches the data from the backend using the `getAboutUsDetails` function. This function makes a request to the backend and retrieves the data stored in the `AboutUs` model.

The data is then passed to the frontend components as props. For example, the `header_title` field from the `AboutUs` model is passed to the `RichText` component to display the main title of the page.

### Django Admin

In the Django admin, the `AboutUs` model can be managed by administrators. They can update the content of the About Us page by editing the fields of the `AboutUs` model. The changes will be reflected on the frontend after the data is fetched again.

## Conclusion

The About Us page is a dynamic page that displays information about the organization. The content is managed in the Django admin and displayed on the frontend using Next.js. The page includes several sections such as a header section, statistics, information blocks, and related companies.