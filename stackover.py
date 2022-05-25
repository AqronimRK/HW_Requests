import datetime
import requests
import time
from pprint import pprint


class StackOverFlow:

    def question_for_day(self, tag, count_days):
        date = f'{datetime.date.today() - datetime.timedelta(days=count_days)}'
        params = {'fromdate': date, 'tagged': tag, 'site': 'stackoverflow'}
        url = 'https://api.stackexchange.com/2.3/questions'
        all_questions = []
        for i in range(1, 26):
            page = {'page': i}
            response = requests.get(url, params={**params, **page}).json()
            page_questions = [question['title'] for question in response['items']]
            all_questions.extend(page_questions)
            time.sleep(2)

        print(f'Найдено запросов: {len(all_questions)}')
        return all_questions


if __name__ == '__main__':
    py_ques = StackOverFlow()
    pprint(py_ques.question_for_day('Python', 2))
