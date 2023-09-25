## Define the people who should appear in the credits as Credit objects  
# url_list is a list of tuple with 'site icon image' and 'clickable url element'. 
# Here the url is the same as the text string that's printed, add another tuple if you want to print different text for clickable url.

# uncategorised credit list that is used in template 1b and 2b
image anth_profile = "images/credits/anth_profile.png"
image rafa_profile = "images/credits/rafa_profile.png"
image renz_profile = "images/credits/renz_profile.png"
image wendy_profile = "images/credits/wendy_profile.png"

image Itch = "images/credits/logo/Itch.png"
image Twitter = "images/credits/logo/Twitter.png"
image Instagram = "images/credits/logo/Instagram.png"
image Youtube = "images/credits/logo/Youtube.png"
image Github = "images/credits/logo/Github.png"
image Behance = "images/credits/logo/Behance.png"

define credit_list = [
    # Gaming Variety Potato
    Credit(name = "Rafael Cruz", role = "Artist", image_name = "rafa_profile", url_list = [
        ("Itch", "https://rafazcruz.itch.io/"),
        ("Behance", "https://www.behance.net/rafazcruz")
    ]),
    # Name 2 (Has no logos for testing purposes)
    Credit(name = "Seoa Nam (Wendy Nam)", role = "Programmer", image_name = "wendy_profile", url_list = [
        ("Itch", "https://seo-a-nam.itch.io/"),
        ("Github", "https://github.com/Wendy-Nam")
    ]),
    # Name 3
    Credit(name = "Renz Ibarra", role = "Writing and Sound Design", image_name = "renz_profile", url_list = [
        ("Itch", "https://renzibgaming.itch.io/"),
        ("Instagram", "https://www.twitter.com/gaming_v_potato/")
    ]),
    Credit(name = "Anthrophantasmus (Hamza Aydın)", role = "Music", image_name = "anth_profile", url_list = [
        ("Itch", "https://anthrophantasmus-music.itch.io/"),
        ("Instagram", "https://www.instagram.com/anthrophantasmus_music/"),
        ("Youtube", "https://www.youtube.com/channel/UCryMx7RshwDKNHQ-amgEm0A"),
        ("Twitter", "@PhantasmusMusic")
    ])
    # Name 4
    
    # Name 5
    # Credit(name = "Name 5", role = "(Placeholder)", image_name = "logo", url_list = [
    #     ("twitter-original", "https://www.twitter.com/gaming_v_potato/")
    # ]),
]