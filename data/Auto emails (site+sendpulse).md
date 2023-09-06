# Auto emails (site+sendpulse)

Automation of letters takes place in the connection — website + sendpuls

- from the side of the website, we send information that is taken from the site's pages and puts on the relevant emails
- the trigger for sending emails is registration or payment (in the future)

The scheme of auto emails logic — [https://whimsical.com/trigger-emails-DCseM9pPcKJbXR535RfEBc](https://whimsical.com/trigger-emails-DCseM9pPcKJbXR535RfEBc)

- Preview
    
    ![Untitled](Untitled%201.png)
    

<aside>
⚠️ Importantly! There are no AI-enabled automated emails, as the main CTA is a call booking (currently this is a Hubspot call booking via the link - [https://meetings-eu1.hubspot.com/kateryna-bova/intro-meeting](https://meetings-eu1.hubspot.com/kateryna-bova/intro-meeting))

</aside>

Paramets which Sendpuls get from the website:

**Курс (факт на зараз)**

- email
- full_name
- event_name
- event_tags
- email_subscription
- додатково чекаємо — мова сайту “client_language” (для різних мов автолистів)
- додатково чекаємо — статус реєстрації (open/waitlist)

**РС (факт на зараз)**

- email
- linked_in
- full_name
- event_tags
- email_subscription
- event_name
- date
- time
- link_to_source
- paper_link
- paper_link_label
- host_full_name
- host_profession
- додатково чекаємо —статус (буде чи вже пройшов)
- додатково чекаємо —відеозапис сесії

[Current and planned auto-emails](Current%20and%20planned%20auto-emails%20c6955a16cfd648d3a8dfdf63d91f5145.md)