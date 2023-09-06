# Papers Club (PC)

# Papers Club (PC)

Welcome to Papers Club (PC), where people share and discuss the latest academic papers about machine learning, including the newest techniques, models, and algorithms. Our goal is to provide a forum for engineers and researchers in the field to meet, share their experiences, and learn from each other. Joining Papers Club can help you stay up-to-date with the latest techniques and models that are being used in the industry and provide actionable follow-up content that can help you apply what you've learned to your work.

## User Documentation

### Papers Club Main Page (index.tsx)

This is the main page for Papers Club. It displays a list of all the Paper Clubs available.

1. **Paper Clubs List**: This section displays all the Paper Clubs. Each Paper Club is represented by a box that includes details like the title, description, and status (coming soon, ongoing, completed). Users can filter the Paper Clubs by categories or partners.
2. **Free Block**: This section encourages users to join the Discord community. It includes a button that redirects users to the Discord link.
3. **How It Works (HIW) Block**: This section explains how Papers Club works. It includes a series of steps or guidelines for users to follow.
4. **Become a Host Block**: This section invites users to become a host for a Paper Club. It includes a button that opens an email to [help@gathers.ai](mailto:help@gathers.ai) when clicked.

### Individual Paper Club Page ([paperClubId].tsx)

This page provides detailed information about a specific Paper Club.

1. **Paper Club Details**: This section displays detailed information about the Paper Club, including the title, description, start and end dates, and price.
2. **Registration Form**: This section allows users to register for the Paper Club. It includes a form where users can enter their contact information.
3. **How It Works (HIW) Block**: Similar to the main page, this section explains how Papers Club works.
4. **Become a Host Block**: This section invites users to become a host for a Paper Club. It includes a button that opens an email to [help@gathers.ai](mailto:help@gathers.ai) when clicked.
5. **Recommended By Block**: If available, this section displays reviews from experts who recommend the Paper Club.
6. **You May Also Like Block**: This section suggests other Paper Clubs that the user might be interested in.

## Backend Models ([models.py](http://models.py/))

The backend models define the data structure for the Paper Clubs. The main model is PaperClub, which includes fields for the Paper Club's details, hosts, partners, tags, and reviews. Other models include PartnerInfo, PaperClubReview, and PaperClubEnrollmentApplication, which represent additional information related to the Paper Club.

<aside>
👉 Note: This document has been edited for clarity and readability.

</aside>

[Paper Club Admin](Paper%20Club%20Admin%204616beae46d84b19a4163c0bf1b14018.md)

[Paper Club Technical](Paper%20Club%20Technical%206a9389ae52e1422388719b84177761f7.md)