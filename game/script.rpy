# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Remy", voice="R")
define p = Character("Profesor", voice="P")
default ocena_profesora = 0
    
image remy happy = "remy_happy.png"
image remy normal = "remy_normal.png"
image remy unhappy = "remy_unhappy.png"

image profesor happy = "profesor_happy.png"
image profesor normal = "profesor_neutral.png"
image profesor unhappy = "profesor_unhappy.png"
image profesor sick = "profesor_sick.png"

image ceue = "ceue.png"
image restaurant = "restaurant.png"
image kitchen = "kitchen.png"

image duck = "duck.png"
image chicken = "chicken.png"
image shrimp = "shrimps.png"
image coctail = "coctail.png"
image tiramisu = "tiramisu.png"
image salt = "salt.png"

define music_kitchen = "audio/kitchen_theme.mp3"
define music_intro = "audio/cinematic_ai.mp3"
define music_restaurant = "audio/restaurant_theme.mp3"
define sound_bell = "audio/bell.mp3"
define sound_shock = "audio/shock.mp3"
define sound_doors = "audio/doors.mp3"
define sound_angry_doors = "audio/angry_doors.mp3"

define r_1 ="audio/r_co_by_tu_podać.ogg"
define r_sól ="audio/r_czy_dodać_sól.ogg"
define r_dziękuję ="audio/r_dziękuję_za_opinię.ogg"
define r_najlepszy_wybór ="audio/r_juz_wiem_najlepszym_wyborem_bedzie.ogg"
define r_koktail ="audio/r_koktail.ogg"
define r_mam_nadzieję ="audio/r_mam_nadzieję_że_również_danie.ogg"
define r_mięso ="audio/r_pieczenia_mięsa_w_piekarniku.ogg"
define r_tiramisu ="audio/r_tiramisu.ogg"
define r_nie_prawda ="audio/r_to_nie_prawda.ogg"

define p_d ="audio/p_doskonałe_to_jedno_z_najlepszych.ogg"
define p_n ="audio/p_Niestety_Remy_ale_to_danie.ogg"
define p_o ="audio/p_o_nie_do_lekarza.ogg"
define p_niesamowite="audio/p_yummy_niesamowite.ogg"
define p_wygląda ="audio/p_Yummy_wygląda_naprawdę.ogg"
define p_miejsce ="audio/To_miejsce_jest.ogg"


transform center:
    xalign 0.5 yalign 0.5

transform right_side:
    xalign 0.8 yalign 0.5

transform left_side:
    xalign 0.2 yalign 0.5

transform remy_walk:
    xalign 0.5 # Start from the left (20% from the left edge)
    linear 5.0 xalign 0.75 
    linear 5.0 xalign 0.25
    linear 5.0 xalign 0.5
    repeat

transform remy_enter:
    xalign -0.1 yalign 0.5
    linear 2.0 xalign 0.2 

transform shake:
    xalign 0.8 yalign 0.5
    linear 0.02 xoffset 5
    linear 0.02 xoffset -5
    linear 0.02 yoffset 5
    linear 0.02 yoffset -5
    linear 0.02 xoffset 0
    linear 0.02 yoffset 0
    repeat

transform profesor_exit:
    xalign 0.8 yalign 0.5
    linear 3.0 xalign 2.0 

transform resize_1920_1080:
    size (1920, 1080)

label start:
    play music music_intro volume 0.6 loop
    scene ceue at resize_1920_1080 with fade

    "Paryż. Restauracja Podyplomówka."
    "Remy, utalentowany szef kuchni, dowiaduje się, że pewien profesor z UEP zagościł w jego restauracji."
    "Remy postanawia przygotować wyjątkowe danie, aby zdobyć uznanie Profesora."
    stop music fadeout 2.0

    scene kitchen  at resize_1920_1080 with fade
    play music music_kitchen volume 0.6  loop 
    
    show remy happy at center with dissolve
    "W kuchni, Remy zastanawia się, jakie danie zaskoczy Profesora."
    r "Hmm, co by tu podać???"
    play voice r_1
    hide remy happy with dissolve

    menu:
        "Przygotuj coś lekkiego i eleganckiego.":
            $ danie = "Krewetki z mango"
            show shrimp at center with dissolve
            $ ocena_profesora += 2  
            r "Najlepszym wyborem będzie [danie]."
            voice r_najlepszy_wybór
            hide shrimp with dissolve
        "Zaskocz go czymś nieoczekiwanym.":
            $ danie = "Kaczka w sosie borówkowym"
            show duck at center with dissolve
            r "Najlepszym wyborem będzie [danie]."
            voice r_najlepszy_wybór
            hide duck with dissolve   
            $ ocena_profesora += 4
        "Postaw na klasyczną francuską kuchnię.":
            $ danie = "Filet z kurczaka po francusku"
            show chicken at center with dissolve
            $ ocena_profesora += 6 
            r "Najlepszym wyborem będzie [danie]."
            voice r_najlepszy_wybór
            hide chicken with dissolve   

    "Remy zaczyna przygotowywać danie. W trakcie potrzebuje wsparcia w dwóch decyzjach.."

    show remy happy at center
    r "Czy dodać sól?"
    voice r_czy_dodać_sól

    menu:
        "Tak dodaj sól":
            $ ocena_profesora += 1  
            show salt at shake
            "Remy dodaje sól do potrawy."
            r "W sam raz."
            hide salt with dissolve

        "Nie, nie dodawaj sól.":
            "Remy kontynuuje gotowanie bez soli."

    r "Teraz czas na decyzję dotyczącą pieczenia mięsa w piekarniku."
    voice r_pieczenia_mięsa_w_piekarniku

    menu:
        "Piec [danie] krócej.":
            "Remy piecze mięso krócej, zachowując soczystość."
            $ ocena_profesora += 2
        "Piec [danie] dłużej.":
            "Remy decyduje się na dłuższe pieczenie, uzyskując intensywniejszy smak."
            $ ocena_profesora += 3

    play sound sound_bell volume 0.2
    hide remy happy with dissolve
    "Danie jest gotowe. Pora na ocenę profesora."
    stop music fadeout 1.0  # Stop current music with 1 second fadeout
    
    play music music_restaurant loop volume 0.6
    scene restaurant  at resize_1920_1080  with fade
    show profesor normal at right_side with dissolve
    show remy happy at remy_enter

    voice p_miejsce
    p "To miejsce jest naprawdę wyjątkowe, Remy. Podoba mi się panująca tu atmosfera."
    
    voice r_mam_nadzieję_że_również_danie
    r "Mam nadzieję, ze równiez danie przypadnie Panu do gustu."

    "Remy z uśmiechem prezentuje [danie] Profesorowi."
    hide remy happy with dissolve

    voice p_Yummy_wygląda_naprawdę
    p "Hmm, wygląda naprawdę apetycznie."
    hide profesor normal with dissolve

    if ocena_profesora < 7:
        
        show profesor unhappy at right_side with dissolve
        voice p_Niestety_Remy_ale_to_danie
        p "Niestety, Remy, ale to danie mi nie przypadło do gustu. Musisz jeszcze popracować nad smakiem."
        hide profesor unhappy with dissolve
        show remy unhappy at left_side with dissolve
        menu:
            "Przyjmij krytykę z pokorą.":
                "Remy przyjmuje krytykę z pokorą, obiecując poprawę."
                voice r_dziękuję_za_opinię
                r "Dziękuję za opinię, profesorze. Następnym razem postaram się bardziej sprostać Pańskim oczekiwaniom."
                hide remy unhappy with dissolve
                show profesor unhappy at profesor_exit 
                play sound sound_doors volume 0.65
                "Profesor wychodzi z restauracji z postanowieniem o powrocie w najbliższej przyszłości."
            "Wybuchnij z gniewem.":
                "Remy nie potrafi ukryć swojego rozgoryczenia."
                voice r_nie_prawda
                r "To nieprawda! To jedno z najlepszych dań, jakie kiedykolwiek stworzyłem! Może Pan nie zna się na jedzeniu!"
                hide remy unhappy with dissolve
                show profesor unhappy at profesor_exit 
                play sound sound_angry_doors volume 0.65
                "Profesor wychodzi z restauracji z postanowieniem, ze nigdy już tu nie wróci."
                
        
    else:
        show profesor happy at right_side
        voice p_doskonałe_to_jedno_z_najlepszych
        p "Doskonałe! To jedno z najlepszych dań, jakie kiedykolwiek próbowałem. Jesteś prawdziwym mistrzem kulinarnym!"

        "Remy jest zadowolony z pozytywnej oceny profesora. Teraz musi zadecydować, jaki deser zaproponować."
        hide profesor happy with dissolve
        menu:
            "Tiramisu":
                "Remy proponuje klasyczny deser."
                show remy happy at left_side with dissolve
                show tiramisu at right_side with dissolve
                voice r_tiramisu
                r "Mam dla Pana coś wyjątkowego - klasyczne tiramisu z własnym akcentem."
                $ wybrany_deser = "Tiramisu"
                hide tiramisu with dissolve
            "Koktajl owocowy":
                "Remy proponuje lekki deser."
                show remy happy at left_side with dissolve
                show coctail at right_side with dissolve
                voice r_koktail
                r "Może coś orzeźwiającego? Proszę spróbować naszego koktajlu owocowego."
                $ wybrany_deser = "Koktajl owocowy"
                hide coctail with dissolve
        hide remy happy with dissolve
        "Profesor entuzjastycznie zgadza się spróbować [wybrany_deser] jako deseru."
        if wybrany_deser == "Koktajl owocowy":
            show profesor sick at shake with dissolve
            play sound sound_shock volume 1.1
            "Niestety, po zjedzeniu deseru profesor nagle zaczyna odczuwać dziwne objawy. Okazuje się, że ma alergię na składniki zawarte w deserze."
            voice p_o_nie_do_lekarza
            p "O nie, coś tu nie gra. Muszę natychmiast udać się do lekarza!"
            hide profesor sick
            show profesor sick at profesor_exit 
            
            "Remy, przerażony, patrzy, jak profesor opuszcza restaurację w pośpiechu."
        else:
            show profesor happy at right_side with dissolve
            "Profesor delektuje się deserem, wyrażając pełne zadowolenie."
            voice p_yummy_niesamowite
            p "Yummy, niesamowite!"
            hide profesor happy 
            show profesor happy at profesor_exit 
            play sound sound_doors volume 0.65
            "Remy jest zadowolony z udanej kolacji i pozytywnej reakcji profesora."
    stop music fadeout 2.0
    "Koniec."