# Course Technical

## Overview

The Courses page in the application is built using Next.js for the frontend and Django for the backend.

## Frontend

The frontend of the Courses page is handled by two main files: `[trackId].tsx` and `index.tsx`.

### `[trackId].tsx`

This file is responsible for rendering a specific course page based on the `trackId` provided in the URL. It fetches the course details from the backend using the `getTrackDetails` and `getTracksList` functions from the `apiHandlers` utility.

The `getServerSideProps` function is used to fetch the course details and list of all courses during server-side rendering. The fetched data is then passed as props to the main component for rendering the course details.

### `index.tsx`

This file is responsible for rendering the main Courses page which lists all the available courses. It fetches the list of all courses, categories, and home page details from the backend using the `getTracksList`, `getCategories`, and `getHomePage` functions from the `apiHandlers` utility.

The `getServerSideProps` function is used to fetch the required data during server-side rendering. The fetched data is then passed as props to the main component for rendering the list of courses.

## Backend

The backend of the Courses page is handled by Django. The main files involved are `models.py`, `views.py`, `serializers.py`, and `services.py`.

### `models.py`

This file defines the `Track` model which represents a course. It includes fields for the course name, subtitle, description, start and end dates, registration dates, price, and many others.

The `TrackEnrollmentApplication` model is used to handle course enrollments. It includes fields for the user's full name, email, and preferences for receiving newsletters and sharing info with the host.

### `views.py`

This file defines the `TrackViewSet` which handles the API endpoints for fetching course details (`retrieve` action) and enrolling in a course (`enroll` action).

### `serializers.py`

This file defines the serializers for the `Track` and `TrackEnrollmentApplication` models. The `TrackListSerializer` and `TrackDetailSerializer` are used to serialize the course details for the API responses. The `TrackEnrollSerializer` is used to validate the data for course enrollments.

### `services.py`

This file defines the `track_enroll` function which handles the process of enrolling a user in a course. It creates a `TrackEnrollmentApplication` instance, sends a course registration form to SendPulse, and adds the course to the user's list of courses.

## Connection Between Frontend and Backend

The frontend fetches the course details and list of all courses from the backend using the `getTrackDetails` and `getTracksList` functions in the `apiHandlers` utility. These functions make API requests to the backend endpoints defined in the `TrackViewSet`.

When a user enrolls in a course, the frontend sends a POST request to the `enroll` endpoint with the user's details. The backend then handles the enrollment process as described above.

## Django Admin

In the Django admin, you can create and manage courses by editing the `Track` model. You can also manage course enrollments through the `TrackEnrollmentApplication` model. The fields in these models correspond to the data displayed on the Courses page in the frontend.

## Courses Page Documentation

This document describes the technical details of the Courses page in the application, including the frontend and backend components, as well as the connection between the two. It also provides information on how to manage courses using the Django admin.