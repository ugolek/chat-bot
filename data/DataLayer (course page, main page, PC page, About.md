# DataLayer (course page, main page, PC page, About us page)

| Page | Event Name | Event Paramenters | User’s action | Data Layer |
| --- | --- | --- | --- | --- |
| Sample page | event_sample |  |  | "dataLayer.push({ 
'event': 'event_sample',
'parameter_name': {parameter_name},
'parameter_2': {parameter_2}
});" |
| Course page | course_enroll_scroll | event_name = назва курсу,
page_lang = мовна версія сайту,
page_block = first screen | “enroll” button click in the first screen (scroll to form) | "dataLayer.push({ 
'event': 'course_enroll_scroll', 
'event_name': {event_name},
'page_lang': {page_lang},
'page_block': {page_block}
});" |
| Course page | course_enroll_form_success | event_name = назва курсу, page_lang = мовна версія сайту | fill up form (success state) | "dataLayer.push({ 
'event': 'course_enroll_form_success', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Course page | course_enroll_form_error | event_name = назва курсу, page_lang = мовна версія сайту | fill up form (error state) | "dataLayer.push({ 
'event': 'course_enroll_form_error', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Course page | course_video_button | event_name = назва курсу, page_lang = мовна версія сайту | “start video” button click | "dataLayer.push({ 
'event': 'course_video_button', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Course page | course_free_session_button | event_name = назва курсу, page_lang = мовна версія сайту | “join” free session button click | "dataLayer.push({ 
'event': 'course_free_session_button', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Course page, Papers club page | email_button | event_name = назва курсу, page_lang = мовна версія сайту,
page_type = course or pc | “Send an email” button click on Course page or “consult me” on Papers club page | "dataLayer.push({ 
'event': 'email_button', 
'event_name': {event_name},
'page_lang': {page_lang},
'page_type': {page_type}
});" |
| Course page | lnd_button | event_name = назва курсу, page_lang = мовна версія сайту | “Send a request” button click in Use your L&D budget block | "dataLayer.push({ 
'event': 'lnd_button', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Course page | course_free_session_scroll | event_name = назва курсу, page_lang = мовна версія сайту | “join free session” button click in first screen | "dataLayer.push({ 
'event': 'course_free_session_scroll', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Main page, About Us | explore_courses_button | page_block = main_first_screen/main_featured/about_page, page_lang = мовна версія сайту | “explore courses” button click (first screen)
or
“all courses” button click (featured courses screen)
or “explore all courses” on Abous us page | "dataLayer.push({ 
'event': 'explore_courses_button', 
'event_name': {event_name},
page_block': {page_block},
'page_lang': {page_lang}
});" |
| Main page | become_expert_button | page_lang = мовна версія сайту | “Join as an expert” button click | "dataLayer.push({ 
'event': 'become_expert_button', 
'page_lang': {page_lang}
});" |
| Main page, About us | book_demo_button | page_lang = мовна версія сайту
page_type = main or about us | “Book a demo” button click on Main page
or
”Book a meeting” button click on About us | "dataLayer.push({ 
'event': 'all_pc_button', 
'page_lang': {page_lang},
'page_type': {page_type}
});" |
| Main page, About us | all_pc_button | page_lang = мовна версія сайту
page_type = main or about us | “All Papers Club” button click on main page or About us page | "dataLayer.push({ 
'event': 'all_pc_button', 
'page_lang': {page_lang},
'page_type': {page_type}
});" |
| Main page, Papers Club page | discord_button | page_lang = мовна версія сайту
page_type = main or pc | “Join Discord” button click | "dataLayer.push({ 
'event': 'discord_button', 
'page_lang': {page_lang},
'page_type': {page_type}
});" |
| Header/Footer | community_button | page_lang = мовна версія сайту
page_block = header or footer | “Join the community” button click | "dataLayer.push({ 
'event': 'community_button', 
'page_lang': {page_lang},
'page_block': {page_block}
});" |
| Papers club page | pc_join_scroll | page_lang = мовна версія сайту,
page_block = first screen,
event_name = назва PC | “Join the event” button click (scroll to form) | "dataLayer.push({ 
'event': 'pc_join_scroll', 
'event_name': {event_name},
'page_lang': {page_lang},
'page_block': {page_block}
});" |
| Papers club page | pc_become_moderator | event_name = назва PC, page_lang = мовна версія сайту | “Become moderator” button click | "dataLayer.push({ 
'event': 'pc_become_moderator', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Papers club page | pc_enroll_form_success | event_name = назва PC, page_lang = мовна версія сайту | fill up form (success state) | "dataLayer.push({ 
'event': 'pc_enroll_form_success', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| Papers club page | pc_enroll_form_error | event_name = назва PC, page_lang = мовна версія сайту | fill up form (error state) | "dataLayer.push({ 
'event': 'pc_enroll_form_error', 
'event_name': {event_name},
'page_lang': {page_lang}
});" |
| About us | about_sales_email | page_lang = мовна версія сайту | Email click in Quesions block | "dataLayer.push({ 
'event': 'about_sales_email', 
'page_lang': {page_lang}
});" |