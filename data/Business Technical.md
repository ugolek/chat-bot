# Business Technical

# Technical Documentation for Business Page

The Business page provides a comprehensive overview of various aspects of the business, including courses, experts, reviews, and more.

## Frontend

The frontend of the Business page is built using Next.js. The main component is `BusinessPage` which is defined in `gathers-FE/pages/business/index.tsx`.

The `BusinessPage` component receives several props including `incomingCourses`, `incomingPaperClubs`, `business`, `locale`, `initialProps`, and `breadcrumbs`. These props are fetched from the backend using the `getServerSideProps` function.

The `BusinessPage` component is composed of several blocks, each representing a different section of the page. These blocks include:

- Base Info Block
- Navigation Block
- Statistics Block
- Courses Block
- Contact Block
- Experts Block
- Review Block
- Paper Block
- Arrow Block
- Questions Block

Each block is a `div` element with a unique `id` and a specific set of classes for styling. The content of each block is dynamic and depends on the data provided by the backend.

## Backend

The backend of the Business page is built using Django. The main model is `Business` which is defined in `gathers-BE/apps/business/models.py`.

The `Business` model includes several fields that correspond to the blocks in the frontend. These fields include:

- `title`, `description`, `button_title`, `button_link`, `link_target`, `main_image` for the Base Info Block
- `navigation_title`, `navigation_blocks` for the Navigation Block
- `statistics_title`, `statistics_description`, `statistics`, `partners_title`, `partners` for the Statistics Block
- `courses_title` for the Courses Block
- `contact_title` for the Contact Block
- `experts_orders` for the Experts Block
- `business_reviews` for the Review Block
- `paper_clubs_title` for the Paper Block
- `arrows_title`, `arrows_list`, `arrow_button`, `arrow_link`, `arrow_link_target`, `arrow_image` for the Arrow Block
- `questions_title`, `questions_description`, `questions_contact_email` for the Questions Block

The `Business` model also includes several related models such as `NavigationBlock`, `ExpertOrder`, `Review`, and `BusinessEnrollmentApplication`.

## Connection between Frontend and Backend

The frontend fetches data from the backend using the `getServerSideProps` function. This function calls several API handlers including `getBusinessPage`, `getTracksList`, and `getPaperClubsList`. The data fetched from these API handlers is then passed as props to the `BusinessPage` component.

In the `BusinessPage` component, the data is used to populate the content of the different blocks. For example, the `title`, `description`, and `button_title` fields from the `business` prop are used in the Base Info Block.
:::