<h2>Hey Welcome to chatComapny project🙏🏻, I'm ali darzi! <img src="https://media.giphy.com/media/12oufCB0MyZ1Go/giphy.gif" width="50"></h2>
<img align='right' src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="230">
<p><em>Software Engineer<img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30">
</em></p>
<pre>Hope you enjoy and I hope it will be usfull</pre>


### <img src="https://media.giphy.com/media/VgCDAzcKvsR6OM0uWg/giphy.gif" width="50"> instalation ...

## 🤝 Requirements
0. redis

1. Mysql

2. install virtualenv
  ```bash
  pip install virtualenv
  ```


3. let's make sure you have the following installed(it's only needed in linux):

- in Debain:
  ```bash
  sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
  ```
- in Red Hat / CentOS:
  ```zsh
  sudo yum install python3-devel mysql-devel pkgconfig
  ```
- in Arch:
  ```zsh
  sudo pacman -S pkg-config

## 🚀 Installation

0.Go On Project Directory ;D

<details>
<summary>linux</summary>

1.make a virtual environment:

```zsh title="Terminal"
python -m venv vnev
```

2.active virtual environment:

```zsh title="Terminal"
source ./venv/bin/activate
```
3.install requirements in virtual

```zsh title="Terminal"
pip install -r requirements.txt
```

4.Mysql prompt:

``` sql
CREATE DATABASE chatCompany CHARACTER SET utf8;
```
5.go on /ChatCompany/setting.py:

``` py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatCompany',
        'USER': '<enter_your_Mysql_username>',
        'PASSWORD': '<Enter_your_Mysql_password>',
        'OPTIONS': {
        }
    }
}
```
6.migrate to DB:
```zsh title="Terminal"
python manage.py migrate
```


7.run redis(port:6379) :
```zsh title="Terminal"
sudo docker run redis
```
</details>

<details>
<summary>Windows</summary>
1.make a virtual environment:

```zsh title="Terminal"
python -m venv vnev
```

2.active virtual environment:

```zsh title="Terminal"
.\venv\Script\activate
```
3.install requirements in virtual

```zsh title="Terminal"
pip install -r requirements.txt
```

4.Mysql prompt:

``` sql
CREATE DATABASE chatCompany CHARACTER SET utf8;
```
5.on .\ChatCompany\setting.py:

``` py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chatCompany',
        'USER': '<enter_your_Mysql_username>',
        'PASSWORD': '<Enter_your_Mysql_password>',
        'OPTIONS': {
        }
    }
}
```
6.migrate to DB:
```zsh title="Terminal"
python manage.py migrate
```


7.run redis(port:6379) or be in local :
```cmd
docker run --rm -p 6379:6379 redis:7
```
</details>






