from KomuniQ import create_app

app = create_app()

# ony run web server if the condition is true
if __name__ == '__main__':
    app.run(debug=True)
