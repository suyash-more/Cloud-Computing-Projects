# Using GAE launcher to launch the web applications

#### GAE - Google App Engine

## Installation and Reference Material

 - [GCloud SDK](https://cloud.google.com/sdk/docs/install)
 - [Python](https://www.python.org/downloads/)
 - [WebApp](https://webapp2.readthedocs.io/en/latest/)
 - [Tutorials (Google Documentation)](https://cloud.google.com/python/docs/setup)

In order to run this application you need to install Gcloud SDK and Python.
Refer [this video](https://www.youtube.com/watch?v=k-8qFh8EfFA) for installation of Gcloud SDK
## How to

1. Start your Cloud Shell after installation of _Gcloud SDK_
2. After starting the shell you need your local dev app server file to run the application
3. So as you have opened the shell, you will have the dev app server file under the relative location of the shell 
i.e. **google-cloud-sdk\bin\dev_appserver.py**

Absolute Path : **C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\dev_appserver.py**

4. Run the application with the following command in shell
```sh
cmd > py google-cloud-sdk\bin\dev_appserver.py <path to the directory where application resides>
```