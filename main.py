import asyncio

from flask import Flask, render_template, request, redirect, send_file

from Parser_vacancy.parser import GetJobs
from Parser_vacancy.download import save_csv_file

app = Flask('JobScripter')

data = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/find')
def about():
    key_vacancy = request.args.get('key_vacancy')
    if key_vacancy is not None:
        key_vacancy = key_vacancy.lower()
        get_data = data.get(key_vacancy)
        if get_data:
            result = get_data

        else:
            get_jobs_instance = GetJobs()
            result =  get_jobs_instance.get_jobs(job=key_vacancy)
            data[key_vacancy] = result

    else:
        return redirect('/')
    return render_template('find_vacations.html', vacancy=key_vacancy,
                           count_result=len(result), name_vacancy=result
                           )


@app.route('/download')
def download():
    try:
        key_vacancy = request.args.get('key_vacancy')
        if not key_vacancy:
            raise Exception()
        key_vacancy = key_vacancy.lower()
        result = data.get(key_vacancy)
        if not result:
            raise Exception()
        save_csv_file(result)
        return send_file('vacancies.csv')
    except:
        return redirect('/')


app.run()
