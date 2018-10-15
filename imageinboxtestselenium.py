from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import requests
import shutil
import os
import time

starting_url = 'https://web.whatsapp.com/' # WhatsApp URL
directory_name = '/Users/alexharris/Desktop/'
website_url = "https://phototap-production-001.s3.amazonaws.com/uploads/events/359/photos/cjmjr23ew00003bf1pwg6y9q7-branded.jpg"


def send_to_whatsapp(file_name, starting_url="https://web.whatsapp.com/"):
    driver = init_driver()
    driver.get(starting_url)
    number_list = []
    photo_list = []
    number_list.append("Blasper")
    photo_list.append(file_name)
    print(file_name) #Figure out file_name to reference for sending
    start_automation = raw_input("Please scan QR code in browser [Press any key to continue] ")
    if start_automation:
        counter = 0
        while counter != len(number_list):
            # for number in number_list:
            #     contact_id = number
            # for photo in photo_list:
            #     msg_content = photo

            # Focus search_bar and bring up contact
                search_bar_container_id = driver.find_element_by_css_selector('#side > div._3CPl4 > div > label > input')
                search_bar_container_id.click()
                search_bar_container_id.send_keys("Blasper")
                search_bar_container_id.send_keys(Keys.ENTER)

                driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span').click()
                driver.find_element_by_xpath('/html/body/div/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button').click()



            # Focus message box and send msg_content
                # msg_box = driver.find_element_by_css_selector('#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text')
                # msg_box.click()
                # msg_box.send_keys(actual_file_name)
                # msg_box.send_keys(Keys.ENTER)
        counter = counter + 1

    return "File sent through WhatsApp"

def init_driver():
    driver = webdriver.Chrome(executable_path="/Users/alexharris/Desktop/chromedriver")
    driver.wait = WebDriverWait(driver, 5)
    return driver


def download_images_and_send(website_url, directory_name):
    length = 1
    w = website_url
    for index in range(length):
        print ('Downloading {0} of 1 images'.format(index + 1))
        response = requests.get(w, stream = True)
        save_image_to_disk(response, directory_name, index)
        send_to_whatsapp(save_image_to_disk(response,directory_name, index))
        time.sleep(2)
        del response


def save_image_to_disk(image, directory_name, suffix):
    with open('{directory_name}/img_{suffix}.jpg'.format(directory_name = directory_name, suffix = suffix), 'wb') as out_file:
        shutil.copyfileobj(image.raw, out_file)
    return out_file


if __name__ == '__main__':
    driver = init_driver()
    driver.get('https://phototap-production-001.s3.amazonaws.com/uploads/events/359/photos/cjmjr23ew00003bf1pwg6y9q7-branded.jpg')
    time.sleep(5)
    driver.quit
    download_images_and_send(website_url, directory_name)
