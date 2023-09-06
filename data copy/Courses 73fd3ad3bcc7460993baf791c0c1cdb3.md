# Courses

# User Documentation for the Courses Pages

## Courses List Page (index.tsx)

This page displays a list of all available courses (also referred to as "tracks") offered by the platform. Here's a brief overview of the main sections:

1. **Course Categories:** This section allows users to filter courses based on their categories. Users can select one or more categories to view the corresponding courses.
2. **Ongoing Courses:** This section displays the courses that are currently ongoing. Each course is presented in a box that includes the course title, description, and other relevant details.
3. **Coming Soon Courses:** Similar to the ongoing courses section, this section lists the courses that are scheduled to start in the future.
4. **Hypotheses Block:** This section provides some insights or hypotheses related to the courses. It also includes a button that redirects users to the "Paper Clubs" page.
5. **Come For Block:** This section is designed to attract users to join the platform's community on Discord. It includes a button that links to the Discord server.

## Course Details Page ([trackId].tsx)

This page provides detailed information about a specific course. The course is identified by its trackId. Here's a brief overview of the main sections:

1. **Course Details:** This section presents comprehensive information about the course, including its title, description, price, duration, start and end dates, and more.
2. **Course Schedule:** This section provides a schedule of the course sessions, including the date and time of each session.
3. **Course Reviews:** If available, this section displays reviews given by previous participants of the course.
4. **FAQ Block:** This section provides answers to frequently asked questions about the course.
5. **Registration Form:** If the course registration is open, this section displays a form that users can fill out to register for the course.
6. **You May Also Like:** This section suggests other courses that users might be interested in, based on the current course.

## Course Model (models.py)

The Track model in the models.py file represents a course in the backend of the application. It includes fields for storing various details about a course, such as its title, description, price, duration, start and end dates, and more. The model also includes methods for filtering and sorting courses based on different criteria.

---

[Course Admin](Course%20Admin%20dcb7135705e9494793e1a8c5aa71c705.md)

[Course Technical](Course%20Technical%2048debbcd1f99419d86fcea3342d866c9.md)