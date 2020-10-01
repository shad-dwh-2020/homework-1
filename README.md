# Домашнее задание 1
## Доступ к Hadoop кластеру
### Доступ к клиентской машине

- На почту должно прийти письмо с логином и паролем. Если не пришло, надо обратиться к @abelousova в телеграме
- Для работы с кластером требуется зайти по SSH на сервер `ysda-client.velkerr.ru`, используя полученное имя пользователя и пароль. На Windows для этого можно использовать клиент PuTTY. 
- После успешной авторизации вы попадете в консоль головной машины кластера, находясь внутри вашей домашней директории /home/$USER. 
- Для копирования файлов на сервер можно использовать любой SCP-клиент. На Windows рекомендуется использовать WinSCP. Не забудьте указать свой SSH-ключ в настройках соединения (Advanced Site Settings / SSH / Authentication / Private key file)
### Генерация ssh-ключа
Мы советуем сгенерировать ssh-ключ для доступа к клиентской машине, чтобы не вводить пароль каждый раз.
- Если у вас Linux или Mac, инструкция тут 
- Если у вас Windows, то используйте PuTTYgen
- Если вы используете другой способ генерации или существующий ключ, проверьте, что ключ имеет тип RSA и длину 2048 бит
- После генерации ключ надо положить на клиентскую машину. На Linux и Mac для этого нужно использовать ssh-copy-id, на Windows ???
### Настройка доступов к веб-интерфейсам
- Прокидываем порты через ssh port forwarding:
```
ssh -N ysda-client.velkerr.ru \
-L 8088:ysda-master.velkerr.ru:8088 \
-L 19888:ysda-master.velkerr.ru:19888 \
-L 18089:ysda-master.velkerr.ru:18089 \
-L 18088:ysda-master.velkerr.ru:18088 \
-L 8042:ysda-node01.velkerr.ru:8042 \
-L 8043:ysda-node02.velkerr.ru:8042 \
-L 8044:ysda-node03.velkerr.ru:8042 \
-L 8041:ysda-node01.velkerr.ru:8041 \
-L 8889:ysda-node01.velkerr.ru:8889 \
-L 7180:ysda-master.velkerr.ru:7180
```
- В /etc/hosts прописываем алиасы:
```
127.0.0.1       ysda-master.velkerr.ru
127.0.0.1       ysda-node01.velkerr.ru
127.0.0.1       ysda-node02.velkerr.ru
127.0.0.1       ysda-node03.velkerr.ru
```
??? про Windows

Ссылки:
- http://ysda-node01.velkerr.ru:8889/hue
- http://ysda-master.velkerr.ru:8088/cluster

## Сбор статистики по данным
Потренироваться запускать spark-джобы, собрать небольшую статистику по датасетам
### Написать код
Посчитать статистику по /data/stg/usage:
- число уникальных значений в колонке staff_login
- минимум и максимум в utc_event_dttm
- топ-10 используемых команд
### Запустить на кластере
Джобы надо запускать вот такой командой `spark-submit --master yarn --deploy-mode cluster my_program.py`. Результат можно писать в /user/$USER на кластере
### Выложить код и результат
В репозиторий нужно выложить файл с кодом и таблички с результатом в csv
