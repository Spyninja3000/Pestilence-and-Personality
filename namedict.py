combo = {
    3: "Sad Middle Ground",
    4: "Miniature Overachiever",
    5: "Dedicated Deliveryman",
    6: "Stressed",
    7: "Terminator",
    8: "99.9 percent",
    9: "Perfectionist"
}

# 3-Dimensional Dictionary!

names = {

    # P = 0
    0: {
        # M = 0
        0: {
            0:"A Lowly Nobody", # S = 0
            1:"The Popular Kid", # S = 1        P = 0, M = 0
            2:"Talk Show Host", # S = 2
            3:"President" # S = 3
        },
        # M = 1
        1: {
            0:"Valedictorian", # S = 0
            1:"The Presenter", # S = 1        P = 0, M = 1
            2:"Talkative Engineer", # S = 2
            3:"Social Strategist" # S = 3
        },
        # M = 2
        2: {
            0:"Double Doctorate", # S = 0
            1:"Procrastinator", # S = 1        P = 0, M = 2
            2:"Snapchat Student", # S = 2
            3:"Study Partner" # S = 3
        },
        # M = 3
        3: {
            0:"Quantum Physicist", # S = 0
            1:"Nerd", # S = 1                    P = 0, M = 3
            2:"ERROR 404", # S = 2
            3:"Living Contradiction" # S = 3
        }

    },

    # P = 1
    1: {
        # M = 0
        0: {
            0:"Varsity Athlete", # S = 0
            1:"Dumb and Determined", # S = 1        P = 1, M = 0
            2:"Active Activist", # S = 2
            3:"Pop Singer" # S = 3
        },
        # M = 1
        1: {
            0:"Student Athlete", # S = 0
            1:combo[3], # S = 1                     P = 1, M = 1
            2:combo[4], # S = 2
            3:combo[5] # S = 3
        },
        # M = 2
        2: {
            0:"Fit Factorer", # S = 0
            1:combo[4], # S = 1                   P = 1, M = 2
            2:combo[5], # S = 2
            3:combo[6] # S = 3
        },
        # M = 3
        3: {
            0:"Athletic Axiomatician", # S = 0
            1:combo[5], # S = 1                   P = 1, M = 3
            2:combo[6], # S = 2
            3:combo[7] # S = 3
        }

    },

    # P = 2
    2: {
        # M = 0
        0: {
            0:"Bodybuilder", # S = 0
            1:"No one ever", # S = 1        P = 2, M = 0
            2:"Normal", # S = 2
            3:"Sports Youtuber" # S = 3
        },
        # M = 1
        1: {
            0:"AP Phys Ed", # S = 0
            1:combo[4], # S = 1              P = 2, M = 1
            2:combo[5], # S = 2
            3:combo[6] # S = 3
        },
        # M = 2
        2: {
            0:"Scientific Shooter", # S = 0
            1:combo[5], # S = 1                  P = 2, M = 2
            2:combo[6], # S = 2
            3:combo[7] # S = 3
        },
        # M = 3
        3: {
            0:"Smart and Strong", # S = 0
            1:combo[6], # S = 1                   P = 2, M = 3
            2:combo[7], # S = 2
            3:combo[8] # S = 3
        }

    },

    # P = 3
    3: {
        # M = 0
        0: {
            0:"Global Ninja Warrior", # S = 0
            1:"Failed Footballer", # S = 1        P = 3, M = 0
            2:"Post-game Puppet", # S = 2
            3:"Super Star" # S = 3
        },
        # M = 1
        1: {
            0:"Differential Dunker", # S = 0
            1:combo[5], # S = 1                  P = 3, M = 1
            2:combo[6], # S = 2
            3:combo[7] # S = 3
        },
        # M = 2
        2: {
            0:"Strong and Smart", # S = 0
            1:combo[6], # S = 1                  P = 3, M = 2
            2:combo[7], # S = 2
            3:combo[8] # S = 3
        },
        # M = 3
        3: {
            0:"Quadratic Quarterback", # S = 0
            1:combo[7], # S = 1                   P = 3, M = 3
            2:combo[8], # S = 2
            3:combo[9] # S = 3
        }

    }


}

# names[p][m][s] = "Name Assigned"
# names[1][2][0] == "Fit Factorer"
