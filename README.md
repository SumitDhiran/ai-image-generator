# ai-image-generator
1. create virtualenv env and activate it.
2. install requirements.txt using
   ```
   pip install -r requirements.txt
   ```
5. install redis or user redis docker image.
6. create a .env and fill it with required credentials.
   ```
   API_HOST=https://api.stability.ai
   STABILITY_API_KEY=sk-mop2***************
   ```
9. run commands:
    ```
   python manage.py makemigrations
   python manage.py migrate
    ```
11. create a superuser using:
    ```
    python manage.py createsuperuser
    ```
13. run the server using:
    ```
    python manage.py runserver 0.0.0.0:8000
    ```
15. go to:
    ```
    http://0.0.0.0:8000/docs
    ```
    to open swagger.
    
    use the
    ```
    http://0.0.0.0:8000/api/token/
    ```
    endpoint to generate jwt token for authentication the API(use username and password for superadmin previously created)
16. to run celery open another terminal and eneter
    ```
    python -m celery -A chaotix worker -l info
    ```
18. go to:
    ```
    http://0.0.0.0:8000/core/image-generator/
    json
    {
      "prompt_1": "",
      "prompt_2": "",
      "prompt_3": "",
      "prompt_4": "",
      "prompt_5": ""
    }
    ```
    to generate 5 images based on 5 given prompts, if prompts are not given default prompts are used.
19. the images data is being stored in Database, you can use different Datbase.
20. additionally the images are being stored under image directory inside out folder.

## start using docker
   install docker and docker compose and run
    ```
    change 
    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    to
    CELERY_BROKER_URL = "redis://redis:6379"
    CELERY_RESULT_BACKEND = "redis://redis:6379"
    then
    docker-compose up
    ```

