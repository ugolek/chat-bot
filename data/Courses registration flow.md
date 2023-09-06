# Courses registration flow

According to the flow course:

- on the site, the client's flow ends with filling out the form. His data is stored in the admin
- after filling out the form, the user receives an automatic letter "thank you for registration, wait for the payment link" + a letter to Sofia that we have +1 registration for the course.
- Communication regarding payment or clarifications regarding a specific course is handled manually by Sofia.

<aside>
⚠️ Separately, in the registration flow, there is a question about surveying participants for potential ML matching. Do we want to ask questions about the skills of people who register and at what point (before checkout or in the letter after payment)?

</aside>

---

Checkout flow prototype — [https://www.figma.com/file/CBkDEJAiZt6FgSnkWSS72O/Checkout-flow-(online-courses)?node-id=0%3A1&t=Lvh6vtLe2WTLTyFD-1](https://www.figma.com/file/CBkDEJAiZt6FgSnkWSS72O/Checkout-flow-(online-courses)?node-id=0%3A1&t=Lvh6vtLe2WTLTyFD-1)

After checkout integration, the registration flow on the courses pages should look like this:

ℹ️ a registration form on a separate page, not a screen, or a pop-up on the landing page

- the user fills out the form - name + email + linkedin
- the user sees the course payment screen with information about what he is buying (course name, dates):
    - if the payment is successful:
        - the user receives automatically a letter in the mail with confirmation of the seat reservation and organisational information (*to create an automatic letter, the site must send the parameters that the user will see in the letter. Sandpulse needs to create a letter template that will be responsible for this flow*)
    - if the payment is not successful:
        - the user receives a letter with the context "we are glad that you have registered for the course" and additional information about the free event + with a duplicate link to continue the payment flow (*to create an automatic letter, the site must send the parameters that the user will see in the letter. Sandpulse needs to create a letter template that will be responsible for this flow)*
        - a week before the start of the course, if the user has not paid for the course, we will remind him of the payment + send a video from the free session of the same course (*to create an automatic letter, the site must send the parameters that the user will see in the letter. Sandpulse needs to create a letter template that will be responsible for this flow)*
        

If the user registers for a course for which there is currently no recruitment (join the wait list):

- we send an automatic letter that as soon as recruitment for this course opens, we will inform you (*to create an automatic letter, the site must send the parameters that the user will see in the letter. Sandpulse needs to create a letter template that will be responsible for this flow)*