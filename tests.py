from selene import browser, be, have

def test_lesson_1(set_up_browser_settings):
    browser.element('[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id=react-layout]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_homework_3(set_up_browser_settings):
    browser.element('[name=q]').clear().type('sdkmcm23endlfn23kfn2l3fnl2126n').press_enter()
    browser.element('[aria-level="3"]').should(have.text(' ничего не найдено.'))
    browser.element('[name=q]').clear().type('.').press_enter()
    browser.element('[class="LC20lb MBeuO DKV0Md"]').should(have.text('Точка (знак препинания)'))
