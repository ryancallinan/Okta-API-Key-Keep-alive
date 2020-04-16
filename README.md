# Okta-API-Key-Keep-alive

This script simply takes a json list of okta urls and api keys as an argument then queries the Okta api for users containing "cenet". You can than run it as a cronjob to prevent your api keys from expiring if they aren't used for a month. There is also a json template file in this repo for reference.
