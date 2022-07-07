# 4 Digit MWC 3 Data Engineering

This repository is data conversion of 4dm3 into the style of 4dm4 sqlite `.db`

## utility Documentation

There consists of two modules in utilities, one for url fetching (requests) and one for tournament data

### tournament_data

This is self-explanatory, a data for 4 digit MWC 3 tournament

### get_main_data

This is a main data of tournament which can be found in [this link](https://raw.githubusercontent.com/Paturages/derpament/master/docs/data/4dmwc3.json)

It consists of 4dmwc3 rounds data and players data

### get_round_data

This is a round data of a tournament which can be called using

```python
get_round_data(round_id)
```

`round_id` is an id of the round which can be found in `tournament_data`, for example `"5.semifinals"`

The output will be consisting of round information and scores of each player in each map
