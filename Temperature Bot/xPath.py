
def xPath_AuthenticateBtn():  # xpath for the AuthenticateBtn
    return "/html/body[@class='modal-open']/div[@id='modal']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']/div[@id='modal-body']/div[@id='history-pin-container']/button[@class='btn btn-warning']"


def xPath_dateNtimeTemp():  # get the first row of the date and temp readings for AM and PM respectively
    xPath_dateNtimeTempList = [
        "/html/body[@class='modal-open']/div[@id='modal']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']/div[@id='modal-body']/div[@id='history-records-container']/table[@id='temp-history-table']/tbody[@id='history-records-table']/tr[1]/td[" + str(i) + "]" for i in range(1, 4)]
    return xPath_dateNtimeTempList


def xPath_CloseBtn1():
    return "/html/body[@class='modal-open']/div[@id='modal']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']/div[@id='modal-footer']/button[@class='btn btn-primary action-btn']"


def xPath_CloseBtn2():
    return "/ html/body[@class = 'modal-open']/div[@id = 'modal']/div[@class = 'modal-dialog modal-dialog-centered']/div[@class = 'modal-content']/div[@id = 'modal-footer']/button[@class = 'btn btn-primary action-btn']"


def xPath_SubmitBtn():
    return "/html/body/div[@id='main-content-with-title']/div[@id='main-content']/div[@id='submit-temperature-container']/button[@class='btn btn-warning']"


def xPath_ConfirmBtn():
    return "/html/body[@class='modal-open']/div[@id='modal']/div[@class='modal-dialog modal-dialog-centered']/div[@class='modal-content']/div[@id='modal-footer']/button[@id='submit-temp-btn']"
