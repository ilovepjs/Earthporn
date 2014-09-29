Earthporn
=========

A beautiful visualisation of images from reddit.com/r/earthporn.

Uses Python 2.7

**To get it up and running**:

  - git clone https://github.com/ilovepjs/earthporn.git
  - cd earthporn
  - pip install requirements.txt
  - python manage.py runserver
  - Go to 127.0.0.1:8000

**To fetch new images**:

  *NOTE*: 
  
  This does not need to be done as there are already images but it can be used to add more.

  - python manage.py fetch_images

**Known bugs**:

  - Country matching is not perfect. So valid countries may not always be resolved.
    https://github.com/ilovepjs/earthporn/issues/1