# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action ,Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
class utter_greet(Action):
    def name(self):
        return "utter_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []

class action_inquire_rules(Action):
    def name(self) -> Text:
        return "action_inquire_rules"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        rules = next(tracker.get_latest_entity_values("rules"), None)

        if not rules:
            dispatcher.utter_message(text=f"bạn muốn tìm hiểu về luật nào")
            return []

        url = f"https://script.google.com/macros/s/AKfycbyz0gInPXPi5S2cVYWoPaG5lCEmTUqjfE1aLuHySABCONEMCpoa6hJicY7f5KJcvXWh/exec?category={rules}"  # Cập nhật URL API thực tế

        response = requests.get(url)
        response.raise_for_status()
        boxing_rules = response.json()
        if boxing_rules["data"]:
            boxer_data = boxing_rules["data"][0]
            msg = (
                f" {boxer_data['category']} là : "
                f"{boxer_data['rule_content']}"
            )
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text="Không tìm thấy thông tin về luật.")
        return []

class action_inquire_techniques(Action):
    def name(self) -> Text:
        return "action_inquire_techniques"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tech = next(tracker.get_latest_entity_values("technique"), None)

        if not tech:
            dispatcher.utter_message(text=f"xin lỗi tôi không biết bạn đang tìm kiếm kỹ thuật nào")
            return []

        url = f"https://script.google.com/macros/s/AKfycbyQZFcFTvvSaTVkn_bU6dFrmHTQN_i5ek79IrdoEQhxfITiEdrTmOJq4wADzydtkwrZ/exec?technique_name={tech}"  # Cập nhật URL API thực tế
        response = requests.get(url)
        techniques = response.json()
        if techniques["data"]:
            boxer_data = techniques["data"][0]
            msg = (

                f"Tên kỹ thuật: {boxer_data['technique_name']}, "
                f"Nội dung: {boxer_data['description']}"
            )
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text="Không tìm thấy thông tin về Kỹ thuật.")

        return []

class action_provide_athlete_info(Action):
    def name(self) -> Text:
        return "action_provide_athlete_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        boxer_name = next(tracker.get_latest_entity_values("boxer_name"), None)
        if not boxer_name:
            dispatcher.utter_message(text=f"xin lỗi tôi không biết bạn đang tìm kiếm võ sĩ nào")
            return []
        url = f"https://script.google.com/macros/s/AKfycbwFKTo7z55NfBapOwEIQCyc59oLC1rofk4CZh79nf39lhKm0Inl2Mtw2KFU3xeKDmBU/exec?boxer_name={boxer_name}"  # Cập nhật URL API thực tế
        response = requests.get(url)
        boxer_info = response.json()

        if boxer_info["data"]:
            boxer_data = boxer_info["data"][0]
            msg = (
                f"Thông tin võ sĩ: Tên: {boxer_data['boxer_name']}, "
                f"Tuổi: {boxer_data['boxer_age']}, "
                f"Chiều cao: {boxer_data['boxer_height']}, "
                f"Cân nặng: {boxer_data['boxer_weight']}, "
                f"Nơi ở hiện tại: {boxer_data['boxer_location']}, "
                f"Quê quán: {boxer_data['boxer_hometown']}"
            )
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text="Không tìm thấy thông tin về võ sĩ.")

        return []
class inform_championship_info(Action):
    def name(self) -> Text:
        return "inform_championship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any])->List[Dict[Text,Any]]:
        # Lấy thông tin về giải vô địch từ slot
        championship = next(tracker.get_latest_entity_values("championship"), None)

        if not championship:
            dispatcher.utter_message(text=f"xin lỗi tôi không biết bạn đang tìm kiếm võ sĩ nào")
            return []
        url = f"https://script.google.com/macros/s/AKfycbx6-FbVwdrhRv-shymj8ZVMrscI8mtoB9vtvouyINYj2OngVprpPmjtOXv50QXnL9UX/exec?championship_name={championship}"  # Thay thế bằng URL API thực tế
        response = requests.get(url)
        championship_info = response.json()
        if championship_info["data"]:
            boxer_data = championship_info["data"][0]
            msg = (

                f"Tên Giải Đấu: {boxer_data['championship_name']}, "
                f"Thông Tin Giải Đấu: {boxer_data['championship_infor']}"
            )
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text="Không tìm thấy thông tin về Giải đấu.")

        return []