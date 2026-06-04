import allure
import pytest

from data import AnswerText, QuestionText
from pages.main_page import MainPage


class TestMainPage:

    @allure.title("Проверка ответов на вопросы")
    @allure.description("Проверяем, что при нажатии на вопрос, открывается соответствующий текст ответа.")
    @pytest.mark.parametrize("index", range(len(QuestionText.QUESTIONS)))
    def test_questions_and_answers(self, driver, index):
        main_page = MainPage(driver)
       
        expected_answer_text = AnswerText.ANSWERS[index]
        actual_answer_text = main_page.get_answer_text(index)
        
        assert actual_answer_text == expected_answer_text, (
                f'Ожидали ответ {expected_answer_text}, '
                f'получили {actual_answer_text}')