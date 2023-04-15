Directory Map:
"KomuniQ" folder = stores all files related to the site
    "static" folder = stores all JavaScript files, images, and CSS files
        "css" folder = stores all CSS files
        "Javascript" folder = stores all JavaScript
        "images" folder = stores all images/icons
    
    "templates" folder = stores all HTML files
        "index.html" = the file from which all other HTML files get their structure and theme
        "acerca-de.html" = the content for the ABOUT page, 
                           imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "ajustes.html" = the content for the AJUSTES page, 
                         imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "cuentas.html" = the content for the CUENTAS page, 
                         imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "dashboard.html" = the content for the DASHBOARD page, 
                           imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "login.html" = the content for the LOGIN page, 
                       imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "mensajes.html" = the content for the MENSAJES page, 
                          imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
        "notas.html" = the content for the NOTAS page, 
                       imports structure from index.html and replace content with everything within {% block content %} and {% endblock %}
    
    "auth.py" = all routes related to authorization & passwords
    "models.py" =  all database models
    "views.py" = all general routes
    "__init__.py" = makes KomuniQ into a packaged app
"main.py" = calls to "__init__.py" to run package



The following code is put within HTML files to load from the static folder:
    If JavaScript:
        <script type="text/javascript" src="{{ url_for('static', filename='fileName.js') }}"></script>

    If image & using img tag:
        <img src="{{ url_for('static', filename='/images/imageName.jpg') }}">
    If Image & using variable:
        <img src="{{image}}">
        Given app.py/__init__.py contains something like the following:
            from flask import Flask, render_template
            import os

            app = Flask(__name__)

            img = os.path.join('static', 'Image')                       <<<=====

            @app.route('/')
            def home():
                file = os.path.join(img, 'GP.png')                      <<<=====
                return render_template('image_render.html', image=file) <<<=====

            if __name__ == '__main__':
                app.run(debug=True)

    If CSS:
    Add the following to the __init__.py:
        package_dir = os.path.dirname(
            os.path.abspath(__file__)
        )
        static = os.path.join(
            package_dir, "static"
        )
        app.static_folder=static
    And the following to the HTML file:
        <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}">
