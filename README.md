# Stake Sport Odds

## Overview
This simple Python script takes the data from the Stake.com API and parses it into a list of competitors with their respective betting odds. 
<br>
<br>
## Notes
- The Stake.com API is a **CLOSED API**, meaning there is no documentation for it. Therefore, the query parameters may change at any time.
- Because this API is closed, this project will **NOT** be maintained on a regular basis
<br>
<br>

## Usage

### You will need two things for this to work:
- The **URL** of the game you wish to get the odds from
    - Example: https://stake.com/sports/mma/ufc/ufc-279-chimaev-vs-diaz
- Your Stake API token
    - You can get this by going to **Profile** -> **Settings** -> **API** on Stake and copying it from the **Token** field. **DO NOT GIVE THIS TOKEN AWAY! STORE IT IN A SECURE LOCATION!**
<br>
<br>

In this section, we will grab the data from the URL and put it in the appropriate fields. This example is using the URL from above:

```python
"variables": {
        "sport": "mma",
        "category": "ufc",
        "tournament": "ufc-279-chimaev-vs-diaz",
...
```
<br>
Your API token will replace **API KEY** but remain inside the quotes:
<br><br>

```python
session.headers["x-access-token"] = "API KEY"
```

You will most likely need to play around with the code a bit more to get it to work. 
<br>
<br>
### **Have Fun!**