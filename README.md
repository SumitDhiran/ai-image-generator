# ai-image-generator
1. create virtualenv env and activate it.
2. install requirements.txt using "pip install -r requirements.txt".
3. install redis or user redis docker image.
4. create a .env and fill it with required credentials.
   """
   txt
   API_HOST=https://api.stability.ai
   STABILITY_API_KEY=sk-mop2***************
8. """
9. run commands:
   """
   txt
   python manage.py makemigrations
   python manage.py migrate
   """
10. create a superuser using:
    """
    txt
    python manage.py createsuperuser
    """
11. run the server using:
    """
    txt
    python manage.py runserver 0.0.0.0:8000
    """
12. go to:
    """
    txt
    http://0.0.0.0:8000/docs
    """
    to open swagger.
    use the
    """
    txt
    http://0.0.0.0:8000/api/token/
    """
    endpoint to generate jwt token for authentication the API(use username and password for superadmin previously created)
14. go to:
    """
    txt
    http://0.0.0.0:8000/core/image-generator/
    json
    {
      "prompt_1": "",
      "prompt_2": "",
      "prompt_3": "",
      "prompt_4": "",
      "prompt_5": ""
    }
    """
    to generate 5 images based on 5 given prompts, if prompts are not given default prompts are used.
15. the images data is being stored in Database, you can use different Datbase.
16. additionally the images are being stored under image directory inside out folder. 
