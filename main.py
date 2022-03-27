import os
import requests
import json


def main():
    webex_token = os.environ["INPUT_WEBEXTOKEN"]
    room_id = os.environ["INPUT_ROOMID"]
    text_msg = os.environ["INPUT_TEXTMSG"]
    markdown_msg = os.environ["INPUT_MARKDOWNMSG"]

    # Build payload
    api_payload = {
        "roomId":  room_id,
        "text": text_msg,
        "markdown": markdown_msg
    }

    # Send notification
    api_headers = {'Authorization': 'Bearer ' +
                   webex_token, 'Content-Type': 'application/json'}

    resp = requests.post("https://webexapis.com/v1/messages",
                         data=json.dumps(api_payload), headers=api_headers)

    msg_id = resp.json()['id']

    print(f"::set-output name=msgId::{msg_id}")


if __name__ == "__main__":
    main()
