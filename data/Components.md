# Components

- [Accordion](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [Breadcrumb](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [Carousel](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [CheckBox](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [CountDownTimer](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [CourseBox](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [ExperienceBlock](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [PaperClubBox](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [RegistrationFormComponent](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [AdaptiveLink](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [CheckMarkText](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [IconText](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [LocaleSwitcher](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [MediumCard](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [PopUp](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [ReviewBlock](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [RichText](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [SmallCard](Components%20aa3920ae476145b1bfa72d7d8f878918.md)
- [YoutubeVideo](Components%20aa3920ae476145b1bfa72d7d8f878918.md)

# Accordion

This component is used to create an interactive collapsible content panel for presenting information in a limited amount of space.

**AccordionProps:**

- `title`: The title of the accordion.
- `children`: The content of the accordion.
- `id`: The unique identifier for the accordion.

# Breadcrumb

This component is used to create a navigation aid that allows users to keep track of their locations within programs, documents, or websites.

**BreadCrumpsProps:**

- `children`: The individual breadcrumb items.

# Carousel

This component is used to create a rotating set of images, rotation stops on keyboard focus on carousel tab controls or hovering the mouse pointer over images.

**CarouselProps:**

- `children`: The items of the carousel.
- `breakpoints`: The breakpoints for responsive design.
- `enableBreakpoints`: Flag to enable breakpoints.
- `enableAutoplay`: Flag to enable autoplay.
- `hideNavigation`: Flag to hide navigation.

# CheckBox

This component is used to create a checkbox that can be toggled by the user.

**CheckBoxProps:**

- `children`: The label of the checkbox.
- `onChange`: The function to call when the checkbox value changes.
- `value`: The current value of the checkbox.
- `id`: The unique identifier for the checkbox.

# CountDownTimer

This component is used to create a countdown timer.

**CountDownTimerProps:**

- `targetDate`: The date to count down to.
- `t`: The translation function.

# CourseBox

This component is used to display course information in a box layout.

**CourseBoxProps:**

- `trackDetails`: The details of the course.
- `index`: The index of the course.
- `locale`: The current locale.

# ExperienceBlock

This component is used to display experience information in a block layout.

**ExperienceBlockProps:**

- `title`: The title of the experience.
- `description`: The description of the experience.

# PaperClubBox

This component is used to display paper club information in a box layout.

**PaperClubBoxProps:**

- `paperClub`: The details of the paper club.
- `index`: The index of the paper club.
- `locale`: The current locale.

# RegistrationFormComponent

This component is used to create a registration form.

**RegistrationFormComponentProps:**

- `targetDate`: The target date for the registration.
- `handleSubmit`: The function to call when the form is submitted.
- `t`: The translation function.
- `buttonText`: The text for the submit button.
- `titleText`: The title of the form.
- `showTimer`: Flag to show a timer.
- `showPhone`: Flag to show a phone input field.
- `showLinkedIn`: Flag to show a LinkedIn input field.
- `showName`: Flag to show a name input field.
- `shareInfoWithHost`: Flag to allow sharing info with the host.

# AdaptiveLink

A component for rendering adaptive links.

**AdaptiveLinkProps:**

- `url`: The URL of the link.
- `text`: The text of the link.

# CheckMarkText

A component for rendering text with a checkmark.

**CheckMarkTextProps:**

- `text`: The text to display.
- `isChecked`: Flag to indicate if the text is checked or not.

# IconText

A component for rendering text with an icon.

**IconTextProps:**

- `text`: The text to display.
- `icon`: The name of the icon to display.

# LocaleSwitcher

A component for switching between different locales.

**LocaleSwitcherProps:**

- `locales`: An array of available locales.
- `currentLocale`: The currently selected locale.
- `onLocaleChange`: The function to call when the locale changes.

# MediumCard

A component for rendering a medium-sized card.

**MediumCardProps:**

- `title`: The title of the card.
- `description`: The description of the card.
- `image`: The image URL of the card.

# PopUp

A component for displaying a popup.

**PopUpProps:**

- `content`: The content to display in the popup.
- `isOpen`: Flag to indicate if the popup is open or not.
- `onClose`: The function to call when the popup is closed.

# ReviewBlock

A component for displaying a review block.

**ReviewBlockProps:**

- `rating`: The rating of the review.
- `comment`: The comment of the review.

# RichText

A component for rendering rich text.

**RichTextProps:**

- `content`: The content to display as rich text.

# SmallCard

A component for rendering a small-sized card.

**SmallCardProps:**

- `title`: The title of the card.
- `description`: The description of the card.
- `image`: The image URL of the card.

# YoutubeVideo

A component for embedding a YouTube video.

**YoutubeVideoProps:**

- `videoId`: The ID of the YouTube video.

## Accordion

This component is used to create an interactive collapsible content panel for presenting information in a limited amount of space.

**AccordionProps:**

- `title`: The title of the accordion.
- `children`: The content of the accordion.
- `id`: The unique identifier for the accordion.

## Breadcrumb

This component is used to create a navigation aid that allows users to keep track of their locations within programs, documents, or websites.

**BreadCrumpsProps:**

- `children`: The individual breadcrumb items.

## Carousel

This component is used to create a rotating set of images, rotation stops on keyboard focus on carousel tab controls or hovering the mouse pointer over images.

**CarouselProps:**

- `children`: The items of the carousel.
- `breakpoints`: The breakpoints for responsive design.
- `enableBreakpoints`: Flag to enable breakpoints.
- `enableAutoplay`: Flag to enable autoplay.
- `hideNavigation`: Flag to hide navigation.

## CheckBox

This component is used to create a checkbox that can be toggled by the user.

**CheckBoxProps:**

- `children`: The label of the checkbox.
- `onChange`: The function to call when the checkbox value changes.
- `value`: The current value of the checkbox.
- `id`: The unique identifier for the checkbox.

## CountDownTimerComponent

This component is used to create a countdown timer.

**CountDownTimerProps:**

- `targetDate`: The date to count down to.
- `t`: The translation function.

## CourseBox

This component is used to display course information in a box layout.

**CourseBoxProps:**

- `trackDetails`: The details of the course.
- `index`: The index of the course.
- `locale`: The current locale.

## ExperienceBlock

This component is used to display experience information in a block layout.

**ExperienceBlockProps:**

- `title`: The title of the experience.
- `description`: The description of the experience.

## PaperClubBox

This component is used to display paper club information in a box layout.

**PaperClubBoxProps:**

- `paperClub`: The details of the paper club.
- `index`: The index of the paper club.
- `locale`: The current locale.

## RegistrationFormComponent

This component is used to create a registration form.

**RegistrationFormComponentProps:**

- `targetDate`: The target date for the registration.
- `handleSubmit`: The function to call when the form is submitted.
- `t`: The translation function.
- `buttonText`: The text for the submit button.
- `titleText`: The title of the form.
- `showTimer`: Flag to show a timer.
- `showPhone`: Flag to show a phone input field.
- `showLinkedIn`: Flag to show a LinkedIn input field.
- `showName`: Flag to show a name input field.
- `shareInfoWithHost`: Flag to allow sharing info with the host.

## TextInput

This component is used to create a text input field.

**TextInputProps:**

- `placeholder`: The placeholder text for the input field.
- `onChange`: The function to call when the input value changes.
- `label`: The label for the input field.
- `value`: The current value of the input field.
- `validation`: The validation rules for the input field.

add this component in same format 

## Accordion

This component is used to create an interactive collapsible content panel for presenting information in a limited amount of space.

**AccordionProps:**

- `title`: The title of the accordion.
- `children`: The content of the accordion.
- `id`: The unique identifier for the accordion.

## Breadcrumb

This component is used to create a navigation aid that allows users to keep track of their locations within programs, documents, or websites.

**BreadCrumpsProps:**

- `children`: The individual breadcrumb items.

## Carousel

This component is used to create a rotating set of images, rotation stops on keyboard focus on carousel tab controls or hovering the mouse pointer over images.

**CarouselProps:**

- `children`: The items of the carousel.
- `breakpoints`: The breakpoints for responsive design.
- `enableBreakpoints`: Flag to enable breakpoints.
- `enableAutoplay`: Flag to enable autoplay.
- `hideNavigation`: Flag to hide navigation.

## CheckBox

This component is used to create a checkbox that can be toggled by the user.

**CheckBoxProps:**

- `children`: The label of the checkbox.
- `onChange`: The function to call when the checkbox value changes.
- `value`: The current value of the checkbox.
- `id`: The unique identifier for the checkbox.

## CountDownTimerComponent

This component is used to create a countdown timer.

**CountDownTimerProps:**

- `targetDate`: The date to count down to.
- `t`: The translation function.

## CourseBox

This component is used to display course information in a box layout.

**CourseBoxProps:**

- `trackDetails`: The details of the course.
- `index`: The index of the course.
- `locale`: The current locale.

## ExperienceBlock

This component is used to display experience information in a block layout.

**ExperienceBlockProps:**

- `title`: The title of the experience.
- `description`: The description of the experience.

## PaperClubBox

This component is used to display paper club information in a box layout.

**PaperClubBoxProps:**

- `paperClub`: The details of the paper club.
- `index`: The index of the paper club.
- `locale`: The current locale.

## RegistrationFormComponent

This component is used to create a registration form.

**RegistrationFormComponentProps:**

- `targetDate`: The target date for the registration.
- `handleSubmit`: The function to call when the form is submitted.
- `t`: The translation function.
- `buttonText`: The text for the submit button.
- `titleText`: The title of the form.
- `showTimer`: Flag to show a timer.
- `showPhone`: Flag to show a phone input field.
- `showLinkedIn`: Flag to show a LinkedIn input field.
- `showName`: Flag to show a name input field.
- `shareInfoWithHost`: Flag to allow sharing info with the host.

## AdaptiveLink

A component for rendering adaptive links.

**AdaptiveLinkProps:**

- `url`: The URL of the link.
- `text`: The text of the link.

## CheckMarkText

A component for rendering text with a checkmark.

**CheckMarkTextProps:**

- `text`: The text to display.
- `isChecked`: Flag to indicate if the text is checked or not.

## IconText

A component for rendering text with an icon.

**IconTextProps:**

- `text`: The text to display.
- `icon`: The name of the icon to display.

## LocaleSwitcher

A component for switching between different locales.

**LocaleSwitcherProps:**

- `locales`: An array of available locales.
- `currentLocale`: The currently selected locale.
- `onLocaleChange`: The function to call when the locale changes.

## MediumCard

A component for rendering a medium-sized card.

**MediumCardProps:**

- `title`: The title of the card.
- `description`: The description of the card.
- `image`: The image URL of the card.

## PopUp

A component for displaying a popup.

**PopUpProps:**

- `content`: The content to display in the popup.
- `isOpen`: Flag to indicate if the popup is open or not.
- `onClose`: The function to call when the popup is closed.

## ReviewBlock

A component for displaying a review block.

**ReviewBlockProps:**

- `rating`: The rating of the review.
- `comment`: The comment of the review.

## RichText

A component for rendering rich text.

**RichTextProps:**

- `content`: The content to display as rich text.

## SmallCard

A component for rendering a small-sized card.

**SmallCardProps:**

- `title`: The title of the card.
- `description`: The description of the card.
- `image`: The image URL of the card.

## YoutubeVideo

A component for embedding a YouTube video.

**YoutubeVideoProps:**

- `videoId`: The ID of the YouTube video.