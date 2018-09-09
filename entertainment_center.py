#Stores details of movies and displays them on a website.

import fresh_tomatoes
import media

#Creates six Movie objects, initialising these objects with title, storyline, poster image link, video trailer link and release date.

lalaland = media.Movie("La La Land",
                        "La La Land ist ein US-amerikanischer Spielfilm von Damien Chazelle aus dem Jahr 2016. Das Filmmusical basiert auf einem Originaldrehbuch des Regisseurs Chazelle und ist in vier Kapitel („Winter“, „Frühling“, „Sommer“, „Herbst“) und einen zeitlich versetzten Epilog („Winter“) gegliedert. Es stellt einen ehrgeizigen Jazzpianisten (gespielt von Ryan Gosling) und eine aufstrebende Schauspielerin (dargestellt von Emma Stone) in den Mittelpunkt, die beide nach beruflichem Erfolg in Los Angeles streben und sich dabei ineinander verlieben. Der Titel des Films nimmt Bezug auf den Spitznamen der Stadt Los Angeles sowie auf eine euphemistische Bezeichnung eines realitätsfernen Seelenzustandes",
                        "https://www.vintagemovieposters.co.uk/wp-content/uploads/2017/06/IMG_6573.jpg",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

last_dance = media.Movie("Save the last dance",
                     "Save the Last Dance (engl. in etwa: „Reservier den letzten Tanz [für mich]“) ist ein US-amerikanischer Tanz- und Liebesfilm aus dem Jahr 2001. Regie führte Thomas Carter, produziert wurde der Film von MTV Films.",
                     "https://images.store.sky.com/api/img/asset/en/66D8BB8A-E4E8-4422-9242-603110084545_D11131C8-57F6-4042-B100-E42ABED3F238_2017-12-5-T14-20-34.jpg?s=260x371",
                     "https://www.youtube.com/watch?v=cm-tgph1IQw")

love_actually = media.Movie("Tatsaechlich Liebe",
                     "Tatsächlich… Liebe (Originaltitel: Love Actually) ist eine romantische Komödie aus dem Jahr 2003 von Regisseur Richard Curtis, der auch das Drehbuch schrieb.",
                     "http://johannes.freudendahl.net/files/2008/01/love_actually_01.jpg",
                     "https://www.youtube.com/watch?v=n6YZUUNoThM")

radio_rock = media.Movie("Radio Rock Revolution",
                     "Radio Rock Revolution (Originaltitel: The Boat That Rocked) ist eine britische Musikkomödie aus dem Jahr 2009. Erzählt wird die Geschichte eines Piratensenders, der in den 1960er Jahren von einem Schiff in der Nordsee aus Rock ’n’ Roll sendet. Vorlage für die fiktive Handlung war der damalige Piratensender Radio Caroline. Regie führte Richard Curtis, der auch das Drehbuch verfasst hat.",
                     "https://images-na.ssl-images-amazon.com/images/I/515tXHqW9qL._SY445_.jpg",
                     "https://www.youtube.com/watch?v=HMZhEpXsjJc")

breakfast = media.Movie("Breakfast at Tiffany's",
                     "Frühstück bei Tiffany (Originaltitel: Breakfast at Tiffany’s) ist ein US-amerikanischer Spielfilm aus dem Jahr 1961 mit Audrey Hepburn in der Hauptrolle. Er basiert auf dem gleichnamigen Roman von Truman Capote. Regie führte der Komödienspezialist Blake Edwards.",
                     "https://www.movieposter.com/posters/archive/main/180/MPW-90372",
                     "https://www.youtube.com/watch?v=urQVzgEO_w8")

christmas_vacation = media.Movie("Schoene Bescherung",
                     "Schöne Bescherung (Originaltitel: Christmas Vacation, Alternativtitel: Hilfe, es weihnachtet sehr, National Lampoon’s Christmas Vacation, National Lampoon’s Winter Holiday) ist eine US-amerikanische Filmkomödie aus dem Jahr 1989. Die Regie führte Jeremiah S. Chechik, das Drehbuch schrieb John Hughes. Die Hauptrollen spielten Chevy Chase und Beverly D’Angelo. Der Film ist eine Fortsetzung der Komödien Die schrillen Vier auf Achse aus dem Jahr 1983 und Hilfe, die Amis kommen aus dem Jahr 1985. 1997 folgte mit Die schrillen Vier in Las Vegas ein weiterer Teil der Griswold-Reihe sowie 2003 Schöne Bescherung 2 – Eddie geht baden in der jedoch die Griswolds nicht mitwirken und stattdessen Cousin Eddie der Protagonist ist. 2015 entstand Vacation – Wir sind die Griswolds.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/NationalLampoonsChristmasVacationPoster.JPG/220px-NationalLampoonsChristmasVacationPoster.JPG",
                     "https://www.youtube.com/watch?v=NBTTipJX-h4")

# Store the Movie objects in a list.
movies = [lalaland, last_dance, love_actually, radio_rock, breakfast, christmas_vacation]

# Open the movie website in the user's browser.
fresh_tomatoes.open_movies_page(movies)


