# Paper Club Technical

## Frontend

The frontend of the PapersClub page is handled by Next.js. The main files related to this page are `paperClub.ts` and `[paperClubId].tsx`.

### `paperClub.ts`

This file defines the `PaperClub` type which includes all the properties related to a paper club such as `id`, `slug`, `name`, `description`, `format`, `time_status`, `time_placeholder`, `start_date`, `end_date`, `end_registration_date`, `price`, `main_host`, `main_host_about`, `hosts`, `partners`, `tags`, `paperLinkLabel`, `paperLink`, `partner_infos`, `paper_club_reviews`, and `additional_behavior2`.

### `[paperClubId].tsx`

This file is responsible for rendering the details of a specific paper club. It fetches the details of the paper club from the backend using the `getServerSideProps` function and the `getPaperClubsDetails` API handler. It also fetches a list of all paper clubs using the `getPaperClubsList` API handler.

## Backend

The backend of the PapersClub page is handled by Django. The main files related to this page are `models.py`, `views.py`, `admin.py`, and `serializers.py`.

### `models.py`

This file defines the `PaperClub` model which includes all the fields related to a paper club such as `slug`, `name`, `paperLink`, `paperLinkLabel`, `linkToSource`, `start_date`, `time_placeholder`, `end_date`, `end_registration_date`, `price`, `description`, `format`, `active`, `club_recording`, `additional_behavior`, and others.

### `views.py`

This file defines the `PaperClubViewSet` which handles the HTTP methods for the paper club. It includes actions like `list`, `retrieve`, and `enroll`. The `list` action fetches a list of all paper clubs, the `retrieve` action fetches the details of a specific paper club, and the `enroll` action enrolls a user to a paper club.

### `admin.py`

This file defines the Django admin interface for the `PaperClub` model. It includes inline models for `PaperClubHostInline`, `PaperClubReviewInline`, `FeaturedPaperClubsInline`, and `PartnerInfoInline`.

### `serializers.py`

This file defines the serializers for the `PaperClub` model. It includes serializers like `PaperClubListSerializer`, `PaperClubDetailSerializer`, `PaperClubEnrollSerializer`, and `PaperClubsListingPageSerializer`.

## Connection Between Frontend and Backend

The frontend fetches the data from the backend using API handlers like `getPaperClubsDetails` and `getPaperClubsList`. These handlers make HTTP requests to the backend and receive the data in the form of JSON. This data is then used to populate the properties of the `PaperClub` type in the frontend.

The backend receives these requests, fetches the data from the database, and sends it back to the frontend. The Django views handle these requests and use the serializers to convert the Django models into JSON format.

The Django admin interface allows for the creation and management of the `PaperClub` entities. The fields in the Django admin correspond to the properties of the `PaperClub` type in the frontend.

In summary, the frontend sends HTTP requests to the backend, the backend fetches the data from the database and sends it back to the frontend in JSON format. The frontend then uses this data to populate the properties of the `PaperClub` type and render the PapersClub page.