from lab.database.database.DatabaseExt import DatabaseExt
from lab.database.Exercise5 import Exercise5
from lab.database.Exercise6 import Exercise6
from lab.database.gui.Menu import Menu


class Application:
    def __init__(self):
        self.db = DatabaseExt()
        self.exe5 = Exercise5()
        self.exe6 = Exercise6()
        self.width = 0

        self.menu = Menu("Menu: Glowne")
        self.menu.add_graphic("""
              Witaj w aplikacji moja baza :)

            |                         _...._
         \  _  /                    .::o:::::.
          (\o/)                    .:::'''':o:.
      ---  / \  ---                :o:_    _:::
           >*<                     `:}_>()<_{:'
          >0<@<                 @    `'//\\'`    @
         >>>@<<*              @ #     //  \\     # @
        >@>*<0<<<           __#_#____/'____'\____#_#__
       >*>>@<<<@<<         [__________________________]
      >@>>0<<<*<<@<         |=_- .-/\ /\ /\ /\--. =_-|
     >*>>0<<@<<<@<<<        |-_= | \ \\ \\ \\ \ |-_=-|
    >@>>*<<@<>*<<0<*<       |_=-=| / // // // / |_=-_|
   >0>>*<<@<>0><<*<@<<      |=_- |`-'`-'`-'`-'  |=_=-|
  >*>>@><0<<*>>@><*<0<<     | =_-| o          o |_==_|
 >@>>0<*<<0>>@<<0<<<*<@<    |=_- | !     (    ! |=-_=|
 >((*))_>0><*<0><@<<<0<*<  _|-,-=| !    ).    ! |-_-=|_
        """)
        self.load_menu = Menu("Menu: Wczytywanie danych")
        self.view_menu = Menu("Menu: Wyswietlanie danych")

        self.menu.add_option("Wczytywanie danych ->", self.load_menu.init_menu)
        self.menu.add_option("Zapisywanie bazy danych do pliku o okreslonej nazwie.", self.db.save_ext)
        self.menu.add_option("Dodawanie nowych wpisow do bazy danych", self.db.add_record_ext)
        self.menu.add_option("Usuwanie wpisow z bazy danych", self.db.remove_record_ext)
        self.menu.add_option("Wyswietlanie danych ->", self.view_menu.init_menu)
        self.menu.add_option("Sortowanie", self.db.sort_ext)
        self.menu.add_option("Zadanie 5", self.exe5.exercise5)
        self.menu.add_option("Zadanie 5_1", self.exe5.exercise5_1)
        self.menu.add_option("Zadanie 6 posortowane dane", self.exe6.exercise6a)
        self.menu.add_option("Zadanie 6 bwygenerowane dane + polskie znaki", self.exe6.exercise6b)
        self.menu.add_option("Zadanie 6c zpis", self.exe6.save_data_from_exercise_6c)
        self.menu.add_option("Zadanie 6c upload", self.exe6.upload_data_from_exercise_6c)
        self.menu.add_option("Zadanie 6d komputer", self.exe6.exercise6d)
        self.menu.add_option("Zadanie 6e", self.exe6.exercise6e)
        self.menu.add_option("Wyswietlanie listy opcji", self.menu.print)

        self.load_menu.add_option("Wczytywanie bazy danych o okreslonej nazwie.", self.db.load_ext)
        self.load_menu.add_option("Wczytywanie bazy danych z pliku.", self.db.load_from_file_ext)
        self.load_menu.add_option("Wczytywanie bazy danych z URL.", self.db.load_from_url_ext)
        self.load_menu.add_option("Wyswietlanie listy opcji", self.load_menu.print)
        self.load_menu.add_option("Wroc", self.menu.init_menu)

        self.view_menu.add_option("Wyswietlanie zawartosci bazy danych", self.db.open_db_ext)
        self.view_menu.add_option("Wyswietlanie rekorów bez wszystkich danych", self.db.open_incomplete_records_ext)
        self.view_menu.add_option("Wyswietlanie listy opcji", self.load_menu.print)
        self.view_menu.add_option("Wroc", self.menu.init_menu)

    def init(self):
        self.menu.init_menu()
