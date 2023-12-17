[a]ccess [l]og [q]uery [u]ser - ip
----------------------------------

[PL]

Wymagania:

    pip install requests

Skrypt pozwalający na odfiltrowanie z wielu plików apache access_log adresów IP wskazanego przez nas użytkownika platformy Nextcloud.
Wykorzystuje API serwisu ipinfo.io do pozyskiwania informacji o adresach IP, (Nazwa ISP, Geolokalizacja). 
Wymaga tokena dostępu do API.

Przy pierwszym uruchomieniu wprowadzamy token do API, który następnie zostanie zapisany w pliku ./token.dat
Zostanie również utworzony folder ./logs/, w którym należy umieścić logi.

Następnie uruchamiamy skrypt ponownie i wpisujemy login interesującego nas użytkownika i zatwierdzamy.

Wyniki zostaną wyświetlone w konsoli oraz zapisane do pliku ./<login>.log