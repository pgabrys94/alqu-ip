[a]ccess [l]og [q]uery [u]ser - ip

[PL]

Wymagania:

    pip install requests

Skrypt pozwalający na odfiltrowanie z wielu plików apache access_log adresów IP wskazanego przez nas użytkownika platformy Nextcloud.
Wykorzystuje API ipinfo.io do pozyskiwania informacji o adresach IP, (Nazwa ISP, Geolokalizacja). Wymaga tokena dostępu do API.

Przy pierwszym uruchomieniu zostaniemy zapytani o token, który następnie zostanie zapisany w pliku ./token.dat
Zostanie również utworzony folder ./logs/, w którym należy umieścic logi.

Następnie uruchamiamy skrypt ponownie i wpisujemy login interesującego nas użytkownika i zatwierdzamy.
