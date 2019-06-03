Feature: Showing off behave (tutorial02)

Scenario Outline: some scenario
  Given a set of specific users
     | name      | department  |
     | Barry     | Beer Cans   |
     | Pudey     | Silly Walks |
     | Two-Lumps | Silly Walks |

  When we count the number of people in each department
  Then we will find <count> people in <department>

  Examples: Counts
    | count | department  |
    | 2     | Silly Walks |
    | 1     | Beer Cans   |
