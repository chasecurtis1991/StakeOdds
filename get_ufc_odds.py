import requests

# Query based on Graphql data found in Chrome dev tools
query = """
query SlugTournament(
  $sport: String!,
  $category: String!,
  $tournament: String!,
  $groups: [String!]!,
  $limit: Int = 10,
  $offset: Int = 0
) {
  slugTournament(sport: $sport, category: $category, tournament: $tournament) {
    fixtureList(type: active, limit: $limit, offset: $offset) {
      data {
        ... on SportFixtureDataMatch {
          competitors {
            name
          }
        }
      }
      groups(groups: $groups, status: [active]) {
        templates(limit: 3, includeEmpty: true) {
          name
          markets(limit: 1) {
            outcomes {
                id
                odds
                name
            }
          }
        }
      }
    }
  }
}
"""

# Here's where we put the data of the sport we want to see the odds
# In this case, let's work with a UFC tournament
request_data = {
    "operationName": "SlugTournament",
    "query": query,
    # variables based on SLUG names
    "variables": {
        "sport": "mma",
        "category": "ufc",
        "tournament": "ufc-279-chimaev-vs-diaz",
        "groups": ["winner"],
        "limit": 10,
        "offset": 0,
    },
}

# Replace "API KEY" with your API token inside the quotes. This gets you access to run the query.
# You can find the API key by going to Profile -> Settings -> API and copying your token and pasting it there.
# DO NOT GIVE OUT YOUR TOKEN! THIS CAN GIVE ANYONE ACCESS TO YOUR ACCOUNT!!
session = requests.Session()
session.headers["x-access-token"] = "API KEY"

# Let's ask the Stake API to get the data we need
response = session.post("https://api.stake.com/graphql", json=request_data)
response_data = response.json()

# We got the data! Now let's parse it to make it look good :D
for fixture in response_data["data"]["slugTournament"]["fixtureList"]:
  competitor1 = fixture["data"]["competitors"][0]["name"]
  competitor2 = fixture["data"]["competitors"][1]["name"]
  
  try:
    template = next(t for t in fixture["groups"][0]["templates"])
    market_outcomes = template["markets"][0]["outcomes"]
  except Exception:
    continue
  print("{competitor1} vs {competitor2}")
  for outcome in market_outcomes:
    print("  - {name} @ {odds}".format_map(outcome))
  print()
