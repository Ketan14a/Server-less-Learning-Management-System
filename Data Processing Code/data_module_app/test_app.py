from data import data

def test_data():
    response = data.test_client().get('https://csci5410-project-data-processing-dgsicmdfsa-ue.a.run.app/upload?')

    assert response.status_code == 200
   

def test_data2():
    response = data.test_client().get('https://csci5410-project-data-processing-dgsicmdfsa-ue.a.run.app')

    assert response.status_code == 200


def test_data3():
    response = data.test_client().get('https://csci5410-project-data-processing-dgsicmdfsa-ue.a.run.app/wordcloud')

    assert response.status_code == 200


def test_data4():
    response = data.test_client().get('https://csci5410-project-data-processing-dgsicmdfsa-ue.a.run.app/clean_data_bucket?')

    assert response.status_code == 200

def test_data5():
    response = data.test_client().get('https://csci5410-project-data-processing-dgsicmdfsa-ue.a.run.app/clean_word_bucket?')

    assert response.status_code == 200